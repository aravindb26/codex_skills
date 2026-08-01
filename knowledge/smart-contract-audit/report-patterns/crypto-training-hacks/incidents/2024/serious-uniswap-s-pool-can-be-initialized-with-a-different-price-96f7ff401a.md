# Crypto Training Exploit Pattern Stub: Serious — Uniswap's pool can be initialized with a different price

Source:
- https://crypto.training/hacks/36318-c-02-uniswaps-pool-can-be-initialized-with-a-different-price/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- oracle/spot-price-manipulation, dex/front-run-pool-init, logic/unverified-external-state

Dedupe:
- id: `36318-c-02-uniswaps-pool-can-be-initialized-with-a-different-price`
- fingerprint: `96f7ff401a7d2e861df49bac306f6941a19b1060707498e051638eb214b54a17`

Core exploit idea:
- 1. createPoolAndAddLiquidity creates AND initializes the Uniswap V3 pool only if it doesn't already exist. 2. Anyone can create and initialize a Uniswap V3 pool for any…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
