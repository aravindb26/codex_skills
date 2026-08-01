# Crypto Training Exploit Pattern Stub: Maia DAO — redeem() in beforeRedeem uses the wrong owner parameter

Source:
- https://crypto.training/hacks/26041-h-07-redeem-in-beforeredeem-is-using-the-wrong-owner-paramet/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `26041-h-07-redeem-in-beforeredeem-is-using-the-wrong-owner-paramet`
- fingerprint: `1f80b757a61b15a6323b4622c1d0c1bc2580124e0776c43c460f84efede80e7d`

Core exploit idea:
- 1. redeem burns _owner shares but calls beforeRedeem(receiver).\n2. flywheel.accrue hits receiver (0 shares).\n3. Owner never accrues; rewards stranded in flywheel.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
