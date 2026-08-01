# Crypto Training Exploit Pattern Stub: Rubicon — Opening a position reuses prior collateral for borrowing

Source:
- https://crypto.training/hacks/48952-h-13-when-opening-a-position-the-collateral-of-the-previous/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `48952-h-13-when-opening-a-position-the-collateral-of-the-previous`
- fingerprint: `c84ea812ed522d9e63418bdb5c6c415b6a31a3a5a48f1bba942d25ae55608027`

Core exploit idea:
- openPosition borrow budget uses _maxBorrow which includes residual capacity from prior positions on the shared Position account.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
