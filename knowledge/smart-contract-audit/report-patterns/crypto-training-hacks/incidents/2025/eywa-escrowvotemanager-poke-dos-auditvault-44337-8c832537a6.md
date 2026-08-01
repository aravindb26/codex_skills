# Crypto Training Exploit Pattern Stub: EYWA EscrowVoteManager poke DoS — AuditVault 44337

Source:
- https://crypto.training/hacks/44337-eywa-poke-dos/

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
- access-control/missing-owner-check, dos/griefing

Dedupe:
- id: `44337-eywa-poke-dos`
- fingerprint: `8c832537a64d41dd0c9abc6b93164e1cbb2cf156a03bc77a1ffde9dbe1ec467d`

Core exploit idea:
- poke accepts a token ID owned by another account and lets an untrusted caller poison vote state.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
