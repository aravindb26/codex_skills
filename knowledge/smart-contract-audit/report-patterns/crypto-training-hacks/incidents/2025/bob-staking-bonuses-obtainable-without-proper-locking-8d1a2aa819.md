# Crypto Training Exploit Pattern Stub: BOB Staking — Bonuses obtainable without proper locking

Source:
- https://crypto.training/hacks/63719-h-01-bonuses-obtainable-without-proper-locking-due-to-flawed/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-condition

Dedupe:
- id: `63719-h-01-bonuses-obtainable-without-proper-locking-due-to-flawed`
- fingerprint: `8d1a2aa819e2a73ec9eef4d30e0702606b8cc9ee6cd864f6a9a9f94d2eda4ce2`

Core exploit idea:
- 1. First stake with lockPeriod = 0 sets unlockTimestamp = now and stores lockPeriod = 0. 2. Second stake with a long lock period still passes the consistency check (guar…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
