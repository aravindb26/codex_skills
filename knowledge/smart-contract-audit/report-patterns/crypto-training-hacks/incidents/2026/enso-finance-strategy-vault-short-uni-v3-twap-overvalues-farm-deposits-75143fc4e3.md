# Crypto Training Exploit Pattern Stub: Enso Finance strategy vault — short Uni V3 TWAP overvalues FARM deposits

Source:
- https://crypto.training/hacks/2026-09-ensofinance/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Ethereum

Loss / impact summary:
- Headline ~5.6 ETH spot of UNI/AAVE/MKR pulled, net of 0.683 WETH spent on FARM. PoC reali…

Tags:
- oracle/manipulable-twap, oracle/spot-price, oracle/missing-circuit-breaker, logic/price-calculation

Dedupe:
- id: `2026-09-ensofinance`
- fingerprint: `75143fc4e38bb599d1e4c8cb619d2b9c84411ea828147a3315b43f0428b8ef73`

Core exploit idea:
- The Enso strategy vault mints deposit shares as:

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
