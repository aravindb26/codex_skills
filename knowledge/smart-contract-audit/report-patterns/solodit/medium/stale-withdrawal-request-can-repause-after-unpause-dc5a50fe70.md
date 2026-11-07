# Solodit Pattern: Stale withdrawal request can re-pause a vault after unpause

Source:
- https://solodit.cyfrin.io/issues/stale-withdrawal-requests-let-anyone-re-pause-the-vault-after-every-unpause-quantstamp-telescope-markdown

Imported:
- 2026-11-07

Severity:
- MEDIUM

Protocol / source:
- Telescope / Quantstamp

Tags:
- stale queued request, pause liveness, caught revert, withdrawal

Dedupe:
- id: `75102`
- fingerprint: `dc5a50fe70b3e2a756ecf3b5b2609e278e54d6e71a197a2be99aee286b7b927f`

Core mechanism:
- A queued withdrawal retains parameters based on an earlier backing or exchange rate. Finalization later trips a circuit breaker; a permissionless router catches that failure and pauses the vault instead of reverting the outer call. If the stale request remains actionable, anyone can repeat the failure after each timelocked unpause.

Invariant and audit checks:
- A resolved or stale request must not let an unprivileged caller repeatedly restore a global pause after governance unpauses.
- Trace request snapshots, backing changes, finalization/circuit-breaker reverts, catch-and-pause behavior, and every unpause path. Check whether cancellation or expiry removes the trigger and whether the pause actually blocks user exits.

False-positive checks:
- Confirm the call is permissionless, the caught failure really mutates global pause state, the request remains reusable, and no automatic cancellation/recovery path clears it. Do not report a single expected pause or an admin-only re-pause.

PoC shape:
1. Queue a withdrawal, then change backing so its stored values fail finalization.
2. Trigger the permissionless caught-revert path and observe the pause.
3. Execute the documented unpause, repeat the trigger, and prove users remain unable to exit.

Triage notes:
- Impact depends on the pause scope and duration; distinguish a repeatable exit freeze from temporary operational friction.
