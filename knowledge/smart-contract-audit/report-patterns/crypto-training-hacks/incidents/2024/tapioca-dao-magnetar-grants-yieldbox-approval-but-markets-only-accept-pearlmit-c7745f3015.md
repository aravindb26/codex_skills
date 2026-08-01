# Crypto Training Exploit Pattern Stub: Tapioca DAO — Magnetar grants YieldBox approval but markets only accept pearlmit

Source:
- https://crypto.training/hacks/32315-h-04-incorrect-approval-mechanism-breaks-all-magnetar-functi/

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
- unknown

Dedupe:
- id: `32315-h-04-incorrect-approval-mechanism-breaks-all-magnetar-functi`
- fingerprint: `c7745f301589f990b8c4db979feb0bc190b743e55a2a6f22a54187417f072e8f`

Core exploit idea:
- Magnetar grants YieldBox approval but markets only accept pearlmit. Harm demonstrated: Magnetar deposit/lend permanently fails — wrong approval mechanism vs pearlmit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
