# Crypto Training Exploit Pattern Stub: Ribbon Finance MarginPool — corrupted oToken expiry prices via pricer proxy takeover

Source:
- https://crypto.training/hacks/2025-12-RibbonMarginPool/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2025

Chain:
- Other

Loss / impact summary:
- ~$2.7M

Tags:
- oracle/price-manipulation, access-control/broken-logic, logic/incorrect-calculation, dependency/upgradeable-contract

Dedupe:
- id: `2025-12-RibbonMarginPool`
- fingerprint: `0d319d97acb90929168251b206545a9a183781225b7d93280000f0d60cce2623`

Core exploit idea:
- Legacy Ribbon/Opyn-style MarginPool held collateral for cash-secured call oTokens that expired OTM. The attacker temporarily took ownership of multiple asset pricer prox…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
