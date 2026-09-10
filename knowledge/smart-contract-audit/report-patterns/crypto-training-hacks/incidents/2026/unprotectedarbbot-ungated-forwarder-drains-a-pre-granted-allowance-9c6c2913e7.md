# Crypto Training Exploit Pattern Stub: UnprotectedArbBot: ungated forwarder drains a pre-granted allowance

Source:
- https://crypto.training/hacks/2026-07-unprotectedarbbot/

Imported:
- 2026-09-10

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2026

Chain:
- Base

Loss / impact summary:
- ~16.623 WETH (~$31.7K)

Tags:
- unknown

Dedupe:
- id: `2026-07-unprotectedarbbot`
- fingerprint: `9c6c2913e70e63bde0d8bdf0acf20d87cf5de073c1a4860d8ec92f924eb926c7`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
