# Crypto Training Exploit Pattern Stub: Panoptic — commission fees can always be bypassed

Source:
- https://crypto.training/hacks/65027-h-03-commission-fees-can-always-be-bypassed-code4rena-panopt/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `65027-h-03-commission-fees-can-always-be-bypassed-code4rena-panopt`
- fingerprint: `04195f194cecc6ab7ee72f664f7f298b717993aa200e5bbe4cd8d4a20880d371`

Core exploit idea:
- 1. settleBurn takes commission = min(premiumFee, notionalFee). 2. _settleOptions passes long=short=amm=0 so notionalFee = 0 → commission 0. 3. If realizedPremium == 0 th…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
