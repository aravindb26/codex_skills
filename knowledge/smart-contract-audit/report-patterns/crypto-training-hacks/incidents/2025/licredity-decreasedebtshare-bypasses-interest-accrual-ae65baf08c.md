# Crypto Training Exploit Pattern Stub: Licredity — decreaseDebtShare bypasses interest accrual

Source:
- https://crypto.training/hacks/62350-licreditydecreasedebtshare-bypasses-interest-accrual-cyfrin/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- accounting/missing-accrual

Dedupe:
- id: `62350-licreditydecreasedebtshare-bypasses-interest-accrual-cyfrin`
- fingerprint: `ae65baf08cae59764eeebdf9f9f36b9c26dc03485643ef0462f6b3541fe62aaa`

Core exploit idea:
- 1. Interest accrues only in unlock / swap / LP add-remove paths. 2. decreaseDebtShare is allowed outside unlock because it only reduces debt. 3. It burns fullMulDivUp(de…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
