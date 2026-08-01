# Crypto Training Exploit Pattern Stub: Majority Protocol — start without ranked rewards locks prize pool

Source:
- https://crypto.training/hacks/65377-impossible-to-claim-rewards-when-ranked-rewards-or-number-of/

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
- id: `65377-impossible-to-claim-rewards-when-ranked-rewards-or-number-of`
- fingerprint: `06d564c61bbc9c9d2c675a493af7e9d8df0764d40095c3c7ba658c91ebee17ee`

Core exploit idea:
- FixedRanksReward.setRankedRewards (and ProportionalToXPReward.setNumberOfWinners) require Created state, but the game can start and conclude without them. claimRewards t…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
