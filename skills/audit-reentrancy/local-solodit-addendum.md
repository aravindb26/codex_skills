# Local Solodit Addendum: Reentrancy Companion Mini-Skill

## Purpose
- Extend `audit-reentrancy` with battle-tested High/Medium report patterns from the local Solodit index.
- Do not replace `SKILL.md`, `reference.md`, or `checklist.md`.
- Do not duplicate the broad original categories: token callback reentrancy, state-update-after-call, cross-function reentrancy, and read-only reentrancy.

## When To Use

Use after reading `audit-reentrancy/SKILL.md` when:
- The audit involves Solidity/EVM contracts.
- The target code has external calls, native/token transfers, callbacks, hooks, flash actions, minting, claiming, bridge/message handlers, or oracle/accounting views.
- A candidate resembles reentrancy but needs sharper real-world pattern matching.
- You need duplicate-risk comparison against accepted High/Medium public findings.

Do not use as:
- A replacement for the original `audit-reentrancy` workflow.
- A reason to report a pattern without proving exploitability in the current code.
- A reason to ignore current program scope, trusted-token assumptions, or exclusions.

## Companion Workflow

Follow this after the original `audit-reentrancy` workflow:

1. Load the original skill context.
   - Read `SKILL.md`.
   - Use `reference.md` for core patterns.
   - Use `checklist.md` before finalizing.

2. Run this Solodit pattern expansion.
   - Search the current repo with the extra terms below.
   - Map matches to one of the sharper patterns in this file.
   - Ignore matches that only duplicate the original broad skill categories without adding a new exploit shape.

3. Trace real execution.
   - Identify the external interaction or callback point.
   - Identify every state variable that is stale, temporary, partially updated, or shared cross-function/cross-contract.
   - Identify every reentry target reachable before state is finalized.
   - Identify the exact asset, authorization, accounting, replay, quota, or pricing invariant that can break.

4. Kill false positives early.
   - Apply the false-positive filters in this file.
   - If the branch is only a generic CEI smell, mark it `NOT WORTH SUBMITTING`.
   - If the program excludes the required token/callback/trusted-role assumption, mark it `NOT WORTH SUBMITTING`.

5. Check duplicate and pattern risk.
   - Search the local Solodit index by function name, primitive, callback name, and pattern.
   - Treat matching stubs as duplicate-risk leads.
   - Open original source/report only when needed for a live candidate.

6. Escalate only if evidence survives.
   - Re-read the full path from entry point to final state effect.
   - Build a PoC only if the candidate is in scope, non-duplicate enough, and impact is meaningful.

## Output Requirements

When this addendum materially affects an audit branch, include:
- Pattern name from this addendum.
- Exact callback/reentry point.
- Reentered function(s).
- Stale or temporary state.
- Broken invariant.
- Why existing guards do not cover the full path.
- False-positive filters checked.
- Solodit duplicate-risk search terms used.

Local Solodit source:
- `/home/dinesh/.codex/knowledge/smart-contract-audit/report-patterns/solodit/`
- Reentrancy/callback query terms matched hundreds of High/Medium stubs, so this file stores distilled patterns only.

## Extra Search Terms

Use alongside the original skill's terms:

```text
safeMint
_safeMint
onERC721Received
onERC1155Received
onERC1155BatchReceived
flashAction
flashActionByCreditor
callback
cross_chain_callback
uniswapV3MintCallback
nonReentrant
reentrantSettle
claimRewards
distribute
redeemNative
withdrawExcessCollateral
withdrawExcessPayment
rageQuit
MessageProxy
authorizedOpenPacket
settleAuction
startLiquidationAuction
purchaseLiquidationAuctionNFT
retrySettlement
BridgeAgent
queue
batch
adapter
```

## Missing / Sharper Patterns To Check

### 1. Mint / claim callback reentrancy

Shape:
- A mint, claim, reward, or distribution path performs `_safeMint`, ERC721/1155 safe transfer, ERC777 transfer, or native transfer before all eligibility/accounting state is finalized.

Questions:
- Can `onERC721Received`, `onERC1155Received`, `tokensReceived`, or `receive()` reenter the same claim/mint path?
- Are per-wallet, per-token, per-round, per-subject, or reward-claimed flags updated after the callback?
- Can a callback mint/claim twice, bypass a max mint, or pull rewards before an index/checkpoint advances?

### 2. Limit / quota bypass through payment or receiver callbacks

Shape:
- A callback occurs while a per-wallet, max-liquidity, max-mint, cap, nonce, or order counter still has the old value.

Questions:
- Is the limit checked before the external interaction but incremented after it?
- Can the callback split one logical action into multiple accepted actions in the same transaction/block?
- Does the protocol rely on `balanceOf()` or transient ownership during a callback to enforce the limit?

### 3. Arbitrary callback / flash-action reentrancy

Shape:
- A protocol intentionally gives the caller a hook, flash action, arbitrary callback, adapter callback, or settlement callback while assets, debt, allowances, or account ownership are in a temporary state.

Questions:
- During the callback, can the attacker call another function that assumes the temporary state is final?
- Can collateral, debt, approvals, account assets, or liquidation state be moved before the callback settles?
- Does the callback allow draining without the normal withdraw/redeem path?

