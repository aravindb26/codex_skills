# Crypto Training Exploit Pattern Stub: Unverified670471 — Balancer flash-loan callback forwarded to a victim that repays the loan with its own funds

Source:
- https://crypto.training/hacks/2025-07-Unverified670471/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Ethereum

Loss / impact summary:
- ~$1,818.33 (484.9 mETH net profit ≈ 0.4849 ETH at fork-block prices)

Tags:
- access-control/missing-auth, logic/incorrect-state-transition, dependency/unsafe-external-call

Dedupe:
- id: `2025-07-Unverified670471`
- fingerprint: `1e2e3d66c59462fb135bae7fd6a879caedb4f1a025dacdf7569ddb3d9678d1cc`

Core exploit idea:
- The victim contract 0x6704713B... is configured to act as a Balancer IBalancerFlashLoanRecipient. Balancer's flash-loan primitive works by sending the borrowed tokens to…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
