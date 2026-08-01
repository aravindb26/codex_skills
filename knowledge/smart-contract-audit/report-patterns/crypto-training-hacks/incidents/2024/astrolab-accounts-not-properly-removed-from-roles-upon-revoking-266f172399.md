# Crypto Training Exploit Pattern Stub: Astrolab — Accounts not properly removed from roles upon revoking

Source:
- https://crypto.training/hacks/58098-h-01-accounts-not-properly-removed-from-roles-upon-revoking/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/broken-logic

Dedupe:
- id: `58098-h-01-accounts-not-properly-removed-from-roles-upon-revoking`
- fingerprint: `266f172399be98c96eee946bb01090be8be2e86e9307c80775a0e99cf375bf00`

Core exploit idea:
- 1. Roles are stored in AsSequentialSet.Set (data[] + 1-based index map). 2. remove(o) reads index[o] and calls removeAt, but never sets index[o] = 0. 3. has(o) returns t…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
