# Crypto Training Exploit Pattern Stub: Royco ERC4626i — User rewards can be permissionlessly erased

Source:
- https://crypto.training/hacks/46672-user-rewards-can-be-permissionlessly-erased-cantina-none-roy/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-modifier

Dedupe:
- id: `46672-user-rewards-can-be-permissionlessly-erased-cantina-none-roy`
- fingerprint: `37943d742e9b3274d22a66b2f5715d36b86627b2ed3735077f1d400a72139616`

Core exploit idea:
- 1. updateUserRewards(campaignId, user) is public and callable for any user. 2. It overwrites userData.accumulated = (balance elapsed rate) / WAD instead of accruing. 3.…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
