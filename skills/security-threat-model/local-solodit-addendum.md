# Local Solodit Addendum: Web3 Threat Modeling

## Purpose

Use this companion with `security-threat-model` for smart contract and Web3 repositories.

The goal is to make the threat model useful for bounty hunting: assets, trust boundaries, attacker capabilities, abuse paths, invariants, and likely triage constraints.

## When To Use

Use this addendum when threat modeling:

- DeFi protocols
- bridges and cross-chain systems
- appchains, L1/L2 modules, and rollups
- Solana, Cosmos, Cairo/StarkNet, Substrate, TON, Algorand, Solidity, or Vyper systems
- source-code bounty targets with Web3 integrations

## Companion Workflow

1. Lock scope, exclusions, severity rules, trusted roles, and deployment assumptions.
2. Identify assets: user funds, protocol reserves, debt, shares, rewards, messages, privileges, signatures, and liveness.
3. Identify actors: users, attackers, liquidators, keepers, solvers, validators, sequencers, relayers, bridge executors, oracle providers, admins, and guardians.
4. Map money flow and lifecycle state machines.
5. Search local knowledge and Solodit stubs for matching protocol primitives.
6. Convert accepted report patterns into concrete abuse paths.
7. Convert rejected local findings into explicit non-goals or rejection filters.

## False-Positive Filters

Do not include threats as likely findings if they depend on:

- trusted-role misuse outside scope
- impossible deployment state
- purely offchain failure where onchain enforcement is not promised
- weak informational impact
- public report similarity without the same invariant and same missing guard

## Output Requirements

When this addendum is used, include:

- assets and security boundaries
- attacker capabilities
- top abuse paths
- invariants to audit
- Solodit/local patterns worth checking
- scope and triage constraints that may kill candidates
