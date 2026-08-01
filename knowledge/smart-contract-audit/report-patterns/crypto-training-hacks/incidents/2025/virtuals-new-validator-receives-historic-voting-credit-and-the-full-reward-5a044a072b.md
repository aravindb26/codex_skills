# Crypto Training Exploit Pattern Stub: Virtuals — new validator receives historic voting credit and the full reward

Source:
- https://crypto.training/hacks/61826-h-05-validatorregistryvalidatorscoregetpastvalidatorscore-al/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/reward-calculation, logic/incorrect-state-transition, logic/missing-check

Dedupe:
- id: `61826-h-05-validatorregistryvalidatorscoregetpastvalidatorscore-al`
- fingerprint: `5a044a072be7baf59293145f10f543df17f0129bae4d068ed6b794ab9714e06a`

Core exploit idea:
- A validator score should count actual engagement. When a validator is initialized, the audited code assigns its base score to the total number of past proposals. That ma…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
