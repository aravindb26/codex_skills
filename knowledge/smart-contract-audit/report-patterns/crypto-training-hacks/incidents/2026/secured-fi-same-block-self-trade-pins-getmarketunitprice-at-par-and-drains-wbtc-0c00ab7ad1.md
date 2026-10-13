# Crypto Training Exploit Pattern Stub: Secured.Fi — same-block self-trade pins `getMarketUnitPrice` at par and drains WBTC

Source:
- https://crypto.training/hacks/2026-09-securedfi/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Ethereum

Loss / impact summary:
- Incident ~$104K across bots. This PoC: 0.89899004 WBTC (~$72K) from TokenVault output.txt

Tags:
- oracle/price-manipulation, logic/price-calculation, oracle/missing-circuit-breaker

Dedupe:
- id: `2026-09-securedfi`
- fingerprint: `0c00ab7ad1bee6a9cf8887a1988f9c4f38699c68b65735016b58ea8dce5b2e67`

Core exploit idea:
- Secured.Fi values lending-order-book collateral from getMarketUnitPrice(). Within a block that is:

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
