# Crypto Training Exploit Pattern Stub: Forte Float128 — [H-04] eq ignores L_MANTISSA_FLAG / dual encodings

Source:
- https://crypto.training/hacks/55706-h-04-unwrapping-while-equating-inside-the-eq-function-fails/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `55706-h-04-unwrapping-while-equating-inside-the-eq-function-fails`
- fingerprint: `d8bc4b2b67245ed73131582ee8b631c3ab38b66b250457abb16adb00fdaadf20`

Core exploit idea:
- 1. Mantissas may be M (38 digits) or L (72 digits); the L flag is bit 241 of the packed word. 2. eq only checks unwrap(a) == unwrap(b). 3. 1.0 encoded as L (1e71 10^-71)…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
