# Crypto Training Exploit Pattern Stub: Blueberry approved withdrawal drain — AuditVault 61458

Source:
- https://crypto.training/hacks/61458-blueberry-approved-withdrawals/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-auth, logic/missing-validation

Dedupe:
- id: `61458-blueberry-approved-withdrawals`
- fingerprint: `459de3c6d1b2aa3fc03c5ad4cf24224729e699951063bf682fc1b277e330378f`

Core exploit idea:
- requestRedeem debits escrow without checking that the caller is an approved withdrawal owner.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
