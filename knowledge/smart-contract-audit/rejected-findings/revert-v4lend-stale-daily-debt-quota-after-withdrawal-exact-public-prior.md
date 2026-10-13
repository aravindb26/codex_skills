# Rejected Finding: Revert V4 stale daily debt quota after withdrawal

Program:
- Cantina Revert v4lend competition

Candidate:
- In V4Vault, a same-day settled lender withdrawal after the daily debt quota is initialized leaves `dailyDebtIncreaseLimitLeft` at its pre-withdraw value. A later borrow can exceed a fresh quota based on remaining lender supply.

Why it looked valid:
- At pinned commit `f6d0fb41b7487f60ce64e011312a956e184e2a75`, `_withdraw` updates lender supply and `dailyLendNetInflow` but does not rebase the cached debt quota; `_resetDailyDebtIncreaseLimit` recalculates only at a new day or forced reset.
- A fork-free production-contract test enforced the deployed 100,000-unit/day deposit floor, building 900,000 units over nine days and adding 100,000 units of separate lender supply before the attack. The stale-quota branch and same-price control passed 2/2; V4LE-122/127 regressions passed 5/5.
- With deployment-shaped quota and collateral settings, the stale allowance enables roughly 100,000 units of debt versus a fresh 75,000-unit floor. A later synchronized external repricing in deterministic Chainlink/TWAP test doubles reduces the remaining lender claim by about 26,218.916 asset units. The test proves conditional consequence, not attacker control of production price sources.

Why it was rejected:
- Exact-root public prior disclosure (duplicate-prone). A self-published Revert V3 report, [M-01: Daily Debt Cap Bypass via Inflated Lender Base](https://gist.github.com/blessingblockchain/0e3691b028de5913631774b5ee3a412b), describes the same affected withdrawal/borrow path, stale `dailyDebtIncreaseLimitLeft`, calculate-then-withdraw ordering, temporary-supply setup, and lender-utilization risk.
- V4's `_settledLentAssets` change prevents same-day deposits from inflating the cap at calculation time, but it does not repair the stale cached allowance after settled supply is later withdrawn. Thus the V4 change is not a distinct root or mitigation for the disclosed sequence.
- The Gist is self-published, not an official C4 finding or a Cantina-listed known issue. The conservative verdict is still `NOT WORTH SUBMITTING` because the root-cause overlap is exact and uniqueness is not defensible.

Intent and related-pattern distinctions:
- Revert's commit `e684a07` and `docs/audit-handoff.md:97` state that settled withdrawals shrink both supply-relative bounds immediately, including the daily debt quota; this candidate was not killed as intended behavior.
- V4LE-127 concerns same-day deposit exclusion when the quota is calculated; V4LE-122 covers the dynamic per-token concentration cap. Their tested branches differ from the post-initialization quota cache, but the separate V3 Gist is an exact prior.
- MixBytes DIA Lumina Staking M-1 concerns a live-recomputed withdrawal cap shrinking and blocking later withdrawals; its client explicitly accepted that behavior. It is a semantic analogy, not the exact duplicate.
- Official Revert V3 C4 M-08 and M-22 have different roots (reset ordering after repayment/withdrawal and quota restoration on liquidation, respectively); they are not substitutes for the exact Gist comparison.

Future filter:
- For a daily cap based on a mutable aggregate, compare both (a) the value used when the cap is calculated and (b) every later mutation of the base before the cap resets.
- When a version changes the base formula, re-test whether the cached cap is rebased after later withdrawals; a fix for same-day deposit inflation does not prove withdrawal-side synchronization.
- Search public reports for the exact state variable and operation ordering, not only official contest reports. Separate confirmed protocol behavior from the report's evidence quality and acceptance status.
- Do not submit this candidate as a V4 variant unless new evidence shows the V3 public report's root differs materially or the V4 scope introduces a distinct affected invariant/impact path.

Evidence:
- Audit card: `/home/dinesh/cantina/revert-v4lend-audit/.context/vault-daily-debt-quota-after-withdrawal-verification-2026-10-11.md`
- Primary Revert V3 report: https://gist.github.com/blessingblockchain/0e3691b028de5913631774b5ee3a412b
- Primary source code path: `/home/dinesh/cantina/revert-v4lend-audit/repo/src/vault/V4Vault.sol`
