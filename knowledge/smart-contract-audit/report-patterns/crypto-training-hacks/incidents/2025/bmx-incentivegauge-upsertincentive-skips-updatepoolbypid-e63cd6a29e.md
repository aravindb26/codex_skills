# Crypto Training Exploit Pattern Stub: BMX — IncentiveGauge.upsertIncentive() skips updatePoolByPid()

Source:
- https://crypto.training/hacks/62814-bmx-incentivegauge-upsertincentive-skips-updatepoolbypid/

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
- logic/reward-calculation, logic/wrong-condition

Dedupe:
- id: `62814-bmx-incentivegauge-upsertincentive-skips-updatepoolbypid`
- fingerprint: `e63cd6a29e41d542d90d814d7c726d91c866e9ee7e0dd7d11a4d26d157f977da`

Core exploit idea:
- The pool update is incorrectly inside the new-incentive branch, so an existing gauge can accrue rewards from a stale index.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
