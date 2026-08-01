# Crypto Training Exploit Pattern Stub: GTE — swap drains pair via phantom amountIn from launchpad fees

Source:
- https://crypto.training/hacks/64852-h-04-attacker-can-drain-funds-from-gtelaunchpadv2pair-using/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `64852-h-04-attacker-can-drain-funds-from-gtelaunchpadv2pair-using`
- fingerprint: `3cb40a5a7f8193c5dad37e4ba587a55ccc0ce51a7563cf5b7ab4a6f01bb06dd8`

Core exploit idea:
- 1. Reserves exclude accrued launchpad fees; balances include them. 2. amountIn is inferred as balance - (reserve - amountOut). 3. Taking amountOut ≈ fee with no transfer…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
