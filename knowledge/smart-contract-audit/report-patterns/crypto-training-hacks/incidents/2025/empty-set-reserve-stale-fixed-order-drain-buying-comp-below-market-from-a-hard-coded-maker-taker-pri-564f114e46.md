# Crypto Training Exploit Pattern Stub: Empty Set Reserve stale fixed-order drain — buying COMP below market from a hard-coded maker/taker price

Source:
- https://crypto.training/hacks/2025-07-EmptySetReserve/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Ethereum

Loss / impact summary:
- ~$1,509.78 (≈ 0.4157 ETH extracted)

Tags:
- oracle/price-manipulation, oracle/stale-price, logic/price-calculation

Dedupe:
- id: `2025-07-EmptySetReserve`
- fingerprint: `564f114e4677faf8ec994f8e2b62124ebded566425af3e8c7f5ba77682371ae3`

Core exploit idea:
- Empty Set Reserve (ESR) is a legacy Empty Set Dollar derivative contract that, among other things, runs a small on-chain OTC "order book." Each order is just a (price, a…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
