# Crypto Training Exploit Pattern Stub: UPENG burn+sync drain — permissionless `burn(address,uint256)` lets anyone torch a Uniswap-V2 pair's token side, then `sync()` commits the manipulated balance as reserves

Source:
- https://crypto.training/hacks/2025-07-UPENGBurnSync/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- BNB Chain

Loss / impact summary:
- ~1.5 WBNB (1,500,999,999,999,999,999 wei) — the pair's near-total WBNB reserve [output.tx…

Tags:
- access-control/missing-auth, logic/incorrect-order-of-operations, defi/slippage

Dedupe:
- id: `2025-07-UPENGBurnSync`
- fingerprint: `c4bffa6a529cf58658997ca00ba14653b80cac1fbc09366906a3e2e8cacd18fc`

Core exploit idea:
- UPENG is a low-liquidity BEP-20 token paired against WBNB on PancakeSwap. Its UPENG/WBNB pair held roughly 21,000,000 UPENG against 1.5 WBNB at the time of the attack [o…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
