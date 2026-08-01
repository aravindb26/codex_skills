# Crypto Training Exploit Pattern Stub: Rio Network — requested withdrawal can be impossible to settle due to EigenLayer share value appreciation

Source:
- https://crypto.training/hacks/30901-h-6-requested-withdrawal-can-be-impossible-to-settle-due-to/

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
- accounting/rate-mismatch, dos/liveness-freeze, liquid-staking/withdrawal-stuck

Dedupe:
- id: `30901-h-6-requested-withdrawal-can-be-impossible-to-settle-due-to`
- fingerprint: `94bfc7cb6ada51db918f17c15196e05261a886e9bcee7079b0bf3732b81da6d2`

Core exploit idea:
- 1. RioLRTCoordinator.requestWithdrawal() converts the withdrawal amount to a fixed number of EigenLayer shares, using the exchange rate at request time, and records that…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
