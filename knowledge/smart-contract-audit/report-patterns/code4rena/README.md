# Code4rena Imports

This folder stores Code4rena High and Medium severity findings as compact pattern stubs and metadata indexes.

Do not store full raw report bodies here by default. Keep links to Code4rena reports and distill useful findings into reusable pattern cards.

## Source

The importer uses public Code4rena pages:

- report discovery: `https://code4rena.com/sitemap.xml`
- report pages: `https://code4rena.com/reports/<slug>`

No API key is required.

## Import

Import the first 10 discovered reports:

```bash
/home/dinesh/.codex/knowledge/smart-contract-audit/scripts/code4rena_ingest.py --discover --max-reports 10
```

Import one specific report:

```bash
/home/dinesh/.codex/knowledge/smart-contract-audit/scripts/code4rena_ingest.py --slug 2024-06-size
```

Preview without writing files:

```bash
/home/dinesh/.codex/knowledge/smart-contract-audit/scripts/code4rena_ingest.py --slug 2024-06-size --dry-run
```

Import all discovered reports carefully:

```bash
/home/dinesh/.codex/knowledge/smart-contract-audit/scripts/code4rena_ingest.py --discover --all --delay 1.0
```

## Dedupe

The importer skips duplicates using:

- report slug + finding anchor
- SHA-256 fingerprint of source URL + title + report slug + severity

Imported metadata is appended to:

```text
indexes/code4rena-findings-index.jsonl
```

Generated pattern stubs go into:

```text
high/
medium/
```

Each stub starts as `needs distillation`. When a finding is useful, fill in the reusable attack pattern, invariant, attack path, false-positive checks, and PoC shape.
