# Crypto Training Exploit Pattern Stub: Unverified proxy `0x6f7a` drained via permissionless `rebalanceAndAddLiquidity` selector — anyone could push a victim's live token balance through its liquidity path

Source:
- https://crypto.training/hacks/2025-08-unverified_6f7a/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Ethereum

Loss / impact summary:
- 7,630.46 USD reported (~0.25 WETH realized by the attacker on this fork) [output.txt:1539…

Tags:
- access-control/missing-auth, access-control/missing-modifier, defi/price-manipulation, logic/incorrect-order-of-operations

Dedupe:
- id: `2025-08-unverified_6f7a`
- fingerprint: `d477f00817408a1d1a6beeefd2c1f025cc4b81e6d3b43eeba304cc1f6fda0a0c`

Core exploit idea:
- The victim contract 0x6f7a is a proxy that holds a treasury of DAI, WETH and FEI and, through its implementation, can "rebalance" its holdings into liquidity positions b…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
