# Crypto Training Exploit Pattern Stub: Arrakis Finance G-UNI — Uniswap V3 mint/burn sandwich with no same-tx snapshot

Source:
- https://crypto.training/hacks/2026-08-arrakisfinance/

Imported:
- 2026-09-10

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Ethereum

Loss / impact summary:
- 2.941350352900037140 WETH (~$7,170) from the legacy G-UNI ENS–WETH vault

Tags:
- defi/sandwich-attack, oracle/spot-price, oracle/missing-circuit-breaker

Dedupe:
- id: `2026-08-arrakisfinance`
- fingerprint: `bade2a3a428f78e32dad7cd7698ea1be2b637bbf91445dd3ce83a1aeb84544a7`

Core exploit idea:
- 1. Arrakis V1 / G-UNI is a shared Uniswap V3 LP token. mint() and burn() size deposits and redemptions from getUnderlyingBalances(), which reads the pool's live slot0()…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
