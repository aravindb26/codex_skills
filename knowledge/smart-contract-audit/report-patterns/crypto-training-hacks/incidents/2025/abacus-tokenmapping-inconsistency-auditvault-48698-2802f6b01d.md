# Crypto Training Exploit Pattern Stub: Abacus tokenMapping inconsistency — AuditVault 48698

Source:
- https://crypto.training/hacks/48698-abacus-token-mapping/

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
- logic/missing-validation, logic/incorrect-state-transition

Dedupe:
- id: `48698-abacus-token-mapping`
- fingerprint: `2802f6b01dc40504392122c5f4ede0616577cbfbf6fcfa3d5a5ec66018f7f087`

Core exploit idea:
- The registration path writes tokenMapping but updates a different existence key, so lookups disagree.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
