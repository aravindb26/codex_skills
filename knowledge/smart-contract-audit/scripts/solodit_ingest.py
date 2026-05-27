#!/usr/bin/env python3
"""
Import Solodit High/Medium findings into the local audit knowledge base.

This stores compact metadata and pattern-card stubs, not full raw report text.
Set CYFRIN_API_KEY before running, or save the key in /home/dinesh/.codex/solodit.env.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


API_URL = "https://solodit.cyfrin.io/api/v1/solodit/findings"
ROOT = Path("/home/dinesh/.codex/knowledge/smart-contract-audit")
SOLODIT_ROOT = ROOT / "report-patterns" / "solodit"
INDEX_PATH = SOLODIT_ROOT / "indexes" / "solodit-findings-index.jsonl"
ENV_PATH = Path("/home/dinesh/.codex/solodit.env")


def slugify(value: str, fallback: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return (value or fallback)[:100]


def first_value(item: dict[str, Any], names: list[str]) -> Any:
    for name in names:
        if name in item and item[name] not in (None, ""):
            return item[name]
    return None


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return ", ".join(normalize_text(v) for v in value if v is not None)
    if isinstance(value, dict):
        return json.dumps(value, sort_keys=True, ensure_ascii=True)
    return str(value).strip()


def normalize_impact(value: Any) -> str:
    text = normalize_text(value).upper()
    if "HIGH" in text:
        return "HIGH"
    if "MEDIUM" in text or text == "MED":
        return "MEDIUM"
    return text


def result_items(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return [x for x in payload if isinstance(x, dict)]
    if not isinstance(payload, dict):
        return []
    for key in ("data", "findings", "results", "items"):
        value = payload.get(key)
        if isinstance(value, list):
            return [x for x in value if isinstance(x, dict)]
        if isinstance(value, dict):
            nested = result_items(value)
            if nested:
                return nested
    return []


def load_seen() -> tuple[set[str], set[str]]:
    ids: set[str] = set()
    fingerprints: set[str] = set()
    if not INDEX_PATH.exists():
        return ids, fingerprints
    with INDEX_PATH.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get("dedupe_id"):
                ids.add(row["dedupe_id"])
            if row.get("fingerprint"):
                fingerprints.add(row["fingerprint"])
    return ids, fingerprints


def fingerprint_for(row: dict[str, str]) -> str:
    raw = "|".join(
        [
            row.get("title", "").lower(),
            row.get("source_url", "").lower(),
            row.get("protocol", "").lower(),
            row.get("impact", "").lower(),
        ]
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def finding_url(item: dict[str, Any], slug: str) -> str:
    direct = first_value(item, ["url", "link", "findingUrl", "sourceUrl", "reportUrl"])
    if direct:
        return normalize_text(direct)
    if slug:
        return f"https://solodit.cyfrin.io/issues/{slug}"
    return ""


def normalize_item(item: dict[str, Any]) -> dict[str, str]:
    title = normalize_text(first_value(item, ["title", "name", "issueTitle", "findingTitle"]))
    impact = normalize_impact(first_value(item, ["impact", "severity", "risk", "level"]))
    slug = normalize_text(first_value(item, ["slug", "issueSlug", "findingSlug"]))
    item_id = normalize_text(first_value(item, ["id", "_id", "uuid", "findingId", "issueId"]))
    protocol = normalize_text(first_value(item, ["protocol", "protocolName", "project", "projectName"]))
    source = normalize_text(first_value(item, ["source", "firm", "auditFirm", "provider"]))
    tags = normalize_text(first_value(item, ["tags", "reportTags", "categories", "vulnerabilityTags"]))
    source_url = finding_url(item, slug)
    dedupe_id = item_id or slug or source_url

    row = {
        "dedupe_id": dedupe_id,
        "slug": slug,
        "title": title,
        "impact": impact,
        "protocol": protocol,
        "source": source,
        "tags": tags,
        "source_url": source_url,
    }
    row["fingerprint"] = fingerprint_for(row)
    return row


def request_page(api_key: str, page: int, page_size: int, sort: str) -> Any:
    body = {
        "page": page,
        "pageSize": page_size,
        "filters": {
            "impact": ["HIGH", "MEDIUM"],
            "sortField": sort,
            "sortDirection": "Desc",
        },
    }
    data = json.dumps(body).encode("utf-8")
    request = urllib.request.Request(
        API_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "X-Cyfrin-API-Key": api_key,
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def load_api_key() -> str:
    api_key = os.environ.get("CYFRIN_API_KEY") or os.environ.get("SOLODIT_API_KEY")
    if api_key:
        return api_key.strip()

    if not ENV_PATH.exists():
        return ""

    raw_key_parts: list[str] = []
    for raw_line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            name, value = line.split("=", 1)
            name = name.strip().removeprefix("export ").strip()
            if name in {"CYFRIN_API_KEY", "SOLODIT_API_KEY"}:
                return value.strip().strip("\"'")
        else:
            raw_key_parts.append(line)

    return "".join(raw_key_parts).strip()


def write_stub(row: dict[str, str]) -> Path:
    impact_dir = "high" if row["impact"] == "HIGH" else "medium"
    title_slug = slugify(row["title"], row["dedupe_id"] or row["fingerprint"][:12])
    file_path = SOLODIT_ROOT / impact_dir / f"{title_slug}-{row['fingerprint'][:10]}.md"
    if file_path.exists():
        return file_path

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    content = f"""# Solodit Pattern Stub: {row["title"] or "Untitled finding"}

