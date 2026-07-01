#!/usr/bin/env python3
"""Import manually reviewed, non-duplicate Pashov High/Medium findings."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/home/dinesh/.codex/knowledge/smart-contract-audit")
OUT = ROOT / "report-patterns" / "pashov-audits"
INDEX = OUT / "indexes" / "pashov-audits-findings-index.jsonl"
DECISIONS = OUT / "indexes" / "reviewed-decisions.jsonl"
OTHER_INDEXES = (
    ROOT / "report-patterns/solodit/indexes/solodit-findings-index.jsonl",
    ROOT / "report-patterns/code4rena/indexes/code4rena-findings-index.jsonl",
)
HEADING = re.compile(
    r"^\s{0,3}#{1,6}\s+\[(?P<sev>[CHMLI])-0*(?P<num>\d+)\]\s*(?P<title>.+?)\s*$",
    re.I,
)


def norm(value: str) -> str:
    value = re.sub(r"^\s*\[(?:C|H|M|L|I)-\d+\]\s*", "", value, flags=re.I)
    return re.sub(r"[^a-z0-9]+", " ", value.replace("`", "").lower()).strip()


def body_norm(value: str) -> str:
    value = re.sub(r"```.*?```", " ", value, flags=re.S)
    value = re.sub(r"<[^>]+>", " ", value)
    return " ".join(value.lower().split())


def sha(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", norm(value)).strip("-")[:100]


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as error:
            raise ValueError(f"Invalid JSONL at {path}:{number}") from error
    return rows


def commit_for(source: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(source), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def parse(source: Path, commit: str) -> list[dict]:
    rows = []
    for category in ("team", "solo"):
        for path in sorted((source / category / "md").glob("*.md")):
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
            headings = [(i, m) for i, line in enumerate(lines) if (m := HEADING.match(line))]
            for position, (start, match) in enumerate(headings):
                severity = match.group("sev").upper()
                if severity not in {"H", "M"}:
                    continue
                end = headings[position + 1][0] if position + 1 < len(headings) else len(lines)
                relative = path.relative_to(source).as_posix()
                finding_id = f"{severity}-{int(match.group('num')):02d}"
                title = match.group("title").strip()
                rows.append(
                    {
                        "key": f"{relative}#{finding_id}",
                        "finding_id": finding_id,
                        "severity": "HIGH" if severity == "H" else "MEDIUM",
                        "title": title,
                        "normalized_title": norm(title),
                        "content_hash": sha(body_norm("\n".join(lines[start + 1 : end]))),
                        "report": path.stem,
                        "category": category,
                        "source_url": f"https://github.com/pashov/audits/blob/{commit}/{relative}#L{start + 1}",
                    }
                )
    return rows


def text_field(decision: dict, name: str) -> str:
    value = decision.get(name, "")
    if isinstance(value, list):
        return "\n".join(f"- {item}" for item in value)
    return str(value)


def write_card(finding: dict, decision: dict) -> None:
    fingerprint = sha(
        f"{finding['key']}|{finding['normalized_title']}|{finding['content_hash']}"
    )
    severity_dir = "high" if finding["severity"] == "HIGH" else "medium"
    name = (
        f"{slug(finding['report'])}-{finding['finding_id'].lower()}-"
        f"{slug(finding['title'])}-{fingerprint[:10]}.md"
    )[:180]
    path = OUT / severity_dir / name
    path.parent.mkdir(parents=True, exist_ok=True)
    card = f"""# Pashov Audit Pattern: {finding['title']}

- Source: Pashov Audit Group
- Imported: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}
- Severity: {finding['severity']}
- Report: `{finding['report']}` ({finding['category']})
- Finding ID: `{finding['finding_id']}`
- Source finding: <{finding['source_url']}>
- Dedupe key: `{finding['key']}`
- Fingerprint: `{fingerprint}`

## Core Idea

{text_field(decision, 'core_idea')}

## Broken Invariant

{text_field(decision, 'broken_invariant')}

