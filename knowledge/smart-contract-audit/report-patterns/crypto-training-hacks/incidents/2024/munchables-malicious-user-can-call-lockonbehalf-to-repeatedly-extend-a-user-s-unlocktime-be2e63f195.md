# Crypto Training Exploit Pattern Stub: Munchables — Malicious user can call lockOnBehalf to repeatedly extend a user's unlockTime

Source:
- https://crypto.training/hacks/33594-h-01-malicious-user-can-call-lockonbehalf-repeatedly-extend/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-authorization, dos/griefing, loss-of-funds/locked-funds

Dedupe:
- id: `33594-h-01-malicious-user-can-call-lockonbehalf-repeatedly-extend`
- fingerprint: `be2e63f195ebfe85b9277a5c3755ccc4ea6ac20b7c4d106e790fa4fe51e22cf6`

Core exploit idea:
- 1. LockManager.lockOnBehalf(tokenContract, quantity, onBehalfOf) lets any caller donate tokens "on behalf of" any other address — with no access control and no minimum q…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
