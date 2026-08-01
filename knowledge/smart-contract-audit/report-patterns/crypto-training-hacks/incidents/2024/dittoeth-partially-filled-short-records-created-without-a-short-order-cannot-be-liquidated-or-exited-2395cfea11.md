# Crypto Training Exploit Pattern Stub: DittoETH — partially filled Short Records created without a short order cannot be liquidated or exited

Source:
- https://crypto.training/hacks/34174-h-04-partially-filled-short-records-created-without-a-short/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dos/permanent-lock, logic/state-order-mismatch, access-control/missing-linkage

Dedupe:
- id: `34174-h-04-partially-filled-short-records-created-without-a-short`
- fingerprint: `2395cfea118fe7c51834e47f951f8e968631f1a6a5b7fe10e6c4a0c100c55957`

Core exploit idea:
- 1. When a short only partially matches the order book, sellMatchAlgo marks the Short Record's status PartiallyFilled — implying "the rest of this short is still resting…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
