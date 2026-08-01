# Crypto Training Exploit Pattern Stub: Fluid — processNormalSupplyAction permits an uncapped withdrawal

Source:
- https://crypto.training/hacks/65649-fluid-processnormalsupplyaction-permits-an-uncapped-withdrawal/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2026

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/missing-check, input-validation/missing

Dedupe:
- id: `65649-fluid-processnormalsupplyaction-permits-an-uncapped-withdrawal`
- fingerprint: `86914eea9f2aa4e95afad18b450e46259f701ca76354f63533b9140148ac9845`

Core exploit idea:
- The normal-supply action does not cap the requested withdrawal by the user's tracked shares, allowing a caller to withdraw more than was supplied.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
