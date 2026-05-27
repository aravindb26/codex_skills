# Rejected Finding: Sundial distribution change defaults to user timelock

Program:
- Sundial Protocol btc-locker HackenProof Dual Defense, critical-only, commit `c3d16f60606ec30c26078b9a1f16622828b1dcd6`.

Candidate:
- `createDistributionTransaction` sends above-dust change to `params.changeAddress || timelockAddress`.
- With `sourceAddress + api` auto-fetch, an oversized provider wallet UTXO can be swept to the user's timelock when `changeAddress` is omitted.

Why it looked valid:
- `changeAddress` is optional in `DistributionParams`.
- Docs describe a separate distribution output and change output.
- PoC showed intended distribution of `25_000` sats producing `99_996_560` sats paid to the recipient timelock from `100_000_000` sats of provider UTXOs.

Why it was rejected:
- intended behavior / out of scope / developer integration error.

Exact rejection reason:
- Triage and Sundial stated the standard Distribute step returns the user's principal and yield to the user's timelock using the claimed Escrow UTXO.
- Under that standard flow, `params.changeAddress || timelockAddress` is considered correct.
- Using an oversized external provider UTXO without `changeAddress` was classified as developer integration error rather than protocol defect.

Root lesson:
- For flexible SDK/library APIs in critical-only programs, do not equate unsafe generic integration with protocol defect.
- First prove the exploit occurs in the protocol's documented standard flow and with the intended ownership of the input UTXO.
- If the team defines a value path as user-owned return flow, overpayment-looking behavior can be treated as intentional.

Future filter:
- Before escalating Sundial distribution issues, verify whether the input is the claimed escrow-related UTXO that should entirely return to the user.
- Only submit a distribution candidate if the standard flow itself creates an unauthorized transfer, permanent lock, wallet-secret exposure, or transaction tampering that cannot be explained as provider-controlled off-chain obligation or integration misuse.

Related files or reports:
- `/home/dinesh/sundial-audit/notes/SD-BTC-DIST-001-report.md`
- `/home/dinesh/sundial-audit/notes/audit-ledger.md`
- `packages/core/src/locker/transactions/distribute.ts`
