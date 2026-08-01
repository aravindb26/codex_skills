# Crypto Training Exploit Pattern Stub: DeGate — arbitrary token integration can lock deposits

Source:
- https://crypto.training/hacks/17856-degate-arbitrary-token-balance-check/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- input-validation/missing, logic/state-update, dos/frozen-funds

Dedupe:
- id: `17856-degate-arbitrary-token-balance-check`
- fingerprint: `1130a26856466efc3db008d88a39fa1509218394ba20c3b2b46779e8432ccb99`

Core exploit idea:
- Any user can add a token before its special balance check is enabled. A 10% deflationary transfer credits 100 while only 90 arrives, leaving the credited withdrawal perm…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
