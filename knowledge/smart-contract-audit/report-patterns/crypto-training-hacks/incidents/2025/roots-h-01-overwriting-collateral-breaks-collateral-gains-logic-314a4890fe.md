# Crypto Training Exploit Pattern Stub: Roots — [H-01] Overwriting collateral breaks collateral gains logic

Source:
- https://crypto.training/hacks/55111-h-01-overwriting-collateral-breaks-collateral-gains-logic-pa/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `55111-h-01-overwriting-collateral-breaks-collateral-gains-logic-pa`
- fingerprint: `314a4890febef48672c72cd75b630a558e3a8a542c6210e8296adf2c7edfc503`

Core exploit idea:
- 1. Alice accrues coll-A gains on stability-pool index 0 and leaves them unclaimed. 2. Coll A is sunset; coll C is enabled and reuses index 0. 3. Product sums for index 0…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
