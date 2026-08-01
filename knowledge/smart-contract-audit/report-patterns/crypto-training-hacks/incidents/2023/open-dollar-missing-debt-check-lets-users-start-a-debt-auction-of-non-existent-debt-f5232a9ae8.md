# Crypto Training Exploit Pattern Stub: Open Dollar — missing debt check lets users start a debt auction of non-existent debt

Source:
- https://crypto.training/hacks/29348-h-02-missing-debt-check-lets-users-start-a-debt-auction-of-n/

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
- logic/check-ordering, accounting/stale-precondition

Dedupe:
- id: `29348-h-02-missing-debt-check-lets-users-start-a-debt-auction-of-n`
- fingerprint: `f5232a9ae805ccfc32dad30afd2bced2fbf51d92aee9e58288bcb4dda217f8c8`

Core exploit idea:
- 1. auctionDebt() checks debtAuctionBidSize > _unqueuedUnauctionedDebt(debtBalance) using the current (pre-settle) debt balance, reverting only if there isn't enough. 2.…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
