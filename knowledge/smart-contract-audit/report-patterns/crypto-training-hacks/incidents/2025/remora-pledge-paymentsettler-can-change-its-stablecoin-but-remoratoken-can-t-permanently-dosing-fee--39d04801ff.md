# Crypto Training Exploit Pattern Stub: Remora Pledge: PaymentSettler can change its stablecoin but RemoraToken can't, permanently DoSing fee-bearing transfers

Source:
- https://crypto.training/hacks/61177-paymentsettler-can-change-stablecoin-but-remoratoken-cant-/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `61177-paymentsettler-can-change-stablecoin-but-remoratoken-cant-`
- fingerprint: `39d04801ffc3b05e84a5887eea67db25de2269130c019f86656661ff3a7bb09c`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
