# Crypto Training Exploit Pattern Stub: LEND — Cross-chain repayment updates the wrong borrow balance

Source:
- https://crypto.training/hacks/58393-lend-cross-chain-repayment-updates-the-wrong-borrow-balance/

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
- id: `58393-lend-cross-chain-repayment-updates-the-wrong-borrow-balance`
- fingerprint: `22019105bc86a476f946afba99c445182ce1b873e31adfa2f999b2131a246f7b`

Core exploit idea:
- The repayment handler indexes the same-chain borrow slot even for a remote chain id, so the actual cross-chain balance remains unchanged.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
