# Crypto Training Exploit Pattern Stub: Accountable — `AccountableOpenTerm` interest cannot be repaid once principal hits zero

Source:
- https://crypto.training/hacks/62973-accountableopenterm-loan-interest-cannot-be-repaid-once-prin/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/debt-accounting

Dedupe:
- id: `62973-accountableopenterm-loan-interest-cannot-be-repaid-once-prin`
- fingerprint: `b3431bd20ef78aec8eb6a8c391701bc07805cc1ec39040c1c54dc95152bb6974`

Core exploit idea:
- 1. Interest accrues virtually via _scaleFactor / scaleFactor. 2. repay() only reduces outstandingPrincipal; excess for interest is optional. 3. When principal reaches ze…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
