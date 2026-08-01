# Crypto Training Exploit Pattern Stub: TSAggregatorGeneric arbitrary swap-target calldata drains victim allowance — attacker-chosen `swapRouter`/`data` lets `swapIn()` call any function on any token the aggregator is allowed to spend

Source:
- https://crypto.training/hacks/2025-06-TSAggregatorGeneric/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- BNB Chain

Loss / impact summary:
- 1,300.00 USDT (BEP-20) — 1,300 10*18 [output.txt:1621]

Tags:
- logic/incorrect-order-of-operations, access-control/missing-validation, dependency/unsafe-external-call

Dedupe:
- id: `2025-06-TSAggregatorGeneric`
- fingerprint: `fa91ea0454d748a0fb820f364aef4dad5bb8b07d4db1afb0d3b997f18553db0c`

Core exploit idea:
- TSAggregatorGeneric is the THORChain Saver-style EVM swap aggregator: a user deposits an input token, the aggregator swaps it through some DEX and forwards native BNB to…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
