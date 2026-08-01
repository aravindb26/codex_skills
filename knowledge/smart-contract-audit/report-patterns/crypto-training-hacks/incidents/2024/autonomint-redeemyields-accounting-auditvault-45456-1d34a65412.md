# Crypto Training Exploit Pattern Stub: Autonomint redeemYields accounting — AuditVault 45456

Source:
- https://crypto.training/hacks/45456-autonomint-redeem-yields/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/incorrect-state-transition, access-control/missing-auth

Dedupe:
- id: `45456-autonomint-redeem-yields`
- fingerprint: `1d34a65412c715253302c0d50ee7c70671c3cc56f38e819887a80af69e983b43`

Core exploit idea:
- The caller’s ABOND is debited while redemption state is credited to a different user.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
