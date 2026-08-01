# Crypto Training Exploit Pattern Stub: LEND — Repeated claims of the same rewards drain LEND reserves

Source:
- https://crypto.training/hacks/58370-lend-repeated-claims-of-the-same-rewards-drain-lend-reserves/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/reward-calculation, logic/state-update

Dedupe:
- id: `58370-lend-repeated-claims-of-the-same-rewards-drain-lend-reserves`
- fingerprint: `7ffd1d35f3b9112b626446172f31e5377a7295322672f938a7910e2f57c6734c`

Core exploit idea:
- claimLend() transfers the reward but fails to mark the epoch as claimed, allowing the same reward to be collected repeatedly.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
