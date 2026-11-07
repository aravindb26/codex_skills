# Solodit Pattern: External NAV donation plus share-supply collapse enables tick-share inflation

Source:
- https://solodit.cyfrin.io/issues/tick-share-inflation-attack-mixbytes-none-barterlab-markdown

Imported:
- 2026-11-07

Severity:
- HIGH

Protocol / source:
- BarterLab / MixBytes

Tags:
- share accounting, external NAV, donation, rounding, adapter

Dedupe:
- id: `75086`
- fingerprint: `ab13980b5be754fec99d93c9c1eb2c3a01144a4e452df5025a377079f2e4582a`

Core mechanism:
- A tick's share price is derived from an ERC-4626-like adapter whose NAV includes externally held pool positions. A donation or direct balance change moves NAV without minting corresponding tick shares; a provider can then withdraw most shares and leave a tiny supply. Subsequent deposits encounter extreme conversion rounding and can capture value from existing positions.

Invariant and audit checks:
- Share pricing must remain manipulation-resistant when external NAV changes independently of local share supply, especially immediately after large withdrawals.
- Trace `totalAssets`/NAV sources (including aToken or lending-pool balances), who can donate or alter them, share mint/burn rounding, and whether minimum liquidity/virtual offsets/reconciliation protect post-withdrawal low-supply states.

False-positive checks:
- Distinguish ordinary ERC-4626 donation inflation from this specific shared-adapter/supply-collapse path. Prove the attacker can control the external NAV and leave the affected tick at low supply without losing more than the value extracted.

PoC shape:
1. Seed a tick/provider position and manipulate externally counted NAV.
2. Withdraw most shares while preserving a tiny share supply.
3. Deposit from a second account and compare minted shares/assets with an unmanipulated baseline.

Triage notes:
- Quantify net extractable value after the attacker's donation and withdrawal costs; tiny rounding shifts are not enough.