### 4. Cross-contract and cross-service shared-state reentrancy

Shape:
- Contract A has a guard or correct CEI locally, but Contract B/C reads or mutates the same logical state during a callback.

Questions:
- Are accounting variables split across manager/vault/token/tracker contracts?
- Can reentrancy convert temporary shares, phantom shares, pending withdrawals, or intermediate accounting into real withdrawable value?
- Is only one entry point guarded while another shared-state entry point remains callable?

### 5. Read-only reentrancy into pricing/accounting views

Shape:
- A view function is called during a callback while reserves, balances, pool state, oracle state, or fees are inconsistent.

Questions:
- Does another protocol consume this view as a price, solvency, collateral, fee, or share-value signal?
- Are balances updated before reserves, or reserves before balances?
- Can an attacker force the view to report a temporary value and settle profit elsewhere?

### 6. Message, replay, and duplicate-operation reentrancy

Shape:
- Bridge/message/order/packet processing marks messages consumed, nonces used, signatures spent, or operations complete after an external callback.

Questions:
- Can a callback replay the same message/order/signature before the consumed flag is written?
- Can the same packet or tier be duplicated into another contract/account?
- Is replay protection local to one function but bypassable through a second callback route?

### 7. Guard misuse, bypass, and self-DoS

Shape:
- `nonReentrant` exists, but it is incomplete, placed on the wrong function, nested through wrappers, bypassed through another entry point, or causes critical flows to revert.

Questions:
- Are all shared-state entry points guarded, not only the obvious external-call function?
- Do modifiers execute in an order where external logic can run before the lock is set?
- Do wrapper functions with `nonReentrant` call other `nonReentrant` functions and create stuck/unusable flows?
- Does the guard protect only same-function reentry while cross-function reentry remains open?

### 8. Callback target authentication

Shape:
- Callback functions such as `uniswapV3MintCallback`, taker callbacks, settlement callbacks, or cross-chain callbacks transfer funds or update state without proving the caller/context is the expected pool/router/message endpoint.

Questions:
- Is `msg.sender` authenticated against a factory, pool, endpoint, or stored request?
- Are callback parameters bound to an active request/order/nonce?
- Can an attacker call the callback directly to drain approved tokens or finalize fake state?

### 9. Auction and liquidation reentrancy

Shape:
- Collateral removal, liquidation start, auction settlement, or auction purchase gives control to a token/NFT/native receiver before collateral ownership, debt, auction status, or index/timelock state is fully finalized.

Questions:
- Can the callback reenter collateral removal, liquidation, bidding, claiming, or auction settlement while the auction still sees stale collateral/debt/state?
- Can the attacker start or purchase an auction against state that is about to change?
- Can reentrancy bypass an auction timelock, inject a malicious index, or buy collateral twice?

### 10. Bridge and cross-chain accounting reentrancy

Shape:
- Bridge, settlement, retry, or cross-chain message handlers perform callbacks or external sends before local accounting, message status, or remote-event assumptions are finalized.

Questions:
- Can a callback emit/send a second bridge event while local balance/accounting is temporarily restored?
- Can `retrySettlement`, message receipt, or callback processing be reentered before status is consumed?
- Can cross-chain token accounting be corrupted even if each individual chain call appears locally balanced?

### 11. Queue, batch, and adapter callback reentrancy

Shape:
- Queued deposits/withdrawals/trades, batched operations, strategy actions, or adapter callbacks process items while queue indices, batch cursors, or per-item status are mutable or partially advanced.

Questions:
- Can callback reentry reorder queued actions or process an item twice?
- Can an adapter-side callback cause message loss, skipped items, stale queue length, or out-of-order strategy execution?
- Are batch/queue cursors written before or after external callbacks?

### 12. Callback griefing and forced failure

Shape:
- The callback cannot profitably drain funds, but it can refuse receipt, consume gas, revert, or return wrong magic values to force stuck funds, forced liquidation, blocked auction/payment, or permanent DoS.

Questions:
- Can a receiver callback intentionally revert to block repayment, payment, withdrawal, claim, or auction settlement?
- Does a failed callback leave assets locked or user state permanently inconsistent?
- Does the protocol assume safe-transfer callbacks always accept assets or return correct magic values?

## False-Positive Filters

Do not escalate from this addendum unless:
- The callback/reentry path is reachable by an in-scope attacker.
- The external call target can actually execute attacker-controlled code or a protocol-controlled callback.
- The reentered function is externally reachable during the callback.
- The stale/intermediate state affects funds, accounting, authorization, replay protection, or another rewardable asset.
- Existing guards/modifiers do not cover the full cross-function or cross-contract path.
- Griefing-only callbacks cause a program-rewardable impact such as locked funds, forced liquidation, accounting corruption, or permanent DoS.

Common dead branches:
- Only internal functions are involved.
- Token set is strictly trusted and program rules exclude nonstandard tokens.
- Callback can happen but no security-relevant state is stale.
- Admin-only callback path with no user-fund or scope-relevant impact.
- Read-only inconsistency exists but no consumer can profit from it.
