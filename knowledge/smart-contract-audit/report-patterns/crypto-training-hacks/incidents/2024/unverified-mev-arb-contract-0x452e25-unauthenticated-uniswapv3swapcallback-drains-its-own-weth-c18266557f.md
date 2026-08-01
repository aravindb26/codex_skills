# Crypto Training Exploit Pattern Stub: Unverified MEV/Arb Contract `0x452E25…` — Unauthenticated `uniswapV3SwapCallback` Drains Its Own WETH

Source:
- https://crypto.training/hacks/2024-07-UnverifiedContr_0x452E25/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2024

Chain:
- Ethereum

Loss / impact summary:
- 27.349 WETH (~$90.3K @ ≈ $3,300/ETH on the day) drained from the contract's own balance

Tags:
- access-control/missing-auth

Dedupe:
- id: `2024-07-UnverifiedContr_0x452E25`
- fingerprint: `c18266557fc33a9bb9bcb9b00b052d148a86087a264fde0a109479d067c25449`

Core exploit idea:
- The vulnerable address is an unverified contract — almost certainly a private MEV/arbitrage helper that performs Uniswap V3 swaps and therefore implements the Uniswap V3…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
