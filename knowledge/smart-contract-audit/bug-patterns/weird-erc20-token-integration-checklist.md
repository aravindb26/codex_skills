# Weird ERC20 Token Integration Checklist

Source:
- <https://github.com/d-xo/weird-erc20>

Reviewed snapshot:
- `781c8f039c106eb2d5c6071046b0dbb2f72c9870`
- Reviewed on 2026-08-01

Local policy:
- Distilled local checklist only. Do not copy the full repository into the knowledge base unless licensing is clarified.
- Use as a token-integration lead source, not as proof by itself.
- A finding must show that the current protocol accepts or is configured with an affected token behavior and that the integration breaks a real asset, accounting, authorization, or liveness invariant.

## When To Use

Use this when a protocol:

- accepts arbitrary ERC20s
- accepts allowlisted ERC20s whose behavior is not fully pinned
- escrows, lends, borrows, swaps, wraps, bridges, distributes, or prices ERC20s
- credits users by requested transfer amount instead of actual balance delta
- caches balances, reserves, token metadata, or token addresses
- supports permit, approval-management, native-token wrappers, or cross-chain token representations

## Defensive Baseline

Prefer one of these designs:

- strict allowlist of known-good tokens with pinned semantics
- dedicated wrapper/adaptor contracts at the system edge
- balance-delta accounting for every token movement
- explicit handling of pause, blocklist, fee, rebase, nonstandard return, approval, and native-representation behavior

If a protocol is permissionless and cannot maintain an onchain allowlist, it needs defensive accounting and failure isolation. "Any ERC20 works" is usually false.

## Patterns To Test

### Reentrant transfer callbacks

Examples:
- ERC777-style hooks
- token callbacks during `transfer` or `transferFrom`

Checks:
- Does token transfer happen before internal accounting is finalized?
- Can callback re-enter deposit, withdraw, swap, repay, liquidation, claim, or settlement?
- Are cross-contract callbacks protected, not only direct same-function reentrancy?

### Missing, false, or unchecked return values

Examples:
- no boolean return
- returns `false` on failure
- returns `false` even after a successful transfer

Checks:
- Does the code use low-level calls or raw `IERC20.transfer` without checking success?
- Does it assume success because the call did not revert?
- Can a free deposit, unpaid repayment, or unpaid swap still credit state?

### Fee-on-transfer and transfer-less-than-amount

Examples:
- transfer fee tokens
- tokens that transfer only `balanceOf(sender)` for `amount == type(uint256).max`

Checks:
- Is credit/debt/share math based on requested `_amount` instead of actual balance delta?
- Can collateral, LP shares, rewards, or repayments be overcredited?
- Can withdrawal or accounting drift be amplified by repeated transfers?

### Rebasing, airdrops, donation, and external balance changes

Examples:
- rebasing tokens
- yield-bearing balances
- direct donation to vault/pair/escrow
- governance-token airdrops

Checks:
- Does internal accounting assume `balanceOf(this)` only changes through protocol code?
- Can direct balance changes inflate shares, reserves, collateral value, or rewards?
- Can cached balances desync from real balances?

### Upgradeable, pausable, and blocklistable tokens

Examples:
- USDC/USDT-style admin controls
- proxy-upgradeable token logic

Checks:
- Can a token admin pause or blocklist the protocol and freeze exits, liquidation, settlement, or distribution?
- Does the protocol isolate failures per user/token, or does one token revert block a whole batch?
- Are token semantics revalidated after upgrades?

### Approval quirks

Examples:
- must approve zero before nonzero
- approve zero reverts
- approve spender zero address reverts
- large approvals revert or truncate

Checks:
- Does the protocol manage allowances safely across repeated operations?
- Can approval reset behavior DoS swaps, zaps, bridges, or routers?
- Does `type(uint256).max` approval map to a smaller internal allowance?

### Decimal and metadata quirks

Examples:
- low decimals
- high decimals
- mutable/untrusted decimals
- `bytes32` name/symbol instead of string
- malicious token name/symbol content

Checks:
- Are decimals cached, bounded, and normalized before accounting/pricing?
- Can high decimals overflow or low decimals create material truncation?
- Is metadata used in signatures, code generation, UI rendering, or security-sensitive identity?

### Multiple token addresses and proxy confusion

Examples:
- proxied tokens with more than one address
- underlying/proxy address mismatch

Checks:
- Does rescue/sweep logic assume one address per asset?
- Can an owner or attacker bypass "not pool token" checks using the other token address?
- Are token identity checks based on canonical asset identity, not only one contract address?

### `transferFrom(src == msg.sender)` semantics

Examples:
- some tokens skip allowance decrement when caller is the source
- others always decrement allowance

Checks:
- Does code assume `transfer` and `transferFrom(address(this), ...)` are equivalent?
- Can self-transfer paths fail unexpectedly or skip intended allowance controls?

### Permit incompatibilities

Examples:
- DAI-like `permit`
- non-EIP-2612 permit
- tokens that no-op instead of reverting

Checks:
- Is permit success checked by validating nonce/allowance after the call?
- Can a failed/no-op permit allow later logic to continue?
- Is Permit2 used with correct owner, spender, token, amount, nonce, deadline, and witness/domain binding?

### ERC20 representation of native currency

Examples:
- CELO on Celo
- POL on Polygon
- ETH representation on zkSync Era

Checks:
- Can native currency and ERC20 representation be double-counted or used interchangeably?
- Does pool/vault/router accounting separate `msg.value` from ERC20 balance movement?
- Can settlement, wrapping, or rescue logic drain native-currency pools?

## False-Positive Filters

Do not report only "this token could be weird."

Escalate only if:

- the affected token behavior is accepted by scope, configuration, or permissionless listing
- the code path is reachable by an unprivileged or in-scope actor
- the behavior changes actual accounting, asset movement, solvency, authorization, or liveness
- wrappers, allowlists, balance-delta checks, and per-token failure isolation do not neutralize the issue
- the impact survives the current program's severity and duplicate rules

