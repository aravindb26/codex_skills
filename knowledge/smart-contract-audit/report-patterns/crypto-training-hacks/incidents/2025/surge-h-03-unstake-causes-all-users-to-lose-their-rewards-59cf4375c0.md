# Crypto Training Exploit Pattern Stub: Surge — [H-03] Unstake causes all users to lose their rewards

Source:
- https://crypto.training/hacks/55142-unstake-causes-all-users-to-lose-rewards/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `55142-unstake-causes-all-users-to-lose-rewards`
- fingerprint: `59cf4375c0377cda1890e179dc8fde5777aed9cd65a6a173217d31c865b4c69f`

Core exploit idea:
- 1. User and attacker each stake 1000 into cycle 1 (total shares = 2000). 2. Rewards are injected for the cycle. 3. Attacker unstakes; _unstake reads total pool shares an…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
