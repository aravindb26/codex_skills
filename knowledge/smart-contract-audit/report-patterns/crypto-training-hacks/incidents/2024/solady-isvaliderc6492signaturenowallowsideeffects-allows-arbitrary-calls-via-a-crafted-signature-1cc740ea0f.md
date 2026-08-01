# Crypto Training Exploit Pattern Stub: Solady — `isValidERC6492SignatureNowAllowSideEffects` allows arbitrary calls via a crafted signature

Source:
- https://crypto.training/hacks/45407-isvaliderc6492signaturenowallowsideeffects-allows-arbitrary/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/signature-validation, logic/arbitrary-external-call, loss-of-funds/direct-drain

Dedupe:
- id: `45407-isvaliderc6492signaturenowallowsideeffects-allows-arbitrary`
- fingerprint: `1cc740ea0fc09f65be916ab1a5dcdd153364a21094488de468661df9485a8d52`

Core exploit idea:
- 1. ERC-6492 lets a signature be postfixed with a magic suffix so a verifier can "prepare" (deploy) a smart-account signer before doing the ERC-1271 check. 2. Solady's Al…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
