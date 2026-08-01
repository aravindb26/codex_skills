# Crypto Training Exploit Pattern Stub: Gnosis Pay / Zodiac Delay — `moduleTxSignedBy` ignores EIP-1271 `staticcall` success

Source:
- https://crypto.training/hacks/2026-06-GnosisPay/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2026

Chain:
- Gnosis

Loss / impact summary:
- unknown

Tags:
- auth/signature-validation, access-control/broken-logic, logic/missing-check

Dedupe:
- id: `2026-06-GnosisPay`
- fingerprint: `64578e8a9ce664dee9393240caf9ad2a0618a155219096f4fae12bae93d6fbd5`

Core exploit idea:
- 1. Gnosis Pay card accounts are Safe smart accounts with Zodiac Roles + Delay modules. Outgoing non-card transfers queue in Delay for a short cooldown (txCooldown = 180…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
