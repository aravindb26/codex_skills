# Crypto Training Exploit Pattern Stub: ParaSpace — [H-09] UniswapV3 tokens of certain pairs will be wrongly valued

Source:
- https://crypto.training/hacks/15982-h-09-uniswapv3-tokens-of-certain-pairs-will-be-wrongly-value/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `15982-h-09-uniswapv3-tokens-of-certain-pairs-will-be-wrongly-value`
- fingerprint: `eac431dcd5eb173dbf84afff47b0918612b0c4e8f84d89f68ec2ff44a71acad1`

Core exploit idea:
- 1. Same-decimal branch: sqrt(token0Price 1e18 / token1Price) 2^96 / 1e9. 2. If token1Price > token0Price * 1e18, inner div is 0 → sqrtPriceX96 = 0. 3. Amount math treats…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
