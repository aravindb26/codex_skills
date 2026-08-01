# Crypto Training Exploit Pattern Stub: InfiniFi — StakedToken holders can circumvent restriction by approving another address to withdraw

Source:
- https://crypto.training/hacks/55053-stakedtoken-holders-can-circumvent-restriction-by-approving/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `55053-stakedtoken-holders-can-circumvent-restriction-by-approving`
- fingerprint: `bd3a7ffd24a733e3871e44ffab3b47fab2f07692b6451c3299af28636e79f716`

Core exploit idea:
- 1. Alice holds siUSD and is action-restricted (cannot transfer/withdraw). 2. Alice approves an unrestricted third party for her shares. 3. Alice's own withdraw reverts w…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
