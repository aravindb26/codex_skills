# Crypto Training Exploit Pattern Stub: Stakehouse Protocol — repeated reward claims drift, letting a curator extract more than their fair share

Source:
- https://crypto.training/hacks/43025-h-01-any-user-being-the-first-to-claim-rewards-from-giantmev/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- accounting/incorrect-checkpoint-update, economic/reward-drift, logic/insolvency-risk

Dedupe:
- id: `43025-h-01-any-user-being-the-first-to-claim-rewards-from-giantmev`
- fingerprint: `03fb7977d1cda66dd7e317649c72965ee3e311f842210a3ee390f85820f9bdff`

Core exploit idea:
- 1. _distributeETHRewardsToUserForToken computes due — the ETH newly owed to a user — as accumulatedETHPerLPShare * balance / PRECISION - claimed[user][token], and pays i…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
