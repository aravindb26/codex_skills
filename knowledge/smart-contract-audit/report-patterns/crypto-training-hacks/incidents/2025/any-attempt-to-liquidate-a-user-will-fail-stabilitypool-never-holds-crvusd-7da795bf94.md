# Crypto Training Exploit Pattern Stub: Any attempt to liquidate a user will fail — StabilityPool never holds crvUSD

Source:
- https://crypto.training/hacks/57187-any-attempt-to-liquidate-a-user-will-fail-because-stabilityp/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `57187-any-attempt-to-liquidate-a-user-will-fail-because-stabilityp`
- fingerprint: `7da795bf94fc08470b8c4b8dee7949241c6fa78f3f0450b115dc57aad05a0e6f`

Core exploit idea:
- 1. Operational deposits route crvUSD into the reserve, never into the StabilityPool. 2. A borrower has outstanding debt and should be liquidatable. 3. liquidateBorrower…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
