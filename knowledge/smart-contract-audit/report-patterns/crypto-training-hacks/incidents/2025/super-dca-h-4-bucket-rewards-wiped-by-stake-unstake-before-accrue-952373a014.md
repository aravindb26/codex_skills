# Crypto Training Exploit Pattern Stub: Super DCA — H-4: Bucket rewards wiped by stake/unstake before accrue

Source:
- https://crypto.training/hacks/63422-h-4-bucket-rewards-will-be-wiped-by-stakeunstake-before-accr/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `63422-h-4-bucket-rewards-will-be-wiped-by-stakeunstake-before-accr`
- fingerprint: `952373a0148e04d805679fe746be8cdce01042a05abb21ca3177c5db097bd4b3`

Core exploit idea:
- After rewards accrue on a bucket, any stake/unstake resets lastRewardIndex to current rewardIndex. Subsequent accrueReward sees delta 0 → paid = 0.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
