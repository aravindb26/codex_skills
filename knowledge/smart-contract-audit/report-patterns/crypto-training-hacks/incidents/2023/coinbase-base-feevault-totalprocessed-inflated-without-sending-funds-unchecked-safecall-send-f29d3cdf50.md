# Crypto Training Exploit Pattern Stub: Coinbase/Base FeeVault — `totalProcessed` inflated without sending funds (unchecked `SafeCall.send`)

Source:
- https://crypto.training/hacks/54655-vault-s-totalprocessed-count-can-be-inaccurately-increased-b/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2023

Chain:
- Optimism

Loss / impact summary:
- unknown

Tags:
- dependency/unchecked-return-value, dos/unbounded-loop, accounting/integrity

Dedupe:
- id: `54655-vault-s-totalprocessed-count-can-be-inaccurately-increased-b`
- fingerprint: `f29d3cdf50597124131b687ae45482fc0edc16df47f1a733630afd5ccec8d472`

Core exploit idea:
- 1. FeeVault.withdraw() does totalProcessed += value before attempting the outbound transfer. 2. It transfers via SafeCall.send(RECIPIENT, gasleft(), value), which perfor…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
