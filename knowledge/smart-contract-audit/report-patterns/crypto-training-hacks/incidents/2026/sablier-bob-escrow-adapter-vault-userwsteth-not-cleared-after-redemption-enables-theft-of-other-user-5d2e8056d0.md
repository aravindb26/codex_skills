# Crypto Training Exploit Pattern Stub: Sablier Bob Escrow — Adapter vault `_userWstETH` not cleared after redemption enables theft of other users' funds

Source:
- https://crypto.training/hacks/65582-adapter-vault-userwsteth-not-cleared-after-redemption-enabl/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2026

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `65582-adapter-vault-userwsteth-not-cleared-after-redemption-enabl`
- fingerprint: `5d2e8056d0d33310bec42441cfeb73cf9b67cbe8d907714d1a48a541b94a705e`

Core exploit idea:
- 1. Adapter vaults track each user's staked amount in _userWstETH. 2. On redeem, shares are burned and WETH is paid from calculateAmountToTransferWithYield — but _userWst…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
