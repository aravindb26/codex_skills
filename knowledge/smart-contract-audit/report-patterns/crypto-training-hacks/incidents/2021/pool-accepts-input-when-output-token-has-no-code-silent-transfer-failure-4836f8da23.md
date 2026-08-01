# Crypto Training Exploit Pattern Stub: Pool accepts input when output token has no code — silent transfer failure

Source:
- https://crypto.training/hacks/18260-transfer-operations-may-silently-fail-due-to-the-lack-of-con/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2021

Chain:
- Ethereum

Loss / impact summary:
- A swapper loses input tokens without receiving output

Tags:
- dependency/unchecked-return-value, input-validation/missing

Dedupe:
- id: `18260-transfer-operations-may-silently-fail-due-to-the-lack-of-con`
- fingerprint: `4836f8da23e6078e101ac3738bec757cd82053a3d7fcf7157f6f463a23378531`

Core exploit idea:
- Solidity low-level calls to an account with no code return success. The pool therefore accepts 1,000 input tokens while its “output token” call to a non-deployed address…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