Source:
- {row["source_url"] or "Solodit"}

Imported:
- {now}

Status:
- needs distillation

Severity:
- {row["impact"]}

Protocol:
- {row["protocol"] or "unknown"}

Source platform / firm:
- {row["source"] or "unknown"}

Tags:
- {row["tags"] or "unknown"}

Dedupe:
- id: `{row["dedupe_id"] or "unknown"}`
- fingerprint: `{row["fingerprint"]}`

Core idea:
- TODO: Distill the reusable attack pattern from the source.

Broken invariant:
- TODO

Where to look in code:
- TODO

Attack path:
1. TODO

False-positive checks:
- TODO

PoC shape:
- TODO

Triage notes:
- TODO
"""
    file_path.write_text(content, encoding="utf-8")
    return file_path


def append_index(rows: list[dict[str, str]]) -> None:
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    with INDEX_PATH.open("a", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True, ensure_ascii=True) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-page", type=int, default=1)
    parser.add_argument("--max-pages", type=int, default=1)
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument("--sort", default="Quality")
    parser.add_argument("--delay", type=float, default=3.2)
    parser.add_argument("--no-stubs", action="store_true")
    args = parser.parse_args()

    api_key = load_api_key()
    if not api_key:
        print("Missing CYFRIN_API_KEY, SOLODIT_API_KEY, or /home/dinesh/.codex/solodit.env.", file=sys.stderr)
        return 2

    seen_ids, seen_fingerprints = load_seen()
    imported: list[dict[str, str]] = []
    skipped = 0

    end_page = args.start_page + args.max_pages - 1
    for page in range(args.start_page, end_page + 1):
        try:
            payload = request_page(api_key, page, args.page_size, args.sort)
        except urllib.error.HTTPError as exc:
            print(f"Solodit API error on page {page}: HTTP {exc.code}", file=sys.stderr)
            print(exc.read().decode("utf-8", errors="replace"), file=sys.stderr)
            return 1

        items = result_items(payload)
        if not items:
            break

        page_rows: list[dict[str, str]] = []
        for item in items:
            row = normalize_item(item)
            if row["impact"] not in {"HIGH", "MEDIUM"}:
                continue
            if row["dedupe_id"] and row["dedupe_id"] in seen_ids:
                skipped += 1
                continue
            if row["fingerprint"] in seen_fingerprints:
                skipped += 1
                continue
            seen_ids.add(row["dedupe_id"])
            seen_fingerprints.add(row["fingerprint"])
            page_rows.append(row)
            if not args.no_stubs:
                write_stub(row)

        append_index(page_rows)
        imported.extend(page_rows)
        print(f"page={page} items={len(items)} imported={len(page_rows)} skipped={skipped}", flush=True)

        if len(items) < args.page_size:
            break
        if page != end_page:
            time.sleep(args.delay)

    print(f"done imported={len(imported)} skipped={skipped} index={INDEX_PATH}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
