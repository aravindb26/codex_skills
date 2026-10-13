# Crypto Training Exploit Pattern Stub: Tectonic TONIC Thin-Oracle Collateral Manipulation — Over-Borrow Against Inflated Spot Mark

Source:
- https://crypto.training/hacks/2026-08-tectonictonicoraclemanipulation/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Cronos

Loss / impact summary:
- ~$75M (PeckShield ~$74M; researcher Weilin Li ~$66M then +~$8M → ~$75M). PoC drains 55M U…

Tags:
- oracle/spot-price, oracle/price-manipulation, oracle/missing-validation, oracle/single-source

Dedupe:
- id: `2026-08-tectonictonicoraclemanipulation`
- fingerprint: `07432dbdaa3f30624a305f9021a7f97d9375edb7c1a2df1701e33ceb06790f08`

Core exploit idea:
- 1. Tectonic listed TONIC (its own illiquid governance token) as collateral with a 20% collateral factor. 2. The protocol’s internal oracle priced TONIC from a VVS + Cryp…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
