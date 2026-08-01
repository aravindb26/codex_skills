# Crypto Training Exploit Pattern Stub: Collective (Revolution Protocol) — malicious delegatees can permanently block delegators from redelegating or transferring their NFTs

Source:
- https://crypto.training/hacks/30091-h-04-malicious-delegatees-can-block-delegators-from-redelega/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-condition, governance/vote-delegation-loop, dos/permanent-freeze

Dedupe:
- id: `30091-h-04-malicious-delegatees-can-block-delegators-from-redelega`
- fingerprint: `6607021a0c13d47de3a6f8a96c5ff1d7946e4dadebba52080fac91056ddaf629`

Core exploit idea:
- 1. OpenZeppelin's original Votes.delegates(account) returns $._delegatee[account] verbatim — including address(0) when the account never delegated. 2. Revolution Protoco…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
