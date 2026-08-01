# Crypto Training Exploit Pattern Stub: ParaSpace — [H-03] Interest rates are incorrect on Liquidation

Source:
- https://crypto.training/hacks/15976-h-03-interest-rates-are-incorrect-on-liquidation-code4rena-p/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/liquidation-logic

Dedupe:
- id: `15976-h-03-interest-rates-are-incorrect-on-liquidation-code4rena-p`
- fingerprint: `7ded7313424c4e47ba30f2fad50d17adfb92c1263a47322f488b818c9a45ba63`

Core exploit idea:
- 1. _burnDebtTokens safeTransferFroms the repayment into the xToken, then calls updateInterestRates(liquidityAdded). 2. calculateInterestRates does balanceOf(xToken) + li…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
