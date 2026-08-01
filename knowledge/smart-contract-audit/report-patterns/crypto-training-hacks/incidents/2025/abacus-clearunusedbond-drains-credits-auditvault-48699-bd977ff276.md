# Crypto Training Exploit Pattern Stub: Abacus clearUnusedBond drains credits — AuditVault 48699

Source:
- https://crypto.training/hacks/48699-abacus-clear-unused-bond/

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
- access-control/missing-modifier, logic/state-update

Dedupe:
- id: `48699-abacus-clear-unused-bond`
- fingerprint: `bd977ff276f4b970780dba8ec29c79d9681d5734c27484458a86f5165ec39d40`

Core exploit idea:
- clearUnusedBond lacks the bond-owner restriction and can erase all outstanding credit bonds.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
