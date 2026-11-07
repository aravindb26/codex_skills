# Crypto Training Exploit Pattern Stub: Slice FundsModule — Unbacked Release From a Caller-Chosen Source

Source:
- https://crypto.training/hacks/2026-10-slicefundsmodule/

Imported:
- 2026-11-07

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2026

Chain:
- Base

Loss / impact summary:
- 8.716935563284127413 ETH and 19,820.734001 USDC to the exploit contract (output.txt:6–out…

Tags:
- access-control/missing-auth, logic/missing-validation, dependency/unsafe-external-call

Dedupe:
- id: `2026-10-slicefundsmodule`
- fingerprint: `5ee71b94f217dafce4ae7cbb3ee23dfe8e257ed552ce92727b50f405deee5cc9`

Core exploit idea:
- Slice’s FundsModule is the settlement contract for Slice stores. One permissionless entry point takes a list of source contracts, a recipient, a token (address(0) means…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
