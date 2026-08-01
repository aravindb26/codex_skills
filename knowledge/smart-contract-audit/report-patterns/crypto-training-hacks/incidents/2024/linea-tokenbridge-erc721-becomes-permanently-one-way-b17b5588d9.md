# Crypto Training Exploit Pattern Stub: Linea TokenBridge — ERC721 becomes permanently one-way

Source:
- https://crypto.training/hacks/33298-tokenbridgebridgetoken-allows-1-way-erc721-bridging-causing/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2024

Chain:
- zkSync

Loss / impact summary:
- unknown

Tags:
- bridge/missing-validation, dos/frozen-funds

Dedupe:
- id: `33298-tokenbridgebridgetoken-allows-1-way-erc721-bridging-causing`
- fingerprint: `b17b5588d91787daade2bc3733bd94bd1d69c4ae81bc82fa2d97f296a80dde1d`

Core exploit idea:
- The ERC20 bridge accepts an ERC721 because both expose a transferFrom-shaped call. The NFT is locked and represented as one fungible unit, but the return flow cannot rel…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
