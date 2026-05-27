# Pattern: Exact-out rounding error compounds in composable stable pools

Source:
- https://x.com/Balancer/status/1986104426667401241
- https://medium.com/balancer-protocol/nov-3-exploit-post-mortem-51dcbeb6b020
- https://www.certora.com/blog/breaking-down-the-balancer-hack
- https://blog.trailofbits.com/2025/11/07/balancer-hack-analysis-and-guidance-for-the-defi-ecosystem/

Source type:
- official X incident update / official post-mortem / third-party technical analyses

Status:
- verified historically

Protocol type:
- DEX / stableswap AMM / composable pool / Balancer-style Vault

Bug class:
- rounding direction / precision loss / invariant manipulation / batch swap / BPT share-value accounting

Core idea:
- In an exact-out stable-swap path, the protocol rounded the requested output amount down while upscaling it for token decimals/rates.
- That made the invariant calculation believe the user was taking slightly less output than requested, so the computed input amount was also too low.
- In normal liquidity, the loss was tiny. In composable stable pools with rate providers and low liquidity, repeated swaps amplified the rounding bias enough to lower the invariant and BPT value, allowing value extraction.

Broken invariant:
- Exact-out swaps must never let the user underpay for the requested output.
- Rounding direction must be proven per operation and per user flow, not only with the generic rule "round in favor of the protocol."
- Swap round trips must not increase user value.
- BPT/share value must not decrease from valid swaps, joins, exits, or composable batch operations.
- Low-liquidity states must not magnify one-wei or tiny rounding errors into extractable value.

Where to look in code:
- Exact-out swap paths such as `_swapGivenOut`, `swapGivenOut`, `batchSwap`, or equivalent.
- Upscaling/downscaling helpers for token decimals, rate providers, ERC4626 rates, LST exchange rates, or yield-bearing token rates.
- Mixed rounding paths where upscaling uses `mulDown` but later downscaling or invariant math assumes the opposite direction.
- Stable invariant calculations where small precision changes affect BPT price or pool invariant `D`.
- Composable pools where the pool token/BPT is itself a swappable asset.
- Vault batch/flash-swap settlement that allows temporary deficits as long as final credits and debits net out.
- Low-liquidity or drained-pool states reachable before the vulnerable math executes.

Attack path:
1. Identify a composable stable pool with rate providers and exact-out swap support.
2. Use BPT-as-token / exitSwap / batch-swap mechanics to push the pool into a low-liquidity state.
3. Execute a carefully calculated sequence of exact-out swaps.
4. Each swap pays slightly too little because output upscaling/downstream invariant math rounds the wrong way.
5. The repeated bias lowers the pool invariant and the implied BPT/share value.
6. Repay any temporary BPT flash-swap deficit cheaply.
7. Extract remaining value tokens, potentially through Vault internal balance withdrawal in a later transaction.

False-positive checks:
- Confirm the exact-out path rounds the output-side scaled amount in a direction that benefits the user.
- Confirm the resulting input amount is too low after stable invariant math and fee handling.
- Confirm rate providers or non-integer scaling factors introduce real imprecision.
- Confirm the attacker can reach a low-liquidity state in the same batch/transaction or through normal public actions.
- Confirm the pool token/share token is composable or otherwise usable to manipulate liquidity/invariant state.
- Confirm repeated operations compound the bias enough to overcome gas, fees, and liquidity constraints.
- Kill the branch if round-trip swaps are proven value-nonincreasing under the reachable pool configuration.
- Kill the branch if low-liquidity states are impossible or exact-out is disabled for affected assets.
- Kill the branch if the issue is only a theoretical one-wei discrepancy with no compounding path.

PoC shape:
- Fork a vulnerable stable/composable pool or build a local minimal pool with rate scaling and BPT-as-token behavior.
- Create or reach a low-liquidity state through public batch-swap/exit-swap mechanics.
- Execute a sequence of exact-out swaps that alternate assets or directions.
- Track pool invariant, BPT price/share value, attacker token balances, and any internal balance.
- Assert invariant/share value decreases or attacker value increases after the round trip.
- Include a control test showing the issue disappears when output upscaling rounds conservatively or when BPT composability/low-liquidity is removed.

Triage notes:
- Strong impact when the exploit drains live pool reserves or materially reduces BPT value.
- Do not frame it as "rounding bug" only. The submit-worthy issue is the full exploit chain: wrong exact-out rounding plus rate-provider imprecision plus low-liquidity amplification plus composable BPT/batch settlement.
- Mature/audited code does not reduce impact; but duplicate risk is high if the public Balancer exploit or its variants are already known.
- For new targets, uniqueness depends on proving the same bug class in a distinct implementation or an unpatched fork with real TVL.
- Internal balances may be the extraction mechanism but are not necessarily the root cause; avoid blaming accounting storage unless it actually contributes to the exploit.

Audit heuristics:
- For every exact-out swap, ask which side should be rounded up/down at each scaling, invariant, fee, and settlement step.
- Add a property: swap A to B and then B to A must not return more value than started with.
- Add a property: share/BPT value must be monotonic or value-neutral across swaps and batch operations.
- Fuzz low-liquidity states aggressively; do not assume tiny rounding errors stay tiny.
- Fuzz multi-step batch swaps, not just single swaps.
- Include rate-provider values that create awkward non-integer scaling factors.
- Treat composability of pool shares as a risk multiplier because it lets joins/exits look like swaps.
- Revisit old "low severity rounding" findings when the protocol later adds composability, batch settlement, rate providers, or new low-liquidity states.

Operational lessons:
- Pause windows and recovery mode matter. Long-lived immutable pools outside pause windows can turn a fixable bug into an unrecoverable loss.
- Monitoring and war-room response can reduce blast radius but do not replace prevention.
- Safe Harbor / whitehat recovery frameworks can materially improve incident outcomes.
- Security programs should refresh fuzz/property suites after major public incidents; old tests should evolve with new threat intelligence.

Related patterns:
- exact-out underpayment
- stable invariant manipulation
- low-liquidity rounding amplification
- BPT/share value monotonicity
- batch swap temporary deficit
- rate-provider precision loss
- composable LP token risk
