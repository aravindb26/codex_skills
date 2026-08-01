# Crypto Training Exploit Pattern Stub: LEND — Borrower can redeem collateral immediately after borrowing

Source:
- https://crypto.training/hacks/58390-lend-borrower-can-redeem-collateral-immediately-after-borrowing/

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
- logic/incorrect-state-transition, logic/missing-check

Dedupe:
- id: `58390-lend-borrower-can-redeem-collateral-immediately-after-borrowing`
- fingerprint: `ced52bdc6dad750c37cd090d0046e6fc2a4e7d6f8563d0ebac2248a8544290b7`

Core exploit idea:
- The collateral redemption path does not account for a borrow initiated in the same epoch, enabling an immediately undercollateralized position.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
