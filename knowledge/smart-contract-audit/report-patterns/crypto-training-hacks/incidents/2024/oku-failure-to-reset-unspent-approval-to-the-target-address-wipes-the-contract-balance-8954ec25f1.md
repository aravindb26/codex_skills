# Crypto Training Exploit Pattern Stub: Oku — Failure to reset unspent approval to the target address wipes the contract balance

Source:
- https://crypto.training/hacks/44376-h-6-failure-to-reset-unspent-approval-to-the-target-address/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- approval/residual, logic/direct-drain, access/untrusted-target

Dedupe:
- id: `44376-h-6-failure-to-reset-unspent-approval-to-the-target-address`
- fingerprint: `8954ec25f11f31a9af7ae9eb0e890b20170847701513549be07a76b550c45717`

Core exploit idea:
- 1. execute approves an arbitrary target for the full order.amountIn. 2. The target call need only move 1 wei of tokenIn / tokenOut to pass the minAmountOut / over-spend…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
