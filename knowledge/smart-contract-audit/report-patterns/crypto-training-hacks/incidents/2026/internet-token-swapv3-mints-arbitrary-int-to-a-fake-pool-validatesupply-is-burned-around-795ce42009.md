# Crypto Training Exploit Pattern Stub: Internet Token `swapV3` mints arbitrary INT to a fake pool — `validateSupply` is burned around

Source:
- https://crypto.training/hacks/2026-09-internettoken/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Base

Loss / impact summary:
- Mint 925,411,678.379023085745037207 INT, dump 161,265,976.195260022578593802 INT for 5.84…

Tags:
- reentrancy/cross-contract, logic/missing-validation, access-control/missing-auth, logic/incorrect-state-transition

Dedupe:
- id: `2026-09-internettoken`
- fingerprint: `795ce4200930b9e3cd29cdddb3c0dc620130cb7921e627732300b1227d8c2930`

Core exploit idea:
- Internet Token (INT, RewardToken 0x968D6A…eC19) on Base mints only from addresses that hold TOKEN_MINTER. LiquidityUnifier holds that role. Its swapV3(address token, add…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
