# Crypto Training Exploit Pattern Stub: KittenSwap — `RebaseReward` fails because of incorrect token handling

Source:
- https://crypto.training/hacks/58065-c-01-rebasereward-fails-because-of-incorrect-token-handling/

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
- id: `58065-c-01-rebasereward-fails-because-of-incorrect-token-handling`
- fingerprint: `71418672492181853cbd80803fc8c163a1c6dda3b0b8f2fbfcfca5fdfcbb5233`

Core exploit idea:
- 1. notifyRewardAmount only accepts Kitten, but incentivize accepts any token. 2. On claim, every reward token's share is deposited as Kitten via deposit_for. 3. Equal-we…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
