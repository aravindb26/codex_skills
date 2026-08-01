# Crypto Training Exploit Pattern Stub: LEND — Malicious liquidator can liquidate without providing collateral

Source:
- https://crypto.training/hacks/58379-lend-malicious-liquidator-can-liquidate-without-providing-collateral/

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
- logic/missing-check, access-control/missing-auth

Dedupe:
- id: `58379-lend-malicious-liquidator-can-liquidate-without-providing-collateral`
- fingerprint: `76d5cae49a37fe603cb14180f97b6daa501b05db9b544001c226a187bc57ec50`

Core exploit idea:
- The liquidation path checks the borrower's debt but never verifies that the liquidator supplied the required repayment collateral.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
