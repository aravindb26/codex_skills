# Crypto Training Exploit Pattern Stub: Base Unverified Arbitrary CALL — Allowance Drain via 0x42be3129

Source:
- https://crypto.training/hacks/2026-08-baseunverifiedarbitrarycall_a317/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Base

Loss / impact summary:
- ~16.623 WETH (~$31k, SlowMist TI)

Tags:
- access-control/missing-auth, dependency/unsafe-external-call, logic/missing-validation

Dedupe:
- id: `2026-08-baseunverifiedarbitrarycall_a317`
- fingerprint: `f4375a27e6912f81ba942c2743bde8da1a7e620c0f557f01c60db469ae276a0d`

Core exploit idea:
- 1. An unverified Base contract holds a privileged pattern: a public function that performs a low-level CALL to an arbitrary target with attacker-controlled calldata (Slo…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
