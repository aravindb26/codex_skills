# Crypto Training Exploit Pattern Stub: Session key can be consumed by another smart wallet — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/61396-h-01-session-key-can-be-consumed-by-unauthorized-scw-shieldi/

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
- access-control/missing-owner-check, auth/signature-validation

Dedupe:
- id: `61396-h-01-session-key-can-be-consumed-by-unauthorized-scw-shieldi`
- fingerprint: `d78c564a3e532a48507f5e480f9c9c994615b548f945cfe2fd6f6f8dee7d1b01`

Core exploit idea:
- The bug report describes an issue with the CredibleAccountModule contract, where there is a lack of check to verify that the session key being used belongs to the actual…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
