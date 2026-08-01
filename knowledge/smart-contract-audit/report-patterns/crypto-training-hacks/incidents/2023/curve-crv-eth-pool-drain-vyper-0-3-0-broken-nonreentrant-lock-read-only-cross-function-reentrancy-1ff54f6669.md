# Crypto Training Exploit Pattern Stub: Curve `crv/ETH` Pool Drain — Vyper 0.3.0 Broken `@nonreentrant` Lock (Read-Only/Cross-Function Reentrancy)

Source:
- https://crypto.training/hacks/2023-07-Curve_exp02/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2023

Chain:
- Ethereum

Loss / impact summary:
- ~7,929.44 WETH extracted in the reproduced single-transaction PoC. The wider July-30-2023…

Tags:
- unknown

Dedupe:
- id: `2023-07-Curve_exp02`
- fingerprint: `1ff54f6669b7aa336e4e0671a8896a2f411e9ca6d68c94494f6b8d070a5b4f56`

Core exploit idea:
- The Curve crv/ETH pool is a two-coin crypto-swap pool written in Vyper 0.3.0. Every state-changing entry point (exchange, add_liquidity, remove_liquidity, remove_liquidi…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
