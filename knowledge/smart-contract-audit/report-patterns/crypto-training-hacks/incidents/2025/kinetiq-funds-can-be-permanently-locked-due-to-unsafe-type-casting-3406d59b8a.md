# Crypto Training Exploit Pattern Stub: Kinetiq — Funds can be permanently locked due to unsafe type casting

Source:
- https://crypto.training/hacks/58613-h-05-funds-can-be-permanently-locked-due-to-unsafe-type-cast/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `58613-h-05-funds-can-be-permanently-locked-due-to-unsafe-type-cast`
- fingerprint: `3406d59b8a29c7fb5d8ca747bea8de12e1707a39dc7767d53bd85ad5b934b7a6`

Core exploit idea:
- 1. L1Write.sendTokenDelegate takes uint64 amount. 2. StakingManager casts uint256 → uint64 without SafeCast. 3. For amount = type(uint64).max + 1, the cast becomes 0. 4.…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
