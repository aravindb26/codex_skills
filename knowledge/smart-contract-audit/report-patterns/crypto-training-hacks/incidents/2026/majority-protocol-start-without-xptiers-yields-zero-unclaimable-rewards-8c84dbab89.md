# Crypto Training Exploit Pattern Stub: Majority Protocol — start without XPTiers yields zero unclaimable rewards

Source:
- https://crypto.training/hacks/65378-impossible-to-claim-rewards-when-xptiers-are-not-set-resulti/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2026

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `65378-impossible-to-claim-rewards-when-xptiers-are-not-set-resulti`
- fingerprint: `8c84dbab89b286637c24fc4eba65488a9a414513a975a4c0edeb8f8d94c3cfc7`

Core exploit idea:
- setXPTiers is only allowed in Created, but the game can start without tiers. XP computation yields 0; ProportionalToXPReward then produces zero rewards and _distributeRe…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
