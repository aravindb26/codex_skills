# Crypto Training Exploit Pattern Stub: Bonzo Lend / Supra Oracle — BLS Zero-Signature Price Forgery

Source:
- https://crypto.training/hacks/2026-07-BonzoLend/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2026

Chain:
- Other

Loss / impact summary:
- ~$9.05M Wallet A principal (BlockSec / Bonzo Finance; excludes ~$1.0M white-hat Wallet B)

Tags:
- auth/signature-validation, oracle/missing-validation, oracle/price-manipulation, input-validation/missing-validation

Dedupe:
- id: `2026-07-BonzoLend`
- fingerprint: `68949ec772d95b6f9987775de9f4744d902197891161467777245400ca1aa142`

Core exploit idea:
- 1. Bonzo Lend prices ecosystem collateral (including SAUCE) from Supra's on-chain pull-oracle feed. It does not re-verify committee signatures; it reads the latest store…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
