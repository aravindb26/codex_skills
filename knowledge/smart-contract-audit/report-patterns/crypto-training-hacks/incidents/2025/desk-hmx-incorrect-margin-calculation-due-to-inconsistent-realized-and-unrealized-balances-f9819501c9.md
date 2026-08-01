# Crypto Training Exploit Pattern Stub: DESK / HMX — Incorrect margin calculation due to inconsistent realized and unrealized balances

Source:
- https://crypto.training/hacks/53108-incorrect-margin-calculation-due-to-inconsistent-realized-an/

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
- logic/liquidation-logic

Dedupe:
- id: `53108-incorrect-margin-calculation-due-to-inconsistent-realized-an`
- fingerprint: `f9819501c97ebf5e96dfa030918ac9409b2982c618cb69918f1f2e5a38a7238b`

Core exploit idea:
- 1. Liquidation margin = getSubaccountTotalMargin (realized, CF already applied) + unsettled PnL. 2. Unsettled PnL only gets the collateral factor when positive; negative…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
