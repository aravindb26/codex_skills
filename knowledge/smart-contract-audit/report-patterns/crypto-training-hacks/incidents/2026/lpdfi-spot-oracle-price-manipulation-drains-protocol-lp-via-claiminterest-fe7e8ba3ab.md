# Crypto Training Exploit Pattern Stub: LpdFi — Spot-Oracle Price Manipulation Drains Protocol LP via claimInterest

Source:
- https://crypto.training/hacks/2026-08-lpdfi/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- BNB Chain

Loss / impact summary:
- ~693,529.79 USDC (~$690K) drained from protocol LPD/USDC LP in the claim tx; public repor…

Tags:
- oracle/spot-price, oracle/price-manipulation, oracle/single-source, logic/price-calculation

Dedupe:
- id: `2026-08-lpdfi`
- fingerprint: `fe7e8ba3aba49247c92f2924eaf912fab68f4b280329c08b5b0839526029fc6d`

Core exploit idea:
- 1. LpdFi is a staking product. Users deposit LPD, open an “order” denominated in a notional uAmount (USDC units), and earn 0.5%/day interest (capped at 50% of uAmount).…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
