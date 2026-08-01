# Crypto Training Exploit Pattern Stub: Virtuals — public impact recalculation redirects reward allocation

Source:
- https://crypto.training/hacks/61824-h-03-public-servicenftupdateimpact-call-leads-to-cascading-i/

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
- access-control/missing-auth, logic/reward-calculation, logic/incorrect-state-transition

Dedupe:
- id: `61824-h-03-public-servicenftupdateimpact-call-leads-to-cascading-i`
- fingerprint: `9f3333f8949e12e08e737708480d51ef7871a1f2a07625dba4ed60960da9bdde`

Core exploit idea:
- Impact values determine the allocation used to mint rewards. updateImpact is public, and it persists a recalculated allocation using the current datasetImpactWeight. Aft…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
