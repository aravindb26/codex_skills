# Crypto Training Exploit Pattern Stub: Rio Network — malicious operators can `undelegate` theirselves to manipulate the LRT exchange rate

Source:
- https://crypto.training/hacks/30898-h-3-malicious-operators-can-undelegate-theirselves-to-manipu/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- oracle/live-external-read, economic/tvl-manipulation, trust/semi-trusted-operator

Dedupe:
- id: `30898-h-3-malicious-operators-can-undelegate-theirselves-to-manipu`
- fingerprint: `9dd349dd2292703a11c104e2cc5ed28d098ef6ec07bb78e8fbf66c41e86dbd2c`

Core exploit idea:
- 1. RioLRTOperatorDelegator.getEigenPodShares() is a direct, live pass-through read of EigenLayer's EigenPodManager.podOwnerShares() for the delegator's own EigenPod — no…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
