# Crypto Training Exploit Pattern Stub: Etherspot CredibleAccountModule — session owner can consume a sibling session

Source:
- https://crypto.training/hacks/62848-h-01-sessionkey-owner-impersonate-session-key-owner/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-owner-check, auth/signature-validation

Dedupe:
- id: `62848-h-01-sessionkey-owner-impersonate-session-key-owner`
- fingerprint: `a1b5508c5fb92e390bcf63d4a4436d14dafbbd6f650e2b638a83f02e3f1b06f4`

Core exploit idea:
- The module verifies that a signer belongs to the smart wallet but never checks that the session named in claim() is the same signer. One active session key can therefore…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
