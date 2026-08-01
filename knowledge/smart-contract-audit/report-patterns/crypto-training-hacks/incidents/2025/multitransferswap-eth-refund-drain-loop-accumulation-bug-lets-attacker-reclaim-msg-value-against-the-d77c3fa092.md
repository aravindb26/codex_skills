# Crypto Training Exploit Pattern Stub: MultiTransferSwap ETH refund drain — loop-accumulation bug lets attacker reclaim msg.value against the contract's own balance

Source:
- https://crypto.training/hacks/2025-04-multitransferswap/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Ethereum

Loss / impact summary:
- ~0.339 ETH (339,014,011,988,554,657 wei) drained from the contract; attacker net ~0.3366…

Tags:
- logic/incorrect-order-of-operations, logic/incorrect-state-transition, logic/missing-validation, defi/slippage

Dedupe:
- id: `2025-04-multitransferswap`
- fingerprint: `d77c3fa09279b91352216ebce380e97249509345353fe833964545dd100bb37d`

Core exploit idea:
- MultiTransferSwap is a thin Uniswap-V2 wrapper that lets a caller swap ETH for an exact amount of some output token, repeated times times in a single call. The author me…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
