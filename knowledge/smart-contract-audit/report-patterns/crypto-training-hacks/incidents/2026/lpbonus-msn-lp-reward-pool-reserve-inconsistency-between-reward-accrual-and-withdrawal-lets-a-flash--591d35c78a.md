# Crypto Training Exploit Pattern Stub: LPBonus (MSN LP-reward pool) — reserve-inconsistency between reward accrual and withdrawal lets a flash-manipulated reserve inflate an LP's FIST claim

Source:
- https://crypto.training/hacks/2026-09-lpbonus/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- BNB Chain

Loss / impact summary:
- Final attacker USDT balance 92,633.859396071632955691 (≈ $92.6k). The exploit's net new U…

Tags:
- logic/reward-calculation, oracle/price-manipulation, defi/fee-manipulation, defi/flash-loan

Dedupe:
- id: `2026-09-lpbonus`
- fingerprint: `591d35c78a4d461836ef862b3139d50a783d77837fd1bc04c35cb73d548092be`

Core exploit idea:
- 1. LPBonus is an LP-reward pool for the MSN token. Its reward callbacks are all gated require(msg.sender == MSN) — they are hooks the MSN token fires from inside its own…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
