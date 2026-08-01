# Crypto Training Exploit Pattern Stub: Streaming — arbitraryCall lets compromised gov drain user allowances

Source:
- https://crypto.training/hacks/42395-h-04-improper-implementation-of-arbitrarycall-allows-protoco/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2021

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/dangerous-call, approval/leftover-allowance

Dedupe:
- id: `42395-h-04-improper-implementation-of-arbitrarycall-allows-protoco`
- fingerprint: `b0a14bcf2d409695d46cac974a64829687f6f6e25319cf0e75d6d3e69805889d`

Core exploit idea:
- After an incentive is claimed, incentives[token]==0 so compromised governance can arbitraryCall the token with transferFrom and steal leftover allowances

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
