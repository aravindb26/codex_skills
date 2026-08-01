# Crypto Training Exploit Pattern Stub: DittoETH — New orders can overwrite active orders when order id reaches 65000

Source:
- https://crypto.training/hacks/27444-new-orders-can-overwrite-active-orders-when-order-id-reaches/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/linked-list-corruption, loss-of-funds/permanent-lock, access-control/missing-check

Dedupe:
- id: `27444-new-orders-can-overwrite-active-orders-when-order-id-reaches`
- fingerprint: `2957eed8abbe72dae112b4d0e1458f03481e81585bf1c6fbd6cfbc520456afe5`

Core exploit idea:
- 1. DittoETH tracks each order side (bids/asks/shorts) as a doubly-linked list between HEAD and TAIL sentinels, PLUS a second, dual-purpose "reuse chain" of cancelled ord…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
