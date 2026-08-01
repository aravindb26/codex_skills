# Crypto Training Exploit Pattern Stub: Munchables — Invalid validation allows users to unlock early

Source:
- https://crypto.training/hacks/33595-h-02-invalid-validation-allows-users-to-unlock-early-code4re/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/mismatched-invariant-anchor, access-control/reward-gaming

Dedupe:
- id: `33595-h-02-invalid-validation-allows-users-to-unlock-early-code4re`
- fingerprint: `3ba60dd2de842ec5df87d68e7e6e31fbf97dfd40013de0c853b25adfd0d94a67`

Core exploit idea:
- 1. When a user locks tokens, unlockTime = block.timestamp + lockDuration and lastLockTime = block.timestamp are recorded together, at the same instant. 2. setLockDuratio…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
