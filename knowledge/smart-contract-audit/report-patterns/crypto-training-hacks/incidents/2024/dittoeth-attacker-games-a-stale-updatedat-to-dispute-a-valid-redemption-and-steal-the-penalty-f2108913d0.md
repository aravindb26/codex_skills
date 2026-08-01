# Crypto Training Exploit Pattern Stub: DittoETH — attacker games a stale `updatedAt` to dispute a valid redemption and steal the penalty

Source:
- https://crypto.training/hacks/34177-h-07-valid-redemption-proposals-can-be-disputed-by-decreasin/

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
- loss-of-funds/direct-drain, logic/missing-state-update, access-control/timing-manipulation

Dedupe:
- id: `34177-h-07-valid-redemption-proposals-can-be-disputed-by-decreasin`
- fingerprint: `f2108913d0ec2374137f33783b83dfe779469665853c4322cdced04ab7a59f21`

Core exploit idea:
- 1. disputeRedemption only trusts a disputer's Short Record as evidence that a redeemer's proposal wrongly skipped a lower-CR candidate if that Short Record's updatedAt i…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
