# Crypto Training Exploit Pattern Stub: Pyth price and exponent mismatch — AuditVault 51982

Source:
- https://crypto.training/hacks/51982-pyth-price-exponent-mismatch/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- oracle/wrong-feed, logic/price-calculation

Dedupe:
- id: `51982-pyth-price-exponent-mismatch`
- fingerprint: `5d511cefd93a7812646af380ce502256b85782b1f1c5ccda7ed0f496f1dfa476`

Core exploit idea:
- A negative Pyth price is converted to an unsigned reported value while the signed stored value remains negative.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
