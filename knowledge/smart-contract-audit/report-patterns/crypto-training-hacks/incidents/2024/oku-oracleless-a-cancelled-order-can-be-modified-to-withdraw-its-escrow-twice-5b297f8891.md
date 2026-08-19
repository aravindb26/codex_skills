# Crypto Training Exploit Pattern Stub: Oku OracleLess: a cancelled order can be modified to withdraw its escrow twice

Source:
- https://crypto.training/hacks/44374-h-4-users-can-modify-a-cancelled-order-withdrawing-the-same/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/missing-check, defi/direct-drain, accounting/double-spend

Dedupe:
- id: `44374-h-4-users-can-modify-a-cancelled-order-withdrawing-the-same`
- fingerprint: `5b297f889110049abeb01a35d044733a459b181ffb2bf232ebc1a7bb296b265f`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
