# Crypto Training Exploit Pattern Stub: Autonomint withdrawUser deduction — AuditVault 45460

Source:
- https://crypto.training/hacks/45460-autonomint-withdraw-accounting/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/incorrect-state-transition, arithmetic/precision-loss

Dedupe:
- id: `45460-autonomint-withdraw-accounting`
- fingerprint: `aee92d580cb0e28c46eb7c05d767a847142ab8deefc082370968dcd3ecbda3a1`

Core exploit idea:
- withdrawUser deducts one tenth of the user’s deposit instead of the full amount.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
