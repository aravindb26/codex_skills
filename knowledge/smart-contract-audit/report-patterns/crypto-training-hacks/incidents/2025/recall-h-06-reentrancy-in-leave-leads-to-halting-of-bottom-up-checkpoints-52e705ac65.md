# Crypto Training Exploit Pattern Stub: Recall — [H-06] Reentrancy in leave() leads to halting of bottom-up checkpoints

Source:
- https://crypto.training/hacks/65093-h-06-reentrancy-in-function/

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
- id: `65093-h-06-reentrancy-in-function`
- fingerprint: `52e705ac65f039d55f2b8af7597c396ffb34dabd76696ec717dd53c13218254d`

Core exploit idea:
- Reentrancy via genesis ETH refund + unguarded stake() bootstraps mid-leave; confirmDeposit reverts forever

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
