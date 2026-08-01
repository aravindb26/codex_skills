# Crypto Training Exploit Pattern Stub: Next Generation — Cross-chain signature replay via user-supplied domainSeparator

Source:
- https://crypto.training/hacks/56703-h-01-cross-chain-signature-replay-attack-due-to-user-supplie/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `56703-h-01-cross-chain-signature-replay-attack-due-to-user-supplie`
- fingerprint: `b076d05446b73325a9d1383eb23dd86b818356ec9774d23022738c3c183ae805`

Core exploit idea:
- _verifySig takes domainSeparator from the caller. Two chain deployments both accept the same domain label; independent nonces allow draining EURF on each chain under tha…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
