# Code4rena Pattern Stub: _calculateRewards() in PirexGmx don’t handle reward calculation properly, and it would revert when totalSupply() is zero which will cause claimRewards() to revert if one of 4 rewardTracker’s totalSupply was zero

Source:
- https://code4rena.com/reports/2022-11-redactedcartel#m-10-_calculaterewards-in-pirexgmx-dont-handle-reward-calculation-properly-and-it-would-revert-when-totalsupply-is-zero-which-will-cause-claimrewards-to-revert-if-one-of-4-rewardtrackers-totalsupply-was-zero

Imported:
- 2026-08-19

Status:
- needs distillation

Severity:
- MEDIUM

Report:
- Redacted Cartel contest

Report date:
- 2023-01-27

Source platform:
- Code4rena

Dedupe:
- id: `2022-11-redactedcartel#m-10-_calculaterewards-in-pirexgmx-dont-handle-reward-calculation-properly-and-it-would-revert-when-totalsupply-is-zero-which-will-cause-claimrewards-to-revert-if-one-of-4-rewardtrackers-totalsupply-was-zero`
- fingerprint: `7c253ed1a239ce7bc718069170d3be3531c11b8e5480b025ff4651eb8b1608a5`

Core idea:
- TODO: Distill the reusable attack pattern from the source.

Broken invariant:
- TODO

Where to look in code:
- TODO

Attack path:
1. TODO

False-positive checks:
- TODO

PoC shape:
- TODO

Triage notes:
- TODO
