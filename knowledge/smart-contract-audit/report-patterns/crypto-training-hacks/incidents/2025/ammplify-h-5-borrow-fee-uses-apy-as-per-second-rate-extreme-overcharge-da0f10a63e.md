# Crypto Training Exploit Pattern Stub: Ammplify — H-5: Borrow fee uses APY as per-second rate (extreme overcharge)

Source:
- https://crypto.training/hacks/63171-h-5-borrow-fee-uses-apy-as-per-second-rate-causing-extreme-o/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `63171-h-5-borrow-fee-uses-apy-as-per-second-rate-causing-extreme-o`
- fingerprint: `da0f10a63eb131257f5ce8323ebf76d32217e271dd6e112510f78f4a9c21ff5a`

Core exploit idea:
- 1. Smooth rate curve returns an annual rate (APY) in Q64.64. 2. chargeTrueFeeRate does takerRateX64 = timeDiff * calculateRateX64(util) with no / 365 days. 3. Even 1 sec…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
