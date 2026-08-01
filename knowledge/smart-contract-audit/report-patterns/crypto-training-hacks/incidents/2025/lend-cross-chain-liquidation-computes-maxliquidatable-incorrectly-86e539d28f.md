# Crypto Training Exploit Pattern Stub: LEND — Cross-chain liquidation computes maxLiquidatable incorrectly

Source:
- https://crypto.training/hacks/58377-lend-cross-chain-liquidation-computes-maxliquidatable-incorrectly/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/liquidation-logic, logic/incorrect-state-transition

Dedupe:
- id: `58377-lend-cross-chain-liquidation-computes-maxliquidatable-incorrectly`
- fingerprint: `86e539d28f8944b6b074ab9b1587088265ff2a611765c4e669f76a2d4bee276e`

Core exploit idea:
- The maximum liquidation amount is derived from collateral seized rather than outstanding debt, making valid liquidations fail or leaving bad debt.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
