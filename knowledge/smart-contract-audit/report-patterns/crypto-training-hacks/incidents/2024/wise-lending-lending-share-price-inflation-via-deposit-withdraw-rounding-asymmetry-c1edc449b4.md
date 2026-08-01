# Crypto Training Exploit Pattern Stub: Wise Lending — Lending-Share Price Inflation via Deposit/Withdraw Rounding Asymmetry

Source:
- https://crypto.training/hacks/2024-01-WiseLending02/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2024

Chain:
- Ethereum

Loss / impact summary:
- ~$464,000 (live incident, multiple drained pools)

Tags:
- arithmetic/rounding-direction, arithmetic/rounding

Dedupe:
- id: `2024-01-WiseLending02`
- fingerprint: `c1edc449b48d8a007f6b6ad3f84a5f59eced5801d59735f2522fa5734ad096e9`

Core exploit idea:
- WiseLending is a share-based money market. Each lending pool tracks two numbers — a token accumulator pseudoTotalPool and a share accumulator totalDepositShares — and th…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
