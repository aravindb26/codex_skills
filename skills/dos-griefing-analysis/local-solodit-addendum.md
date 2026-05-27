# Local Solodit Addendum: DoS Griefing Companion Mini-Skill

## Purpose
- Extend `dos-griefing-analysis` with distilled High/Medium Solodit liveness and griefing patterns.
- Do not replace `SKILL.md`.
- Use this for missing exploit shapes around queues, callbacks, single-user failures, pause/blacklist locks, and epoch stuck states.

## When To Use

Use after reading `dos-griefing-analysis/SKILL.md` when code has:
- queues, batches, claims, withdrawals, reward distribution, validator operations, callbacks, blacklisting/pausing, gas-sensitive accounting, or round/epoch transitions.

## Companion Workflow

1. Load the original DoS/griefing skill first.
2. Search current code with the extra terms below.
3. Identify whether one attacker-controlled item can block many users or a critical protocol transition.
4. Check if the stuck state is temporary, retryable, paginated, slashable, or permanently blocking.
5. Search Solodit stubs by queue/round/callback function and stuck-state variable before escalating.

## Extra Search Terms

```text
queue
batch
for (
while (
claim
confirmChange
process
executeRequest
retry
callback
receive
fallback
blacklist
paused
round
epoch
cycle
gasleft
gasLimit
snapshot
pending
```

## Missing / Sharper Patterns To Check

### 1. Queue pollution blocks protocol transitions

Shape:
- Attackers create many pending requests, duplicate entries, invalid entries, or expensive entries that block confirmation, settlement, withdrawal, or validator operations.

Questions:
- Can one actor cheaply grow a queue processed by others?
- Are invalid/stale entries removable without processing the whole queue?
- Can queue congestion delay or block user exits?

### 2. Single failed item blocks batch or vault operations

Shape:
- One paused/blacklisted/reverting vault, token, recipient, or callback blocks all withdrawals, claims, liquidations, or distributions.

Questions:
- Is failure isolated per item?
- Is there skip, retry, quarantine, or pull-claim path?
- Can an attacker choose the failing receiver/token/vault?

### 3. Callback gas or revert griefing

Shape:
- Receiver/callback can consume gas, revert, return wrong magic bytes, or exploit 63/64 gas forwarding to mark work complete while inner execution fails.

Questions:
- Is success checked before marking request consumed?
- Can insufficient gas burn a nonce/request permanently?
- Can wrong magic bytes or revert force stuck funds?

### 4. Pause/blacklist creates asymmetric lock

Shape:
- Pause or blacklist blocks only the user's escape path while allowing debt, liquidation, fees, or bad state to continue.

Questions:
- Can principal withdrawal be blocked by reward wallet/token failure?
- Can repayment be blocked while liquidation continues?
- Can liquidation be blocked while bad debt grows?

### 5. Round, epoch, or cycle cannot advance

Shape:
- A round/epoch depends on all participants, all claims, all callbacks, or a mutable condition that one user can prevent.

Questions:
- Can one user keep a round from finalizing?
- Can old unclaimed tickets/rewards keep accounting stale forever?
- Is there a timeout/admin escape, and is it in scope/trusted?

### 6. Gas accounting snapshot is taken too early

Shape:
- Protocol records gas before all post-handlers/callbacks finish, causing undercharged execution, refund abuse, or unpaid gas.

Questions:
- Are gas snapshots taken before post-processing?
- Can undercharged work repeat enough to affect block/liveness assumptions?
- Does program severity accept gas-accounting DoS, or is it likely out of scope?

## False-Positive Filters

Do not escalate unless:
- The stuck state blocks critical user/protocol operations or creates rewardable liveness impact.
- The attacker cost is meaningfully lower than the harm caused.
- Existing pagination, skip, retry, timeout, or admin rescue is insufficient under program assumptions.
- You distinguish temporary inconvenience from permanent lock, systemic DoS, or critical griefing.
