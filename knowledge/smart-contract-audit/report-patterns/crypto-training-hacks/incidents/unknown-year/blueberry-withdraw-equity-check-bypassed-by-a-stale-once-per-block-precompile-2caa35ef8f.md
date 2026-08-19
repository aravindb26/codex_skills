# Crypto Training Exploit Pattern Stub: Blueberry: `withdraw()` equity check bypassed by a stale once-per-block precompile

Source:
- https://crypto.training/hacks/61455-h-02-withdraw-check-can-be-bypassed-pashov-audit-group-none/

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
- id: `61455-h-02-withdraw-check-can-be-bypassed-pashov-audit-group-none`
- fingerprint: `2caa35ef8f4ccb7e56eef9d62bf4d9a4645c8f10b182b11c33689f7f8e444cb3`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
