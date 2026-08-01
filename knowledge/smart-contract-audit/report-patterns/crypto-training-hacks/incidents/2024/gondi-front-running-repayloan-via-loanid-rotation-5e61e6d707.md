# Crypto Training Exploit Pattern Stub: Gondi — front-running repayLoan via loanId rotation

Source:
- https://crypto.training/hacks/35212-h-10-the-attackers-front-running-repayloans-so-that-the-debt/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `35212-h-10-the-attackers-front-running-repayloans-so-that-the-debt`
- fingerprint: `5e61e6d707dd8fed9116a8037f551230e04137194409a9165a644b2be04afdcd`

Core exploit idea:
- 1. repayLoan requires _loan.hash() == _loans[loanId]. 2. mergeTranches writes a new loanId and delete _loans[old]. 3. Front-running a repay with merge makes the old id i…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
