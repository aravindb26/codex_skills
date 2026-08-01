# Crypto Training Exploit Pattern Stub: Unverified "Slot" Staking Contract — `releaseSlot()` Reentrancy BNB Drain

Source:
- https://crypto.training/hacks/2025-02-unverified_35bc/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- BNB Chain

Loss / impact summary:
- ~$6,700 — 10.2 BNB drained from the contract's native balance (attacker walked off with 1…

Tags:
- reentrancy/single-function, logic/incorrect-order-of-operations

Dedupe:
- id: `2025-02-unverified_35bc`
- fingerprint: `af9d3197e0b93e4bf37952e49db2ffdfbe35296b37ab8801c7b4ad83646f9191`

Core exploit idea:
- The contract is a BNB "slot" staking / lottery product. A user calls unlockSlot(uint256) with BNB to activate a slot, and later calls releaseSlot(uint256) to get their d…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
