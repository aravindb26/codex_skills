# Crypto Training Exploit Pattern Stub: Polynomial — Exchange._liquidate burns too much powerPerp

Source:
- https://crypto.training/hacks/20224-h-01-exchange-liquidate-function-can-cause-liquidator-to-bur/

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
- liquidation/over-burn, accounting/asymmetric-settlement

Dedupe:
- id: `20224-h-01-exchange-liquidate-function-can-cause-liquidator-to-bur`
- fingerprint: `7e8706a5d33ceed6ba81bc0032bfd23aa32c163789503a8298b939bbba925b8d`

Core exploit idea:
- When ShortCollateral caps collateral returned on an underwater short, Exchange still burns the full debtRepaying of powerPerp from the liquidator

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
