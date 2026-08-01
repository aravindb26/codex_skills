# Crypto Training Exploit Pattern Stub: Burve — Incorrect netting logic leads to excessive withdrawal amounts

Source:
- https://crypto.training/hacks/56952-burve-incorrect-netting-logic-leads-to-excessive-withdrawal-amounts/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/incorrect-state-transition, logic/price-calculation

Dedupe:
- id: `56952-burve-incorrect-netting-logic-leads-to-excessive-withdrawal-amounts`
- fingerprint: `a42e227809371371a69978544c7ebfd3853e5bc13a8b5c4a9416b8a73c8600f9`

Core exploit idea:
- Net liabilities are subtracted with the wrong sign, making a withdrawal quote exceed the closure's assets.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
