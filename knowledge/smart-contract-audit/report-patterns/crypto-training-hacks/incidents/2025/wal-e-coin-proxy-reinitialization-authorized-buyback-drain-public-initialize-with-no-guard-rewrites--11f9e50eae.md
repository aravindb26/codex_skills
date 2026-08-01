# Crypto Training Exploit Pattern Stub: WAL-E Coin proxy reinitialization → authorized buyback drain — public `initialize()` with no guard rewrites owner/router and unlocks `triggerZeusBuyback`

Source:
- https://crypto.training/hacks/2025-06-WaleCoin/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- BNB Chain

Loss / impact summary:
- 1.415367204023272901 BNB (~$430 at the time)

Tags:
- access-control/missing-auth, logic/incorrect-state-transition, dependency/upgradeable-contract

Dedupe:
- id: `2025-06-WaleCoin`
- fingerprint: `11f9e50eaeb8dc4a57849437e6f3feb5c063a75277de28bb56ba4b95dac1dfb8`

Core exploit idea:
- WAL-E Coin ($WAL-E) is a BSC "dividend + buyback" token deployed behind an ERC-1967-style transparent upgradeable proxy. The implementation, RewardsChain, performs all o…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
