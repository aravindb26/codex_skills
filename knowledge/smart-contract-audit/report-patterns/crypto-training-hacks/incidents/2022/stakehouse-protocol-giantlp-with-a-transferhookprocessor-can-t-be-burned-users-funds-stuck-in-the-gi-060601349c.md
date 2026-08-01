# Crypto Training Exploit Pattern Stub: Stakehouse Protocol — GiantLP with a `transferHookProcessor` can't be burned, users' funds stuck in the Giant Pool

Source:
- https://crypto.training/hacks/43030-h-07-giantlp-with-a-transferhookprocessor-cant-be-burned-use/

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
- logic/missing-guard-clause, liveness/frozen-funds, logic/asymmetric-branches

Dedupe:
- id: `43030-h-07-giantlp-with-a-transferhookprocessor-cant-be-burned-use`
- fingerprint: `060601349c01d076deff0d43d35445bbeea88f61965d33f62d1542f380ed44e8`

Core exploit idea:
- 1. GiantLP calls transferHookProcessor.beforeTokenTransfer(_from, _to, amount) on every mint/burn/transfer whenever a hook processor is set. 2. GiantMevAndFeesPool (whic…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
