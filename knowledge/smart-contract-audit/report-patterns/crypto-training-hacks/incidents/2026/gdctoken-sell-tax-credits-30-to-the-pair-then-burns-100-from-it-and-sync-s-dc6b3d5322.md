# Crypto Training Exploit Pattern Stub: GDCToken — sell-tax credits 30% to the pair then burns 100% from it and `sync()`s

Source:
- https://crypto.training/hacks/2026-09-gdctoken/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- BNB Chain

Loss / impact summary:
- Pair drained 38.075473326480291171 WBNB (~$27k). PoC attacker profit 35.15333822653155477…

Tags:
- logic/fee-calculation, logic/incorrect-state-transition, reentrancy/single-function, access-control/broken-logic

Dedupe:
- id: `2026-09-gdctoken`
- fingerprint: `dc6b3d5322b7f9f4d6cee5e2ad1928404927bd564361074796dea77489572806`

Core exploit idea:
- GDC is a BSC “deposit / deflation / node-reward” token paired against WBNB. Ordinary buys from the pair revert BuyingProhibited. Sells into the pair run swapSellAward: 7…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
