# Crypto Training Exploit Pattern Stub: Stakehouse Protocol — `withdrawETH` from `GiantMevAndFeesPool` can steal most of the ETH because `idleETH` is reduced before burning the LP token

Source:
- https://crypto.training/hacks/43031-h-08-function-withdraweth-from-giantmevandfeespool-can-steal/

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
- logic/wrong-condition, accounting/reward-inflation, logic/instruction-ordering

Dedupe:
- id: `43031-h-08-function-withdraweth-from-giantmevandfeespool-can-steal`
- fingerprint: `8e2140b688dd2c25b88e3f75a55b03ee98b13fb2f9f89277eefe2cd4d6c50943`

Core exploit idea:
- 1. GiantPoolBase.withdrawETH does, in this exact order: idleETH -= _amount; then lpTokenETH.burn(msg.sender, _amount); then a plain ETH transfer of _amount to msg.sender…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
