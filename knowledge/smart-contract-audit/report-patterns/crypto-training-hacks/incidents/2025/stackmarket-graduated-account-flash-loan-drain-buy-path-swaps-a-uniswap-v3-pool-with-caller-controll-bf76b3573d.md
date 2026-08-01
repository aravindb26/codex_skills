# Crypto Training Exploit Pattern Stub: StackMarket graduated-account flash-loan drain — buy path swaps a Uniswap V3 pool with caller-controlled (zero) slippage, then unwinds at the inflated pool price

Source:
- https://crypto.training/hacks/2025-03-StackMarket/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2025

Chain:
- Base

Loss / impact summary:
- 0.56 WETH (per @KeyInfo; single-attack tx magnitude)

Tags:
- defi/slippage, logic/incorrect-order-of-operations, governance/flash-loan-attack

Dedupe:
- id: `2025-03-StackMarket`
- fingerprint: `bf76b3573d248ee6fad67d0468aeaf335018b06983dd67bd7ddd1f5eadec2b31`

Core exploit idea:
- StackMarket is a Base bonding-curve launchpad: every "account" gets its own ERC-20 (StackToken) that trades on an internal AMM (BondingCurve, y = A·x²/B) until 50 % of t…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
