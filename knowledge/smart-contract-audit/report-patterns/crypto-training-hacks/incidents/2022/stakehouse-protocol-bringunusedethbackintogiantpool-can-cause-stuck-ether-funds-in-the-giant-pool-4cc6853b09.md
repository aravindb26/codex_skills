# Crypto Training Exploit Pattern Stub: Stakehouse Protocol — `bringUnusedETHBackIntoGiantPool` can cause stuck ether funds in the Giant Pool

Source:
- https://crypto.training/hacks/43029-h-06-bringunusedethbackintogiantpool-can-cause-stuck-ether-f/

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
- accounting/missing-state-update, liveness/frozen-funds, logic/asymmetric-operations

Dedupe:
- id: `43029-h-06-bringunusedethbackintogiantpool-can-cause-stuck-ether-f`
- fingerprint: `4cc6853b09c18c36529cd40278fd7e8481789121cf4f531bd3bae2cbbcf95a10`

Core exploit idea:
- 1. A depositor supplies ETH to the Giant Pool via depositETH. idleETH tracks "ETH available for withdrawal or staking" and is incremented. 2. The pool stakes that ETH in…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
