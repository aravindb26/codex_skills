# Crypto Training Exploit Pattern Stub: Zaros — LiquidationBranch::checkLiquidatableAccounts() array out-of-bounds

Source:
- https://crypto.training/hacks/37994-liquidationbranchcheckliquidatableaccounts-executes-for-loop/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/off-by-index, liveness/dos, integer-bounds/array-out-of-bounds

Dedupe:
- id: `37994-liquidationbranchcheckliquidatableaccounts-executes-for-loop`
- fingerprint: `f0e6b1399db94db0d8375bebbefdc238a7f4baf930df5e6b88c63778ed7c1450`

Core exploit idea:
- 1. checkLiquidatableAccounts(lowerBound, upperBound) is explicitly designed for segmented/paginated scanning of active trading accounts (per its own NatSpec @param docs)…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
