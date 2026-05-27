# Protocol Patterns

Use this file to collect recurring architecture patterns and their risk zones.

## Batch Systems

Risk zones:

- global moving pointers
- finalized-but-unsettled states
- rolling hashes
- skipped settlement windows
- public unwind/cancel paths
- request counters that only track the current batch

## Vaults

Risk zones:

- same-batch deposits and withdrawals
- share price snapshots
- fee-on-transfer or rebasing assets
- executor-held balances
- cross-chain supply views
- withdrawal share custody

## Strategy Vaults / Asset Managers

Risk zones:

- manager-controlled calls through external integrations
- contract guards that infer effects by decoding calldata
- pre/post balance snapshots for slippage or value checks
- unsupported asset handling in valuation logic
- malicious ERC20 `balanceOf` or transfer behavior during guard checks
- aggregator routes where bit flags override declared token fields

## Oracle-Driven Auctions

Risk zones:

- source priority between fast and fallback feeds
- stale feed acceptance
- quote-time vs execution-time prices
- signed order validation
- partial-fill assumptions

## Concentrated Liquidity AMMs

Risk zones:

- exact tick-boundary price states
- continuous price vs discrete tick/index desynchronization
- no-op swap steps that still update tick state
- mint/burn behavior when a position starts or ends at the current tick
- tick crossing that applies liquidity deltas more or less than once
- attacker-controlled price limits such as `limitSqrtP`

## Constant-Product AMMs

Risk zones:

- LP mint formulas that divide before enforcing minimum token amounts
- tiny LP deposits where one side rounds to zero
- asymmetric deposits in code paths intended to be two-sided
- upper-bound slippage checks without lower-bound/nonzero validation
- deposit/withdraw round-trip profit from rounding
- transfer-fee adjustment that can turn a small amount into zero received

## Stable / Composable AMMs

Risk zones:

- exact-out swaps with output-side rounding before invariant math
- token decimal scaling and rate-provider scaling with inconsistent rounding direction
- low-liquidity states that amplify tiny precision loss
- pool share tokens/BPT included as swappable pool assets
- batch swaps or flash-swap settlement that allow temporary deficits
- invariant or share-price changes across long alternating swap sequences
- old pool implementations whose pause window or recovery controls have expired
- zero-amount liquidity operations that still recalculate or mutate virtual balances
- custom Newton/invariant solvers without explicit domain checks
- rebasing or rate-provider assets that change balances/rates outside normal liquidity flow

## Legacy Live Products

Risk zones:

- deprecated products that still hold TVL
- isolated codebases not covered by current audits or active monitoring
- novel math no longer maintained by the current team
- old compiler semantics or unchecked arithmetic assumptions
- emergency controls, pause windows, or recovery processes that no longer operate
- products omitted from current docs/UI but still reachable onchain
