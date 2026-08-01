# Crypto Training Exploit Pattern Stub: BMX — Voter::finalize() transfers WETH before setting the distributor rate

Source:
- https://crypto.training/hacks/62815-bmx-voter-finalize-transfers-weth-before-setting-the-distributor-rate/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/incorrect-order-of-operations, logic/reward-calculation

Dedupe:
- id: `62815-bmx-voter-finalize-transfers-weth-before-setting-the-distributor-rate`
- fingerprint: `2d914412325ae675a441e5fc5afd70c5cd2306cb55d6b9836c2bb7c146d1a030`

Core exploit idea:
- Finalization transfers the reward token before updating the distributor rate, so the interval accounting uses the wrong balance and over/under-distributes rewards.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
