# Invariant Library

Reusable invariants by protocol family.

## Vaults

- New deposit value must not be redeemable by old shares before new shares are minted.
- Finalized or queued requests must remain reachable until settled, canceled, or unwound.
- Share supply and asset accounting must move together under deposits, withdrawals, settlement, and unwind.
- Zero-amount deposit/withdraw/liquidity operations must revert or be true no-ops.
- Minted shares/LP value must be bounded by real deposited value and explicit rounding tolerance.

## Lending

- A healthy position must not be liquidatable.
- An unhealthy position must not escape liquidation by manipulating accounting order, stale indexes, or oracle timing.
- Repayments must reduce exactly the correct debt bucket and interest index state.

## DEX / Auctions

- Slippage and floor-price invariants must hold at execution time, not only quote time.
- Aggregator guards must account for the actual token deltas caused by execution, not only decoded calldata metadata.
- Declared source/destination tokens in calldata must match the assets actually pulled from and sent to the vault.
- Partial fills must not let tiny actions suppress competitive execution unless that is explicitly intended.
- LP minting in two-token AMMs must require nonzero/proportional contribution of both assets unless single-sided deposits are explicitly supported and priced.
- Deposit-then-withdraw round trips must not create profit from rounding, zero amounts, or share-supply edge cases.
- Exact-out swaps must not undercharge input after token scaling, rate-provider conversion, invariant math, or fees.
- Swap round trips must not increase user value, especially under low liquidity and awkward scaling factors.
- Pool-share/BPT value must not decrease through swaps, batch swaps, joins, exits, or composable share-token operations.
- Virtual balances, real balances, rates, invariant inputs, and LP supply must remain mutually consistent after rate updates, rebases, joins, exits, and no-op calls.
- Stable-swap/Newton solvers must reject invalid-domain inputs and must not wrap negative intermediate values into large unsigned outputs.
- In CLMMs, active liquidity must equal exactly the sum of initialized ranges containing the current price.
- In CLMMs, crossing a tick boundary must apply each liquidity delta exactly once, even when price sits exactly on a tick.
- Continuous price state and discrete tick/index state must be normalized before computing the next initialized tick.

## Cross-Chain

- Total supply across chains must match minted/burned/locked accounting under message delay, retry, and replay conditions.
- Messages must be domain-separated by chain, sender, nonce, and intent.

## Strategy Vaults / Asset Managers

- Trust-minimized managers must not be able to bypass integration guards and extract depositor assets.
- Unsupported or unpriced assets must not disable value checks for actions that spend supported vault assets.
