# Crypto Training Exploit Pattern Stub: Alchemix — newly created gauge may miss out on its rewards

Source:
- https://crypto.training/hacks/38182-newly-created-gauge-may-missed-out-on-its-rewards-immunefi-a/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/stale-memory-variable, timing/read-before-write, liveness/delayed-reward

Dedupe:
- id: `38182-newly-created-gauge-may-missed-out-on-its-rewards-immunefi-a`
- fingerprint: `80c5df63b3b050d8e874925ff460d564fda098f44c572f38dc2a67d21d406cdc`

Core exploit idea:
- 1. Voter._distribute(gauge) starts by reading _claimable = claimable[gauge] into memory, then resets claimable[gauge] to 0, THEN calls _updateFor(gauge) — the function t…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
