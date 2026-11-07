# Crypto Training Exploit Pattern Stub: GoldPesa GPXHooks — TAKE_PAIR settles the shared unlock, so another position's debt cancels the burn credit

Source:
- https://crypto.training/hacks/2026-10-goldpesa/

Imported:
- 2026-11-07

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2026

Chain:
- Base

Loss / impact summary:
- unknown

Tags:
- logic/missing-check, logic/state-update, defi/flash-loan-attack

Dedupe:
- id: `2026-10-goldpesa`
- fingerprint: `84504d84a6dee031f4b89aa34795b923fe332257fa1b7e74cffed053e226376e`

Core exploit idea:
- GPXHooks owns the GPX/USDC Uniswap V4 liquidity. Any swap whose beforeSwap sees block.timestamp - lastRebalance >= 1 hours calls reBalanceRoutine() → checkRebalance → re…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
