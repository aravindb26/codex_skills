# Crypto Training Exploit Pattern Stub: Zaros — SettlementBranch._fillOrder does not guarantee collateral covers the future liquidation fee

Source:
- https://crypto.training/hacks/37983-settlementbranch-fillorder-does-not-guarantee-the-collateral/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/missing-validation, loss-of-funds/fee-shortfall, economic-design/underfunded-liquidation

Dedupe:
- id: `37983-settlementbranch-fillorder-does-not-guarantee-the-collateral`
- fingerprint: `f7c3be2c77d9ddc0075fa5f754251d37a28be1051159d8ea91abef8dcd30d1c1`

Core exploit idea:
- 1. Opening a position (_fillOrder) deducts the settlement fee and order fee from the trader's margin balance. 2. It never checks that whatever margin remains afterward c…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
