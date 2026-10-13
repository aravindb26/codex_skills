# Crypto Training Exploit Pattern Stub: Reddio RedSonic Vault — permissionless `registerErc20(stETH)` double-counts one balance

Source:
- https://crypto.training/hacks/2026-09-reddio/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Ethereum

Loss / impact summary:
- 9.253090281137114614 ETH (~$23K; reported ~9.25 ETH) output.txt

Tags:
- logic/price-calculation, access-control/missing-auth, logic/missing-check

Dedupe:
- id: `2026-09-reddio`
- fingerprint: `0f5b6da2ce027b63181c3b6a91c7946e2492d1d2c7546ee29c7c4205cd281ab6`

Core exploit idea:
- RedSonic Vault (EIP-2535 diamond) prices rsvETH from getTotalAssetBalance, which for the Lido leg is IERC20(stETH).balanceOf(vault) — no per-share-class accounting. regi…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
