# Crypto Training Exploit Pattern Stub: Alchemix — Stuck yield tokens upon withdrawal of votes from Bribe contract

Source:
- https://crypto.training/hacks/38190-stucked-yield-tokens-upon-withdrawal-of-votes-from-bribe-con/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `38190-stucked-yield-tokens-upon-withdrawal-of-votes-from-bribe-con`
- fingerprint: `b2b1f6cebaa381dfef49302a646a678210c11f0fff9bf92b004bce25db47b661`

Core exploit idea:
- 1. Bribe.deposit(amount, tokenId) increments totalSupply, balanceOf[tokenId], and totalVoting. 2. Bribe.withdraw(amount, tokenId) decrements totalSupply and balanceOf[to…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
