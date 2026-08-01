# Crypto Training Exploit Pattern Stub: Stake.Link — instant withdrawals can burn LST while stranding underlying

Source:
- https://crypto.training/hacks/45292-instant-withdrawals-in-priority-pool-can-result-in-loss-of-f/

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
- logic/state-update, dos/frozen-funds

Dedupe:
- id: `45292-instant-withdrawals-in-priority-pool-can-result-in-loss-of-f`
- fingerprint: `c77f45bf09423f6c57e51c8b4798ea9b6494411fd2b4dc572d001ca1a6332550`

Core exploit idea:
- During an instant withdrawal, PriorityPool receives underlying assets from StakingPool and reduces toWithdraw, but it never increments withdrawn. StakingProxy has alread…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
