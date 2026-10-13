# Solodit Imports

This folder stores Solodit High and Medium severity findings as compact pattern stubs and metadata indexes.

Do not store full raw report bodies here by default. Keep links to Solodit/source reports and distill useful findings into reusable pattern cards.

## Optional API Key

The default importer uses Solodit's public website query path and does not require an API key.
The protected API is optional and requires a valid Cyfrin API key.

Set one of:

```bash
export CYFRIN_API_KEY="sk_your_key_here"
export SOLODIT_API_KEY="sk_your_key_here"
```

Or save the key in:

```text
/home/dinesh/.codex/solodit.env
```

Accepted formats:

```bash
CYFRIN_API_KEY="sk_your_key_here"
```

or raw key text.

## Import

Import one public page of High/Medium findings:

```bash
/home/dinesh/.codex/knowledge/smart-contract-audit/scripts/solodit_ingest.py --max-pages 1
```

Import several public pages while respecting the documented 20 requests/minute rate limit:

```bash
/home/dinesh/.codex/knowledge/smart-contract-audit/scripts/solodit_ingest.py --max-pages 10 --delay 3.2
```

Use the protected API only explicitly when a valid key is available:

```bash
/home/dinesh/.codex/knowledge/smart-contract-audit/scripts/solodit_ingest.py --source api --max-pages 10 --delay 3.2
```

The public route returns ten High/Medium findings per page and is intentionally throttled. It stores the same compact stubs and uses the same dedupe index; it does not bypass login-protected data or store full report bodies. The public website query format may change, so use the protected API explicitly only when needed.

## Dedupe

The importer skips duplicates using:

- Solodit ID / slug / URL when available
- SHA-256 fingerprint of title + source URL + protocol + severity

Imported metadata is appended to:

```text
indexes/solodit-findings-index.jsonl
```

Generated pattern stubs go into:

```text
high/
medium/
```

Each stub starts as `needs distillation`. When a finding is useful, fill in the reusable attack pattern, invariant, attack path, false-positive checks, and PoC shape.
