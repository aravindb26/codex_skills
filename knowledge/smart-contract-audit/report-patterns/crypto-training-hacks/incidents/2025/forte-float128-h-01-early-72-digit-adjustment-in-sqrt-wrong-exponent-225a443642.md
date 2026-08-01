# Crypto Training Exploit Pattern Stub: Forte Float128 — [H-01] Early 72-digit adjustment in sqrt wrong exponent

Source:
- https://crypto.training/hacks/55703-h-01-early-72-digit-adjustment-in-sqrt-will-lead-to-incorrec/

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
- id: `55703-h-01-early-72-digit-adjustment-in-sqrt-will-lead-to-incorrec`
- fingerprint: `225a44364294977dac2232ddd209171fd69dece6c5326c2eefec55d7136481a0`

Core exploit idea:
- 1. Large-path sqrt computes a 73-digit rMan via Uint512.sqrt512. 2. The code trims to 72 digits (rMan /= 10; ++rExp) before rExp /= 2. 3. Integer division drops the +1 (…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
