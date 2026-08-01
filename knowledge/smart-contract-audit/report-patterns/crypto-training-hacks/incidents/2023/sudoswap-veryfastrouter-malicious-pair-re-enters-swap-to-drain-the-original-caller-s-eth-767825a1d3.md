# Crypto Training Exploit Pattern Stub: Sudoswap `VeryFastRouter` — malicious pair re-enters `swap` to drain the original caller's ETH

Source:
- https://crypto.training/hacks/18412-malicious-pair-can-re-enter-veryfastrouter-to-drain-original/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- reentrancy/single-function, access-control/missing-input-validation

Dedupe:
- id: `18412-malicious-pair-can-re-enter-veryfastrouter-to-drain-original`
- fingerprint: `767825a1d3102257c3790463910a08d401da89ee540310c214723fd179757dc8`

Core exploit idea:
- 1. VeryFastRouter.swap is the batch sell/buy entry point. It is not nonReentrant and never checks that a supplied order.pair is a real factory pair. 2. A user is tricked…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
