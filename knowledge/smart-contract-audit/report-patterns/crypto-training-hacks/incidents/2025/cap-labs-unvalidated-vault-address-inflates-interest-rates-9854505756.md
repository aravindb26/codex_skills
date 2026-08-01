# Crypto Training Exploit Pattern Stub: CAP Labs — unvalidated vault address inflates interest rates

Source:
- https://crypto.training/hacks/61535-unvalidated-vault-address-interest-rate/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- oracle/price-manipulation, input-validation/missing, dependency/unsafe-external-call

Dedupe:
- id: `61535-unvalidated-vault-address-interest-rate`
- fingerprint: `9854505756a25bac2da72db35998c49d77fd9e900ee4e283e911611fe2eed501`

Core exploit idea:
- VaultAdapter.rate accepts any vault address and trusts its currentUtilizationIndex/utilization responses. A malicious implementation returns extreme values and permanent…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
