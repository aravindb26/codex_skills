# Crypto Training Exploit Pattern Stub: Phi — Forced endTime extension in updateArtSettings allows attacker to mint

Source:
- https://crypto.training/hacks/41090-h-04-forced-endtime-extension-in-updateartsettings-allows-at/

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
- timing/forced-window-reopen, nft/unauthorized-mint

Dedupe:
- id: `41090-h-04-forced-endtime-extension-in-updateartsettings-allows-at`
- fingerprint: `b3ee9c4056b6758d6396d93d52509ba5a0228cf056d4bb98487bba751cb45934`

Core exploit idea:
- After a mint event ends, updateArtSettings forces endTime_ >= now, reopening minting so an attacker can snipe residual maxSupply and dilute holders

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
