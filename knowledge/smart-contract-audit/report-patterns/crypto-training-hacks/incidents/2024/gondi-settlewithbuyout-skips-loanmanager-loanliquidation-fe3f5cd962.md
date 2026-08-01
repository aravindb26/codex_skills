# Crypto Training Exploit Pattern Stub: Gondi — settleWithBuyout skips LoanManager.loanLiquidation

Source:
- https://crypto.training/hacks/35208-h-06-function-settlewithbuyout-does-not-call-loanmanagerloan/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `35208-h-06-function-settlewithbuyout-does-not-call-loanmanagerloan`
- fingerprint: `fe3f5cd9621d29fe9d7e66cf00af792eacde50fc2235ddd22c56e6905cf45add`

Core exploit idea:
- 1. Gondi Pool implements LoanManager.loanLiquidation to clear outstanding and credit cash/queues. 2. settleWithBuyout transfers owed principal to other lenders (includin…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
