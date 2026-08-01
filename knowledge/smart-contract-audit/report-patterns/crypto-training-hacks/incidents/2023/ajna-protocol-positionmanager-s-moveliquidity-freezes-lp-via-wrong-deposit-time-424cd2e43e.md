# Crypto Training Exploit Pattern Stub: Ajna Protocol — PositionManager's `moveLiquidity` freezes LP via wrong deposit time

Source:
- https://crypto.training/hacks/20070-h-02-positionmanagers-moveliquidity-can-set-wrong-deposit-ti/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `20070-h-02-positionmanagers-moveliquidity-can-set-wrong-deposit-ti`
- fingerprint: `424cd2e43e377fa68d2e1f67e95c06d4327ccfd8275652da2037d00cf869471c`

Core exploit idea:
- 1. moveLiquidity copies fromPosition.depositTime onto toPosition. 2. Destination bucket may have bankruptcyTime > from.depositTime. 3. Pool-side LenderActions renews dep…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
