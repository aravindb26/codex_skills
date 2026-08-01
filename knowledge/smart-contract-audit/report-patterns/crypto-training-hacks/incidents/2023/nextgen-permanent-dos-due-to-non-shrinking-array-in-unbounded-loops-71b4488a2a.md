# Crypto Training Exploit Pattern Stub: NextGen — Permanent DoS due to non-shrinking array in unbounded loops

Source:
- https://crypto.training/hacks/29526-h-05-permanent-dos-due-to-non-shrinking-array-usage-in-an-un/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `29526-h-05-permanent-dos-due-to-non-shrinking-array-usage-in-an-un`
- fingerprint: `71b4488a2a19723f842b5439ff5c61ac993c06fa6e18c7a1d0e15f519eb3621c`

Core exploit idea:
- participateToAuction only pushes bids; arrays never shrink. returnHighestBid / claimAuction iterate the full array. Enough dust bids make claim OOG → permanent auction D…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
