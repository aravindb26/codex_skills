# Crypto Training Exploit Pattern Stub: CAP Labs — inconsistent vault balance tracking bricks borrowing

Source:
- https://crypto.training/hacks/61528-inconsistent-balance-tracking-vault-dos/

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
- logic/state-update, dos/frozen-funds, input-validation/missing

Dedupe:
- id: `61528-inconsistent-balance-tracking-vault-dos`
- fingerprint: `9a37b6da1558e516d852b8cba7f4e73c1a00f3cdbd235f0358e60f769fd70da1`

Core exploit idea:
- An untracked donation supplies physical tokens for burn, but the burn still decrements totalSupplies. The accounting invariant falls below totalBorrows and subsequent bo…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
