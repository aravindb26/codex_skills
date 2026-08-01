# Crypto Training Exploit Pattern Stub: LEND — Cross-chain debt accrues incorrectly

Source:
- https://crypto.training/hacks/58395-lend-cross-chain-debt-accrues-incorrectly/

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
- logic/reward-calculation, oracle/stale-price

Dedupe:
- id: `58395-lend-cross-chain-debt-accrues-incorrectly`
- fingerprint: `fba7821ecd357eb2934cb79c96c2908d95ee8ce262544bbf96853b7c31e847b1`

Core exploit idea:
- Debt interest is accrued against the stale local principal after a remote borrow, causing the cross-chain debt to diverge from the canonical balance.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
