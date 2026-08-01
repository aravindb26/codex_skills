# Crypto Training Exploit Pattern Stub: H-2: Attacker drains Morpho suppliers by inflating collateral price

Source:
- https://crypto.training/hacks/62483-h-2-attacker-can-drain-the-entire-suppliers-on-morpho-market/

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
- id: `62483-h-2-attacker-can-drain-the-entire-suppliers-on-morpho-market`
- fingerprint: `30f502f39cfa41c39eb93dd1a8cc18ac0432e396a84c3ae7a68ad4a86540c344`

Core exploit idea:
- 500k USDC drained from Morpho suppliers via post-withdraw yield donation

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
