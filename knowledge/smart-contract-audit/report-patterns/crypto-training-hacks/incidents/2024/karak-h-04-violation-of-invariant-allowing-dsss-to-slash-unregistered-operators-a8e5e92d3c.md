# Crypto Training Exploit Pattern Stub: Karak — [H-04] Violation of Invariant Allowing DSSs to Slash Unregistered Operators

Source:
- https://crypto.training/hacks/41068-h-04-violation-of-invariant-allowing-dsss-to-slash-unregiste/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-condition, access-control/missing-validation, state/invariant-violation

Dedupe:
- id: `41068-h-04-violation-of-invariant-allowing-dsss-to-slash-unregiste`
- fingerprint: `a8e5e92d3c03e78b59e181c0b500a74e1cbdbec7df29bcd6b30f2f85f0cbcb94`

Core exploit idea:
- 1. An operator can request to unstake their vaults from a DSS, starting a 9-day MIN_STAKE_UPDATE_DELAY. 2. While that request is still pending, the DSS can legitimately…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
