# Local Solodit Addendum: Signature Replay Companion Mini-Skill

## Purpose
- Extend `signature-replay-analysis` with Solodit-style replay and account-abstraction patterns.
- Avoid duplicating `audit-signature/local-solodit-addendum.md`; read that file too for broader signature authorization patterns.

## When To Use

Use after reading `signature-replay-analysis/SKILL.md` when signatures authorize execution, permits, sessions, messages, account modules, or cross-chain actions.

## Companion Workflow

1. Build the exact replay domain: signer, chain, contract, account, nonce, action, deadline, message id, and consumed state.
2. Identify every route where the same signed intent can be submitted again or under a different context.
3. Check `audit-signature/local-solodit-addendum.md` for EIP-712, ERC-1271, permit DoS, and signer-gate patterns.
4. Search Solodit stubs by nonce variable, domain/typehash, session/checkpoint, and replayed action before escalating.

## Extra Search Terms

```text
usedNonces
nonceBitmap
nonceUsed
consumed
executed
successfulTransactions
messageId
clientId
session
checkpoint
checkpointer
isValidSignature
domainSeparator
typeHash
permit
```

## Missing / Sharper Patterns To Check

### 1. Action consumed state is not the same as signature nonce

Shape:
- Nonce is checked, but message/action/client id/success status is not atomically recorded.

Questions:
- Can a different client id suppress or replay the same action?
- Is success stored before external calls?
- Can failed execution consume nonce and block intended execution?

### 2. Partial replay through session or checkpoint options

Shape:
- A signature binds high-level session approval but not exact checkpoint, subcall, module, or execution mode.

Questions:
- Can disabling checkpoint usage bypass all validation?
- Can signed session call be front-run or replayed with different calldata?
- Are nested calls constrained by the same signed policy?

### 3. Cross-domain replay beyond chain id

Shape:
- Signature includes chain id but misses account, module, version, source chain, destination chain, or verifying contract.

Questions:
- Can same signature work through another module/router/account on same chain?
- Can fork, migration, proxy upgrade, or account clone reuse domain unexpectedly?
- Is cross-chain message id signed with both source and destination context?

## False-Positive Filters

Do not escalate unless:
- Replay changes funds, permissions, governance/account state, message execution, or causes rewardable DoS.
- The signature remains valid after considering every nonce/consumed/deadline/domain check.
- The replay path is executable by an in-scope attacker.
