# Crypto Training Exploit Pattern Stub: BOB Staking — Delegating to address(0) empties contract via alterGovernanceDelegatee

Source:
- https://crypto.training/hacks/63720-h-02-delegating-to-address0-empties-contract-via-altergovern/

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
- logic/missing-check

Dedupe:
- id: `63720-h-02-delegating-to-address0-empties-contract-via-altergovern`
- fingerprint: `1ddac50bcbc597ffa41eb96e26f7e5a8e9fdfd96059f9b6d4aaed6eb12d6cf38`

Core exploit idea:
- 1. First non-zero delegation moves the staker's tokens contract → surrogate. 2. Setting delegatee to address(0) is allowed; tokens move to a zero surrogate. 3. Re-delega…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
