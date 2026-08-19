# Crypto Training Exploit Pattern Stub: Karak NativeVault: `activeValidatorCount` is never incremented, bricking every snapshot

Source:
- https://crypto.training/hacks/38491-h-03-activevalidatorcount-is-never-set-or-increased-pashov-a/

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
- id: `38491-h-03-activevalidatorcount-is-never-set-or-increased-pashov-a`
- fingerprint: `23339964b1dfdbac319109f67f6948b341bee5f04c2db60d1bdadaaaa8c7c1aa`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
