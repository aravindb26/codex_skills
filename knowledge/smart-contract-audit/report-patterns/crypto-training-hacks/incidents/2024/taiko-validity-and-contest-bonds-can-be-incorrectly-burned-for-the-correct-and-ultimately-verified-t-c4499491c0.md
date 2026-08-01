# Crypto Training Exploit Pattern Stub: Taiko — Validity and contest bonds can be incorrectly burned for the correct and ultimately verified transition

Source:
- https://crypto.training/hacks/31930-h-02-validity-and-contests-bond-ca-be-incorrectly-burned-for/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- loss-of-funds/frozen-funds, logic/state-overwrite, accounting/reward-refund

Dedupe:
- id: `31930-h-02-validity-and-contests-bond-ca-be-incorrectly-burned-for`
- fingerprint: `c4499491c0b2f8963bfc2c41193af5a119f5b13899c3e4417d68ad5cf633f545`

Core exploit idea:
- 1. Taiko's TransitionState for a block records one prover, one tier and one validityBond — whoever most recently proved (or re-proved / overrode) the transition. 2. LibP…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
