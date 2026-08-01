# Crypto Training Exploit Pattern Stub: Index Coop ExchangeIssuance TOCTOU — Unlocked SetToken Units + Malicious Manager Hook Drain Residual Inventory

Source:
- https://crypto.training/hacks/2026-07-IndexCoopExchangeIssuanceTOCTOU/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2026

Chain:
- Ethereum

Loss / impact summary:
- ~$9.6K USD (SlowMist TI). PoC drains residual EI inventory including ~436.70 LINK and ~4…

Tags:
- logic/incorrect-state-transition, logic/missing-validation, dependency/unsafe-external-call, reentrancy/cross-contract

Dedupe:
- id: `2026-07-IndexCoopExchangeIssuanceTOCTOU`
- fingerprint: `c6a6473b7cf29fa9075dcd3b0abc3d21eb2182374efa0eda2db47f4b02621ef0`

Core exploit idea:
- 1. Index Coop ExchangeIssuance lets anyone call issueSetForExactToken for any controller-registered SetToken. It reads that SetToken's component real units to size swaps…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
