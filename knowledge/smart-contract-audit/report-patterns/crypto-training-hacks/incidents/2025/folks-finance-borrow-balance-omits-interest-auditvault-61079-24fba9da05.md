# Crypto Training Exploit Pattern Stub: Folks Finance borrow balance omits interest — AuditVault 61079

Source:
- https://crypto.training/hacks/61079-folks-borrow-balance/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/incorrect-state-transition, arithmetic/precision-loss

Dedupe:
- id: `61079-folks-borrow-balance`
- fingerprint: `24fba9da052a079e4fbeaa73de7951c240f72ebce121574ec87400c50d19fe67`

Core exploit idea:
- getLoanLiquidity reports only principal and drops accrued interest from the borrow balance.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
