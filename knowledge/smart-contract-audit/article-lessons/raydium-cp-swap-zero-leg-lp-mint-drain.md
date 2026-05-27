# Pattern: Zero-leg LP mint lets deposits buy pool shares without both assets

Source:
- https://immunefi.com/blog/all/raydium-liquidity-drain-bug-fix-review/
- https://github.com/raydium-io/raydium-cp-swap
- https://docs.rs/raydium-cp-swap/latest/src/raydium_cp_swap/curve/constant_product.rs.html
- https://deepwiki.com/raydium-io/raydium-cp-swap/3.2-depositing-liquidity

Source type:
- article / bug fix review / accepted bounty

Status:
- verified historically and patched

Protocol type:
- DEX / constant-product AMM / Solana program

Bug class:
- rounding / zero-amount edge case / LP share accounting / liquidity drain

Core idea:
- A deposit path calculated required token amounts for a requested LP mint using integer proportional math and ceiling rounding.
- For tiny LP amounts, one side of the proportional deposit could round to zero while the other rounded up, allowing LP tokens to be minted after contributing only one pool asset.
- Repeating the asymmetric deposit and then withdrawing proportionally let the attacker extract the missing asset side from the pool.

Broken invariant:
- Minting LP shares in a two-token AMM must require economically proportional contribution of both pool assets, unless single-sided deposit is explicitly supported and priced.
- A deposit followed by an immediate withdraw must not increase the user's total value, ignoring normal fees.
- The pool value / constant-product safety check must hold across deposit and withdraw cycles, not only individual arithmetic helpers.
- Slippage max checks are not enough; computed required amounts must also satisfy minimum/nonzero constraints.

Where to look in code:
- LP mint/deposit functions that take desired LP amount and compute required token amounts.
- Helpers equivalent to `lp_tokens_to_trading_tokens`.
- Rounding branches that intentionally avoid rounding a zero quotient up to one.
- Deposit functions that validate `lp_token_amount > 0` but not each computed token amount.
- Slippage checks that only enforce upper bounds like `required <= max`, allowing `required == 0`.
- Withdraw functions that burn LP and pay both assets proportionally.

Attack path:
1. Choose a small `lp_token_amount` such that `lp_amount * reserve0 / lp_supply` is nonzero but `lp_amount * reserve1 / lp_supply` truncates to zero.
2. Call deposit with maximums allowing the nonzero side and zero for the other side.
3. The rounding helper returns a nonzero amount for token0 and zero for token1.
4. If the deposit path does not reject zero required token amounts, it transfers only token0 and mints LP.
5. Repeat until enough LP shares are accumulated cheaply.
6. Withdraw the LP shares normally and receive proportional amounts of both token0 and token1.
7. Profit comes from the token1 received on withdrawal despite contributing none during the deposits.

False-positive checks:
- Confirm the protocol does not intentionally support single-sided deposits.
- Confirm the computed zero side still allows LP minting, not just a quote preview.
- Confirm there is no later nonzero validation after transfer-fee adjustment.
- Confirm the withdrawal path redeems both assets proportionally for the minted LP.
- Confirm the attack is profitable after decimals, transfer fees, protocol fees, rent/account costs, and minimum liquidity.
- Kill the branch if computed zero-amount deposits are rejected before minting LP.
- Kill the branch if LP mint amount is also forced to zero or if single-sided deposits are priced through a swap-style curve.

PoC shape:
- Set pool reserves and LP supply so one side truncates to zero for a tiny LP mint.
- Call the deposit instruction repeatedly with `maximum_token_X_amount = 0` for the zero side.
- Assert LP balance increases while one vault receives no corresponding token.
- Burn/withdraw the LP.
- Assert attacker ends with more total value than they deposited.

Triage notes:
- Strong when the cycle is permissionless and drains real pool reserves.
- This is not merely a "rounding dust" issue if repetition converts dust-level asymmetry into pool-value extraction.
- The report must show a closed profitable loop: asymmetric LP mint plus normal proportional withdrawal.
- Distinguish this from expected single-sided liquidity features; the root cause is missing validation on a two-sided deposit path.

Audit heuristics:
- For every LP mint formula, test tiny amounts around reserve/supply ratios where one side computes zero.
- Include explicit invariants for deposit-then-withdraw value monotonicity.
- Fuzz both `lp_amount` and reserve ratios with assumptions that do not filter out zero-side cases.
- Review comments like "rejected later in processing" and verify the later rejection actually exists.
- Treat upper-bound slippage checks as incomplete unless minimum received/provided constraints are also enforced.

Related patterns:
- asymmetric deposit accounting
- integer truncation to zero
- minimum amount validation
- deposit/withdraw round-trip profit
- LP share inflation
