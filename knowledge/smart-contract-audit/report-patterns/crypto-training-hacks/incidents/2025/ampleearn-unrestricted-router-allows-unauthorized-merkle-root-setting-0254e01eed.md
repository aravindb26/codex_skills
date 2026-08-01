# Crypto Training Exploit Pattern Stub: AmpleEarn — unrestricted router allows unauthorized merkle root setting

Source:
- https://crypto.training/hacks/64041-c-01-unrestricted-router-allows-unauthorized-merkle-root-set/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `64041-c-01-unrestricted-router-allows-unauthorized-merkle-root-set`
- fingerprint: `0254e01eed777d6f309bfc5de4f09ac2324b0cb46b70ac461568432d9359f12a`

Core exploit idea:
- Router batchSetMerkleRootsStrict has no auth; vault setMerkleRoots authorizes msg.sender, which is the router when not routed through EVC

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
