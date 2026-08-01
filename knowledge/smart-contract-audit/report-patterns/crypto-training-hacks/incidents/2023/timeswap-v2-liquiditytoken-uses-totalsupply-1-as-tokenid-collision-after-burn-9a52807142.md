# Crypto Training Exploit Pattern Stub: Timeswap V2 — LiquidityToken uses `totalSupply()+1` as tokenId (collision after burn)

Source:
- https://crypto.training/hacks/24902-h-02-timeswapv/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/reused-identifier, accounting/tokenid-collision, loss-of-funds/balance-manipulation

Dedupe:
- id: `24902-h-02-timeswapv`
- fingerprint: `9a52807142b233031e0778158c48c0830975f50d48fa47cea3d4d7383c584478`

Core exploit idea:
- 1. TimeswapV2LiquidityToken.mint assigns a new position's ERC-1155 tokenId with id = totalSupply() + 1. 2. totalSupply() (from ERC1155Enumerable) is _allTokens.length, w…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
