# Crypto Training Exploit Pattern Stub: Remora — resolveUser lock migration can be griefed to extend lock duration

Source:
- https://crypto.training/hacks/63779-migrating-the-existing-locks-for-an-investor-when-is-resolve/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dos/griefing, logic/ordering

Dedupe:
- id: `63779-migrating-the-existing-locks-for-an-investor-when-is-resolve`
- fingerprint: `3b3c79ba5bbb393c42ed23ec7ab9cf862491320cffa343d313f60c1351726f32`

Core exploit idea:
- 1. resolveUser migrates locks by appending old locks after any locks already on newAddress. 2. availableTokens stops at the first unexpired entry. 3. A frontrun transfer…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
