# Crypto Training Exploit Pattern Stub: InitcodeFactory `collectFees` — caller-authorizes via fake token `creator()` and drains ETH on a non-WETH `token1`

Source:
- https://crypto.training/hacks/2025-06-InitcodeFactoryFees/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- Ethereum

Loss / impact summary:
- ~2,383.25 USD (≈ 0.9793 ETH stolen)

Tags:
- access-control/broken-logic, input-validation/missing, logic/incorrect-order-of-operations, dependency/unchecked-return-value

Dedupe:
- id: `2025-06-InitcodeFactoryFees`
- fingerprint: `dc5a172a718c333a5ce08b6e2f6303f639d2377b68576aaa843f723ec70740be`

Core exploit idea:
- Factory (0x930f9f…) is a launchpad that mints its own ERC-20 tokens and seeds a Uniswap V3 pool (token↔WETH, 1% tier). It retains the V3 liquidity NFT itself and exposes…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
