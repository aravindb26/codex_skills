# Crypto Training Exploit Pattern Stub: Rio Network — setting the strategy cap to 0 does not update total shares held or the withdrawal queue

Source:
- https://crypto.training/hacks/30897-h-2-setting-the-strategy-cap-to-0-does-not-update-the-total/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- accounting/missing-decrement, logic/wrong-condition, liquid-staking/double-counted-shares

Dedupe:
- id: `30897-h-2-setting-the-strategy-cap-to-0-does-not-update-the-total`
- fingerprint: `e99238bc184853a8bc29283bbfd7c21e4c3c4e5fbf4b991978fe7d4580d26477`

Core exploit idea:
- 1. OperatorRegistryV1Admin.setOperatorStrategyCap(operatorId, 0) — used both directly and when deactivating/removing an operator — queues the operator's full allocation…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
