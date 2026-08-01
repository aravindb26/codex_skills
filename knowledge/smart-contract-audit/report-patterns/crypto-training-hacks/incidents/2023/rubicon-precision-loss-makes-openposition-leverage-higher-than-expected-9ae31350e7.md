# Crypto Training Exploit Pattern Stub: Rubicon — Precision loss makes openPosition leverage higher than expected

Source:
- https://crypto.training/hacks/48955-h-16-due-to-the-loss-of-precision-openposition-will-make-the/

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
- unknown

Dedupe:
- id: `48955-h-16-due-to-the-loss-of-precision-openposition-will-make-the`
- fingerprint: `9ae31350e7c385e025a83d20c61cc8b5dcfd1baefb0000ce61f2168ed015edd3`

Core exploit idea:
- wmul floor makes desired==init; lastBorrow=0 is treated as full borrow instead of zero extra leverage.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
