---
repo_url: https://github.com/zksecurity/zkbugs
repo_ref: main
contracts_dir: dataset/circom/worm-privacy/proof-of-burn/koukyosyumei_spend_missing_range_check
---

# Ground Truth — worm-privacy proof-of-burn `Spend` (Missing Range Check on GreaterEqThan)

Source: https://github.com/zksecurity/zkbugs/tree/main/dataset/circom/worm-privacy/proof-of-burn/koukyosyumei_spend_missing_range_check

The canonical V-B1 (`comparator-input-not-range-checked`) instance with **both comparator operands free**: `Spend()` checks `balance >= withdrawnBalance` with `GreaterEqThan(252)` but never constrains `balance` or `withdrawnBalance` to fit in 252 bits. Unlike a constant-pinned comparator, both operands are prover-influenced (`balance` is a witness input, `withdrawnBalance` is a public input the prover picks), so the field-overflow attack is directly reachable in this exact instantiation. The vulnerable `Spend` template is fully inlined in `circuit.circom`; the only includes are circomlib (`comparators.circom`, `mimcsponge.circom`).

## Findings

FINDING | id: H-1 | severity: High | template: Spend | signal: balance | bug_class: comparator-input-not-range-checked
description: `GreaterEqThan(252)` is invoked on `balance` and `withdrawnBalance` with no upstream `Num2Bits` (or equivalent) range check on either operand. `GreaterEqThan(n)` is only correct when both inputs are `< 2^n`; here both are arbitrary BN254 field elements. A malicious prover sets `balance = 0` and `withdrawnBalance = p - 38` (any value just below the prime): internally `LessThan(252)` computes `withdrawnBalance + 2^252 - (balance + 1) ≡ 2^252 - 39 (mod p)`, whose bit 252 is 0, so `sufficientBalanceChecker.out === 1` is satisfied even though `balance < withdrawnBalance` in the integer domain. The prover thus produces a valid `Spend` proof withdrawing more than the burned balance, breaking soundness. The fix is to range-check both inputs before the comparison — e.g. `Num2Bits(maxAmountBits)(balance)` and `Num2Bits(maxAmountBits)(withdrawnBalance)` with `maxAmountBits` well below 252 (the upstream fix parameterizes `Spend(maxAmountBits)` and swaps in `AssertGreaterEqThan(maxAmountBits)`, instantiated as `Spend(200)`).
</content>
</invoke>
