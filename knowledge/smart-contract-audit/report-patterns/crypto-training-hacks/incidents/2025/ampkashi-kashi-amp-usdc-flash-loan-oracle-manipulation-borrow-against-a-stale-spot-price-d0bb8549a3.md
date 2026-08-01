# Crypto Training Exploit Pattern Stub: AmpKashi (Kashi AMP/USDC) flash-loan oracle manipulation — borrow against a stale spot price

Source:
- https://crypto.training/hacks/2025-04-AmpKashi/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Ethereum

Loss / impact summary:
- 572.31 USDC (attacker net profit; the AMP collateral left in the pair was effectively wor…

Tags:
- oracle/price-manipulation, oracle/spot-price, oracle/stale-price, defi/flash-loan-attack

Dedupe:
- id: `2025-04-AmpKashi`
- fingerprint: `d0bb8549a373c33871e607069f48b7973043a246e1d6d75cc08f948b4790a2e3`

Core exploit idea:
- Kashi is SushiSwap's BentoBox-based money market: each lending market is a thin KashiPairMediumRiskV1 clone that takes one collateral token and lends one asset token, wi…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
