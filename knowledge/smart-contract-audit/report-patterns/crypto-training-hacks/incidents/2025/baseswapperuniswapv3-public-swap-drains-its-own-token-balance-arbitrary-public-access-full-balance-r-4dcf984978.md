# Crypto Training Exploit Pattern Stub: BaseSwapperUniswapV3 public swap drains its own token balance — arbitrary public access + full-balance refund to caller-chosen recipient

Source:
- https://crypto.training/hacks/2025-08-ArbitrumBaseSwapper/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Arbitrum

Loss / impact summary:
- ~1,847.33 USD (472,997,613,026,749,247,557,538 wei of a deflationary victim token, draine…

Tags:
- access-control/missing-auth, access-control/missing-modifier, logic/state-update, defi/slippage

Dedupe:
- id: `2025-08-ArbitrumBaseSwapper`
- fingerprint: `4dcf98497838bc8bf65a2bc9f02d392c536f2a97771fb3b12748f3906235886b`

Core exploit idea:
- BaseSwapperUniswapV3 is an admin-owned wrapper around the Uniswap V3 ISwapRouter. Its admin registers token paths via setPath() and pre-approves the router for type(uint…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
