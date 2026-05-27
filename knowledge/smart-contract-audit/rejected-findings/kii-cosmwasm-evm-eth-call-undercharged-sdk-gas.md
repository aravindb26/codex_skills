# Rejected Finding: Kii CosmWasm EVM eth_call undercharged SDK gas

Program:
- KiiChain L1 Dual Defense Audit

Report ID:
- KCNL1DDA-109

Target:
- https://github.com/KiiChain/kiichain/tree/f632e7faf979ceb6822be087585798e18db32a3b

Created:
- 2026-05-14

Rejected:
- 2026-05-15

Candidate:
- Kii's CosmWasm EVM custom query binding allowed a wasm contract to execute EVM `eth_call` subqueries during `execute`.
- The binding capped each EVM call by current SDK gas remaining, but did not charge the returned EVM `GasUsed` back to the SDK/block gas meter.
- A malicious wasm contract could repeatedly call a gas-burning EVM contract, catch/ignore each query error, and return success.
- Validators performed EVM interpreter work while block gas recorded mostly wasm/query overhead.

Affected code claimed:
- `wasmbinding/evm/queries.go`
- `HandleEthCall` built an EVM call and returned response data without consuming `res.GasUsed`.
- `callEVMAndHandleRevertError` discarded the response when `VmError` was non-empty, preventing gas charging after error handling.
- `github.com/KiiChain/evm@v0.6.0-fork.1/x/vm/keeper/grpc_query.go`
- `EthCall` returned `MsgEthereumTxResponse.GasUsed` after `ApplyMessageWithConfig`.
- `github.com/CosmWasm/wasmd@v0.61.2/x/wasm/keeper/query_plugins.go`
- Wasmd charged parent wasm execution only for `subCtx.GasMeter().GasConsumed()`.

Why it looked valid:
- The EVM call path had a separate gas accounting domain from the SDK/block gas meter.
- The parent wasm execution was only charged for subquery SDK gas, not full EVM interpreter gas.
- Public genesis evidence showed wasm upload and instantiate were permissionless:
  - `consensus_params.block.max_gas = 10000000`
  - `wasm code_upload_access.permission = Everybody`
  - `wasm instantiate_default_permission = Everybody`
- The attack did not require privileged roles.

Validation evidence provided:
- Unit/keeper PoC:
  - `wasmbinding/evm/missing_precompile_poc_test.go`
  - `wasmbinding/evm/testdata/evm_query_burner/`
- EVM init code:

```text
0x6004600c60003960046000f35b600056
```

- Runtime:

```text
JUMPDEST; PUSH1 0; JUMP
```

- Command:

```bash
go test -tags=test ./wasmbinding/evm -run TestPoCWasmExecuteEthCallSubqueryDoesNotChargeConsumedEVMGas -count=1 -v
```

- Observed output:

```text
SDK gas consumed by wasm execute: 2130023
PASS
```

- The test reportedly used a `10,000,000` SDK gas meter, succeeded, and performed 100 EVM out-of-gas calls while consuming only `2,130,023` SDK gas.

Additional FinalizeBlock evidence:

```bash
go test -tags=test ./wasmbinding/evm -run TestPoCFinalizeBlockEthCallSubqueryUnderchargesBlockGas -count=1 -v
```

Observed output:

```text
pre-FinalizeBlock tx context EthCall vm_error="out of gas" gas_used=2000000 sdk_gas=19493
tx 0 ABCI gas wanted=10000000 used=2086350
tx 1 ABCI gas wanted=10000000 used=2073071
tx 2 ABCI gas wanted=10000000 used=2073221
tx 3 ABCI gas wanted=10000000 used=2072831
FinalizeBlock ran 4 wasm txs x 100 EVM eth_call subqueries in 28.215618818s; total ABCI/block gas used=8305473 of max=10000000
PASS
```

Additional Docker e2e evidence:

```bash
KIICHAIN_AUDIT_LIVENESS_ONLY=true SKIP_IBC_TESTS=true KIICHAIN_E2E_VALIDATORS=2 go test -mod=readonly -tags=test ./tests/e2e -run TestIntegrationTestSuite/TestAuditLivenessEVMEthCallWasm -count=1 -timeout=30m -v
```

Observed output:

