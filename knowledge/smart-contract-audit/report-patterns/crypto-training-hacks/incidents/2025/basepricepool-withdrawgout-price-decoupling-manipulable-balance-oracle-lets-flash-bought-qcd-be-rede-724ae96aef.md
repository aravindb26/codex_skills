# Crypto Training Exploit Pattern Stub: BasePricePool `withdrawGOUT` price-decoupling — manipulable-balance oracle lets flash-bought QCD be redeemed for GOUT at an inflated internal rate

Source:
- https://crypto.training/hacks/2025-06-BasePricePool/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- BNB Chain

Loss / impact summary:
- ~802.57 USD (≈800.97 USDT net profit in the reproduced trace)

Tags:
- oracle/price-manipulation, oracle/spot-price, logic/price-calculation, defi/flash-loan-attack

Dedupe:
- id: `2025-06-BasePricePool`
- fingerprint: `724ae96aefdb859b2378635dbd10bd7c0f399c2de7a91ca348b601867d5d5a20`

Core exploit idea:
- BasePricePool is a simple "coin-to-GOUT" exchange: a user calls withdrawGOUT(amount) with a QCD (coin) allowance, the contract pulls the QCD, computes how many GOUT toke…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
