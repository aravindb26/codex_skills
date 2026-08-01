# Crypto Training Exploit Pattern Stub: Venus Prime — stale staking timestamp permits a free revocable Prime claim

Source:
- https://crypto.training/hacks/28832-h-01-primesol-user-can-claim-prime-token-without-having-any/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/incorrect-state-transition, logic/state-update

Dedupe:
- id: `28832-h-01-primesol-user-can-claim-prime-token-without-having-any`
- fingerprint: `c88751f3af8405301770d364f1f78aae83eeaaf65b6cdd4feabc0e67cf8e0502`

Core exploit idea:
- stakedAt determines whether an account has waited long enough to claim a revocable Prime token. The irrevocable issue branch mints the token but does not clear that time…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
