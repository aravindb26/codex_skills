# Crypto Training Exploit Pattern Stub: Megapot — Unoptimized subset matches counting exceeds Base tx gas limit

Source:
- https://crypto.training/hacks/64141-h-02-unoptimized-subset-matches-counting-implementation-will/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `64141-h-02-unoptimized-subset-matches-counting-implementation-will`
- fingerprint: `8c237c361cf373402a4911015c3a980c39a6ac890feaed088ea6e239288e0acc`

Core exploit idea:
- _countSubsetMatches regenerates subsets for every bonusball. At bonusballMax=129 the settlement callback measures ~25.8M gas and exceeds Base's 25M per-tx limit, so Pyth…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
