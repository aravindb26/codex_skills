# Crypto Training Exploit Pattern Stub: Sweep n Flip Bridge — Permanent failure to bridge wrapped ERC721

Source:
- https://crypto.training/hacks/46493-permanent-failure-to-bridge-wrapped-erc721-using-bridgesende/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dos/frozen-funds

Dedupe:
- id: `46493-permanent-failure-to-bridge-wrapped-erc721-using-bridgesende`
- fingerprint: `e4867742c83ae819d96e01fab66a5d35aa6b13539e329c304ea847019aa1cc31`

Core exploit idea:
- 1. Bridging an origin NFT locks it on the source bridge and mints a wrap on the destination. 2. Reverse-bridging the wrap must read metadata from the wrap (which exists…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
