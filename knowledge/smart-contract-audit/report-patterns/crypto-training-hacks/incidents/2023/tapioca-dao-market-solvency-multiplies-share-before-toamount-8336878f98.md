# Crypto Training Exploit Pattern Stub: Tapioca DAO — Market solvency multiplies share before toAmount

Source:
- https://crypto.training/hacks/27535-h-45-sglliquidation-computeassetamounttosolvency-market-isso/

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
- id: `27535-h-45-sglliquidation-computeassetamounttosolvency-market-isso`
- fingerprint: `8336878f9899be756077a7032c9fa45c134961f0eefcbd86e78ec694f898e39b`

Core exploit idea:
- 1. Solvency multiplies userCollateralShare by rate factors before yieldBox.toAmount. 2. Dust shares that convert to 0 amount inflate into non-zero collateral value. 3. U…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
