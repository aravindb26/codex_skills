# Crypto Training Exploit Pattern Stub: Balancer V1 BPool — `joinswapPoolAmountOut` rounding drain (empirical reconstruction)

Source:
- https://crypto.training/hacks/2026-08-balancerv1bpool/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Ethereum

Loss / impact summary:
- This pool ~$110,839 (99% of DPI/USDC/WETH/WBTC). SlowMist ~$234k is the five-pool aggrega…

Tags:
- arithmetic/rounding, arithmetic/precision-loss, arithmetic/decimal-mismatch, logic/price-calculation

Dedupe:
- id: `2026-08-balancerv1bpool`
- fingerprint: `78ca51e9d37076a2957eac24816b433cf5f9e4e57c80ac06029e5eeedfce018f`

Core exploit idea:
- Balancer V1 joinswapPoolAmountOut lets the caller name the BPT out; the pool reverse-computes the single-token deposit via 18-decimal bmul/bdiv/bpow. MIN_BALANCE is only…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
