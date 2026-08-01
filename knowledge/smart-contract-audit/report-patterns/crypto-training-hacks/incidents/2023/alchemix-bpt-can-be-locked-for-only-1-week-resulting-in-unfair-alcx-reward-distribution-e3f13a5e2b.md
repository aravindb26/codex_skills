# Crypto Training Exploit Pattern Stub: Alchemix — BPT can be locked for only 1 week, resulting in unfair ALCX reward distribution

Source:
- https://crypto.training/hacks/38178-bpt-can-be-locked-for-only-1-week-resulting-in-unfair-alcx-r/

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
- logic/off-by-rounding, access-control/bypassable-invariant-check, economic/reward-dilution

Dedupe:
- id: `38178-bpt-can-be-locked-for-only-1-week-resulting-in-unfair-alcx-r`
- fingerprint: `e3f13a5e2b38325705458248e1e17589297e244c7c7670aea9c1584e2ff860e1`

Core exploit idea:
- 1. VotingEscrow._createLock is supposed to enforce a minimum lock period of 1 epoch (2 weeks): require(unlockTime >= (((block.timestamp + EPOCH) / WEEK) * WEEK), ...). 2…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
