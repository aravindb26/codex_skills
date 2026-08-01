# Crypto Training Exploit Pattern Stub: Unverified Staking Contract — `claim()` Double-Spend of Deposited BUSD

Source:
- https://crypto.training/hacks/2023-06-UnverifiedContr_9ad32/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2023

Chain:
- BNB Chain

Loss / impact summary:
- ~$5,955 — 5,955.466788 BUSD drained from the staking contract

Tags:
- logic/missing-allowance, logic/state-update, logic/incorrect-order-of-operations

Dedupe:
- id: `2023-06-UnverifiedContr_9ad32`
- fingerprint: `f1867d4d23b32ed82844ddc36c1f3f67304081913dccb45926ddd9f10c63e5dd`

Core exploit idea:
- A small BUSD staking/farm contract at 0xAC899… lets a user deposit(pid, amount) and later claim(pid, amount). The trace shows that claim() returns the staked principal t…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