```text
attack tx 662C52E951C0FADDE08D1AFB5F455922CB0004F8AE9288B571119E698C0648F0 height=10 gas_wanted=10000000 gas_used=2411501
attack tx 5BBDC4DBFBB9B79CE5BF1DA182CB680D153D4903C1299B514EAEEA209E631E38 height=10 gas_wanted=10000000 gas_used=2411552
attack tx 3D2C062FBE2F98D532004CBF778B0D146049F6B96A38773D7AEE90672EB485CF height=10 gas_wanted=10000000 gas_used=2411552
attack tx EDB9A01B77365C4B9C0C6EFC9A81D5DE3AA082C98BE6E63856A399C96EF58A9F height=11 gas_wanted=10000000 gas_used=2411501
audit liveness result: validators=2 before_height=8 tx_heights=[10 11] committed_in=26.5279545s total_tx_gas_used=9646106 block_max_gas=10000000
```

Why it was rejected:
- Triage classified it as a duplicate of an earlier submission covering the same root cause:
  - `HandleEthCall` in `wasmbinding/evm/queries.go` did not charge `res.GasUsed` back to the SDK gas meter after executing an EVM call.
- The program only accepted Critical severity vulnerabilities.
- Triage considered the impact to be a gas accounting mismatch leading to potential DoS via underpriced EVM execution.
- Triage stated it did not demonstrate direct theft of user funds, permanent freezing of funds, or consensus disruption meeting the program's Critical threshold.
- Later comments added stronger FinalizeBlock and live-node evidence, but the root cause remained duplicate and severity reconsideration was not accepted in the provided thread.

Exact rejection reason:
- Duplicate root cause and out-of-scope severity for a Critical-only Dual Defense program.

Root lesson:
- Stronger PoC evidence does not always overcome duplicate classification if the root cause is the same as an earlier submission.
- For Critical-only L1 programs, "undercharged consensus-path compute" must be framed and proven as actual consensus/liveness failure, not only slow FinalizeBlock or bounded validator CPU amplification.
- A valid block taking tens of seconds is useful evidence, but triage may still require clearer proof that nodes cannot participate, blocks cannot finalize, or consensus timing assumptions are broken in a way the program recognizes as Critical.

Future filter:
- Before submitting underpriced compute / gas mismatch reports, check whether the same missing gas charge root cause has already been reported.
- If a report shares root cause with an earlier issue, assume high duplicate risk even if the PoC path, wrapper, or severity argument is stronger.
- For Critical-only L1 programs, collect evidence beyond "below block gas but expensive CPU":
  - validator misses/precommit failures
  - block production/finalization delay beyond protocol tolerance
  - repeated blocks causing sustained liveness failure
  - node inability to keep up on recommended hardware
  - mempool/consensus evidence that honest validators fall behind
- Distinguish:
  - underpriced execution
  - bounded block CPU amplification
  - validator overload
  - actual chain halt / consensus disruption

Reusable bug pattern:
- Cross-VM gas accounting gap.
- One execution environment performs expensive work, returns `GasUsed`, but the parent environment only charges wrapper/query overhead.
- Error paths can hide or discard gas usage before the parent meter is charged.

Where to look in future audits:
- Cosmos SDK chains with EVM + CosmWasm integration.
- Wasm custom query plugins that call into EVM or other execution engines.
- Query paths callable during execute or consensus execution.
- Error handling that discards a response before gas accounting.
- Sub-context gas meters that do not reflect downstream VM work.
- Helper queries and precompile wrappers that use default gas caps instead of caller budgets.

PoC shape for future use:
1. Deploy a callee contract in the secondary VM that burns gas or loops until out-of-gas.
2. Deploy a parent-environment contract that repeatedly invokes the secondary VM through a query/helper path.
3. Catch or ignore secondary VM errors so parent execution succeeds.
4. Execute through the real block path, not only direct keeper calls.
5. Compare secondary VM gas used, parent SDK/block gas charged, wall-clock execution time, and consensus/liveness behavior.
6. If seeking Critical, demonstrate sustained validator inability to participate or finalize, not only gas-accounting mismatch.

Related triage category:
- Duplicate root cause.
- Critical-only program rejects bounded underpriced-computation DoS without clear consensus-level failure.

