# Crypto Training Exploit Pattern Stub: SpiralHookV2 — Uniswap V4 spot `getSlot0` prices borrow collateral, and `noSameBlockSwap` keys the guard on `tx.origin`

Source:
- https://crypto.training/hacks/2026-09-spiralhookv2/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Ethereum

Loss / impact summary:
- 10.707280986613435410 ETH net. 54 ETH buys 141,059.241329869479115783 SPIRAL; six same-bl…

Tags:
- oracle/spot-price, oracle/price-manipulation, access-control/tx-origin, access-control/guard-bypass

Dedupe:
- id: `2026-09-spiralhookv2`
- fingerprint: `e107a05f3dc479792b33975bfe5a49b288307575a028203ea5ec033be2727deb`

Core exploit idea:
- 1. Spiral's canonical hook is a Uniswap V4 hook and a SPIRAL/ETH lender. borrow(collateralSpiral, minEthOut) pulls SPIRAL and sizes the ETH debt off LDF.spiralValueInETH…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
