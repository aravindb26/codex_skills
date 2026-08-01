# Crypto Training Exploit Pattern Stub: LEND — Cross-chain repayment updates same-chain borrow balances

Source:
- https://crypto.training/hacks/58385-lend-cross-chain-repayment-updates-same-chain-borrow-balances/

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
- logic/state-update, bridge/missing-validation

Dedupe:
- id: `58385-lend-cross-chain-repayment-updates-same-chain-borrow-balances`
- fingerprint: `db0672a6521a0fa7caebaa4c5560d1dc06082f6c36be1245c6f9256dcea2df11`

Core exploit idea:
- repayBorrowInternal() updates only the local market mapping, leaving the remote debt unchanged after a cross-chain repayment.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
