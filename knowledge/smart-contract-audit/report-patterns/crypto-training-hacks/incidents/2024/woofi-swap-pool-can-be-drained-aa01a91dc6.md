# Crypto Training Exploit Pattern Stub: WOOFi Swap — pool can be drained

Source:
- https://crypto.training/hacks/31886-h-1-pool-can-be-drained-sherlock-woofi-swap-git/

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
- oracle/missing-circuit-breaker, loss-of-funds/direct-drain, logic/per-call-only-guard

Dedupe:
- id: `31886-h-1-pool-can-be-drained-sherlock-woofi-swap-git`
- fingerprint: `aa01a91dc67e94b866e43d157f65b2fc7acb19668c5536f3c6a0bff538f3b623`

Core exploit idea:
- 1. WooPPV2 prices swaps via a PMM curve. Selling baseAmount of a base token computes a gamma (price-impact fraction) from the CURRENT oracle price, checks gamma <= maxGa…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
