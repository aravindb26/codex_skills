# Crypto Training Exploit Pattern Stub: Shiny Pawn — off-chain offer amount creates underwater loans

Source:
- https://crypto.training/hacks/64681-h-01-protocol-insolvency-risk-lack-on-chain-oracle/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- oracle/missing-validation, logic/liquidation-logic

Dedupe:
- id: `64681-h-01-protocol-insolvency-risk-lack-on-chain-oracle`
- fingerprint: `70983c41abcb2a21d5ea12136da0e365006c263d45e5052e2b9fbccdc1733fe0`

Core exploit idea:
- Pawn trusts a backend-signed offerAmount without checking collateral value on-chain, then permits liquidation only after a deadline. A price drop during the term creates…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
