# Local Solodit Addendum: Token Integration Companion Mini-Skill

## Purpose
- Extend `token-integration-analyzer` with distilled High/Medium Solodit token-integration patterns.
- Do not replace `SKILL.md` or its resources.
- Use this for missing exploit shapes around fee-on-transfer, rebasing, blacklists, approvals, decimals, and token receiver callbacks.

## When To Use

Use after reading `token-integration-analyzer/SKILL.md` when code accepts, transfers, prices, escrows, lends, swaps, bridges, or distributes arbitrary ERC20/ERC721/ERC1155 tokens.

## Companion Workflow

1. Load the original token integration skill first.
2. Search current code with the extra terms below.
3. For each token interaction, identify whether accounting uses requested amount, actual balance delta, shares, or external token metadata.
4. Test weird-token behavior only if token set is arbitrary or accepted deployment includes such tokens.
5. Search Solodit stubs by token behavior and impacted function before escalating.

## Extra Search Terms

```text
safeTransfer
safeTransferFrom
transferFrom
approve
allowance
permit
decimals
balanceOf
feeOnTransfer
blacklist
blocklist
paused
rebasing
shares
onERC721Received
onERC1155Received
magic bytes
return value
zero value
```

## Missing / Sharper Patterns To Check

### 1. Requested amount used instead of actual received/sent

Shape:
- Protocol credits deposits, repayments, collateral, or swaps by `_amount` even when token takes fees, rebases, or transfers less.

Questions:
- Is balance delta measured before/after transfer?
- Can debt be underpaid or collateral overcredited?
- Does fee-on-transfer break complete repayment/liquidation accounting?

### 2. Rebasing and yield-bearing token balance drift

Shape:
- Protocol assumes `balanceOf` changes only through its own transfers.

Questions:
- Can rebases create surplus/deficit not reflected in shares?
- Can direct yield change exchange rate in favor of first/last actor?
- Are shares based on internal accounting or raw token balance?

### 3. Blacklist, pause, and receiver restrictions block critical exits

Shape:
- Blacklistable/pausable tokens or receiver-restricted NFTs block repayment, liquidation, withdrawal, auction, or distribution.

Questions:
- Can one blacklisted receiver block batch processing?
- Can collateral become permanently unliquidatable?
- Are failure paths isolated or do they revert the whole operation?

### 4. Approval and permit quirks

Shape:
- Code assumes `approve`, `permit`, or allowance changes behave uniformly across tokens.

Questions:
- Does unchecked `approve` return trap funds?
- Does token require allowance reset to zero first?
- Can permit be front-run to DoS the intended operation?

### 5. Mutable or untrusted decimals/metadata

Shape:
- Token decimals/name/symbol are fetched dynamically or trusted for accounting/price/security-sensitive logic.

Questions:
- Are decimals cached and validated for accepted tokens?
- Can mutable/untrusted decimals change collateral valuation or share math?
- Is metadata used in code generation, signatures, or UI-security assumptions?

### 6. ERC721/ERC1155 receiver and callback authentication

Shape:
- Receiver callbacks accept tokens or perform state changes without validating caller/token/request context.

Questions:
- Does `onERC721Received`/`onERC1155Received` check the expected token contract?
- Can any token invoke callback and register fake collateral/deposit?
- Are magic bytes checked when sending NFTs out?

### 7. Zero-value and large-value transfer edge cases

Shape:
- Token reverts on zero transfers/approvals, large approvals, or unusual self-transfer behavior.

Questions:
- Can zero-amount paths DoS queues, claims, or batch settlement?
- Does the protocol approve max values to tokens that reject large approvals?
- Are self-transfer or `transferFrom(src == msg.sender)` semantics assumed?

## False-Positive Filters

Do not escalate unless:
- The protocol accepts arbitrary affected tokens, or the in-scope configured token has that behavior.
- The behavior changes funds, debt, collateral, accounting, liveness, or authorization.
- There is no wrapper/allowlist/balance-delta accounting that neutralizes the token behavior.
- The report is not just "token is weird"; it must show the integration breaks.
