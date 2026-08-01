# Crypto Training Exploit Pattern Stub: BSC "DD" initcode-token drain — unverified victim exposes arbitrary token-path swap using its own WBNB

Source:
- https://crypto.training/hacks/2025-08-BscInitcodeToken/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- BNB Chain

Loss / impact summary:
- ~0.913 WBNB in the PoC (victim drained from 912.716e15 WBNB to 2,486,728 wei WBNB). On-ch…

Tags:
- logic/missing-validation, dependency/unchecked-return-value, access-control/missing-auth

Dedupe:
- id: `2025-08-BscInitcodeToken`
- fingerprint: `4fffda658fbd639aafcfa2844663c029c557c2a7ad88052597ee789dffe8a558`

Core exploit idea:
- The victim contract 0x0B0d…c4Da exposes a public function (selector 0xdc0b3665) that takes a token pair and an amountIn and performs two PancakeSwap swapExactTokensForTo…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
