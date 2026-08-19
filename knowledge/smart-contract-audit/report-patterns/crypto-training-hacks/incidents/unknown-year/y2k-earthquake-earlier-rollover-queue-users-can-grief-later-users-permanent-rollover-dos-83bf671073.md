# Crypto Training Exploit Pattern Stub: Y2K Earthquake — earlier rollover-queue users can grief later users (permanent rollover DoS)

Source:
- https://crypto.training/hacks/18534-h-2-earlier-users-in-rollover-queue-can-grief-later-users-sh/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 1970

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dos/griefing, logic/state-desync

Dedupe:
- id: `18534-h-2-earlier-users-in-rollover-queue-can-grief-later-users-sh`
- fingerprint: `83bf671073b4da1450a05845ef317984ddf4df3250d90421850effd4abf59631`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
