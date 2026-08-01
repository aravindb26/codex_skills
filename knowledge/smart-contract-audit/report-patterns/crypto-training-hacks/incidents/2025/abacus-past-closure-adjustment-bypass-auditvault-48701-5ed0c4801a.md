# Crypto Training Exploit Pattern Stub: Abacus past-closure adjustment bypass — AuditVault 48701

Source:
- https://crypto.training/hacks/48701-abacus-past-closure-adjustment/

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
- reentrancy/single-function, logic/missing-check

Dedupe:
- id: `48701-abacus-past-closure-adjustment`
- fingerprint: `5ed0c4801a640e1dc4bb0a79bf52fa79ce56becb7dd2a3663edf398b1e9c7b84`

Core exploit idea:
- adjustTicketInfo does not reject a ticket whose closure has already been finalized.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
