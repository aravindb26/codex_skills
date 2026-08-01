# Crypto Training Exploit Pattern Stub: Sharwa Margin Trading — Uniswap-V3 spot-price oracle used to value NFT collateral

Source:
- https://crypto.training/hacks/2026-05-SharwaMarginTrading/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2026

Chain:
- Arbitrum

Loss / impact summary:
- ~32.85K USDC (32,850 USDC, 6 decimals)

Tags:
- oracle/spot-price, oracle/manipulable-twap, logic/price-calculation, governance/flash-loan-attack

Dedupe:
- id: `2026-05-SharwaMarginTrading`
- fingerprint: `171813597e3dee24a9dc9f1ebb8bc44d311d73a75baa44b675f8dc624668ecff`

Core exploit idea:
- Sharwa's margin-trading protocol accepts ERC-721 collateral (here a Hegic option NFT, tokenId 16129) and values it through a "UniswapModuleWithoutChainlink" module. That…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
