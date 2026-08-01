# Crypto Training Exploit Pattern Stub: Karak increaseBalance share loss — AuditVault 38492

Source:
- https://crypto.training/hacks/38492-karak-increase-balance-shares/

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
- arithmetic/rounding-direction, logic/reward-calculation

Dedupe:
- id: `38492-karak-increase-balance-shares`
- fingerprint: `aaaabab513b9f3ded76a3fe028169d2252212262a73687b5c77223d321eae4ce`

Core exploit idea:
- increaseBalance rounds the minted share amount down by a factor of two.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
