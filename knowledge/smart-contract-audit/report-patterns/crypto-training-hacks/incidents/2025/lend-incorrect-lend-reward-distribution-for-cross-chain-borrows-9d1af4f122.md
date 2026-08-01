# Crypto Training Exploit Pattern Stub: LEND — Incorrect LEND reward distribution for cross-chain borrows

Source:
- https://crypto.training/hacks/58381-lend-incorrect-lend-reward-distribution-for-cross-chain-borrows/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/reward-calculation, logic/incorrect-state-transition

Dedupe:
- id: `58381-lend-incorrect-lend-reward-distribution-for-cross-chain-borrows`
- fingerprint: `9d1af4f1229707c5920b7fec4a24cd9c31a732c3dd61160d58a1aef20e496e28`

Core exploit idea:
- Cross-chain borrower rewards are allocated from the aggregate index without subtracting the remote chain's share, diverting rewards from other users.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
