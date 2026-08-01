# Crypto Training Exploit Pattern Stub: Burve — Incorrect implementation of ERC4626ViewAdjustor

Source:
- https://crypto.training/hacks/56951-burve-incorrect-implementation-of-erc4626viewadjustor/

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
- logic/price-calculation, arithmetic/decimal-mismatch

Dedupe:
- id: `56951-burve-incorrect-implementation-of-erc4626viewadjustor`
- fingerprint: `4bb9a336acfe8b82a26f0400b5a17b0df3088293c9b7509f6185386f406088e4`

Core exploit idea:
- The view adjustor applies the fee conversion in the wrong direction, reporting nominal shares where callers expect net assets.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
