#!/usr/bin/env python3
"""
Import Crypto Training hack cards into the local audit knowledge base.

This stores compact searchable metadata and exploit-pattern stubs, not full raw
article bodies. It parses the public index page at https://crypto.training/hacks/
and deduplicates by canonical source URL and content fingerprint.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


INDEX_URL = "https://crypto.training/hacks/"
BASE_URL = "https://crypto.training"
ROOT = Path("/home/dinesh/.codex/knowledge/smart-contract-audit")
CRYPTO_TRAINING_ROOT = ROOT / "report-patterns" / "crypto-training-hacks"
INDEX_PATH = CRYPTO_TRAINING_ROOT / "indexes" / "crypto-training-hacks-index.jsonl"


def strip_tags(value: str) -> str:
    value = re.sub(r"(?is)<script\b.*?</script>", " ", value)
    value = re.sub(r"(?is)<style\b.*?</style>", " ", value)
    value = re.sub(r"(?is)<br\s*/?>", " ", value)
    value = re.sub(r"(?is)<[^>]+>", " ", value)
    return value


def strip_text(value: str) -> str:
    value = html.unescape(strip_tags(value))
    value = value.replace("\xa0", " ")
    value = value.replace("\\$", "$")
    return " ".join(value.split())


def slugify(value: str, fallback: str) -> str:
    value = strip_text(value).lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return (value or fallback)[:100]


def request_text(url: str, timeout: int = 60) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; local-audit-knowledge-importer/1.0)",
            "Accept": "text/html,*/*",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def canonical_source_url(path_or_url: str) -> str:
    raw = html.unescape(path_or_url.strip())
    if raw.startswith("http://") or raw.startswith("https://"):
        parsed = urllib.parse.urlparse(raw)
    else:
        parsed = urllib.parse.urlparse(urllib.parse.urljoin(BASE_URL, raw))
    return urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip("/") + "/", "", "", ""))


def dedupe_id_from_url(source_url: str) -> str:
    path = urllib.parse.urlparse(source_url).path.strip("/")
    if path.startswith("hacks/"):
        return path.removeprefix("hacks/").rstrip("/")
    return path.rstrip("/") or source_url


def fingerprint_for(row: dict[str, str]) -> str:
    raw = "|".join(
        [
            row.get("source_url", "").lower(),
            row.get("title", "").lower(),
            row.get("chain", "").lower(),
            row.get("incident_date", "").lower(),
            row.get("tags", "").lower(),
            row.get("loss", "").lower(),
        ]
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def load_seen() -> tuple[set[str], set[str], set[str]]:
    ids: set[str] = set()
    fingerprints: set[str] = set()
    source_urls: set[str] = set()
    if not INDEX_PATH.exists():
        return ids, fingerprints, source_urls
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
            if row.get("source_url"):
                source_urls.add(canonical_source_url(row["source_url"]))
    return ids, fingerprints, source_urls


def anchor_end(page_html: str, start: int) -> int:
    end = page_html.find("</a>", start)
    return end + len("</a>") if end != -1 else -1


def first_match(pattern: str, value: str) -> str:
    match = re.search(pattern, value, flags=re.S | re.I)
    return match.group(1) if match else ""


def extract_header(card_html: str) -> tuple[str, str]:
    header = first_match(
        r'<div[^>]*class="[^"]*flex flex-wrap items-center[^"]*"[^>]*>(.*?)</div>',
        card_html,
    )
    spans = [strip_text(item) for item in re.findall(r"<span\b[^>]*>(.*?)</span>", header, flags=re.S | re.I)]
    chain = spans[0] if spans else ""
    incident_date = spans[1] if len(spans) > 1 else ""
    return chain, incident_date


def extract_loss_and_preview(card_html: str) -> tuple[str, str]:
    loss = ""
    preview = ""
    for attrs, body in re.findall(r"<p\b([^>]*)>(.*?)</p>", card_html, flags=re.S | re.I):
        text = strip_text(body)
        if not loss and re.match(r"^Loss\s*·", text, flags=re.I):
            loss = re.sub(r"^Loss\s*·\s*", "", text, flags=re.I).strip()
        if not preview and "line-clamp-3" in attrs and text:
            preview = text
    return loss, preview


def year_from_date_or_slug(incident_date: str, slug: str) -> str:
    match = re.search(r"\b(20\d{2})\b", incident_date)
    if match:
        return match.group(1)
    match = re.match(r"^(20\d{2})-", slug)
    if match:
        return match.group(1)
    return "unknown-year"


def parse_cards(page_html: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    seen_paths: set[str] = set()
    href_pattern = re.compile(r'<a\b[^>]*href="(/hacks/[^"]+/)"', flags=re.I)
    for match in href_pattern.finditer(page_html):
        path = html.unescape(match.group(1))
        if path in seen_paths:
            continue
        seen_paths.add(path)

        end = anchor_end(page_html, match.start())
        if end == -1:
            continue
        card_html = page_html[match.start() : end]

        title = strip_text(first_match(r"<h2\b[^>]*>(.*?)</h2>", card_html))
        if not title:
            continue
        source_url = canonical_source_url(path)
        dedupe_id = dedupe_id_from_url(source_url)
        slug = dedupe_id
        chain, incident_date = extract_header(card_html)
        tags = [
            html.unescape(tag).removeprefix("vuln/")
            for tag in re.findall(r'title="(vuln/[^"]+)"', card_html)
        ]
        loss, preview = extract_loss_and_preview(card_html)
        year = year_from_date_or_slug(incident_date, slug)

        row = {
            "dedupe_id": dedupe_id,
            "slug": slug,
            "title": title,
            "chain": chain or "unknown",
            "incident_date": incident_date or "unknown",
            "year": year,
            "tags": ", ".join(tags) if tags else "unknown",
            "primary_tag": tags[0] if tags else "unknown",
            "loss": loss or "unknown",
            "preview": preview or "",
            "source_url": source_url,
        }
        row["fingerprint"] = fingerprint_for(row)
        rows.append(row)
    return rows


def write_stub(row: dict[str, str]) -> Path:
    year_dir = slugify(row["year"], "unknown-year")
    title_slug = slugify(row["title"], row["slug"] or row["fingerprint"][:12])
    file_path = CRYPTO_TRAINING_ROOT / "incidents" / year_dir / f"{title_slug}-{row['fingerprint'][:10]}.md"
    if file_path.exists():
        return file_path

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    content = f"""# Crypto Training Exploit Pattern Stub: {row["title"]}

