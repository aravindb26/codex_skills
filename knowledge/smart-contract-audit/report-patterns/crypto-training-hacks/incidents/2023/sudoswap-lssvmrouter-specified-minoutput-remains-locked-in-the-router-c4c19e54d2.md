# Crypto Training Exploit Pattern Stub: Sudoswap LSSVMRouter — specified `minOutput` remains locked in the router

Source:
- https://crypto.training/hacks/18411-specified-minoutput-will-remain-locked-in-lssvmrouterswapnft/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dos/frozen-funds, logic/refund-miscalculation

Dedupe:
- id: `18411-specified-minoutput-will-remain-locked-in-lssvmrouterswapnft`
- fingerprint: `c4c19e54d2bd5ec17bdc6b8fc844a0976cf25f14c27d3849f6021ba61f55ca8b`

Core exploit idea:
- 1. swapNFTsForSpecificNFTsThroughETH sells the user's NFTs for ETH, then uses that ETH (plus msg.value) to buy the specific NFTs the user wants. 2. For the ETH→NFT half…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
