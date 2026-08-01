# Crypto Training Exploit Pattern Stub: Polynomial Protocol — missing totalFunds update in LiquidityPool.openShort shortchanges LP holders

Source:
- https://crypto.training/hacks/20230-h-07-missing-totalfunds-update-in-liquiditypools-openshort-c/

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
- accounting/fee-accounting, logic/missing-state-update, loss-of-funds/direct-drain

Dedupe:
- id: `20230-h-07-missing-totalfunds-update-in-liquiditypools-openshort-c`
- fingerprint: `5562118d0c1cf67315ea4c75a6df25ea9d60042712899ecf73c45c07393a1bc7`

Core exploit idea:
- 1. openShort charges the trader a fee by paying out only totalCost = tradeCost - fees, so the pool keeps the fee. 2. Of that fee, externalFee goes to the dev/hedge and t…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
