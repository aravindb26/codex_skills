# Crypto Training Exploit Pattern Stub: CAP Labs — decimal count creates an inaccurate staked price

Source:
- https://crypto.training/hacks/61540-stakedcap-decimals-price/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- arithmetic/decimal-mismatch, arithmetic/precision-loss, logic/price-calculation

Dedupe:
- id: `61540-stakedcap-decimals-price`
- fingerprint: `495d1b6e7be64fa64bc9febcf8b00b5a6d1be3a0fc84e60ce6893119b5ebb805`

Core exploit idea:
- The adapter multiplies by capTokenDecimals and divides by stakedTokenDecimals instead of applying 10decimals. Six- and eighteen-decimal assets therefore receive a nonsen…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
