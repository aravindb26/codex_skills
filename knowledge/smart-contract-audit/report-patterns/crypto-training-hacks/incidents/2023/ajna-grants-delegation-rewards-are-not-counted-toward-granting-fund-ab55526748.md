# Crypto Training Exploit Pattern Stub: Ajna Grants — Delegation rewards are not counted toward granting fund

Source:
- https://crypto.training/hacks/20072-h-04-delegation-rewards-are-not-counted-toward-granting-fund/

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
- accounting/double-count, logic/reward-calculation, loss-of-funds/treasury-insolvency

Dedupe:
- id: `20072-h-04-delegation-rewards-are-not-counted-toward-granting-fund`
- fingerprint: `ab55526748b3f3f72a41358d5c04062ffec5f4bbb9c82124a1b447c544792528`

Core exploit idea:
- 1. Each quarter a Global Budget Constraint (GBC = 3% of the treasury) is reserved as fundsAvailable. It splits 90% for proposals and 10% for voter (delegate) rewards. 2.…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
