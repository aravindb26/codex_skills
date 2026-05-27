#!/usr/bin/env python3
"""
Import Code4rena High/Medium findings into the local audit knowledge base.

This stores compact metadata and pattern-card stubs, not full raw report text.
It uses public Code4rena report pages and the public sitemap. No API key is
required.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


SITEMAP_URL = "https://code4rena.com/sitemap.xml"
REPORTS_BASE_URL = "https://code4rena.com/reports"
ROOT = Path("/home/dinesh/.codex/knowledge/smart-contract-audit")
CODE4RENA_ROOT = ROOT / "report-patterns" / "code4rena"
INDEX_PATH = CODE4RENA_ROOT / "indexes" / "code4rena-findings-index.jsonl"


def slugify(value: str, fallback: str) -> str:
    value = strip_text(value).lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return (value or fallback)[:100]


def strip_tags(value: str) -> str:
    value = re.sub(r"(?is)<script\b.*?</script>", " ", value)
    value = re.sub(r"(?is)<style\b.*?</style>", " ", value)
    value = re.sub(r"(?is)<br\s*/?>", " ", value)
    value = re.sub(r"(?is)<[^>]+>", " ", value)
    return value


def strip_text(value: str) -> str:
    value = html.unescape(strip_tags(value))
    value = value.replace("\xa0", " ")
    return " ".join(value.split())


def request_text(url: str, timeout: int = 45) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; local-audit-knowledge-importer/1.0)",
            "Accept": "text/html,application/xml,text/xml,*/*",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def report_url_from_slug(slug: str) -> str:
    slug = slug.strip().strip("/")
    if slug.startswith("http://") or slug.startswith("https://"):
        return slug
    if slug.startswith("reports/"):
        slug = slug.removeprefix("reports/")
    return f"{REPORTS_BASE_URL}/{slug}"


def canonical_report_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url.strip())
    if not parsed.scheme:
        return report_url_from_slug(url)
    return urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip("/"), "", "", ""))


def report_slug(url: str) -> str:
    path = urllib.parse.urlparse(url).path.strip("/")
    if path.startswith("reports/"):
        return path.split("/", 1)[1]
    return path.rsplit("/", 1)[-1]


def discover_report_urls(sitemap_url: str = SITEMAP_URL, newest_first: bool = True) -> list[str]:
    sitemap = request_text(sitemap_url)
    items: list[tuple[str, str]] = []
    seen: set[str] = set()
    for block in re.findall(r"(?is)<url>(.*?)</url>", sitemap):
        loc_match = re.search(r"<loc>\s*(https://code4rena\.com/reports/[^<\s]+)\s*</loc>", block)
        if not loc_match:
            continue
        lastmod_match = re.search(r"<lastmod>\s*([^<\s]+)\s*</lastmod>", block)
        url = loc_match.group(1)
        lastmod = lastmod_match.group(1) if lastmod_match else ""
        url = canonical_report_url(html.unescape(url))
        slug = report_slug(url)
        if not slug or slug in {"reports"}:
            continue
        if url in seen:
            continue
        seen.add(url)
        items.append((lastmod, url))
    if newest_first:
        items.sort(key=lambda item: item[0], reverse=True)
    return [url for _, url in items]


def load_slugs_file(path: Path) -> list[str]:
    slugs: list[str] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        slugs.append(line)
    return slugs


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
            row.get("source_url", "").lower(),
            row.get("title", "").lower(),
            row.get("report_slug", "").lower(),
            row.get("severity", "").lower(),
        ]
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def extract_report_title(page_html: str, fallback_slug: str) -> str:
    match = re.search(r'(?is)<div[^>]*class="[^"]*\breport-header\b[^"]*"[^>]*>.*?<h1[^>]*>(.*?)</h1>', page_html)
    if match:
        title = strip_text(match.group(1))
        title = re.sub(r"\s+Findings\s*&\s*Analysis\s*Report\s*$", "", title, flags=re.I).strip()
        if title:
            return title

    match = re.search(r"(?is)<h1[^>]*>(.*?)</h1>", page_html)
    if match:
        title = strip_text(match.group(1))
        if title:
            return title

    return fallback_slug


def extract_report_date(page_html: str) -> str:
    match = re.search(r'(?is)<div[^>]*class="[^"]*\breport-header\b[^"]*"[^>]*>.*?<h4[^>]*>(.*?)</h4>', page_html)
    if match:
        return strip_text(match.group(1))
    return ""


def normalize_finding_title(text: str) -> str:
    text = strip_text(text)
    text = re.sub(r"^\[(H|M)-0*\d+\]\s*", "", text, flags=re.I).strip()
    return text


def normalize_finding_id(value: str, severity: str) -> str:
    value = value.upper()
    match = re.search(rf"\b{severity[0]}-0*(\d+)\b", value)
    if not match:
        return ""
    return f"{severity[0]}-{int(match.group(1)):02d}"


def extract_toc_region(page_html: str) -> str:
    match = re.search(r'(?is)<div[^>]*class="[^"]*\breport-toc\b[^"]*"[^>]*>(.*?)</div>', page_html)
    if match:
        return match.group(1)
    return page_html


def extract_findings(page_html: str, report_url: str, report_name: str, date: str) -> list[dict[str, str]]:
    toc = extract_toc_region(page_html)
    rows: list[dict[str, str]] = []
    seen_urls: set[str] = set()

    for match in re.finditer(r'(?is)<a\s+[^>]*href="(#([^"]+))"[^>]*>(.*?)</a>', toc):
        anchor = html.unescape(match.group(2)).strip()
        raw_text = match.group(3)
        display_text = strip_text(raw_text)
        anchor_lc = anchor.lower()

        severity = ""
        if re.match(r"^h-0*\d+\b", anchor_lc) or re.match(r"^\[?h-0*\d+\]?", display_text, re.I):
            severity = "HIGH"
        elif re.match(r"^m-0*\d+\b", anchor_lc) or re.match(r"^\[?m-0*\d+\]?", display_text, re.I):
            severity = "MEDIUM"
        else:
            continue

        title = normalize_finding_title(display_text)
        if not title:
            continue

        source_url = f"{report_url}#{anchor}"
        if source_url in seen_urls:
            continue
        seen_urls.add(source_url)

        finding_id = normalize_finding_id(anchor, severity) or normalize_finding_id(display_text, severity)
        slug = report_slug(report_url)
        row = {
            "dedupe_id": f"{slug}#{anchor}",
            "report_slug": slug,
            "report": report_name,
            "report_date": date,
            "finding_id": finding_id,
            "title": title,
            "severity": severity,
            "source_url": source_url,
            "source": "Code4rena",
        }
        row["fingerprint"] = fingerprint_for(row)
        rows.append(row)

    return rows


def write_stub(row: dict[str, str]) -> Path:
    severity_dir = "high" if row["severity"] == "HIGH" else "medium"
    id_prefix = slugify(row.get("finding_id", ""), "")
    title_slug = slugify(row["title"], row["fingerprint"][:12])
    filename_slug = "-".join(part for part in [row["report_slug"], id_prefix, title_slug] if part)
    file_path = CODE4RENA_ROOT / severity_dir / f"{filename_slug[:140]}-{row['fingerprint'][:10]}.md"
    if file_path.exists():
        return file_path

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    content = f"""# Code4rena Pattern Stub: {row["title"] or "Untitled finding"}

