# Crypto Training Exploit Pattern Stub: Caller-supplied ControlTower grants migrator power — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/63046-h-2-caller-supplied-controltower-lets-anyone-be-the-migrator/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-auth, input-validation/missing

Dedupe:
- id: `63046-h-2-caller-supplied-controltower-lets-anyone-be-the-migrator`
- fingerprint: `9207180dc4e23057fe2b09b5ff9859353ef61f93c6fdcc265b5a1098d327a899`

Core exploit idea:
- This bug report is about a vulnerability found in a contract called the "2025-08-usg-tangent-judging" contract. The vulnerability was discovered by multiple individuals…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
