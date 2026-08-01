# Crypto Training Exploit Pattern Stub: INIT Capital — liquidations can be prevented by frontrunning and liquidating 1 debt

Source:
- https://crypto.training/hacks/29589-h-01-liquidations-can-be-prevented-by-frontrunning-and-liqui/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/liquidation-logic, dos/liquidation-evasion

Dedupe:
- id: `29589-h-01-liquidations-can-be-prevented-by-frontrunning-and-liqui`
- fingerprint: `49e31f799c8e88e3f1e773630212775f59c868cb907eb29c165fb74fefa0c21a`

Core exploit idea:
- 1. PosManager.updatePosDebtShares does extraInfo.totalInterest += (debtAmtCurrent - extraInfo.lastDebtAmt), commented // NOTE: debtAmtCurrent is always >= lastDebtAmt. 2…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
