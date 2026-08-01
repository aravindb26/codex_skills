# Crypto Training Exploit Pattern Stub: FactoryDAO — Blacklisted user may permanently block `withdrawExcessRewards`

Source:
- https://crypto.training/hacks/42551-h-02-dos-blacklisted-user-may-prevent-withdrawexcessrewards/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `42551-h-02-dos-blacklisted-user-may-prevent-withdrawexcessrewards`
- fingerprint: `3a8e126a873fb5d719f730b190fe54e390d2f5ec8a0e7bc106989493a18b69bc`

Core exploit idea:
- 1. withdraw AND-chains every ERC20 transfer and reverts if any fails. 2. A blacklisted (or paused-token) user can never clear their deposit. 3. withdrawExcessRewards req…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
