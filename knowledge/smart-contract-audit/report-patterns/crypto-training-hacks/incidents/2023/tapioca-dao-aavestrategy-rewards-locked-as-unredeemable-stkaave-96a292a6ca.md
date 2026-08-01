# Crypto Training Exploit Pattern Stub: Tapioca DAO — AaveStrategy rewards locked as unredeemable stkAAVE

Source:
- https://crypto.training/hacks/27531-h-41-rewards-compounded-in-aavestrategy-are-unredeemable-cod/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `27531-h-41-rewards-compounded-in-aavestrategy-are-unredeemable-cod`
- fingerprint: `96a292a6ca1a54329985bfa7c7584ab2603acba9bfb35cffdd0fb1d353241efe`

Core exploit idea:
- 1. AAVE incentivesController stakes claimed rewards into stkAAVE immediately. 2. compound() claims incentives but never calls redeem. 3. Strategy holds stkAAVE with zero…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
