# Crypto Training Exploit Pattern Stub: Frankencoin — Position owners can deny liquidations (unbounded price overflow)

Source:
- https://crypto.training/hacks/20020-h-05-position-owners-can-deny-liquidations-code4rena-franken/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- arithmetic/overflow-dos, access-control/unbounded-parameter, loss-of-funds/frozen-funds

Dedupe:
- id: `20020-h-05-position-owners-can-deny-liquidations-code4rena-franken`
- fingerprint: `2f116bbbbd7e7a1c870e52e67ca7f95b89719c615ff57174372ee328103f0d14`

Core exploit idea:
- 1. A position owner can set the liquidation price arbitrarily high via adjustPrice (or the opening _liqPrice) — there is no upper bound. 2. Every challenge-resolution pa…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
