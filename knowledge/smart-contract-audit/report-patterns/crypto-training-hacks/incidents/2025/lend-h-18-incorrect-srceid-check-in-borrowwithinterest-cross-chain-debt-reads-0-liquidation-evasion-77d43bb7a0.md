# Crypto Training Exploit Pattern Stub: LEND H-18: incorrect `srcEid` check in `borrowWithInterest` (cross-chain debt reads 0 → liquidation evasion)

Source:
- https://crypto.training/hacks/58387-h-18-incorrect-srceid-check-in-borrowwithinterest-sherlock/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `58387-h-18-incorrect-srceid-check-in-borrowwithinterest-sherlock`
- fingerprint: `77d43bb7a049e63ce4d320259f96da8e1fe904b1bf0b2d75b8b10b2cfb0a63a2`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
