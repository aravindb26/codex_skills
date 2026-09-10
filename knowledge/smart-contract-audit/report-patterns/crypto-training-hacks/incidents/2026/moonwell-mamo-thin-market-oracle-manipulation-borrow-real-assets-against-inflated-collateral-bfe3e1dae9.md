# Crypto Training Exploit Pattern Stub: Moonwell MAMO Thin-Market Oracle Manipulation — Borrow Real Assets Against Inflated Collateral

Source:
- https://crypto.training/hacks/2026-08-moonwellmamooraclemanipulation/

Imported:
- 2026-09-10

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Base

Loss / impact summary:
- ~$8.7M–$10M (ExVul: ~71.36 cbBTC / ~$5.7M from mcbBTC alone; SlowMist totals ~$8.7M incl.…

Tags:
- oracle/spot-price, oracle/thin-liquidity, oracle/missing-validation

Dedupe:
- id: `2026-08-moonwellmamooraclemanipulation`
- fingerprint: `bfe3e1dae922e1395ffb8a5d5fb14cdb4ffaa182fc4fcbf6655280cf9c8c8a1f`

Core exploit idea:
- 1. Moonwell listed MAMO as collateral and priced it through a feed that tracks a thin MAMO/USD market. 2. Attacker pumped MAMO ~$0.0105 → ~$0.088 (~8×), so getUnderlying…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
