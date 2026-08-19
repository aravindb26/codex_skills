# Crypto Training Exploit Pattern Stub: NUTS Finance: A valid large feed price (>~$100k) overflows getPrice()'s plain 256-bit `compositePrice *

Source:
- https://crypto.training/hacks/62694-arithmetic-overflow-in-getprice-when-feeds-return-large-valu/

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
- id: `62694-arithmetic-overflow-in-getprice-when-feeds-return-large-valu`
- fingerprint: `9b098dcd28faac56a5729394134545b7a147da45d0fce27ad86961e5b5e113a5`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
