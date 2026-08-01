# Crypto Training Exploit Pattern Stub: Alchemix — `RevenueHandler.checkpoint` counts unclaimed rewards as new rewards

Source:
- https://crypto.training/hacks/38176-revenuehandlercheckpoint-counts-unclaimed-rewards-as-new-rew/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/reward-calculation, accounting/double-counting, insolvency/late-claimer-lockout

Dedupe:
- id: `38176-revenuehandlercheckpoint-counts-unclaimed-rewards-as-new-rew`
- fingerprint: `6ecda0c0cfca20979b5aa3c41a84b944acb2b96ad183d1a63a5f4888ebbabd92`

Core exploit idea:
- 1. RevenueHandler.checkpoint() runs once per epoch and, for a revenue token with no poolAdapter set, records amountReceived = thisBalance where thisBalance = IERC20(toke…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
