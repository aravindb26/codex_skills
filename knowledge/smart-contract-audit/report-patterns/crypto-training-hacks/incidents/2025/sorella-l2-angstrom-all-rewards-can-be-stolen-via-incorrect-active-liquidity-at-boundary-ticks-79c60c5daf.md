# Crypto Training Exploit Pattern Stub: Sorella L2 Angstrom — All rewards can be stolen via incorrect active liquidity at boundary ticks

Source:
- https://crypto.training/hacks/63008-all-rewards-can-be-stolen-due-to-incorrect-active-liquidity/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- arithmetic/underflow, logic/reward-calculation

Dedupe:
- id: `63008-all-rewards-can-be-stolen-due-to-incorrect-active-liquidity`
- fingerprint: `79c60c5daf9e2272fe72d635e242d622e995bdb395ba1aab3b0454ad365cc448`

Core exploit idea:
- 1. When the current tick is an exact multiple of tick spacing at an upper liquidity bound t1, zero-for-one iteration should apply liquidityNet[t1] first. 2. _advanceToNe…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
