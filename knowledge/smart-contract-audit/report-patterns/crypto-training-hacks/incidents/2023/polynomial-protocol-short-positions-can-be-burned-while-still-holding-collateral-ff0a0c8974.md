# Crypto Training Exploit Pattern Stub: Polynomial Protocol — short positions can be burned while still holding collateral

Source:
- https://crypto.training/hacks/20226-h-03-short-positions-can-be-burned-while-holding-collateral/

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
- logic/wrong-condition, loss-of-funds/locked-funds, nft/burn-with-residual-state

Dedupe:
- id: `20226-h-03-short-positions-can-be-burned-while-holding-collateral`
- fingerprint: `ff0a0c89748ab1eaee3f03399fb5100dfbc2a208c70a83124198624f5735e7de`

Core exploit idea:
- 1. ShortToken.adjustPosition writes the new shortAmount, then burns the position's ERC721 whenever shortAmount == 0. 2. It never checks collateralAmount. A position can…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
