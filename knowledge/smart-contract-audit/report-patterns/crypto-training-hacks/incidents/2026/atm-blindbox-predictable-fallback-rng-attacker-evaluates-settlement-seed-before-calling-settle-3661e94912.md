# Crypto Training Exploit Pattern Stub: ATM BlindBox predictable fallback RNG — attacker evaluates settlement seed before calling `settle`

Source:
- https://crypto.training/hacks/2026-03-ATMBlindBox/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2026

Chain:
- BNB Chain

Loss / impact summary:
- ~13,000,000 ATM (~$99,000) reported; single attacker bet realized 285,000 ATM net profit…

Tags:
- logic/incorrect-state-transition, oracle/missing-validation, oracle/spot-price

Dedupe:
- id: `2026-03-ATMBlindBox`
- fingerprint: `3661e949126e0b84e1698c07c1d254e0f28cde6005fd9e44a509550d54f15945`

Core exploit idea:
- BlindBox is a binary odd/even betting game attached to the ATM token. A user burns ATM to the 0x…dEaD address, the entry hook onBlindBoxEntry records a bet with the user…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
