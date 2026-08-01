# Crypto Training Exploit Pattern Stub: JUDAO sell-hook reserve drain — token transfer hook burns liquidity directly from its own DEX pair, desyncing the AMM reserves the attacker then arbitrages

Source:
- https://crypto.training/hacks/2026-04-JUDAO/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2026

Chain:
- BNB Chain

Loss / impact summary:
- 205,259.49 USDT + 36 BNB (≈ $62k at the time)

Tags:
- defi/fee-manipulation, logic/incorrect-order-of-operations, oracle/price-manipulation

Dedupe:
- id: `2026-04-JUDAO`
- fingerprint: `8a836fa213268f838bfe64a5ead1174e8b8d538ad30e8b8dea3c9086003e3647`

Core exploit idea:
- JUDAOToken overrides _update (ERC-20 transfer) to install a buy-mining / sell-deflation economy on top of its PancakeSwap JUDAO/USDT pair. The sell branch, entered when…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
