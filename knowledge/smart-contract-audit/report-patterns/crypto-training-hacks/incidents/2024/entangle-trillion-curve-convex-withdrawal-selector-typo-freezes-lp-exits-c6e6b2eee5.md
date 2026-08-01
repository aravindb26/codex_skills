# Crypto Training Exploit Pattern Stub: Entangle Trillion — Curve/Convex withdrawal selector typo freezes LP exits

Source:
- https://crypto.training/hacks/51369-withdrawals-are-blocked-due-to-wrong-function-name-on-the-cu/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dependency/unsafe-external-call, logic/missing-validation, dos/frozen-funds

Dedupe:
- id: `51369-withdrawals-are-blocked-due-to-wrong-function-name-on-the-cu`
- fingerprint: `c6e6b2eee5436bde903b55b4336eddab61111609c933f3f52b1b634fd31cbfc9`

Core exploit idea:
- The CurveCompoundConvexSynthChef integration calls convex.witdraw rather than Convex withdraw. The selector does not exist on the target contract, so a legitimate LP wit…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
