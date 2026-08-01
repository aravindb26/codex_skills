# Crypto Training Exploit Pattern Stub: Xocolatl AccountLiquidator — arbitrary caller-supplied HouseOfReserve zeroes the liquidation cost

Source:
- https://crypto.training/hacks/2026-03-XocolatlLiquidator/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2026

Chain:
- Base

Loss / impact summary:
- 3.25 cbETH + 0.22 WETH (≈$11.2k at the time)

Tags:
- access-control/missing-validation, logic/liquidation-logic, arithmetic/rounding

Dedupe:
- id: `2026-03-XocolatlLiquidator`
- fingerprint: `86bb499b2ee28a27075f47fd36686b58085959d157c43d827c275f1f9da19cff`

Core exploit idea:
- Xocolatl is an over-collateralized CDP system on Base: users deposit cbETH/WETH into a HouseOfReserve, receive a minted (backed) token as debt, and can be liquidated thr…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
