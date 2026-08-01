# Crypto Training Exploit Pattern Stub: Tapioca DAO — GlpStrategy currentBalance ignores unclaimed rewards

Source:
- https://crypto.training/hacks/27533-h-43-accounted-balance-of-glpstrategy-does-not-match-withdra/

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
- id: `27533-h-43-accounted-balance-of-glpstrategy-does-not-match-withdra`
- fingerprint: `8c53f528883aeb2db560530d8e84be6428e3e6aa9e42688aea02bbbe64954d13`

Core exploit idea:
- 1. YieldBox prices shares from strategy.currentBalance(). 2. _currentBalance omits unclaimed rewards. 3. Deposit → harvest → withdraw extracts older depositors' rewards.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
