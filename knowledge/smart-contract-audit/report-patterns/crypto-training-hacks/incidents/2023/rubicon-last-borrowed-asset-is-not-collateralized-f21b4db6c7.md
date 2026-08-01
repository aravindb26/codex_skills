# Crypto Training Exploit Pattern Stub: Rubicon — Last borrowed asset is not collateralized

Source:
- https://crypto.training/hacks/48954-h-15-the-last-borrowed-asset-will-not-be-collateralized-and/

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
- id: `48954-h-15-the-last-borrowed-asset-will-not-be-collateralized-and`
- fingerprint: `f21b4db6c72885120fcd8ee31b1eca9fceaae37c9836ca6183b4b65e2dd94d81`

Core exploit idea:
- _borrowLoop supplies, borrows, swaps but never supplies the last swapped asset as collateral.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
