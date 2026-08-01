# Crypto Training Exploit Pattern Stub: DittoETH — flawed `&&` check corrupts protocol-wide collateral/debt accounting

Source:
- https://crypto.training/hacks/34175-h-05-flawed-if-check-causes-inaccurate-tracking-of-the-proto/

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
- logic/wrong-boolean-operator, accounting/invariant-break, access-control/insufficient-guard

Dedupe:
- id: `34175-h-05-flawed-if-check-causes-inaccurate-tracking-of-the-proto`
- fingerprint: `00f1842e585342f87ec13ad05c27ff5a70fa1095a204e911c4a715430f253f2a`

Core exploit idea:
- 1. claimRemainingCollateral(redeemer, claimIndex, id) lets a shorter reclaim a fully-redeemed Short Record's leftover collateral, but only after the NAMED redeemer's dis…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
