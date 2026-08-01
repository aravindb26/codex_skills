# Crypto Training Exploit Pattern Stub: Amphor — claim functions don't validate if the epoch is settled

Source:
- https://crypto.training/hacks/30916-h-1-claim-functions-dont-validate-if-the-epoch-is-settled-sh/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/missing-state-check, access-control/missing-caller-check, loss-of-funds/griefing

Dedupe:
- id: `30916-h-1-claim-functions-dont-validate-if-the-epoch-is-settled-sh`
- fingerprint: `566f2b1301cceea052f01ceb5ba2d4db437adb3c3862763547aa738f74387486`

Core exploit idea:
- 1. When the vault is closed, users call requestDeposit() to queue an amount of assets against the current epoch (epochId). Nothing is convertible to shares until the own…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
