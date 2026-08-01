# Crypto Training Exploit Pattern Stub: Parallel 3.1 — processSurplus always reverts for managed collateral

Source:
- https://crypto.training/hacks/65528-surplusprocesssurplus-always-reverts-for-managed-collateral/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2026

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `65528-surplusprocesssurplus-always-reverts-for-managed-collateral`
- fingerprint: `45aabd273d701128fbf204629ed809827c72fd023d035a002688021aaf1914df`

Core exploit idea:
- 1. Managed collateral lives on an external manager/strategy, never on the diamond. 2. getCollateralSurplus correctly uses manager.totalAssets(). 3. processSurplus self-s…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
