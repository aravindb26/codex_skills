# Crypto Training Exploit Pattern Stub: Epoch Island: withdrawForfeit recomputes the forfeit on an un-scaled reward base, so partial forfeits over-repay

Source:
- https://crypto.training/hacks/59895-calling-withdrawforfeit-multiple-times-for-a-single-deposi/

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
- id: `59895-calling-withdrawforfeit-multiple-times-for-a-single-deposi`
- fingerprint: `211b4c447a4535943cf97ee6cf701c57db00f60234b99e874bc94669fed95ad1`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
