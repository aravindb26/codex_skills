# Crypto Training Exploit Pattern Stub: HoldSafe price-manipulation referral drain — oracle pricing of stake value and rewards from a manipulable DEX spot route

Source:
- https://crypto.training/hacks/2025-06-HoldSafe/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- BNB Chain

Loss / impact summary:
- ~4,824.96 USD (6.9668 WBNB net profit, output.txt:1565)

Tags:
- oracle/price-manipulation, oracle/spot-price, defi/flash-loan-attack, logic/price-calculation

Dedupe:
- id: `2025-06-HoldSafe`
- fingerprint: `ef57a6faee1e2c5a2933575ec6577f692e0b8096b2225b8d884f1852c3e21cf8`

Core exploit idea:
- Hold_Safe is a BSC staking/"donation" contract: a user calls Stake(usdtAmount, referrer) to "donate" a USDT-denominated amount (capped at maximumDeposit = 2000 USDT). Th…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
