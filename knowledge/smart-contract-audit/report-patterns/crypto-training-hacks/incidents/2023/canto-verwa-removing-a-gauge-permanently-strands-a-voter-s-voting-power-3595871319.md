# Crypto Training Exploit Pattern Stub: Canto (veRWA) — removing a gauge permanently strands a voter's voting power

Source:
- https://crypto.training/hacks/26976-h-08-if-governance-removes-a-gauge-users-voting-power-for-th/

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
- access-control/missing-state-reset, governance/stranded-voting-power, logic/incomplete-invalidation

Dedupe:
- id: `26976-h-08-if-governance-removes-a-gauge-users-voting-power-for-th`
- fingerprint: `3595871319a1f1a6ebee5658b254fbedaa1d15e1fdee3b9510c65662b69fff75`

Core exploit idea:
- 1. A voter commits 100% (10,000 bps) of their voting power to gauge1 via vote_for_gauge_weights(gauge1, 10000). 2. Governance later calls remove_gauge(gauge1) — for any…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
