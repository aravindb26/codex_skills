# Crypto Training Exploit Pattern Stub: BonfireSwap `transfer` spends any holder's standing allowance — missing caller check on the router's force-sell

Source:
- https://crypto.training/hacks/2026-09-bonfireswap/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- BNB Chain

Loss / impact summary:
- Full incident ~66.08 WBNB (~$47–50K) across ~41 holders. This PoC, the five largest victi…

Tags:
- access-control/missing-auth, logic/missing-check, input-validation/missing

Dedupe:
- id: `2026-09-bonfireswap`
- fingerprint: `697e55c0066780599a620b637183143ff601c20da3ab717ef27b5b3ccbb99e64`

Core exploit idea:
- BonfireSwap is a custom BSC router for the reflective BONFIRE token (0x5e90253f…5590, 10% tax / 5% reflection, pair 0xD3F478F0…38f2 with WBNB). Holders who had used the…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
