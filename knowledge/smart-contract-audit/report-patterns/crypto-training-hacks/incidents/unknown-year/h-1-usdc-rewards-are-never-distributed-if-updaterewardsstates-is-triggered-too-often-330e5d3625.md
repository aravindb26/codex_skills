# Crypto Training Exploit Pattern Stub: H-1: USDC rewards are never distributed if `_updateRewardsStates` is triggered too often

Source:
- https://crypto.training/hacks/55104-h-1-usdc-rewards-will-not-be-distributed-if-updaterewardsst/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 1970

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `55104-h-1-usdc-rewards-will-not-be-distributed-if-updaterewardsst`
- fingerprint: `330e5d3625ecbe7a6060f7eb435f66568a4dc1151d0902f12f87faecef55e83f`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
