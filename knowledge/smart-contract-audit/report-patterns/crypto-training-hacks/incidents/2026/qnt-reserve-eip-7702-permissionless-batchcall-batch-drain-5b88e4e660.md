# Crypto Training Exploit Pattern Stub: QNT Reserve EIP-7702 + Permissionless `BatchCall.batch()` Drain

Source:
- https://crypto.training/hacks/2026-04-QNT_EIP7702_BatchCall/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2026

Chain:
- Ethereum

Loss / impact summary:
- 1,988.546547972979064297 QNT (exact wei: 1988546547972979064297) → swapped to ~54.93 ETH

Tags:
- access-control/missing-auth, access-control/broken-logic, dependency/unsafe-external-call

Dedupe:
- id: `2026-04-QNT_EIP7702_BatchCall`
- fingerprint: `5b88e4e66080858684cd9f81bb73325625f1998e27e2322e4bc318ff0dc68566`

Core exploit idea:
- 1. A QNT reserve is controlled under the authority of admin EOA 0xc6ddf907…. 2. That EOA is EIP-7702-delegated to BatchExecutor 0x95538e1c… (designator code 0xef0100 ||…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
