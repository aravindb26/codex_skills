# Crypto Training Exploit Pattern Stub: Uniswap The Compact — incorrect emissary storage slot breaks authorization

Source:
- https://crypto.training/hacks/61280-incorrect-storage-slot-derivation-breaks-authorization-spear/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/auth-bypass, loss-of-funds/direct-drain, storage/slot-collision

Dedupe:
- id: `61280-incorrect-storage-slot-derivation-breaks-authorization-spear`
- fingerprint: `e5d8b74bd544c4eb0eef0e5dfbdd5eec3c8eb20dd70fa1d9ece01945aa3e9881`

Core exploit idea:
- 1. Emissary config slots must be keyed by (scope, sponsor, lockTag). 2. Buggy packing writes lockTag over the memory region holding sponsor. 3. All sponsors share one co…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