Source:
- {row["source_url"]}

Imported:
- {now}

Status:
- compact index-derived exploit-pattern lead

Incident date:
- {row["incident_date"]}

Chain:
- {row["chain"]}

Loss / impact summary:
- {row["loss"]}

Tags:
- {row["tags"]}

Dedupe:
- id: `{row["dedupe_id"]}`
- fingerprint: `{row["fingerprint"]}`

Core exploit idea:
- {row["preview"] or "Open the source link and distill the reusable exploit mechanism before applying this to a live audit."}

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
"""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")
    return file_path


def append_index(row: dict[str, str], path: Path) -> None:
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "dedupe_id": row["dedupe_id"],
        "fingerprint": row["fingerprint"],
        "source_url": row["source_url"],
        "title": row["title"],
        "chain": row["chain"],
        "incident_date": row["incident_date"],
        "year": row["year"],
        "tags": row["tags"],
        "loss": row["loss"],
        "local_path": str(path),
    }
    with INDEX_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, sort_keys=True, ensure_ascii=True) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index-url", default=INDEX_URL, help="Crypto Training hacks index URL")
    parser.add_argument("--index-html", type=Path, help="Use a saved index HTML file instead of fetching")
    parser.add_argument("--max-items", type=int, default=0, help="Maximum cards to import, 0 means all")
    parser.add_argument("--dry-run", action="store_true", help="Parse and dedupe, but do not write files")
    args = parser.parse_args()

    if args.index_html:
        page_html = args.index_html.read_text(encoding="utf-8", errors="replace")
    else:
        page_html = request_text(args.index_url)

    rows = parse_cards(page_html)
    if args.max_items > 0:
        rows = rows[: args.max_items]

    seen_ids, seen_fingerprints, seen_urls = load_seen()
    imported = 0
    skipped = 0

    for row in rows:
        source_url = canonical_source_url(row["source_url"])
        if row["dedupe_id"] in seen_ids or row["fingerprint"] in seen_fingerprints or source_url in seen_urls:
            skipped += 1
            continue
        if args.dry_run:
            imported += 1
            continue
        path = write_stub(row)
        append_index(row, path)
        seen_ids.add(row["dedupe_id"])
        seen_fingerprints.add(row["fingerprint"])
        seen_urls.add(source_url)
        imported += 1

    action = "would import" if args.dry_run else "imported"
    print(f"parsed={len(rows)} {action}={imported} skipped_existing={skipped}")
    print(f"output_root={CRYPTO_TRAINING_ROOT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
