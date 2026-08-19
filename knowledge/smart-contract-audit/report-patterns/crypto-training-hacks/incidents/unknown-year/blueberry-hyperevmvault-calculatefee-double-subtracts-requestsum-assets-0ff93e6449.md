# Crypto Training Exploit Pattern Stub: Blueberry HyperEvmVault: `_calculateFee` double-subtracts `requestSum.assets`

Source:
- https://crypto.training/hacks/61468-c-01-incorrect-fee-due-to-double-subtracting-requestsumasset/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 1970

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/fee-calculation, arithmetic/underflow

Dedupe:
- id: `61468-c-01-incorrect-fee-due-to-double-subtracting-requestsumasset`
- fingerprint: `0ff93e6449cae93ed8b18bab04ab92505de16fe89ebcd2c06d7f198af3d4da91`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
