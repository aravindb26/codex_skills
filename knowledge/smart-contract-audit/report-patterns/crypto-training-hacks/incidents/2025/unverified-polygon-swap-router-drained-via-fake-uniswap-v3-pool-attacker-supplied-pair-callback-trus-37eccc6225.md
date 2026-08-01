# Crypto Training Exploit Pattern Stub: Unverified Polygon swap router drained via fake Uniswap V3 pool — attacker-supplied pair/callback trusted without authentication

Source:
- https://crypto.training/hacks/2025-08-unverified_d132/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Polygon

Loss / impact summary:
- 3,131.106630910288079590 DAI (entire victim DAI balance)

Tags:
- access-control/missing-auth, logic/missing-validation, defi/slippage, oracle/spot-price

Dedupe:
- id: `2025-08-unverified_d132`
- fingerprint: `37eccc62254a586ad56bd94f1fac8ae162a70552999df0b1b3abdc24d2999647`

Core exploit idea:
- 0xd132…3B0bafF is an unverified Polygon contract exposing a swapSingleToken(address pair, address from, address token, bool zeroForOne, uint256 amount) selector that mim…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
