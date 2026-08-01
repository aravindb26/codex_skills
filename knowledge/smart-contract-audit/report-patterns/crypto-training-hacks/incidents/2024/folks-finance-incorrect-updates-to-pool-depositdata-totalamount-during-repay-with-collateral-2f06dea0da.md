# Crypto Training Exploit Pattern Stub: Folks Finance — incorrect updates to `pool.depositData.totalAmount` during repay-with-collateral

Source:
- https://crypto.training/hacks/61090-incorrect-updates-to-pooldepositdatatotalamount-and-loancoll/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- accounting/double-count, logic/repay-with-collateral, loss-of-funds/pool-insolvency

Dedupe:
- id: `61090-incorrect-updates-to-pooldepositdatatotalamount-and-loancoll`
- fingerprint: `2f06dea0da75dd86332e8a332278ee05f3b3851b4d67630f73f961459e168fcd`

Core exploit idea:
- 1. When a borrower repays with collateral, LoanManagerLogic.updateWithRepayWithCollateral updates the pool's total deposits with pool.depositData.totalAmount -= principa…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
