# Crypto Training Exploit Pattern Stub: Megapot — Attacker can steal JackpotTicketNFTs from JackpotBridgeManager

Source:
- https://crypto.training/hacks/64140-h-01-attacker-can-steal-jackpotticketnfts-from-jackpotbridge/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `64140-h-01-attacker-can-steal-jackpotticketnfts-from-jackpotbridge`
- fingerprint: `08f780b2682f4c61cf38f0ad3e8bc83d3858d91fd80f991c54d3d6330a4a0fe9`

Core exploit idea:
- _bridgeFunds calls _bridgeDetails.to with attacker-supplied calldata after optionally approving USDC. Pointing to at the ticket NFT and data at safeTransferFrom(bridge →…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
