# Crypto Training Exploit Pattern Stub: TokenOps: withdraw() is gated by `isActive`, so revoking a grant freezes already-vested-but-unclaimed tokens

Source:
- https://crypto.training/hacks/59721-vested-unclaimed-tokens-become-frozen-once-admin-revokes-t/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 1970

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `59721-vested-unclaimed-tokens-become-frozen-once-admin-revokes-t`
- fingerprint: `8e86470a7a1718f8d62f352f3c3b230fc63d5540a2c5f4041822e8b055d9b5f0`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
