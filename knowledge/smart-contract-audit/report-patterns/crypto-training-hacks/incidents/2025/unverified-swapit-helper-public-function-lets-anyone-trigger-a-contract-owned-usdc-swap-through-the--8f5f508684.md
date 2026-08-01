# Crypto Training Exploit Pattern Stub: Unverified `swapit()` helper — public function lets anyone trigger a contract-owned USDC swap through the same AMM pool, harvesting the price impact

Source:
- https://crypto.training/hacks/2025-03-unverified_de7c/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2025

Chain:
- Base

Loss / impact summary:
- 980.32 USDC (~$980) drained from the vulnerable swapper's own balance

Tags:
- access-control/missing-owner-check, defi/sandwich-attack, defi/slippage

Dedupe:
- id: `2025-03-unverified_de7c`
- fingerprint: `8f5f508684fbdc4e43e3ffd27bf697764e45a0381ee04c2faa8296adb596b646`

Core exploit idea:
- The victim is a small, unverified "swap helper" contract holding a USDC balance and bound to the OFFICIALYE token (a low-cap Base memecoin, 0xedb54f9ffA78f0A0d50dC0c1534…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
