# Local Solodit Addendum: State-Transition and Pause Liveness

## Purpose
- Extend `audit-state-validation` with one specific stale-request/pause interaction not covered by its general input-validation workflow.
- Keep the original `SKILL.md`, `reference.md`, and checklist authoritative.

## When To Use
- Use after the original skill when queued withdrawals, request snapshots, circuit breakers, caught reverts, pause toggles, or timelocked unpauses interact.

## Focused Checks

### Stale request can repeatedly restore a global pause

Shape:
- A queued request becomes invalid after backing/state changes. A permissionless execution path catches the revert and sets a global pause, while retaining the stale request. After a valid unpause, the same request can trigger the pause again.

Questions:
- Does the failed operation revert atomically, or does a catch handler persist a pause/state change?
- Can an unprivileged caller retrigger the stale request indefinitely?
- Does cancellation, expiry, or repair remove the trigger, and can affected users still withdraw while paused?
- Does unpause clear or revalidate old requests before reopening the system?

Source pattern: [Stale withdrawal request can re-pause a vault after unpause](../../knowledge/smart-contract-audit/report-patterns/solodit/medium/stale-withdrawal-request-can-repause-after-unpause-dc5a50fe70.md).

## False-Positive Checks
- Do not flag a pause that is intentionally permissionless and self-clearing unless repeated retriggering materially blocks critical user actions.
- Prove the stale request persists, the caller is unprivileged, and every recovery path fails to neutralize it.
