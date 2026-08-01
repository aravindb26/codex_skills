# Crypto Training Exploit Pattern Stub: ParaSpace — flash-loan bypass of the auction recovery health check

Source:
- https://crypto.training/hacks/15980-h-07-user-can-pass-auction-recovery-health-check-easily-with/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2022

Chain:
- Other

Loss / impact summary:
- Auction recovery can be cancelled while the borrower has no lasting recovery collateral;…

Tags:
- reentrancy/single-function, logic/missing-validation, dos/lockup

Dedupe:
- id: `15980-h-07-user-can-pass-auction-recovery-health-check-easily-with`
- fingerprint: `c3c3c2413a5d261d5b045bf50dd541873456174236d2a097d0403ce08e5c78a6`

Core exploit idea:
- ParaSpace checks that the NFT account is above the recovery threshold only at the instant setAuctionValidityTime() executes. A borrower can flash-borrow 1,000 WETH, supp…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
