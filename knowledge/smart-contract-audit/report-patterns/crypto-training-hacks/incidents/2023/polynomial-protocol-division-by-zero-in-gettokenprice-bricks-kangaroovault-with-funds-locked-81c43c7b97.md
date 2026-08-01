# Crypto Training Exploit Pattern Stub: Polynomial Protocol — division-by-zero in getTokenPrice bricks KangarooVault with funds locked

Source:
- https://crypto.training/hacks/20229-h-06-division-by-zero-error-causes-kangaroovault-to-be-dos-w/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dos/frozen-funds, logic/division-by-zero, loss-of-funds/locked-funds

Dedupe:
- id: `20229-h-06-division-by-zero-error-causes-kangaroovault-to-be-dos-w`
- fingerprint: `81c43c7b97536f8336fc890cfba750e89cd337793baa235cd8b79b6cb811e3ab`

Core exploit idea:
- 1. getTokenPrice returns totalFunds.divWadDown(totalSupply) when totalFunds != 0 and positionId == 0, with no guard for totalSupply == 0. 2. That state is reachable: aft…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
