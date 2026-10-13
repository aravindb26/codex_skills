# Solodit Imports

This folder stores Solodit High and Medium severity findings as compact pattern stubs and metadata indexes.

Do not store full raw report bodies here by default. Keep links to Solodit/source reports and distill useful findings into reusable pattern cards.

## API Key

Solodit requires a Cyfrin API key.

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

Import one page of High/Medium findings:

```bash
/home/dinesh/.codex/knowledge/smart-contract-audit/scripts/solodit_ingest.py --max-pages 1
```

Import several pages while respecting the documented 20 requests/minute rate limit:

```bash
/home/dinesh/.codex/knowledge/smart-contract-audit/scripts/solodit_ingest.py --max-pages 10 --delay 3.2
```

If the protected API key is unavailable, use the public website query path:

```bash
/home/dinesh/.codex/knowledge/smart-contract-audit/scripts/solodit_ingest.py --source public --max-pages 10 --delay 3.2
```

The public route returns ten High/Medium findings per page and is intentionally throttled. It stores the same compact stubs and uses the same dedupe index; it does not bypass login-protected data or store full report bodies. The public website query format may change, so use the API source when a valid key is available.

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
