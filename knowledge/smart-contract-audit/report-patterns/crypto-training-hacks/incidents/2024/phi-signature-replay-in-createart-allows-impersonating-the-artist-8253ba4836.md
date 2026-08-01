# Crypto Training Exploit Pattern Stub: Phi — signature replay in `createArt` allows impersonating the artist

Source:
- https://crypto.training/hacks/41088-h-02-signature-replay-in-createart-allows-to-impersonate-art/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- signature/unbound-parameters, access-control/frontrunning, logic/silent-duplicate-success

Dedupe:
- id: `41088-h-02-signature-replay-in-createart-allows-to-impersonate-art`
- fingerprint: `8253ba48366a88863211cb58c9c8f1ae4dd8a178367d32ed7e47ce35670a546e`

Core exploit idea:
- 1. PhiFactory.createArt(signedData_, signature_, config_) verifies a signature over (expiresIn_, uri_, credHash_) only — the CreateConfig (artist/receiver/royaltyBPS) is…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
