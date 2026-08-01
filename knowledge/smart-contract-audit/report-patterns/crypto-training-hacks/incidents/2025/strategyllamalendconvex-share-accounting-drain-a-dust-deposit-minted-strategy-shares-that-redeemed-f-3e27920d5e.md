# Crypto Training Exploit Pattern Stub: StrategyLlamaLendConvex share-accounting drain — a dust deposit minted strategy shares that redeemed for the strategy's entire Curve Lend position

Source:
- https://crypto.training/hacks/2025-07-StrategyLlamaLendConvex/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Ethereum

Loss / impact summary:
- 563.12 USDC (crvUSD-denominated drain of ~563 crvUSD from the strategy's Curve Lend / Con…

Tags:
- logic/incorrect-state-transition, defi/slippage, logic/price-calculation, arithmetic/precision-loss

Dedupe:
- id: `2025-07-StrategyLlamaLendConvex`
- fingerprint: `3e27920d5e6b24f567514b72cadf4aec8c27c362eb6aefc0f055b1c70f1415ae`

Core exploit idea:
- StrategyLlamaLendConvex is a Yearn V3 "tokenized strategy" that takes crvUSD as its asset and routes it into a Curve Lend vault (an ERC-4626), then stakes the resulting…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
