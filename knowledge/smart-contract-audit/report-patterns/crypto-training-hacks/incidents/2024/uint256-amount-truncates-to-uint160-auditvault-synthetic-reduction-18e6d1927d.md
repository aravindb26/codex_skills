# Crypto Training Exploit Pattern Stub: uint256 amount truncates to uint160 — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/44371-h-1-unsafe-type-casting-in-token-amount-handling-sherlock-ok/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- input-validation/wrong-type, arithmetic/underflow

Dedupe:
- id: `44371-h-1-unsafe-type-casting-in-token-amount-handling-sherlock-ok`
- fingerprint: `18e6d1927d1984895e33d49b10477ef966ac37f0dc8ec9a6116d548ff1ab77cc`

Core exploit idea:
- This bug report discusses an issue found in the rotocol's handling of token amounts. The contracts use unsafe type casting from uint256 to uint160, which can lead to sil…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
