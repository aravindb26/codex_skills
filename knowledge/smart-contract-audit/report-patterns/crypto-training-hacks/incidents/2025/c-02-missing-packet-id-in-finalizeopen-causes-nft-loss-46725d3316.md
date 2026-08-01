# Crypto Training Exploit Pattern Stub: C-02: Missing packet ID in finalizeOpen causes NFT loss

Source:
- https://crypto.training/hacks/62593-c-02-missing-packet-id-in-finalizeopen-causes-nft-loss-pasho/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `62593-c-02-missing-packet-id-in-finalizeopen-causes-nft-loss-pasho`
- fingerprint: `46725d3316a943fcf9678a62a3e818a3e90875eed19997c10e6cb693acc957c2`

Core exploit idea:
- Packet NFT stuck in contract; INSTANT_OPEN reverts; user loses NFT with no cards

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
