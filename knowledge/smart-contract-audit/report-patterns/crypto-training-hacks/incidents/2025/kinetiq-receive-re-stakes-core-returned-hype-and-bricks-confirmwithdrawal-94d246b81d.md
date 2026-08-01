# Crypto Training Exploit Pattern Stub: Kinetiq — `receive()` re-stakes Core-returned HYPE and bricks confirmWithdrawal

Source:
- https://crypto.training/hacks/58555-h-03-mishandling-of-receiving-hype-in-the-stakingmanager-use/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- accounting/reward-accounting, logic/state-update, liveness/withdrawal-brick

Dedupe:
- id: `58555-h-03-mishandling-of-receiving-hype-in-the-stakingmanager-use`
- fingerprint: `94d246b81dafe78fce44439ec90469fd807ba45c023fe483c3c7716ad814c9e4`

Core exploit idea:
- 1. On HyperEVM, HYPE is the native gas token. Undelegations from Hypercore arrive as native ETH-like transfers to StakingManager. 2. receive() external payable { stake()…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
