# Crypto Training Exploit Pattern Stub: LEND — Liquidation validation logic is wrong

Source:
- https://crypto.training/hacks/58391-lend-liquidation-validation-logic-is-wrong/

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
- logic/liquidation-logic, logic/wrong-condition

Dedupe:
- id: `58391-lend-liquidation-validation-logic-is-wrong`
- fingerprint: `f2d45c266086b717737bb01142312a143151277a98d85db3374c693c49ea5d9d`

Core exploit idea:
- The validation condition accepts a healthy position because the comparison is inverted, so a liquidator can seize collateral at spot price.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
