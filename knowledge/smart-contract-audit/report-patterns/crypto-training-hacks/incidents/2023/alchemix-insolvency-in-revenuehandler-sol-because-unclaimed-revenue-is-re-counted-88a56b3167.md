# Crypto Training Exploit Pattern Stub: Alchemix — insolvency in `RevenueHandler.sol` because unclaimed revenue is re-counted

Source:
- https://crypto.training/hacks/38111-insolvency-in-revenuehandlersol-because-unclaimed-revenue-is/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- accounting/double-counting, frozen-funds/insolvency, loss-of-funds/direct-drain

Dedupe:
- id: `38111-insolvency-in-revenuehandlersol-because-unclaimed-revenue-is`
- fingerprint: `88a56b3167c8a345c2f180feea52d694f663baaca12aaf6fc61bafb18a8e28aa`

Core exploit idea:
- 1. RevenueHandler.checkpoint() runs once per epoch, reads the contract's current token balance, and records it as this epoch's revenue. 2. For non-alchemic-tokens: amoun…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
