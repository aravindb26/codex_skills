# Crypto Training Exploit Pattern Stub: Majority Protocol — multi assertResults causes bond loss for all but first

Source:
- https://crypto.training/hacks/65379-if-multiple-users-call-defaultsessionassertresults-all-but-t/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2026

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `65379-if-multiple-users-call-defaultsessionassertresults-all-but-t`
- fingerprint: `9684a6e4a436b9bb91b086510d4d27507e62d65e01918d58b68cc6585d71c622`

Core exploit idea:
- assertResults is permissionless and accepts multiple bonds for the same sessionId. The first successful recordResults fills winners[sessionId]; the second reverts Winner…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
