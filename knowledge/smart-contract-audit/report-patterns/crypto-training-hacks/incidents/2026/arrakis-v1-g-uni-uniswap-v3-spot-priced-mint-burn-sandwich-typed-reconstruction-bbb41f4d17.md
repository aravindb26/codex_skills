# Crypto Training Exploit Pattern Stub: Arrakis V1 G-UNI — Uniswap V3 spot-priced `mint`/`burn` sandwich (typed reconstruction)

Source:
- https://crypto.training/hacks/2026-08-arrakisguni/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Ethereum

Loss / impact summary:
- 2.941350352900037140 WETH (~$7,170) from the legacy G-UNI ENS/WETH vault output.txt

Tags:
- defi/sandwich-attack, oracle/spot-price, oracle/missing-circuit-breaker

Dedupe:
- id: `2026-08-arrakisguni`
- fingerprint: `bbb41f4d179c178fac0adb013b1be9cb78dd5dfe93213ac97cae8e241643e275`

Core exploit idea:
- Arrakis V1 (G-UNI) is a shared Uniswap V3 LP token. mint() and burn() size deposits and redemptions from getUnderlyingBalances(), which reads the pool's instantaneous sl…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
