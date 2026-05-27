# Rejected Finding: Kii EVM native fee refund miscalculation

Program:
- KiiChain Dual Defense

Target:
- https://github.com/KiiChain/kiichain/tree/f632e7faf979ceb6822be087585798e18db32a3b

Created:
- 2026-05-17

Rejected:
- 2026-05-21

Candidate:
- The Fee Abstraction EVM antehandler deducts the full EVM transaction fee, stores the paid fee in context, and the EVM keeper refunds unused gas using `paidAmount * leftoverGas / gasUsed`.
- The suspected bug was that refund denominator should be transaction gas limit / paid gas units, not charged `gasUsed`.
- With `MinGasMultiplier = 0.5`, low-work EVM transactions could be charged half the gas limit and then receive a full refund, allowing valid EVM block gas consumption with zero retained native fees.

Why it looked valid:
- The refund formula divided by `gasUsed` instead of the transaction gas limit.
- A native-fee path appeared to satisfy txpool admission requirements, avoiding the prior alternate-token-only false-positive concern.
- The PoC reportedly executed 10 signed EVM transactions in `FinalizeBlock`, consumed `530000` block gas, returned the sender to the original native balance, and left the fee collector with zero retained fees.

Validation evidence provided:
- PoC file: `x/feeabstraction/ante/evm/refund_poc_test.go`
- Command:

```bash
cd /home/dinesh/kiichain-audit/kiichain
go test -tags=test ./x/feeabstraction/ante/evm -run 'TestPoC(NativeEVMTxpoolAcceptsRefundBugPrerequisites|FinalizeBlockNativeEVMRefundCanFillBlockWithZeroNetFees)$' -count=1 -v
```

Observed output:

```text
=== RUN   TestPoCFinalizeBlockNativeEVMRefundCanFillBlockWithZeroNetFees
    refund_poc_test.go:269: FinalizeBlock accepted 10 EVM txs using 530000 block gas with zero net native fee paid
--- PASS: TestPoCFinalizeBlockNativeEVMRefundCanFillBlockWithZeroNetFees (0.24s)
=== RUN   TestPoCNativeEVMTxpoolAcceptsRefundBugPrerequisites
--- PASS: TestPoCNativeEVMTxpoolAcceptsRefundBugPrerequisites (0.20s)
PASS
ok      github.com/kiichain/kiichain/v7/x/feeabstraction/ante/evm 0.576s
```

Why it was rejected:
- Out of scope for the program's Dual Defense severity bar.
- Triage accepted that the refund miscalculation was a real defect, but classified the impact as fee-collector revenue shortfall / bounded throughput degradation.
- The fee collector was protocol-owned, not a user-owned balance.
- No user-fund loss, permanent user-fund lock, chain halt, or consensus-level liveness failure was shown.
- Block gas remained bounded by the block gas limit, so the worst-case effect was crowding/degraded throughput rather than unbounded execution or chain halt.
- Triage stated the attacker still pays the SDK-declared `GasWanted` per transaction from an admission/funding perspective; the issue was over-refund of the upfront amount, not bypass of tx admission funding.

Exact rejection reason:
- Program only rewarded Critical L1 issues such as user-fund loss, permanent fund lock, or chain halt / consensus-level impact. This was closed as out of scope.

Root lesson:
- A real fee-accounting defect is not automatically rewardable if the program's bar is Critical-only and the impact is protocol revenue shortfall or bounded block-space crowding.
- For L1 / appchain programs, separate:
  - real defect
  - economic DoS
  - bounded throughput degradation
  - consensus/liveness failure
  - user-fund loss or permanent lock
- Do not frame "zero net fee" as Critical unless the PoC proves chain halt, consensus disruption, unbounded resource consumption, or direct user-fund impact under the program rules.

Future filter:
- Before submitting gas/refund/fee-abstraction findings, check whether the program rewards protocol revenue loss or bounded DoS.
- If the program only pays for Critical L1 impact, require evidence of at least one of:
  - chain halt
  - consensus safety/liveness failure
  - permanent inability to produce/finalize blocks
  - direct loss of user funds
  - permanent lock of user funds
- If block gas limits bound the attack, quantify whether the attack is merely cheaper congestion or a true liveness failure.
- Identify who loses value: user balances, protocol-owned fee collector, validators, relayers, or only expected revenue.
- Distinguish txpool/admission funding from final retained fees.

Reusable bug pattern:
- Refund denominator mismatch in gas/fee accounting.
- Upfront fee is deducted using gas limit or max fee, but refund is calculated using charged/used gas after clamping or normalization.
- If charged gas can be lower than gas limit, `paidAmount * leftoverGas / gasUsed` may over-refund and can refund the entire fee.

Where to look in future audits:
- EVM antehandlers in Cosmos SDK chains.
- Fee abstraction modules.
- Refund logic that reads paid fees from context.
- Gas multiplier / minimum gas used / gas normalization logic.
- Separate txpool admission checks vs block execution accounting.
- Native fee path and alternate token fee path differences.

PoC shape for future use:
1. Fund sender with exactly enough native fee balance for txpool admission.
2. Submit low-work EVM transactions with gas limit high enough to trigger minimum gas multiplier behavior.
3. Execute transactions through the real block/finalization path, not only unit-level refund logic.
4. Compare sender starting balance, ending balance, fee collector balance, block gas consumed, and tx success status.
5. Prove whether the result is revenue loss, bounded congestion, or true consensus/liveness impact.

Related triage category:
- Critical-only bounty rejects real defects when impact is protocol revenue shortfall or bounded throughput degradation.

