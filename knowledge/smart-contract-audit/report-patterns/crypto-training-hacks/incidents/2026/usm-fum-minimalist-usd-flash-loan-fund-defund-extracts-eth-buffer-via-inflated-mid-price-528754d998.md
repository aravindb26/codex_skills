# Crypto Training Exploit Pattern Stub: USM / FUM (Minimalist USD) — Flash-loan fund/defund extracts ETH buffer via inflated mid-price

Source:
- https://crypto.training/hacks/2026-08-usm_fum/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Ethereum

Loss / impact summary:
- ~70.83 ETH (~$160K) drained from the USM ETH pool; PoC profit 70.831554410317728328 WETH

Tags:
- logic/price-calculation, arithmetic/rounding, governance/flash-loan-attack, oracle/price-manipulation

Dedupe:
- id: `2026-08-usm_fum`
- fingerprint: `528754d9987aec6918269821a68c75816cadbacb925f8d5306cc9f3839dcc89c`

Core exploit idea:
- 1. Minimalist USM is an ETH-backed stablecoin; FUM is the buffer/equity token. Users fund() ETH to mint FUM and defund() FUM to redeem ETH from the shared pool.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
