# Solodit Pattern: Independently rebased aggregates drift and block operations

Source:
- https://solodit.cyfrin.io/issues/bucket-and-tick-aggregates-drift-apart-and-cause-dos-mixbytes-none-barterlab-markdown

Imported:
- 2026-11-07

Severity:
- MEDIUM

Protocol / source:
- BarterLab / MixBytes

Tags:
- aggregate accounting, rounding remainder, underflow, denial of service

Dedupe:
- id: `75091`
- fingerprint: `9e799ff6ed56654a3d7246446ca8a557027117035840c702e28251d75c997840`

Core mechanism:
- Two representations of the same total (bucket-level and tick-level aggregates) are rebased independently with truncating division and do not preserve remainders. Repeated updates make them diverge; later unchecked subtraction or equality assumptions can panic/revert operations such as preview, cancel, borrow, reloan, or refinance.

Invariant and audit checks:
- Redundant aggregates must remain mutually consistent after every partial update and rounding boundary.
- Find every writer of each aggregate; model repeated partial fills, rebases, withdrawals, and empty/dust buckets. Check whether remainders are carried, reconciled, or silently discarded and whether underflow is reachable in production arithmetic.

False-positive checks:
- Verify the update sequence is reachable and the mismatch survives transaction atomicity. Identify the exact user operation blocked and whether a permissionless repair or alternate route exists.

PoC shape:
1. Apply a sequence of partial updates that truncates each aggregate differently.
2. Assert the invariant between the aggregate representations fails.
3. Call affected user operations and show persistent reverts or inaccessible value.

Triage notes:
- A transient mismatch that self-corrects before any consumer reads it is not a reportable DoS.
