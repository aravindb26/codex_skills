# Crypto Training Exploit Pattern Stub: WUKONG Staking — classical reentrancy in `unstake()` drains pooled LP

Source:
- https://crypto.training/hacks/2026-03-WUKONGStaking/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2026

Chain:
- BNB Chain

Loss / impact summary:
- ~57.68 BNB (~$37.7K) on the main tx (attacker EOA net gain); a second tx drained ~$18K

Tags:
- reentrancy/single-function, logic/state-update, logic/missing-check

Dedupe:
- id: `2026-03-WUKONGStaking`
- fingerprint: `93b916910a11bec5b6a7bc3bd7fbcd8451b873613897bc01a6739dfc7161f21b`

Core exploit idea:
- StakingUpgradeableV10.unstake() returns the withdrawer's BNB with a raw payable(msg.sender).call{value: bnbReceived}("") before it closes the position (isStaking = false…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
