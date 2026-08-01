# Crypto Training Exploit Pattern Stub: Stakehouse Protocol — incorrect accounting in `SyndicateRewardsProcessor` lets any LP holder steal others' ETH from the fees and MEV vault

Source:
- https://crypto.training/hacks/43032-h-09-incorrect-accounting-in-syndicaterewardsprocessor-resul/

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
- accounting/ledger-overwrite, logic/reward-calculation, logic/direct-drain

Dedupe:
- id: `43032-h-09-incorrect-accounting-in-syndicaterewardsprocessor-resul`
- fingerprint: `152868ae0c3bedb04db9e4bbfe97d8c579e9ef4c1552b0762ec9e7d11961204c`

Core exploit idea:
- 1. _distributeETHRewardsToUserForToken computes due = (accumulatedETHPerLPShare * balance / PRECISION) - claimed[_user][_token] — the user's total accrued entitlement mi…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
