# Crypto Training Exploit Pattern Stub: More Markets (Flow EVM) — Ankr bonded LST + 97% E-mode drains the WFLOW reserve

Source:
- https://crypto.training/hacks/2026-08-moremarkets/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Other

Loss / impact summary:
- 15,488,124.145 WFLOW emptied from mFlowWFLOW (~$9.3M detector impact at Blockaid's print)…

Tags:
- oracle/wrong-feed, oracle/missing-validation, logic/price-calculation

Dedupe:
- id: `2026-08-moremarkets`
- fingerprint: `82d03b6a1d98a1b6d6eb8f48c5d41ba3e27efd398d8e8a017463f4d06a73c178`

Core exploit idea:
- 1. More Markets is an Aave v3 fork on Flow EVM. ANKRFLOW and WFLOW sit in MOST Mode / E-mode category 1 with 97% LTV / 97.5% LT. 2. AaveOracle.getAssetPrice returns the…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
