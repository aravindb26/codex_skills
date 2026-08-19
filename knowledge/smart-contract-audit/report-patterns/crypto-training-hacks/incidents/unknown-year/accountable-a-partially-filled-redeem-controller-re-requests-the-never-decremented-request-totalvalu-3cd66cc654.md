# Crypto Training Exploit Pattern Stub: Accountable: A partially-filled redeem controller re-requests; the never-decremented request.totalValue

Source:
- https://crypto.training/hacks/62971-partial-redemptions-can-be-used-to-steal-assets-cyfrin-none/

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
- unknown

Dedupe:
- id: `62971-partial-redemptions-can-be-used-to-steal-assets-cyfrin-none`
- fingerprint: `3cd66cc654f48f64fe20b3973edf9e2303e6f2681bc42fba20cd0275fbede8f4`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
