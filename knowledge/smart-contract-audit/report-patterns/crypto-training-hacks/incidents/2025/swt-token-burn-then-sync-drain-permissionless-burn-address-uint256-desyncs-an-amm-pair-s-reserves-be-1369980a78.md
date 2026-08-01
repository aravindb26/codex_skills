# Crypto Training Exploit Pattern Stub: SWT token burn-then-sync drain — permissionless `burn(address,uint256)` desyncs an AMM pair's reserves before `sync()`

Source:
- https://crypto.training/hacks/2025-03-unverified_3f27/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2025

Chain:
- Avalanche

Loss / impact summary:
- ~0.40 WAVAX (the pair held ~0.8957 WAVAX; attacker netted ~0.3957 WAVAX after a 0.5 AVAX…

Tags:
- access-control/missing-auth, logic/state-update, defi/price-manipulation

Dedupe:
- id: `2025-03-unverified_3f27`
- fingerprint: `1369980a7825baabd97846d80252a7a5b748197b5751fd2690973fd388d317b6`

Core exploit idea:
- SWT is an unverified ERC-20 on Avalanche paired against WAVAX in a standard Uniswap-V2-style AMM (0x8234…c5CF). The token ships a burn(address from, uint256 amount) func…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
