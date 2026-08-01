# Crypto Training Exploit Pattern Stub: Maia DAO — User may underpay for remote call ExecutionGas (missing Anycall premium)

Source:
- https://crypto.training/hacks/26048-h-14-user-may-underpay-for-the-remote-call-executiongas-on-t/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `26048-h-14-user-may-underpay-for-the-remote-call-executiongas-on-t`
- fingerprint: `010f0f4d933e553d73deda674ff898ac1ebd8d8a622feebeef6d496e19b41b58`

Core exploit idea:
- 1. _payExecutionGas deposits gasprice gas only.\n2. Anycall charges (gasprice+premium)gas.\n3. Gap taken from other users shared executionBudget.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
