# Crypto Training Exploit Pattern Stub: collect() trusts an arbitrary DAO contract — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/57871-h-04-fee-theft-via-arbitrary-contract-impersonation-in-colle/

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
- access-control/missing-auth, dependency/unsafe-external-call

Dedupe:
- id: `57871-h-04-fee-theft-via-arbitrary-contract-impersonation-in-colle`
- fingerprint: `467131709c795c7fb186168c44f30cd195c62052b181b9ff9995a426751e29a5`

Core exploit idea:
- The report describes a high-risk bug in the DaosLocker::collect() function, which can be exploited by a malicious actor to steal swap fees from legitimate DAOs. This can…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
