# Crypto Training Exploit Pattern Stub: Tapioca DAO — repay allowance checked on part, pulls elastic

Source:
- https://crypto.training/hacks/27534-h-44-bigbangrepay-and-singularityrepay-spend-more-than-allow/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `27534-h-44-bigbangrepay-and-singularityrepay-spend-more-than-allow`
- fingerprint: `b4fc8a7f04a6f6abaecdf8f48de6788d51740fb0ec2438a70473bf77bb040ade`

Core exploit idea:
- 1. approveBorrow documents a maximum spendable amount. 2. repay checks allowance against debt part. 3. _repay converts part→elastic and withdraws amount > part after int…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
