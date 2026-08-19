# Crypto Training Exploit Pattern Stub: Zero Staking: reentrancy in `stake()` re-credits a stale reward timestamp to drain the reward pool

Source:
- https://crypto.training/hacks/59357-malicious-user-can-drain-rewards-through-reentrancy-in-sta/

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
- id: `59357-malicious-user-can-drain-rewards-through-reentrancy-in-sta`
- fingerprint: `2a9f2bee883c6ebea4b0348b6af789d50a9bb86ef6d5ae680ecd70f35ce69848`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
