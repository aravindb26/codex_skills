# Crypto Training Exploit Pattern Stub: Treasury Vesting — `batchRelease` updates state before transfer, users get nothing

Source:
- https://crypto.training/hacks/52680-no-token-distribution-in-batchrelease-due-to-premature-state/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/checks-effects-misapplied, vesting/skipped-transfer

Dedupe:
- id: `52680-no-token-distribution-in-batchrelease-due-to-premature-state`
- fingerprint: `f7670a93f7bca869e9dd7a5704027dfc404c952f9be0fefe27efecb92ec8a800`

Core exploit idea:
- 1. Loop 1: for each user, compute releasable, add to userReleased / totalReleased. 2. Loop 2: recompute releasable — now 0 because loop 1 already credited releases — ski…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
