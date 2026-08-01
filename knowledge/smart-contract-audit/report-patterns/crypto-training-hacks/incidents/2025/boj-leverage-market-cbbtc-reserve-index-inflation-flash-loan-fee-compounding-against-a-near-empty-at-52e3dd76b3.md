# Crypto Training Exploit Pattern Stub: BoJ Leverage Market cbBTC reserve index inflation — flash-loan fee compounding against a near-empty aToken supply inflates the liquidity index to steal every listed asset

Source:
- https://crypto.training/hacks/2025-07-BoJLeverageMarket/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Base

Loss / impact summary:
- ~7,227.59 USD (mixed: WETH, USDC, AERO, MORPHO, DEGEN, VIRTUAL)

Tags:
- oracle/price-manipulation, defi/fee-manipulation, logic/incorrect-state-transition

Dedupe:
- id: `2025-07-BoJLeverageMarket`
- fingerprint: `52e3dd76b32224140260ac98bac06a0cdba30a6628ad14ed16e6b7086e4640a1`

Core exploit idea:
- The BoJ Pool is an Aave-v3-derived lending market on Base branded around "Bank of Japan" leverage. Like upstream Aave v3, when a flash loan is repaid the LP portion of t…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
