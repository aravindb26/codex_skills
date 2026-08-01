# Crypto Training Exploit Pattern Stub: Canto (veRWA) — an integer underflow can permanently DoS a gauge in `GaugeController`

Source:
- https://crypto.training/hacks/26973-h-05-it-is-possible-to-dos-all-the-functions-related-to-some/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- arithmetic/underflow, dos/frozen-funds, logic/incomplete-state-reset

Dedupe:
- id: `26973-h-05-it-is-possible-to-dos-all-the-functions-related-to-some`
- fingerprint: `1fc07fa6b5a7b28b99d5e7459ca2f68db46d04457b0e75145dd919fcc46841e9`

Core exploit idea:
- 1. Users vote their voting power onto a gauge. Each vote schedules a future exit — when the voter's lock ends, changes_weight[gauge][lockEnd] records how much slope shou…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
