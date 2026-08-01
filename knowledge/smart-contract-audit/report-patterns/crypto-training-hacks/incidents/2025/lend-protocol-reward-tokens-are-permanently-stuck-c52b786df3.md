# Crypto Training Exploit Pattern Stub: LEND — Protocol reward tokens are permanently stuck

Source:
- https://crypto.training/hacks/58371-lend-protocol-reward-tokens-are-permanently-stuck/

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
- dos/frozen-funds, logic/missing-check

Dedupe:
- id: `58371-lend-protocol-reward-tokens-are-permanently-stuck`
- fingerprint: `c52b786df3a148d1c6aa239a6ce3ffc8873f4c7913571e1712e440f15ee9bb70`

Core exploit idea:
- The protocol accrues rewards but has no reachable sweep/claim path for the reserve account, permanently locking the tokens.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
