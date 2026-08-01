# Crypto Training Exploit Pattern Stub: LEND — Liquidating CoreRouter can cause excess borrower loss

Source:
- https://crypto.training/hacks/58386-lend-liquidating-corerouter-can-cause-excess-borrower-loss/

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
- id: `58386-lend-liquidating-corerouter-can-cause-excess-borrower-loss`
- fingerprint: `e47d0f9e97c6a871be4eb7a84f1f62314d25853aa95c76171e05f9602e20bf94`

Core exploit idea:
- The router applies the seized collateral amount as repayment and charges the borrower for more debt than the liquidator paid.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
