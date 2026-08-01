# Crypto Training Exploit Pattern Stub: Switchboard reward manipulation — AuditVault 47980

Source:
- https://crypto.training/hacks/47980-switchboard-reward-manipulation/

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
- logic/reward-calculation, access-control/missing-modifier

Dedupe:
- id: `47980-switchboard-reward-manipulation`
- fingerprint: `88b738d3cd36b2b70204a217ed713a948293e30d751f91006c529ccc940dbd39`

Core exploit idea:
- Reward accounting remains writable after an enclave update and has no authorized caller check.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
