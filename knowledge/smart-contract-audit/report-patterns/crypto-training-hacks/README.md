# Crypto Training Hacks Pattern Stubs

Source:
- <https://crypto.training/hacks/>

Purpose:
- Searchable local leads from reproduced on-chain exploits.
- Compact incident cards only, not copied full article bodies.
- Useful for mapping real exploit patterns to current audit surfaces.

Use during audits:
- Search by protocol family, function behavior, value-flow word, invariant, chain, or vulnerability tag.
- Open the source link when a card matches a live candidate and exact details are needed.
- Treat these as lead-generation memory, not as duplicate authority or proof.

Do not:
- Bulk-load unrelated cards into a live audit.
- Submit a finding only because it resembles a known exploit.
- Mark a candidate duplicate unless exact root cause, function/path, broken invariant, attacker setup, and impact overlap are proven.

Importer:
- `/home/dinesh/.codex/knowledge/smart-contract-audit/scripts/crypto_training_hacks_ingest.py`

