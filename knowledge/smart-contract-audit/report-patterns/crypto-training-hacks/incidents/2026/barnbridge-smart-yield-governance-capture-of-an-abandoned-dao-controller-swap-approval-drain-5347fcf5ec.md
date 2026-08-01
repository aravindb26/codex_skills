# Crypto Training Exploit Pattern Stub: BarnBridge SMART Yield — Governance Capture of an Abandoned DAO → Controller Swap → Approval Drain

Source:
- https://crypto.training/hacks/2026-07-CompoundProvider/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2026

Chain:
- Ethereum

Loss / impact summary:
- 776,575.547933 USDC (drain #1 774,943.379409 + drain #2 1,632.168524)

Tags:
- governance/quorum-manipulation, governance/vote-weight-vs-quorum-asymmetry, access-control/live-admin-power-on-dormant-protocol, logic/leftover-approvals

Dedupe:
- id: `2026-07-CompoundProvider`
- fingerprint: `5347fcf5ec4c5086cd05b0be2bfc56797dfc6d25d586e8c68beee9e6105036c8`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
