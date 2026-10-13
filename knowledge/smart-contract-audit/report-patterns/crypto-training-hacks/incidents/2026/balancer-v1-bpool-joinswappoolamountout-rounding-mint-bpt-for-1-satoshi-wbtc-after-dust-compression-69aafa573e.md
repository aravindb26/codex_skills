# Crypto Training Exploit Pattern Stub: Balancer V1 BPool `joinswapPoolAmountOut` rounding — mint BPT for 1 satoshi WBTC after dust compression

Source:
- https://crypto.training/hacks/2026-08-balancerv1joinswaprounding/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Ethereum

Loss / impact summary:
- ~$234k USD across DPI / USDC / WETH / WBTC. PoC residual after flash stand-in repay: 546.…

Tags:
- arithmetic/rounding, arithmetic/precision-loss, arithmetic/decimal-mismatch, logic/price-calculation

Dedupe:
- id: `2026-08-balancerv1joinswaprounding`
- fingerprint: `69aafa573e9ef2706f454154a385c411b831902aac4576dad72297e5d639d961`

Core exploit idea:
- Balancer V1’s joinswapPoolAmountOut lets a caller choose how much BPT to mint and then reverse-computes the required single-token deposit via calcSingleInGivenPoolOut. T…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
