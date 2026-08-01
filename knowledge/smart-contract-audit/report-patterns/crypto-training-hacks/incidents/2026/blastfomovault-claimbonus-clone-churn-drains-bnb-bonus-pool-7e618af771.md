# Crypto Training Exploit Pattern Stub: BlastFOMOVault `claimBonus` clone-churn drains BNB bonus pool

Source:
- https://crypto.training/hacks/2026-05-BlastFOMOVault/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2026

Chain:
- BNB Chain

Loss / impact summary:
- 1.289508079648543283 BNB offline (historical on-chain ~1.288418562948543283 BNB)

Tags:
- logic/missing-check, access-control/broken-logic, logic/reward-calculation

Dedupe:
- id: `2026-05-BlastFOMOVault`
- fingerprint: `7e618af771fc63773b7d456adbf07ee8cdf5ff313244652e267501f22a98559f`

Core exploit idea:
- 1. BlastFOMOVault turns buy-tax BNB into a decaying hype meter. When hype crosses threshold, Blast Mode opens and anyone can call claimBonus(referrer). 2. Each successfu…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
