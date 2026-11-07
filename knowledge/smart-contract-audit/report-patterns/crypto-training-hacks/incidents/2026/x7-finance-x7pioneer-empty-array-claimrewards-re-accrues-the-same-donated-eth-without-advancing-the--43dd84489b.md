# Crypto Training Exploit Pattern Stub: X7 Finance (X7Pioneer) — empty-array claimRewards([]) re-accrues the same donated ETH without advancing the watermark, inflating the per-token reward until one NFT drains the whole pool

Source:
- https://crypto.training/hacks/2026-10-x7finance/

Imported:
- 2026-11-07

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2026

Chain:
- Ethereum

Loss / impact summary:
- unknown

Tags:
- logic/missing-state-update, logic/incorrect-order-of-operations, defi/reward-accounting

Dedupe:
- id: `2026-10-x7finance`
- fingerprint: `43dd84489bd5cd4c7e05e23dde4bdb80dd57db84e0eb62a02aff982e8b1f7d6d`

Core exploit idea:
- X7Pioneer is an airdropped ERC-721 whose holders share any ETH sent to the contract. claimRewards(uint256[]) first accrues address(this).balance - lastETHBalance into to…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
