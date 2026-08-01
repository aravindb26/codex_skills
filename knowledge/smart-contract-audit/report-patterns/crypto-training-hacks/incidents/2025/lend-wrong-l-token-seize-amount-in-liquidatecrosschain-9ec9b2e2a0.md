# Crypto Training Exploit Pattern Stub: LEND — Wrong L-token seize amount in liquidateCrossChain

Source:
- https://crypto.training/hacks/58374-lend-wrong-l-token-seize-amount-in-liquidatecrosschain/

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
- logic/liquidation-logic, logic/price-calculation

Dedupe:
- id: `58374-lend-wrong-l-token-seize-amount-in-liquidatecrosschain`
- fingerprint: `9ec9b2e2a0ef48cf0124f6fe5fbe21630f8bcf1f0af7e742f6e79e523e9f663b`

Core exploit idea:
- The cross-chain liquidation converts debt to seized L-tokens with the collateral-side exchange rate, overstating the amount seized from a borrower.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
