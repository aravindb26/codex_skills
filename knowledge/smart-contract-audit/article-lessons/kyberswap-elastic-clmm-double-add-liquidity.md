# Pattern: CLMM tick-boundary state desync double-adds liquidity

Source:
- https://100proof.org/kyberswap-post-mortem.html
- https://github.com/KyberNetwork/ks-elastic-sc-legacy/blob/362d9b6a726bcb286cc47c082c46f6259a5ae82d/contracts/Pool.sol
- https://github.com/KyberNetwork/ks-elastic-sc/blob/c39eb431a520b83b731c1d03c9ad5b534ec42728/contracts/Pool.sol
- https://github.com/x100proof/kyberswap-exploit

Source type:
- article / post-mortem / public PoC

Status:
- verified historically by Kyber team and patched

Protocol type:
- DEX / CLMM / concentrated liquidity AMM

Bug class:
- accounting desync / liquidity lifecycle / tick-boundary edge case / state-machine bug

Core idea:
- A CLMM can keep continuous price state (`sqrtP`) and discrete tick/index state (`currentTick`, nearest initialized tick) slightly out of phase at exact tick boundaries.
- If active liquidity is added while price sits on a boundary, then the next swap can cross that same boundary and apply the newly-added tick liquidity again, inflating `baseL` and enabling a low-price-impact drain.

Broken invariant:
- Active liquidity must equal the sum of all initialized liquidity ranges containing the current price.
- Crossing a tick boundary must apply each position's liquidity delta exactly once.
- Tick/index state must always point to the correct side of an exact-boundary price before computing the next initialized tick.

Where to look in code:
- CLMM swap loops that split swaps into sub-swaps across tick boundaries.
- Branches where `sqrtP == nextSqrtP`, `sqrtP == startSqrtP`, or a swap step consumes amount without moving price.
- Tick-state updates after partial swap steps, especially `currentTick`, `nearestCurrentTick`, `nextTick`, and initialized tick lookup.
- Mint/add-liquidity paths that immediately update active pool liquidity when the current price is inside the minted range.
- Router fields such as `limitSqrtP` that let an attacker force price exactly onto a tick boundary.

Attack path:
1. Use swaps and/or a price limit parameter to place the pool price exactly on a valid tick-range boundary.
2. Drive discrete tick state into an inconsistent side-of-boundary state, for example `nearestCurrentTick == currentTick - 1`.
3. Mint a narrow liquidity range starting at the boundary. Because the current price is treated as inside the range, the mint adds liquidity to active `baseL`.
4. Perform a minimal opposite-direction swap that crosses the same boundary.
5. The tick-crossing logic applies the minted liquidity delta again, so active liquidity becomes larger than real liquidity.
6. Use the inflated liquidity to swap with artificially low price impact and drain one side of the pool, potentially with flash-loan funding.

False-positive checks:
- Confirm the attacker can force or naturally reach exact tick-boundary price state.
- Confirm discrete tick/index state can become inconsistent with the intended side of the boundary.
- Confirm minting at the boundary updates active liquidity before the crossing.
- Confirm the next swap computes `nextTick` from stale or wrong tick-side state.
- Confirm the same liquidity delta is applied once on mint and again on crossing.
- Kill the branch if exact-boundary states are normalized before every initialized-tick lookup.
- Kill the branch if minting at a boundary does not update active liquidity until after a safe crossing rule.
- Kill the branch if the exploit only creates accounting inconsistency without extractable value or fund lock.

PoC shape:
- Fork or local CLMM pool with real swap/mint code.
- Add liquidity across several ranges so tick crossings are meaningful.
- Use binary search or exact math to reach `sqrtP == getSqrtRatioAtTick(t)`.
- Assert precondition: `sqrtP` on boundary and discrete tick/index state points to the wrong side.
- Mint range `(t, t + n)` and record `baseL`.
- Execute a tiny swap crossing `t`.
- Assert active liquidity increased by the minted delta twice.
- Complete exploit swap and compare pool token balances / attacker profit.

Triage notes:
- Strong impact when inflated liquidity enables draining live pool reserves.
- This is not a generic "rounding" issue; the report must prove a concrete state-machine transition where liquidity is applied twice.
- CLMM findings are duplicate-prone if they only say "boundary bug"; distinguish the exact broken transition: price-on-boundary plus tick-side desync plus double application of range liquidity.
- The article's lesson is depth over breadth: deeply understand one complex primitive, then use that mental model across forks and variants.

Audit heuristics:
- In CLMMs, test every branch where continuous price and discrete tick disagree by exactly one tick.
- Treat exact-boundary price as a separate state, not merely another normal price.
- Look for no-op swap steps that still update tick/index state.
- Check whether a position whose lower or upper tick equals current price is considered in range consistently across mint, burn, collect, swap, and tick-crossing.
- Build stateful tests around "apply liquidity delta exactly once" rather than only checking swap output amounts.

Related patterns:
- liquidity accounting desync
- tick-boundary off-by-one
- state handoff after partial swaps
- flash-loan amplified DEX drain
