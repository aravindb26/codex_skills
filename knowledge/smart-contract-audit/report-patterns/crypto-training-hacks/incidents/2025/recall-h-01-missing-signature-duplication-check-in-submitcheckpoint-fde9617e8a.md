# Crypto Training Exploit Pattern Stub: Recall — [H-01] Missing signature duplication check in submitCheckpoint

Source:
- https://crypto.training/hacks/65088-h-01-missing-signature-duplication-check-in-the-submitcheckp/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `65088-h-01-missing-signature-duplication-check-in-the-submitcheckp`
- fingerprint: `fde9617e8abd0c92c7ebabbadce16fb845489c07c8d61e6855cd93fd0117b729`

Core exploit idea:
- Single weight-6 validator forges majority quorum by repeating itself in signatories[]

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
