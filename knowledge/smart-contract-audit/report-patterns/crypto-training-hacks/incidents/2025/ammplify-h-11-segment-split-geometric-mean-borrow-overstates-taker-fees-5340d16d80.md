# Crypto Training Exploit Pattern Stub: Ammplify — H-11: Segment-split geometric-mean borrow overstates taker fees

Source:
- https://crypto.training/hacks/63177-h-11-takers-pay-significantly-higher-fees-than-expected-due/

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
- unknown

Dedupe:
- id: `63177-h-11-takers-pay-significantly-higher-fees-than-expected-due`
- fingerprint: `5340d16d80503e7d5311951df11e0ded43ba8d4e0e5c0b9a79c6ed9057ee8cc7`

Core exploit idea:
- 1. Full-range borrow at one GM tick is the economically intended base. 2. Segment tree stores liq in multiple nodes; each uses its own GM. 3. Sum of segment borrows ≫ fu…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
