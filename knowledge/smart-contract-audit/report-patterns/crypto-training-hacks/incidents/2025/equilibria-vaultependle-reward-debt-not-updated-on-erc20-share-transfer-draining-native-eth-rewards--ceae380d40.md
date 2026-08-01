# Crypto Training Exploit Pattern Stub: Equilibria (VaultEPendle) — reward debt not updated on ERC20 share transfer, draining native-ETH rewards via fresh receivers

Source:
- https://crypto.training/hacks/2025-08-EquilibriaEPendle/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Ethereum

Loss / impact summary:
- ~62,661.57 USD (≈ 13.29 ETH drained in this reproduction; on-chain incident per @KeyInfo)

Tags:
- logic/missing-state-update, logic/state-update, access-control/missing-auth

Dedupe:
- id: `2025-08-EquilibriaEPendle`
- fingerprint: `ceae380d4068d9e36742cfc40a7d4ea107b16f7abb2c2f0d804346dca21e758b`

Core exploit idea:
- Equilibria's VaultEPendle ("stk-ePendle") is a single-asset auto-compounding vault that wraps ePendle (Equilibria's 1:1 escrowed Pendle) and distributes extra EQB / xEQB…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
