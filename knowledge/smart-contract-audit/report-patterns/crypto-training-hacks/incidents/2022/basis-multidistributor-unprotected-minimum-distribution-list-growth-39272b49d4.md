# Crypto Training Exploit Pattern Stub: Basis MultiDistributor — unprotected minimum-distribution list growth

Source:
- https://crypto.training/hacks/16760-setminimumdistribution-not-protected/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-auth, dos/unbounded-loop

Dedupe:
- id: `16760-setminimumdistribution-not-protected`
- fingerprint: `39272b49d4b16b3853304bf6033e3622055b037c74dd487a8a7889702b92f7e1`

Core exploit idea:
- setMinimumDistribution is documented for trusted participants, but anyone can append token addresses. Repeated zero-minimum entries inflate every distribution loop and c…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
