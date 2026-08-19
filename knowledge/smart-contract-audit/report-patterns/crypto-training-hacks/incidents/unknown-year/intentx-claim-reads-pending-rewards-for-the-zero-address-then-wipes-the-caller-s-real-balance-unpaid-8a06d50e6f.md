# Crypto Training Exploit Pattern Stub: IntentX: claim() reads pending rewards for the zero address, then wipes the caller's real balance unpaid

Source:
- https://crypto.training/hacks/59427-user-pending-rewards-can-never-be-paid-out-quantstamp-inte/

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
- id: `59427-user-pending-rewards-can-never-be-paid-out-quantstamp-inte`
- fingerprint: `8a06d50e6f9da422f85ad9e952f456883355d368ba45e4ffb0e22a23497ebb9d`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
