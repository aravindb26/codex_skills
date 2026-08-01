# Crypto Training Exploit Pattern Stub: InfinitySix — Stale 1-min TWAP + Instant Referral Bonus Over-Mint

Source:
- https://crypto.training/hacks/2026-03-InfinitySix/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2026

Chain:
- BNB Chain

Loss / impact summary:
- ~$273.8K USDT attacker profit (PoC net ~$277.2K without flash fees)

Tags:
- oracle/price-manipulation, logic/incorrect-calculation

Dedupe:
- id: `2026-03-InfinitySix`
- fingerprint: `69e5a1ed9bb73376f746d3f6652cdb44f96d1af3a73ecf43573ab0a465f4ba98`

Core exploit idea:
- invest() immediately credits the sponsor with directBonus += 5% of the invest amount. withdraw() pays that USDT-denominated bonus in i6 tokens priced by twapPrice, but u…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
