# Crypto Training Exploit Pattern Stub: Resolv self-transfer reward theft — AuditVault 61872

Source:
- https://crypto.training/hacks/61872-resolv-self-transfer-rewards/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/reward-calculation, logic/state-update

Dedupe:
- id: `61872-resolv-self-transfer-rewards`
- fingerprint: `72fb24858683372cdb0b6d7b2c1e37d57c54516a5f4944be1a9b8b960be5e6f2`

Core exploit idea:
- Self-transfers credit both sender and recipient reward paths, doubling the reward.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
