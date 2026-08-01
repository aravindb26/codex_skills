# Crypto Training Exploit Pattern Stub: Parity WalletLibrary `kill` — Uninitialized Shared Library Self-Destruct (the "devops199" freeze)

Source:
- https://crypto.training/hacks/2017-11-Parity_kill/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2017

Chain:
- Ethereum

Loss / impact summary:
- 513,774.16 ETH permanently frozen across ~587 Parity multisig wallets (≈ $150–300M at the…

Tags:
- access-control/uninitialized-proxy, access-control/missing-modifier

Dedupe:
- id: `2017-11-Parity_kill`
- fingerprint: `6e10dae5c74055bbf5cad315ba4c4bc7ca98d99c7fe523ed5a8457991a9284e3`

Core exploit idea:
- Parity's multisig wallets were thin proxies: each user's Wallet held only state and forwarded every call via delegatecall into one shared, singleton WalletLibrary deploy…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
