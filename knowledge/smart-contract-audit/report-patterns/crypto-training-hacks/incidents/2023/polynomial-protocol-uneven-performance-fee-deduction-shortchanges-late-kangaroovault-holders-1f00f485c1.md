# Crypto Training Exploit Pattern Stub: Polynomial Protocol — uneven performance-fee deduction shortchanges late KangarooVault holders

Source:
- https://crypto.training/hacks/20228-h-05-uneven-deduction-of-performance-fee-causes-some-kangaro/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- accounting/fee-calculation, logic/price-inconsistency, mev/frontrun-exposure

Dedupe:
- id: `20228-h-05-uneven-deduction-of-performance-fee-causes-some-kangaro`
- fingerprint: `1f00f485c1d4ab2896662781647e7ed78914ae3202ae24651088d3e893799ea8`

Core exploit idea:
- 1. While a position is open, getTokenPrice values the vault as totalFunds + premiumCollected + … and subtracts usedFunds + markPrice*short — but not the performanceFee t…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
