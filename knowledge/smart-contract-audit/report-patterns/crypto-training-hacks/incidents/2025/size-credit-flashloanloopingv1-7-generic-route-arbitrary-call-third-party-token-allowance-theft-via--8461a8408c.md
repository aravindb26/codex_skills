# Crypto Training Exploit Pattern Stub: Size Credit FlashLoanLoopingV1_7 Generic-Route Arbitrary Call — third-party token allowance theft via caller-controlled `router.call(data)`

Source:
- https://crypto.training/hacks/2025-08-SizeFlashLoanLooping/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Ethereum

Loss / impact summary:
- ~533 USD (540.576557 PT-wstUSR-25SEP2025 tokens stolen from one victim) [output.txt:1564-…

Tags:
- dependency/unsafe-external-call, logic/missing-validation, access-control/missing-auth

Dedupe:
- id: `2025-08-SizeFlashLoanLooping`
- fingerprint: `8461a8408cd323b29d94a7a9d86d2bf19c49c429b5a5088ad2ba87e97163bb5a`

Core exploit idea:
- Size Credit's FlashLoanLoopingV1_7 is an Ownable zap contract that lets a user flash-loan from Aave, swap the borrowed token into collateral, deposit, and borrow in one…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
