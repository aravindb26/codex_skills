# Crypto Training Exploit Pattern Stub: IPSeed tokenId reconfiguration drain — AuditVault 31585

Source:
- https://crypto.training/hacks/31585-catalyst-tokenid-reconfiguration/

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
- access-control/missing-owner-check, logic/state-update

Dedupe:
- id: `31585-catalyst-tokenid-reconfiguration`
- fingerprint: `2c1e33d6252d40fe35945b46e330f5b965f501adafe4a62ad00c7888342465c6`

Core exploit idea:
- A caller can reconfigure tokenId and withdraw ETH belonging to the previously configured asset.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
