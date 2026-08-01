# Crypto Training Exploit Pattern Stub: Coinbase Fee-Account Drain — Confused-Deputy via 0x Settler `BASIC` Arbitrary Call

Source:
- https://crypto.training/hacks/2025-08-coinbase/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Ethereum

Loss / impact summary:
- ~$300,000 total across multiple tokens. This PoC reproduces one leg: 105,493.58 ANDY drai…

Tags:
- dependency/unsafe-external-call, logic/missing-check

Dedupe:
- id: `2025-08-coinbase`
- fingerprint: `afd349bbc0a6102f11bace07ed555820b4cbe6abd114a8eb264befbf8b5d9a9f`

Core exploit idea:
- The 0x Settler is a swap router that, by design, can be told to perform a raw external call to any address through its BASIC action (selector 0x38c9c147). The Settler is…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
