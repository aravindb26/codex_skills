# Crypto Training Exploit Pattern Stub: Rubicon — Migration can underpay users via price manipulation

Source:
- https://crypto.training/hacks/48953-h-14-users-might-get-less-assets-than-expected-upon-migratio/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `48953-h-14-users-might-get-less-assets-than-expected-upon-migratio`
- fingerprint: `9c0e7cf1f6c0a5dcd14a24e4f9c2392bf48b9febdf864ca9c01e275fd5fdd3f2`

Core exploit idea:
- migrate redeems V1 then mints V2 with no minOut; low-liquidity exchangeRate inflation rounds victim to 0 shares.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
