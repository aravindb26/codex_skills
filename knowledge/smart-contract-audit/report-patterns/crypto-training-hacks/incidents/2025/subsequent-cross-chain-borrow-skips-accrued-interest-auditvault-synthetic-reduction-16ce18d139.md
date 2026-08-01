# Crypto Training Exploit Pattern Stub: Subsequent cross-chain borrow skips accrued interest — AuditVault synthetic reduction

Source:
- https://crypto.training/hacks/58397-h-28-subsequent-crosschain-borrows-dont-accrue-interest-on-e/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/state-update, arithmetic/precision-loss

Dedupe:
- id: `58397-h-28-subsequent-crosschain-borrows-dont-accrue-interest-on-e`
- fingerprint: `16ce18d1397903d262d9fb9fbb389e489a49b6d51b51b938572e8cc08684734a`

Core exploit idea:
- This bug report discusses an issue that was found by a group of individuals on a platform called GitHub. The issue involves borrowing the same asset more than once on a…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
