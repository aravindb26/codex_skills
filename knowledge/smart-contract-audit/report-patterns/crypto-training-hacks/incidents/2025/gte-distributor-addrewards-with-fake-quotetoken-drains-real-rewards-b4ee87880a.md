# Crypto Training Exploit Pattern Stub: GTE — Distributor addRewards with fake quoteToken drains real rewards

Source:
- https://crypto.training/hacks/64854-h-06-donations-to-distributor-with-arbitrary-quotetoken-can/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `64854-h-06-donations-to-distributor-with-arbitrary-quotetoken-can`
- fingerprint: `b4ee87880a78ae2e58d268395c834450816a5ccf2c0df08945388d0e5de86f5c`

Core exploit idea:
- 1. addRewards(launch, fake, 0, amount) accepts any token1. 2. Fake transferFrom succeeds; pendingQuoteRewards inflates. 3. Claims pay the registered real quote token. 4.…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
