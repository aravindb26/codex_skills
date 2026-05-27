# Pattern: Aggregator guard trusts declared source token that execution ignores

Source:
- https://x.com/s4muraii77/status/2012140371938070888
- https://api.fxtwitter.com/2/status/2012140371938070888

Source type:
- X article / confirmed bounty write-up

Status:
- verified historically by author; reportedly confirmed high severity and patched

Protocol type:
- asset management / strategy vault / DEX aggregator integration / trust-minimized manager

Bug class:
- integration semantic mismatch / slippage bypass / malicious token accounting / external calldata decoding

Core idea:
- dHEDGE used contract guards to let a manager trade through integrations while enforcing post-trade slippage checks.
- In the 1inch `unoswap` integration, the guard decoded the user-provided `token` parameter and pool address to infer the source and destination assets.
- For 1inch UniswapV3 execution, the declared `token` parameter did not determine the actual sold token. The real direction came from a bit inside the encoded `dex` pool value.
- This created a validation/execution desync: the guard measured slippage for one asset pair while 1inch actually swapped a different asset.

Broken invariant:
- The asset used for pre/post balance accounting must be the exact asset spent by the external integration.
- The asset received by the vault must be the exact asset expected by the guard.
- Slippage checks must compare actual value spent and actual value received, not values inferred from calldata fields that the target protocol may ignore.
- An unsupported or malicious token must never be usable as the accounting source for a trade that spends a supported vault asset.

Where to look in code:
- Contract guards/wrappers around 1inch, 0x, Paraswap, Uniswap routers, or other aggregators.
- Code that decodes external calldata to infer `srcToken`, `dstToken`, route pools, or slippage metadata.
- 1inch `unoswap`, `unoswap2`, and `unoswap3` handling.
- Encoded route/pool values where bit flags determine direction, recipient, payer, unwrap behavior, or protocol selection.
- Post-call checks that compare token balances before and after the external call.
- Logic that skips slippage/value checks when a token is unsupported or missing a price feed.
- Any use of arbitrary ERC20 `balanceOf` during security checks, especially when the token can be attacker-created.

Attack path:
1. Manager creates or uses a malicious/fake token whose `balanceOf` returns decreasing values to the guard, making the guard believe the vault spent that token.
2. Manager creates a UniswapV3 pool between a real vault asset to steal and the fake token.
3. Manager prices the fake pool so swapping all of the real vault asset returns only dust fake tokens.
4. Manager crafts 1inch `unoswap2` calldata that declares the fake token as the source asset for guard accounting.
5. The first actual UniswapV3 hop sells the real vault asset into the fake pool because swap direction is controlled by encoded pool bits, not the declared source token.
6. A second hop sends only a dust amount through a legitimate pool, causing the vault to receive a tiny amount of a real destination token.
7. The dHEDGE guard records fake-token balance decrease and tiny real-token receipt.
8. Because the fake source asset is unsupported, the value/slippage check is skipped or made meaningless.
9. The attacker then swaps fake tokens against the fake pool to extract the real vault asset that was moved there.

False-positive checks:
- Confirm the external aggregator actually ignores or overrides the declared source token for the selected execution path.
- Confirm the route bit flags or encoded pool values can make the actual sold token differ from the token used by the guard.
- Confirm the manager is allowed to deploy/use arbitrary pools or route through attacker-controlled pools.
- Confirm the guard's post-call slippage check uses balance deltas of decoded tokens rather than actual transfer deltas.
- Confirm unsupported source assets skip or weaken value checks.
- Confirm malicious ERC20 behavior can influence the guard's balance accounting.
- Kill the branch if the guard independently validates actual token deltas from vault balances for every supported asset.
- Kill the branch if the integration restricts pools/routes to trusted assets and verifies route direction against real pool token ordering.
- Kill the branch if unsupported assets are rejected before any external call.

PoC shape:
- Deploy a mock vault/manager or use the real protocol harness.
- Deploy a malicious ERC20 whose `balanceOf` decreases for guard calls.
- Deploy a fake UniswapV3 pool pairing the real vault asset with the fake token.
- Craft 1inch `unoswap2` calldata where declared token metadata differs from actual UniswapV3 direction bits.
- Execute through the manager's allowed 1inch integration.
- Assert the vault's real asset balance is drained or materially reduced while guard slippage checks pass.
- Recover the real asset from the fake pool to show attacker profit.

Triage notes:
- Strong impact when a trust-minimized manager can drain depositor funds despite integration guards.
- Do not report this as "manager can trade badly"; the submit-worthy root cause is a guard/execution semantic mismatch that bypasses the protocol's promised manager constraints.
- The strongest evidence is a trace showing decoded guard source/destination assets differ from actual token deltas during 1inch execution.
- Duplicate risk is high for generic "bad slippage" wording. Distinguish the exact 1inch `unoswap` pitfall: declared token ignored while encoded pool direction controls the swap.
- Malicious-token balance behavior is an exploit enabler, but the core bug is trusting attacker-declared integration metadata instead of actual execution semantics.

Audit heuristics:
- Never assume aggregator calldata field names match execution semantics; read the aggregator code path for the exact selector.
- For each route type, prove the declared `srcToken`/`dstToken` equals the token actually pulled from and sent to the vault.
- Treat bit-packed route data as security-critical. Decode every flag and compare against guard assumptions.
- Build tests where calldata lies about token identity while actual execution spends a different supported asset.
- Reject unsupported assets before external calls; never let them enter the accounting/slippage path.
- Use actual pre/post balance deltas of all relevant vault assets, not only the decoded pair.
- Consider malicious ERC20 views in guards; `balanceOf` is an external call and can lie if the token is attacker-controlled.

Related patterns:
- slippage bypass via integration semantic mismatch
- calldata-decoding trust bug
- DEX aggregator route bitfield confusion
- malicious ERC20 balance accounting
- trust-minimized manager escape hatch
- unsupported asset price-check bypass
