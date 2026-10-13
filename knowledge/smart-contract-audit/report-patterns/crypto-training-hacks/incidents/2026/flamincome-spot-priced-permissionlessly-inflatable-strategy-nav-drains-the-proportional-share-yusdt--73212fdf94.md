# Crypto Training Exploit Pattern Stub: Flamincome — spot-priced, permissionlessly-inflatable strategy NAV drains the proportional-share YUSDT vault

Source:
- https://crypto.training/hacks/2026-09-flamincome/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Ethereum

Loss / impact summary:
- 344,751.209366 USDT net attacker profit, from 597,352.101480 USDT gross loss of the Strat…

Tags:
- oracle/spot-price, oracle/price-manipulation, logic/price-calculation, access-control/missing-auth

Dedupe:
- id: `2026-09-flamincome`
- fingerprint: `73212fdf948424d01b3a9caef4ad0bfe88974157368273f105fc48c26b56c88a`

Core exploit idea:
- 1. VaultYUSDT is a plain proportional-share vault: deposit(a) mints shares = a totalSupply() / balance(), and withdraw(s) returns balance() s / totalSupply(), where bala…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
