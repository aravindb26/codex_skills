# Crypto Training Exploit Pattern Stub: Streaming — recoverTokens steals rewards when depositToken == rewardToken

Source:
- https://crypto.training/hacks/42394-h-02-tokens-can-be-stolen-when-deposittoken-rewardtoken-code/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2021

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- accounting/same-token-double-count, access-control/privileged-drain

Dedupe:
- id: `42394-h-02-tokens-can-be-stolen-when-deposittoken-rewardtoken-code`
- fingerprint: `beda078ee36f343c849f4a5d2d60b0a9af01fe95775f6d5424853cd3093eafe4`

Core exploit idea:
- When deposit and reward tokens are the same, recoverTokens' deposit excess formula includes the reward inventory and the creator drains user rewards

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
