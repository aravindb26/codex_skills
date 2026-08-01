# Crypto Training Exploit Pattern Stub: H-4: Direct Morpho borrow misprices withdrawal-request collateral

Source:
- https://crypto.training/hacks/62485-h-4-when-users-borrow-directly-from-morpho-price-of-the-coll/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `62485-h-4-when-users-borrow-directly-from-morpho-price-of-the-coll`
- fingerprint: `88ebff63bf9937b9e9411f521fc62c389d356020daddc782b3538840d0ab78cd`

Core exploit idea:
- Over-borrow vs request-backed LTV (bad debt) when Morpho price ignores withdraw request

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
