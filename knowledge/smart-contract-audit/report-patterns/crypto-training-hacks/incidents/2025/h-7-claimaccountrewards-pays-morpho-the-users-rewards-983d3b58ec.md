# Crypto Training Exploit Pattern Stub: H-7: claimAccountRewards pays MORPHO the users rewards

Source:
- https://crypto.training/hacks/62488-h-7-rewardmanagermixinclaimaccountrewards-lacks-of-necessary/

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
- id: `62488-h-7-rewardmanagermixinclaimaccountrewards-lacks-of-necessary`
- fingerprint: `983d3b58ec446c604316a050b5d42531e15b97bedf8c881d8aa1d8e82272d7a9`

Core exploit idea:
- 100 reward tokens stolen to MORPHO address via permissionless claimAccountRewards

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
