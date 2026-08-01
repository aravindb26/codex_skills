# Crypto Training Exploit Pattern Stub: DogeAlliance sync() reserve manipulation — LP pairs with token balances desynced from reserves drained by permissionless sync + swap

Source:
- https://crypto.training/hacks/2025-05-DogeAlliance/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- BNB Chain

Loss / impact summary:
- ~990.33 USD (1.5044 WBNB at the time of the incident) — attacker net profit per [output.t…

Tags:
- oracle/price-manipulation, defi/slippage

Dedupe:
- id: `2025-05-DogeAlliance`
- fingerprint: `16a6656c1405708167c9e15fe769d5e56a9caa2ab50bbca3aa028798a98d3639`

Core exploit idea:
- DogeAlliance (DOGEALLY, BSC) is a meme token that listed across several PancakeSwap/ApeSwap-style DOGEALLY/WBNB, DOGEALLY/BUSD and DOGEALLY/CAKE LP pairs. The DOGEALLY t…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
