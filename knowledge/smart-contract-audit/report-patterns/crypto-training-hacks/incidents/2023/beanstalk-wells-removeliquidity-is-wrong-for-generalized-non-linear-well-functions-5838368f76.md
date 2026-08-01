# Crypto Training Exploit Pattern Stub: Beanstalk Wells — `removeLiquidity` is wrong for generalized (non-linear) Well functions

Source:
- https://crypto.training/hacks/18433-removeliquidity-logic-is-not-correct-for-generalized-well-fu/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-condition, math/invariant-violation

Dedupe:
- id: `18433-removeliquidity-logic-is-not-correct-for-generalized-well-fu`
- fingerprint: `5838368f764806d7abbf0aebe520799db0fcdcac4a2b53225623aefc070c2d28`

Core exploit idea:
- 1. addLiquidity mints LP using the Well function (calcLpTokenSupply), so the invariant holds on the way in. 2. removeLiquidity does not invert the Well function — it pay…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
