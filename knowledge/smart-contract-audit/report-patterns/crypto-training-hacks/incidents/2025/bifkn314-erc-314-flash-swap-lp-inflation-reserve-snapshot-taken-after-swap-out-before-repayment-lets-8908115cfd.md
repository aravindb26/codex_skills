# Crypto Training Exploit Pattern Stub: BIFKN314 (ERC-314) flash-swap LP inflation — reserve snapshot taken after swap-out, before repayment, lets a dust `addLiquidity` mint pool-dominating LP shares

Source:
- https://crypto.training/hacks/2025-07-AvaxBIFKNPair/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Avalanche

Loss / impact summary:
- ~2,422.73 USD (91.15 AVAX profit, on-chain trace output.txt:1565)

Tags:
- logic/incorrect-order-of-operations, oracle/price-manipulation, logic/state-update, reentrancy/cross-function

Dedupe:
- id: `2025-07-AvaxBIFKNPair`
- fingerprint: `8908115cfdc81da5a8a8d79921cc1a5081936ee035b1382b990a6a817be6b2b2`

Core exploit idea:
- BIFKN314Mintable is an ERC-314-style native/token pair that bundles a Uniswap-V2-like constant-product pool with a built-in flash swap: flashSwap() sends AVAX and the pa…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
