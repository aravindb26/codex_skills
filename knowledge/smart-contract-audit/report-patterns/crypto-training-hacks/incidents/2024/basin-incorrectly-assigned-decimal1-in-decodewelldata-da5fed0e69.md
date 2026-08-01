# Crypto Training Exploit Pattern Stub: Basin — Incorrectly assigned `decimal1` in `decodeWellData`

Source:
- https://crypto.training/hacks/36914-h-02-incorrectly-assigned-decimal1-parameter-upon-decoding-c/

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
- unknown

Dedupe:
- id: `36914-h-02-incorrectly-assigned-decimal1-parameter-upon-decoding-c`
- fingerprint: `da5fed0e69f2a1a8a5f8e66636accda73cbbe70c3b57b33b5fd4894858dbcaf0`

Core exploit idea:
- When well data encodes decimal1 = 0 (meaning “default to 18”), the decoder checks decimal0 == 0 instead of decimal1 == 0, so decimal1 stays 0. Scaling token1 reserves by…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
