# Crypto Training Exploit Pattern Stub: Revolution / Collective — art-piece quorum inflated by auctioned ERC721 voting power

Source:
- https://crypto.training/hacks/30089-h-02-artpiecetotalvotessupply-and-artpiecequorumvotes-are-in/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- governance/quorum-manipulation, arithmetic/precision-loss

Dedupe:
- id: `30089-h-02-artpiecetotalvotessupply-and-artpiecequorumvotes-are-in`
- fingerprint: `ed5c32e63c6742aa0edb3eb41c2901421de2bacb256b1849e585475301b25772`

Core exploit idea:
- 1. createPiece sets totalVotesSupply from erc20.totalSupply() + weighted erc721.totalSupply(). 2. The ERC721 currently held by AuctionHouse is included but cannot vote f…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
