# Crypto Training Exploit Pattern Stub: Polynomial — Hedging during liquidation over-hedges the LiquidityPool

Source:
- https://crypto.training/hacks/20225-h-02-hedging-during-liquidation-is-incorrect-code4rena-polyn/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- liquidation/incorrect-hedge, accounting/double-count

Dedupe:
- id: `20225-h-02-hedging-during-liquidation-is-incorrect-code4rena-polyn`
- fingerprint: `836f1ae7ee06409bb0a8cf3f9d04b505c45b57ce22cced212a49791f101464e4`

Core exploit idea:
- Liquidation already balances short inventory and powerPerp burn, but pool.liquidate still hedges again and burns pool funds as fees

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
