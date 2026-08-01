# Crypto Training Exploit Pattern Stub: Conic Finance (ETH Omnipool) — Curve LP Oracle Manipulation via Spot-Reserve Pricing

Source:
- https://crypto.training/hacks/2023-07-Conic_exp2/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2023

Chain:
- Ethereum

Loss / impact summary:
- ~$3.26M — net 1,724.17 ETH extracted by the attacker (≈ $1,886.87/ETH at the fork-block C…

Tags:
- unknown

Dedupe:
- id: `2023-07-Conic_exp2`
- fingerprint: `a93a2e9c79ea5f121d726f785b946366009158a62e79994e630104d0ed231f87`

Core exploit idea:
- Conic's ETH Omnipool mints/redeems its LP token (cncETH) at an exchange rate derived from the USD value of the Curve LP positions it holds (ConicEthPool._exchangeRate, _…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