Source:
- {row["source_url"]}

Imported:
- {now}

Status:
- needs distillation

Severity:
- {row["severity"]}

Report:
- {row["report"] or row["report_slug"]}

Report date:
- {row["report_date"] or "unknown"}

Source platform:
- Code4rena

Dedupe:
- id: `{row["dedupe_id"]}`
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
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")
    return file_path


def append_index(rows: Iterable[dict[str, str]]) -> None:
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    with INDEX_PATH.open("a", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True, ensure_ascii=True) + "\n")


def build_report_targets(args: argparse.Namespace) -> list[str]:
    targets: list[str] = []
    for value in args.report_url:
        targets.append(canonical_report_url(value))
    for value in args.slug:
        targets.append(canonical_report_url(report_url_from_slug(value)))
    if args.slugs_file:
        for value in load_slugs_file(args.slugs_file):
            targets.append(canonical_report_url(report_url_from_slug(value)))
    if args.discover or not targets:
        targets.extend(discover_report_urls(args.sitemap_url, newest_first=not args.sitemap_order))

    deduped: list[str] = []
    seen: set[str] = set()
    for url in targets:
        if url in seen:
            continue
        seen.add(url)
        deduped.append(url)
    return deduped


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sitemap-url", default=SITEMAP_URL)
    parser.add_argument("--report-url", action="append", default=[], help="Specific Code4rena report URL to import.")
    parser.add_argument("--slug", action="append", default=[], help="Specific report slug, e.g. 2024-06-size.")
    parser.add_argument("--slugs-file", type=Path, help="File containing one report slug or URL per line.")
    parser.add_argument("--discover", action="store_true", help="Discover report URLs from the public sitemap.")
    parser.add_argument("--sitemap-order", action="store_true", help="Keep sitemap order instead of sorting reports by lastmod newest-first.")
    parser.add_argument("--max-reports", type=int, default=10, help="Maximum reports to fetch unless --all is set.")
    parser.add_argument("--all", action="store_true", help="Import every discovered/selected report.")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between report fetches.")
    parser.add_argument("--no-stubs", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    report_urls = build_report_targets(args)
    if not args.all:
        report_urls = report_urls[: max(args.max_reports, 0)]

    seen_ids, seen_fingerprints = load_seen()
    imported: list[dict[str, str]] = []
    skipped = 0
    failed = 0

    CODE4RENA_ROOT.mkdir(parents=True, exist_ok=True)
    (CODE4RENA_ROOT / "high").mkdir(parents=True, exist_ok=True)
    (CODE4RENA_ROOT / "medium").mkdir(parents=True, exist_ok=True)
    (CODE4RENA_ROOT / "indexes").mkdir(parents=True, exist_ok=True)

    for idx, report_url in enumerate(report_urls, 1):
        try:
            page_html = request_text(report_url)
        except urllib.error.HTTPError as exc:
            failed += 1
            print(f"report={report_url} error=HTTP-{exc.code}", file=sys.stderr)
            continue
        except urllib.error.URLError as exc:
            failed += 1
            print(f"report={report_url} error={exc}", file=sys.stderr)
            continue

        slug = report_slug(report_url)
        report_name = extract_report_title(page_html, slug)
        report_date = extract_report_date(page_html)
        rows = extract_findings(page_html, report_url, report_name, report_date)
        page_rows: list[dict[str, str]] = []

        for row in rows:
            if row["dedupe_id"] in seen_ids or row["fingerprint"] in seen_fingerprints:
                skipped += 1
                continue
            seen_ids.add(row["dedupe_id"])
            seen_fingerprints.add(row["fingerprint"])
            page_rows.append(row)
            if not args.no_stubs and not args.dry_run:
                write_stub(row)

        if page_rows and not args.dry_run:
            append_index(page_rows)
        imported.extend(page_rows)

        high_count = sum(1 for row in rows if row["severity"] == "HIGH")
        medium_count = sum(1 for row in rows if row["severity"] == "MEDIUM")
        print(
            f"report={idx}/{len(report_urls)} slug={slug} found_high={high_count} "
            f"found_medium={medium_count} imported={len(page_rows)} skipped={skipped}",
            flush=True,
        )

        if idx != len(report_urls) and args.delay > 0:
            time.sleep(args.delay)

    print(
        f"done reports={len(report_urls)} imported={len(imported)} skipped={skipped} "
        f"failed={failed} index={INDEX_PATH}",
        flush=True,
    )
    return 1 if failed and not imported else 0


if __name__ == "__main__":
    raise SystemExit(main())
