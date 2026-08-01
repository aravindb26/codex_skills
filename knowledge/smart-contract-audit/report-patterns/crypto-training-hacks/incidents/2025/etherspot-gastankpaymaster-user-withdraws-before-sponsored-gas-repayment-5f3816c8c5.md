# Crypto Training Exploit Pattern Stub: Etherspot GasTankPaymaster — user withdraws before sponsored gas repayment

Source:
- https://crypto.training/hacks/62850-h-03-users-escape-paying-tx-gas/

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
- logic/state-update, dos/frozen-funds

Dedupe:
- id: `62850-h-03-users-escape-paying-tx-gas`
- fingerprint: `5f3816c8c5433c74bbac951c304c0df67415d867d6b2bd8779beb3e10ec80852`

Core exploit idea:
- postOp records a user's gas debt, but withdraw remains unrestricted. The user can empty the GasTank before the asynchronous repayment job runs, leaving the paymaster una…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
