# Crypto Training Exploit Pattern Stub: Zentra Finance — Custom AToken `_burnScaled` silently caps oversize burns

Source:
- https://crypto.training/hacks/2026-09-zentrafinance/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Citrea

Loss / impact summary:
- ~$140,000 ctUSD. PoC extracts 139,999.999999 ctUSD; zctUSD vault 147,152.479895 → 7,152.4…

Tags:
- logic/missing-check, logic/incorrect-state-transition, input-validation/boundary, arithmetic/rounding

Dedupe:
- id: `2026-09-zentrafinance`
- fingerprint: `7a547aa0240a240f6b95b1bb55ff4a60e8078963b24baeb30d72df7db7bb9cb8`

Core exploit idea:
- Zentra Finance is an Aave v3 fork on Citrea. Its zTokens do not run the AToken implementation listed in the docs (0xe4f00a8e…, revision 0x1). They run 0x62Ff719a…, revis…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
