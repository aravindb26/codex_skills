# Crypto Training Exploit Pattern Stub: LEND — CoreRouter borrow has an incorrect collateral check

Source:
- https://crypto.training/hacks/58396-lend-corerouter-borrow-has-an-incorrect-collateral-check/

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
- logic/missing-check, logic/wrong-condition

Dedupe:
- id: `58396-lend-corerouter-borrow-has-an-incorrect-collateral-check`
- fingerprint: `a9cdffdc423febe2f7135d3e368d15b228d977efbef29269ff33e022207295c2`

Core exploit idea:
- The borrow check compares debt to the wrong collateral variable, accepting a borrow that exceeds the account's available collateral.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
