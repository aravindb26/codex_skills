# Crypto Training Exploit Pattern Stub: Validator proof duplication bypasses consensus — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/55229-h-2-malicious-validators-will-bypass-consensus-threshold-req/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- bridge/missing-validation, bridge/replay

Dedupe:
- id: `55229-h-2-malicious-validators-will-bypass-consensus-threshold-req`
- fingerprint: `5c5c32da3d8f5be41fd3d806ea8cabb590adbe77600a4bfaeb99b4553f0e2a25`

Core exploit idea:
- This bug report discusses a critical security issue with the SEDA protocol's cross-chain data verification system. The issue was discovered by a group of researchers and…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
