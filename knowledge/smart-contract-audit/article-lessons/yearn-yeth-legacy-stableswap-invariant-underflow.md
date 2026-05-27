# Pattern: Legacy stableswap invariant corruption triggers infinite LP mint

Source:
- https://rekt.news/yearn-rekt3
- https://github.com/banteg/yeth-exploit/blob/main/report.pdf
- https://etherscan.io/tx/0x53fe7ef190c34d810c50fb66f0fc65a1ceedc10309cf4b4013d64042a0331156
- https://etherscan.io/address/0x69accb968b19a53790f43e57558f5e443a91af22

Source type:
- exploit write-up / post-mortem references / on-chain incident

Status:
- verified historically

Protocol type:
- legacy stableswap / LST aggregator pool / custom AMM math / abandoned live product

Bug class:
- unchecked arithmetic underflow / invariant corruption / Newton solver failure / rebasing-token accounting / legacy-code risk

Core idea:
- A legacy yETH stableswap pool used custom invariant math over virtual balances and LST-style assets.
- Repeated zero-amount liquidity removals still triggered recalculations and shifted virtual accounting state.
- Combined with `update_rates()`, rebasing asset behavior, and asymmetric rounding helpers, the pool entered an impossible state where balance sum/product/supply no longer represented real assets.
- A dust deposit then called the LP supply solver. The solver evaluated an expression whose numerator became negative, but unchecked EVM arithmetic wrapped it to a huge integer, causing effectively infinite LP minting.

Broken invariant:
- Zero-amount liquidity operations must not mutate pool accounting or virtual balances.
- Virtual balances, real balances, rates, product, sum, and LP supply must remain mutually consistent after every update.
- Rebase/rate updates must not move the pool into an impossible state such as zero supply with corrupted virtual balances.
- Newton/invariant solvers must reject invalid domains instead of trying to converge from impossible inputs.
- LP mint amount must be bounded by real deposited value and current pool state.
- Single-asset withdrawals must not allow counterfeit LP supply to drain real assets.

Where to look in code:
- Legacy or deprecated pools still holding TVL.
- Custom stable-swap math, Newton-Raphson solvers, amplification factors, and invariant `D` calculations.
- `remove_liquidity(0)`, `deposit(0)`, `withdraw(0)`, zero-share, zero-amount, and dust paths.
- Functions that update virtual balances without moving real assets.
- `update_rates()`, rebasing-token hooks, LST exchange-rate integrations, and cached rate logic.
- `pow_up` / `pow_down` or paired rounding helpers that can drift state over repeated calls.
- `unchecked` blocks or Solidity versions/ports where underflow wraps.
- Supply minting paths that use solver output directly without value caps.

Attack path:
1. Repeatedly call a zero-amount liquidity function that should be a no-op but still mutates virtual accounting.
2. Interleave rate updates or exploit rebasing-token balance changes so virtual balances drift away from real balances.
3. Push the invariant state into an impossible domain, for example zero or near-zero supply/product with stale/corrupt balance relationships.
4. Deposit dust amounts of pool assets.
5. Trigger the supply/invariant solver on the corrupted state.
6. The solver underflows inside unchecked arithmetic and wraps the negative numerator to a huge uint.
7. The pool mints enormous LP shares to the attacker.
8. The attacker burns counterfeit LP shares through single-asset withdrawals and drains real pool assets.

False-positive checks:
- Confirm zero-amount calls are externally reachable and do more than revert/no-op.
- Confirm the repeated calls actually change virtual balances, cached rates, supply math, or invariant inputs.
- Confirm rebase/rate updates can happen between or during the manipulation sequence.
- Confirm the solver can receive invalid-domain inputs and does not guard against negative intermediate values.
- Confirm the resulting LP mint is not capped by deposited value, total assets, or max supply.
- Confirm counterfeit LP can be redeemed for real assets.
- Kill the branch if zero-amount liquidity operations revert before state changes.
- Kill the branch if invariant inputs are normalized and domain-checked before solver iteration.
- Kill the branch if rebasing/rate updates are accounted for by syncing real balances before mint/withdraw math.

PoC shape:
- Fork the live pool or build a minimal copy of the stable-swap math.
- Snapshot initial real balances, virtual balances, rates, invariant, and supply.
- Execute repeated `remove_liquidity(0)` and rate/rebase update calls.
- Assert accounting drift without real asset movement.
- Make a dust deposit and record solver inputs.
- Assert the unchecked arithmetic underflow or wrapped intermediate value.
- Assert minted LP supply is wildly disproportionate to deposited value.
- Withdraw single assets and compare attacker profit / pool balance loss.

Triage notes:
- Strong impact if a live pool can mint LP shares far above deposited value and redeem them for real assets.
- Do not reduce this to "legacy code" only. The submit-worthy root cause is an externally reachable accounting drift plus invalid-domain solver underflow plus uncapped LP mint.
- The strongest report evidence is a sequence of state snapshots proving no-op calls corrupted invariant inputs before the dust mint.
- Rebase/rate-provider assets are not automatically vulnerable; prove they are part of the state drift or invalid-domain transition.
- If the product is deprecated but still holds user funds, triage impact remains real unless the program excludes legacy deployments.

Audit heuristics:
- Treat zero-amount calls as adversarial probes. Every `amount == 0` path should revert or be a pure no-op.
- For every custom math solver, document the valid input domain and assert it before iteration.
- Fuzz sequences of no-op liquidity calls, rate updates, rebases, and dust deposits.
- Add a property: minted LP value must be less than or equal to deposited value plus allowed rounding tolerance.
- Add a property: virtual accounting must track real accounting after every public function, including rate-only functions.
- Add a property: invariant solver output must be bounded by pool assets and supply.
- Audit forgotten live products separately from active product lines; isolation protects active systems but does not protect abandoned TVL.

Operational lessons:
- Legacy contracts with TVL need active monitoring, re-audits, or deprecation.
- Custom math that is no longer understood by the current team is a high-risk asset.
- If a product is not worth maintaining, it should not continue processing user funds.
- Incident response can recover funds, but cannot substitute for lifecycle management of abandoned code.

Related patterns:
- zero-amount state mutation
- invalid-domain Newton solver
- unchecked arithmetic wraparound
- rebasing-token accounting drift
- virtual balance desynchronization
- infinite LP mint
- abandoned live product risk
