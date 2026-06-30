# Rejected Finding: BitGo ForwarderFactoryV4 legacy implementation mismatch

Program:
- BitGo Bug Bounty / Cantina

Candidate:
- `eth-multisig-v4/scripts/chainConfig.ts` could select legacy `Forwarder` together with `ForwarderFactoryV4` for BSC mainnet/testnet, Arbitrum One/Sepolia, and Optimism mainnet/Sepolia configs.
- `ForwarderFactoryV4` then calls a V4 initializer selector against a legacy implementation. Legacy `Forwarder.fallback()` accepts the unknown selector through `flush()` when no native value is present, leaving the clone uninitialized.

Why it looked valid:
- Local PoC showed the mismatched factory path succeeds, clone `parentAddress` remains `address(0)`, an unprivileged caller can initialize the clone as parent, and ERC20/ERC721/ERC1155 deposits can be flushed to the attacker.
- Local PoC also showed native coin sent before takeover is forwarded to `address(0)`.
- Program scope included deployment/integration logic affecting wallet security, funds management, or permissions.

Why it was rejected:
- duplicate

Exact rejection reason:
- User reported on 2026-05-29 that Cantina marked the submission duplicate and assessed it as Low severity.

Root lesson:
- Deployment/config mismatch findings can be technically real and still duplicate if the same missing version-pair guard or implementation/factory mismatch root cause was already submitted.
- Severity may be downgraded when checked live deployments are not affected and the issue is framed as source/deployment risk rather than active production impact.

Future filter:
- Before escalating factory/implementation mismatch bugs, verify whether any live supported deployment is actually paired incorrectly.
- Search local/program duplicate sources for the same missing version-pair assertion, not only the same exploit path.
- Escalate again only if the new path proves a separate affected deployment, a different root cause/fix path, or a distinct rewardable impact.

Related files or reports:
- `/home/dinesh/cantina/bitgo-audit/candidates/forwarder-v4-legacy-implementation-mismatch.md`
- `/home/dinesh/cantina/bitgo-audit/reports/forwarder-v4-legacy-implementation-mismatch.md`
- `/home/dinesh/cantina/bitgo-audit/ledgers/coverage-ledger.md`
