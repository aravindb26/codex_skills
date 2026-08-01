# Crypto Training Exploit Pattern Stub: INVISTECH buy-tax drained the AMM pair — fee-on-transfer tax charged from the pair's own reserves on every buy, breaking the constant-product invariant

Source:
- https://crypto.training/hacks/2025-02-INVISTECH/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- BNB Chain

Loss / impact summary:
- ~5.14 BNB (5.137937396574487084 WBNB net profit to attacker) [output.txt:1564-1565]

Tags:
- defi/fee-manipulation, logic/fee-calculation, oracle/price-manipulation

Dedupe:
- id: `2025-02-INVISTECH`
- fingerprint: `78a507769dcea6648180d53a310b8cef1fe0ce70f73bd009a2b5bc10bea855fc`

Core exploit idea:
- INVISTECH (INVT) is a fee-on-transfer BEP-20 on BSC paired with WBNB in a PancakeSwap V2 pool. Its custom _transfer charges a tax whenever either side of a transfer is a…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
