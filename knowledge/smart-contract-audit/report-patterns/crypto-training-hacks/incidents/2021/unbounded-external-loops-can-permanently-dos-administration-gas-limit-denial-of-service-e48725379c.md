# Crypto Training Exploit Pattern Stub: Unbounded external loops can permanently DoS administration — gas-limit denial of service

Source:
- https://crypto.training/hacks/18211-external-calls-in-loop-can-lead-to-denial-of-service-trailof/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2021

Chain:
- Ethereum

Loss / impact summary:
- Asset approval/liquidation administration becomes uncallable

Tags:
- dos/unbounded-loop, dependency/unsafe-external-call

Dedupe:
- id: `18211-external-calls-in-loop-can-lead-to-denial-of-service-trailof`
- fingerprint: `e48725379cf5e998e3cf3ca4b8a7b8c0bf59e5367db76e077c91f5646845001d`

Core exploit idea:
- An ever-growing assetsMapped array is traversed with external approvals. One paused/reverting token traps the whole operation; in production, array growth alone can exce…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
