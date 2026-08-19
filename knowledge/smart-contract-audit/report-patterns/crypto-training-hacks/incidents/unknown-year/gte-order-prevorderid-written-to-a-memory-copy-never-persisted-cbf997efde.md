# Crypto Training Exploit Pattern Stub: GTE: order.prevOrderId written to a memory copy, never persisted

Source:
- https://crypto.training/hacks/64869-h-01-order-double-linked-list-is-broken-because-orderprevord/

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
- id: `64869-h-01-order-double-linked-list-is-broken-because-orderprevord`
- fingerprint: `cbf997efde32dfbd43fef965096ed6ae456b9695dd4e12bb2ca1c7ee5b976218`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
