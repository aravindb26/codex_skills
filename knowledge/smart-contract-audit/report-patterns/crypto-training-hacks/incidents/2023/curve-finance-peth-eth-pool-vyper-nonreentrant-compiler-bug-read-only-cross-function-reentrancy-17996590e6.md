# Crypto Training Exploit Pattern Stub: Curve Finance pETH/ETH Pool — Vyper `@nonreentrant` Compiler Bug Read-Only/Cross-Function Reentrancy

Source:
- https://crypto.training/hacks/2023-07-Curve_exp01/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2023

Chain:
- Ethereum

Loss / impact summary:
- 6,107.41 WETH net profit drained from the pETH/ETH pool (~$11.4M of pool TVL at the time)…

Tags:
- unknown

Dedupe:
- id: `2023-07-Curve_exp01`
- fingerprint: `17996590e6e44d94a5a1912ecae588d30813e5ab2cdff23e2eb5753198228719`

Core exploit idea:
- The pETH/ETH pool is a Curve StableSwap written in Vyper 0.2.15. Every state-mutating entry point — add_liquidity, exchange, remove_liquidity, … — carries a @nonreentran…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