## Where To Look

{text_field(decision, 'where_to_look')}

## Attack Path

{text_field(decision, 'attack_path')}

## False-Positive Checks

{text_field(decision, 'false_positive_checks')}

## PoC Shape

{text_field(decision, 'poc_shape')}

## Triage Note

{text_field(decision, 'triage_note')}
"""
    path.write_text(card, encoding="utf-8")
    finding["fingerprint"] = fingerprint
    finding["semantic_fingerprint"] = sha(norm(text_field(decision, "core_idea")))
    finding["card_path"] = str(path)


def main() -> int:
    global OUT, INDEX

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--commit", default="")
    parser.add_argument("--output-root", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    source = args.source_dir.resolve()
    commit = args.commit or commit_for(source)
    if args.output_root:
        OUT = args.output_root.resolve()
        INDEX = OUT / "indexes" / "pashov-audits-findings-index.jsonl"

    existing_titles = {
        norm(str(row.get("title", "")))
        for path in OTHER_INDEXES
        for row in read_jsonl(path)
        if row.get("title")
    }
    decisions = {str(row["key"]): row for row in read_jsonl(DECISIONS)}
    prior = read_jsonl(INDEX)
    seen_keys = {str(row.get("dedupe_id", "")) for row in prior}
    seen_content = {str(row.get("content_hash", "")) for row in prior}
    seen_semantic = {str(row.get("semantic_fingerprint", "")) for row in prior}
    counts = {name: 0 for name in (
        "total", "existing_title", "reviewed_skip", "already_imported",
        "duplicate_content", "duplicate_semantic", "unreviewed",
        "imported_high", "imported_medium",
    )}
    additions = []
    unreviewed = []

    for finding in parse(source, commit):
        counts["total"] += 1
        key = finding["key"]
        if finding["normalized_title"] in existing_titles:
            counts["existing_title"] += 1
            continue
        if key in seen_keys:
            counts["already_imported"] += 1
            continue
        decision = decisions.get(key)
        if decision is None:
            counts["unreviewed"] += 1
            unreviewed.append(f"{key} | {finding['title']}")
            continue
        if decision.get("decision") != "import":
            counts["reviewed_skip"] += 1
            continue
        semantic = sha(norm(text_field(decision, "core_idea")))
        if finding["content_hash"] in seen_content:
            counts["duplicate_content"] += 1
            continue
        if semantic in seen_semantic:
            counts["duplicate_semantic"] += 1
            continue
        if not args.dry_run:
            write_card(finding, decision)
        else:
            finding.update(fingerprint=sha(key), semantic_fingerprint=semantic, card_path="")
        additions.append(finding)
        seen_keys.add(key)
        seen_content.add(finding["content_hash"])
        seen_semantic.add(semantic)
        counts["imported_high" if finding["severity"] == "HIGH" else "imported_medium"] += 1

    if additions and not args.dry_run:
        INDEX.parent.mkdir(parents=True, exist_ok=True)
        with INDEX.open("a", encoding="utf-8") as handle:
            for finding in additions:
                row = {
                    "dedupe_id": finding["key"],
                    "fingerprint": finding["fingerprint"],
                    "semantic_fingerprint": finding["semantic_fingerprint"],
                    "content_hash": finding["content_hash"],
                    "severity": finding["severity"],
                    "finding_id": finding["finding_id"],
                    "title": finding["title"],
                    "report": finding["report"],
                    "category": finding["category"],
                    "source": "Pashov Audit Group",
                    "source_url": finding["source_url"],
                    "source_commit": commit,
                    "card_path": finding["card_path"],
                }
                handle.write(json.dumps(row, sort_keys=True) + "\n")

    print(json.dumps({"commit": commit, **counts}, indent=2, sort_keys=True))
    if unreviewed:
        print("Unreviewed findings:")
        print("\n".join(f"- {item}" for item in unreviewed))
    return 2 if unreviewed else 0


if __name__ == "__main__":
    raise SystemExit(main())
