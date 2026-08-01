# Crypto Training Exploit Pattern Stub: ATOHook Solady ReentrancyGuard Storage Collision — Inflated `getReward()` Drain

Source:
- https://crypto.training/hacks/2026-06-ATOHook/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2026

Chain:
- Ethereum

Loss / impact summary:
- 14.411518807585587 ETH (exactly 200 × 0xffffffffffffff wei)

Tags:
- access-control/proxy-storage-collision, logic/incorrect-state-transition, logic/reward-calculation, logic/missing-check

Dedupe:
- id: `2026-06-ATOHook`
- fingerprint: `bcbebaa2368bbfab61f191f60c1817adbd7531f6d67256446737181c4794da69`

Core exploit idea:
- 1. ATOHook is a Uniswap v4 hook with a Synthetix-style native ETH reward stream. Accrued balances live in mapping(address => uint256) public rewards at base slot 17.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
