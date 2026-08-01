# Crypto Training Exploit Pattern Stub: Maia DAO — Adversary can poison depositNonce via retrieveDeposit and lock user deposits

Source:
- https://crypto.training/hacks/26042-h-08-due-to-inadequate-checks-an-adversary-can-call-branchbr/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `26042-h-08-due-to-inadequate-checks-an-adversary-can-call-branchbr`
- fingerprint: `23f931fc0b2e8cdeb7f32e1b03963d0299422f748b3eddba4d0d8fc3ed38592f`

Core exploit idea:
- 1. Attacker calls retrieveDeposit(60) with no ownership check.\n2. Root marks nonce 60 executed.\n3. User deposit with nonce 60 is rejected on root; tokens locked on bra…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
