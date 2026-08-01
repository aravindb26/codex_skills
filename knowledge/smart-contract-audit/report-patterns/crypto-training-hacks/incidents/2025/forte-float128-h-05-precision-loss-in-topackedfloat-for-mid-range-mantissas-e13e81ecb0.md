# Crypto Training Exploit Pattern Stub: Forte Float128 — [H-05] Precision loss in toPackedFloat for mid-range mantissas

Source:
- https://crypto.training/hacks/55707-h-05-precision-loss-in-topackedfloat-function-when-mantissa/

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
- id: `55707-h-05-precision-loss-in-topackedfloat-function-when-mantissa`
- fingerprint: `e13e81ecb0acaaab32b887d231e184acaa19e9a585b92dcd35375fb57ef50db2`

Core exploit idea:
- 1. Mantissas with 39–71 digits sit between M-max (38) and L-min (72). 2. toPackedFloat decides M vs L from the exponent alone. 3. For 2^235 with exponent -51, the encode…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
