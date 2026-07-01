# Pashov Audit Report Patterns

This directory stores compact, manually reviewed High/Medium pattern cards from
<https://github.com/pashov/audits>. It does not store full reports or PDFs.

## Noise And Duplicate Controls

- Existing Solodit and Code4rena titles are skipped before import.
- Exact report-section content hashes are deduplicated.
- Distilled core-idea fingerprints are deduplicated within this source.
- A finding must have an explicit `import` decision in
  `indexes/reviewed-decisions.jsonl`; new upstream findings remain unreviewed
  until their root cause and usefulness are checked manually.
- Critical, Low, and informational findings are not parsed for import.

The decision manifest records why near-duplicates, generic patterns, and weak
compatibility observations were excluded. This prevents future refreshes from
reintroducing them under changed titles.

## Refresh

Use a temporary sparse clone so PDF blobs are not downloaded:

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/pashov/audits.git /home/dinesh/.cache/pashov-audits-import
git -C /home/dinesh/.cache/pashov-audits-import sparse-checkout set team/md solo/md
python3 /home/dinesh/.codex/knowledge/smart-contract-audit/scripts/pashov_audits_ingest.py \
  --source-dir /home/dinesh/.cache/pashov-audits-import --dry-run
```

Review every reported `Unreviewed finding`, add a decision, then rerun without
`--dry-run`. A clean second run must import zero findings.
