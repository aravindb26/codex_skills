# Crypto Training Exploit Pattern Stub: Audius Governance Takeover — Re-callable `initialize()` on Live Proxies via Storage-Slot Collision

Source:
- https://crypto.training/hacks/2022-07-Audius/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2022

Chain:
- Ethereum

Loss / impact summary:
- 704.18 ETH (~$1,080,000) — 18,564,497.82 AUDIO drained from the Governance treasury and d…

Tags:
- access-control/uninitialized-proxy, access-control/proxy-storage-collision

Dedupe:
- id: `2022-07-Audius`
- fingerprint: `edd4f3a0a0d8d307593b74894290caa0d3de9d6297bc50e8d4337f29714878aa`

Core exploit idea:
- Audius governance is a set of OpenZeppelin-style upgradeable proxies (AudiusAdminUpgradeabilityProxy) sitting in front of Governance, Staking, and DelegateManagerV2 logi…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
