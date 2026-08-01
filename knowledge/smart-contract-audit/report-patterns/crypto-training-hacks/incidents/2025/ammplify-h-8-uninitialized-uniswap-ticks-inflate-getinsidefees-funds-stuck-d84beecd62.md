# Crypto Training Exploit Pattern Stub: Ammplify — H-8: Uninitialized Uniswap ticks inflate `getInsideFees` (funds stuck)

Source:
- https://crypto.training/hacks/63174-h-8-incorrect-inside-fees-calculation-for-uninitialized-unis/

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
- id: `63174-h-8-incorrect-inside-fees-calculation-for-uninitialized-unis`
- fingerprint: `d84beecd625b7a418b4ddbcd9ca871a2c0fb86f4894c8464335bf16a3f83962f`

Core exploit idea:
- 1. Open maker while ticks uninitialized and price inside range. 2. Snapshot stores feeGrowthInside = feeGrowthGlobal (inflated). 3. Settle initializes ticks; later getIn…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
