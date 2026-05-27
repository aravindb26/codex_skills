# Triage Rejection Patterns

Use this file to reduce false positives and weak submissions.

Common rejection reasons:

- Out of scope: root cause or affected asset is outside the program.
- Known issue: already listed in README, docs, public known issues, prior audits, or V12/excluded AI outputs.
- Duplicate: same root cause or same mitigation path as another report.
- Intended behavior: docs or design explicitly allow the behavior and no stated invariant is broken.
- Trusted-role dependent: requires admin, owner, operator, oracle admin, backend, relayer, or deployer misuse outside the threat model.
- Weak impact: only dust, metadata, griefing with no material cost, or best-practice hardening.
- No realistic path: state cannot occur in the supported deployment/runtime.
- PoC gap: test does not prove the claimed impact or relies on unrealistic mocks.
- Severity bar mismatch: a real defect may still be rejected when the program only rewards Critical impact and the demonstrated effect is protocol revenue shortfall, bounded congestion, or degraded throughput.
- Duplicate root cause: a stronger PoC, alternate path, or better severity framing can still be rejected if the root cause matches an earlier submission.

Before escalating a candidate, ask:

- Is the affected code in scope?
- Is the attacker unprivileged or explicitly in the accepted threat model?
- Is the impact meaningful and rewardable?
- Is the root cause distinct from known issues and likely duplicates?
- Does the evidence beat the strongest rejection argument?

## Critical-Only L1 Programs

For L1/appchain programs with a Critical-only bar, do not assume every gas, fee, or bounded DoS bug is rewardable.

Escalate only if the evidence shows at least one of:

- direct loss of user funds
- permanent lock of user funds
- chain halt
- consensus safety/liveness failure
- sustained inability to produce or finalize blocks

Downgrade or reject early if the impact is only:

- protocol-owned fee collector revenue shortfall
- bounded block-space crowding
- cheaper spam without liveness failure
- expected validator/protocol revenue loss without user-fund impact
- throughput degradation capped by normal block gas limits

Future filter:

- Identify exactly who loses value.
- Separate txpool/admission funding from final retained fees.
- Quantify whether block gas limits bound the attack.
- Check whether the program explicitly rewards economic DoS or protocol revenue loss.

## Duplicate Root Cause

Treat duplicate risk as root-cause based, not PoC-path based.

A report may still be duplicate when it adds:

- a different wrapper or entry point
- stronger runtime evidence
- a live-node or e2e harness
- a better severity argument
- a native-token path instead of alternate-token path
- a more complete exploit narrative

Future filter:

- Identify the exact missing check, wrong formula, uncharged state transition, or broken invariant.
- Search known issues, prior reports, V12/excluded outputs, and local notes for that same root cause.
- If the root cause is already covered, only escalate if the new path has a clearly separate fix or a separately rewardable asset/impact.
- When root cause overlaps, frame it as duplicate-risk immediately instead of polishing the report first.

## Underpriced Compute / Cross-VM Gas

For EVM/CosmWasm/Cosmos SDK and other multi-runtime systems, watch for cross-VM gas accounting gaps:

- parent runtime caps child work but does not charge child `GasUsed`
- error paths discard child execution responses before gas is charged
- query/helper paths are callable during consensus execution
- txpool/admission gas differs from block execution gas
- sub-context gas only tracks wrapper overhead

Critical-only filter:

- Prove more than "expensive work is undercharged."
- Show whether validators actually fail to keep up, miss consensus steps, or cannot finalize blocks under supported hardware/timing assumptions.
- If the block gas limit still bounds inclusion and blocks continue finalizing, expect downgrade or out-of-scope treatment unless the program rewards economic DoS.

## Flexible SDK APIs Vs Protocol Standard Flow

For libraries/SDKs in critical-only Web3 programs, triagers may reject unsafe generic API usage when the exploit uses parameters or UTXOs outside the intended protocol flow.

Watch for:

- optional parameters that are safe only for one canonical flow
- generic wallet/source inputs where the standard flow expects a specific protocol-owned or user-owned UTXO
- docs that describe trust assumptions around off-chain agreements
- PoCs using oversized or unrelated external funds to amplify impact

Future filter:

- Prove the candidate breaks the documented standard flow, not only a dangerous integration pattern.
- Identify who owns the exact input UTXO under the protocol model.
- Check whether the fallback/default is intentional for canonical flow before claiming unauthorized transfer.
- If the impact depends on a developer choosing oversized unrelated inputs or omitting a safety parameter, expect "developer integration error" unless the program explicitly rewards SDK misuse-resistance bugs.
