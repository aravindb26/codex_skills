# Crypto Training Exploit Pattern Stub: DoinGud `acceptOffer` pays the escrow twice — `amount == 0` skips offer deletion

Source:
- https://crypto.training/hacks/2026-09-doingud/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Polygon

Loss / impact summary:
- 35,380.154566 USDC net output.txt:591. Two payouts of 35,486.935717 minus the 35,593.7168…

Tags:
- logic/incorrect-state-transition, logic/missing-check, logic/wrong-condition

Dedupe:
- id: `2026-09-doingud`
- fingerprint: `b491ab3f9b76896a0836494a74ab5c16ac60d2ffe8e0569d67153f7948f46f72`

Core exploit idea:
- DoinGud's Polygon marketplace is an EIP-2535 diamond. The escrow USDC sits on the diamond 0xE3A161…eD6A. The bidding logic lives in an unverified facet 0x123aAFC8…, whic…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
