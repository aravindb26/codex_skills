# Crypto Training Exploit Pattern Stub: Kinetiq — Some stakers may fail to withdraw staking HYPE

Source:
- https://crypto.training/hacks/58614-h-06-some-stakers-may-fail-to-withdraw-staking-hype-pashov-a/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `58614-h-06-some-stakers-may-fail-to-withdraw-staking-hype-pashov-a`
- fingerprint: `3bcb4b9997e6dea66e42577de3abde7d610c4b19eaa60895c379b050626f882d`

Core exploit idea:
- 1. Stake path fills hypeBuffer up to targetBuffer before delegating. 2. queueWithdrawal never spends the buffer; it always undelegates from currentDelegation. 3. After a…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
