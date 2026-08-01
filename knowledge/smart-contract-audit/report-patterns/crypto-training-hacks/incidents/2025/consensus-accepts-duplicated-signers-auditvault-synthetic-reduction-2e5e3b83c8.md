# Crypto Training Exploit Pattern Stub: Consensus accepts duplicated signers — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/62106-h-1-consensuschecksignatures-doesnt-check-duplication-of-sig/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- bridge/missing-validation, auth/signature-validation

Dedupe:
- id: `62106-h-1-consensuschecksignatures-doesnt-check-duplication-of-sig`
- fingerprint: `2e5e3b83c837e5fdc06200b1438f788c8eb6f53a460a18ce5d36c3f40233c2a1`

Core exploit idea:
- This bug report discusses a vulnerability found in the Mellow Flexible Vaults protocol, which was discovered by multiple individuals. The issue lies in the SignatureQueu…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
