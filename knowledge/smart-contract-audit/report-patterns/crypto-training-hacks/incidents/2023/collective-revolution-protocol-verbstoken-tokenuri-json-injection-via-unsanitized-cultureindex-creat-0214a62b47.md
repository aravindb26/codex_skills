# Crypto Training Exploit Pattern Stub: Collective (Revolution Protocol) — `VerbsToken.tokenURI()` JSON injection via unsanitized `CultureIndex.createPiece()` metadata

Source:
- https://crypto.training/hacks/30090-h-03-verbstokentokenuri-is-vulnerable-to-json-injection-atta/

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
- injection/json-injection, logic/wrong-condition, nft/metadata-mutability

Dedupe:
- id: `30090-h-03-verbstokentokenuri-is-vulnerable-to-json-injection-atta`
- fingerprint: `0214a62b47c2e52fd0b3e37accd295beba5cb8b3eee1491b36b4b5e4caf03f4f`

Core exploit idea:
- 1. CultureIndex.createPiece() stores an art piece's ArtPieceMetadata — including image and animationUrl — verbatim, with no check for JSON-breaking characters (", :, ,).…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
