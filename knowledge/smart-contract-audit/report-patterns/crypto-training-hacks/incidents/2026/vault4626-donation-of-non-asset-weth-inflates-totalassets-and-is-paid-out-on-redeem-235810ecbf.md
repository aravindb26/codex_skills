# Crypto Training Exploit Pattern Stub: Vault4626 — Donation of Non-Asset WETH Inflates totalAssets() and Is Paid Out on redeem()

Source:
- https://crypto.training/hacks/2026-06-Vault4626/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2026

Chain:
- Base

Loss / impact summary:
- ~13.53 WETH profit (18366634484619156667 − 4837426434749649311 = 13529208039869487356 wei)

Tags:
- defi/donation-attack, logic/incorrect-accounting, defi/flash-loan-attack

Dedupe:
- id: `2026-06-Vault4626`
- fingerprint: `235810ecbf14ed10930b62d59e03946de5c1f101463a5d22f38927720997c455`

Core exploit idea:
- 1. totalAssets() (Vault4626.sol:496-536) returns idle USDC + LP value plus TWAP-quoted vault balances of the non-asset token (WETH):

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
