# Crypto Training Exploit Pattern Stub: Hardcoded useEth flag traps pool withdrawals — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/62490-h-9-hardcoded-useeth-true-in-remove-liquidity-one-coin-or-re/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/incorrect-state-transition, input-validation/missing

Dedupe:
- id: `62490-h-9-hardcoded-useeth-true-in-remove-liquidity-one-coin-or-re`
- fingerprint: `64ba95de96e8e607e2bae10ad7a38d15482b3dffa8963c83b2423af056bcf76a`

Core exploit idea:
- This bug report is about a problem found by two users, elolpuer and xiaoming90, in a code repository on GitHub. The bug affects a feature called Curve V2 pool, which is…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
