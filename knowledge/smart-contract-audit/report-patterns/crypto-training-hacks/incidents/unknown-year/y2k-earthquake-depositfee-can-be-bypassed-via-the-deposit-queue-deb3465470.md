# Crypto Training Exploit Pattern Stub: Y2K Earthquake — `depositFee` can be bypassed via the deposit queue

Source:
- https://crypto.training/hacks/18535-h-3-depositfee-can-be-bypassed-via-deposit-queue-sherlock-no/

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
- logic/fee-calculation, defi/fee-theft

Dedupe:
- id: `18535-h-3-depositfee-can-be-bypassed-via-deposit-queue-sherlock-no`
- fingerprint: `deb3465470bd32896537fd4fa5f76bb7678801f5e7421258b5b5d4c95dafe230`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
