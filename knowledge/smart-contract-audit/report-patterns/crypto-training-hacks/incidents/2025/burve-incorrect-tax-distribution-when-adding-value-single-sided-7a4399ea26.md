# Crypto Training Exploit Pattern Stub: Burve — Incorrect tax distribution when adding value single-sided

Source:
- https://crypto.training/hacks/56953-h-4-incorrect-tax-distribution-when-adding-value-single-side/

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
- id: `56953-h-4-incorrect-tax-distribution-when-adding-value-single-side`
- fingerprint: `7a4399ea26c7ba0f5cdccfe3af1b270e1cec984667b900101891a08e1f366972`

Core exploit idea:
- 1. Single-sided adds charge a tax meant for existing LPs. 2. valueStaked is incremented before tax is written into earningsPerValueX128. 3. New LP is already in the deno…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
