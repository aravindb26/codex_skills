# PKQS91 Codex Bounty Workflow

Source:

- Local PDF: `/home/dinesh/How I Made $200k With Codex in 3 Months _ XCancel.pdf`
- Public article URL observed from PDF: `https://xcancel.com/i/article/2070157806104457395`
- Original X article/status: `https://x.com/pkqs91/status/2070157806104457395`

Use this lesson for:

- audit workflow design
- bounty-hunting process
- AI-agent orchestration
- false-positive reduction
- deciding when a candidate deserves manual verification

Do not use this as:

- a vulnerability pattern
- proof that AI output is enough to submit
- a reason to skip manual code understanding

## Core Lesson

The useful workflow is not "ask Codex to find bugs." It is:

1. Build a local research bundle.
2. Explore wide across surfaces and bug classes.
3. Maintain and rank a lead bank.
4. Deepen only promising leads from attacker input to concrete impact.
5. Manually verify and reproduce before submission.

Most AI-generated leads should die. The value is in producing more shots on goal, not trusting every candidate.

## Intake Step

Before hunting, convert the target into a local research bundle:

- program scope
- severity and reward rules
- known exclusions
- docs and architecture context
- code and dependency context
- what impact actually matters for the target

This matches our Program Memory and audit gate receipt workflow. Do not start from a vague "find bugs" prompt.

## Explore Wide

Use Codex to cover broad surface area:

- assets and value flows
- entry points
- trust boundaries
- invariants
- known bug patterns
- strange state transitions
- external dependencies
- documentation/code mismatches
- boring corners humans skip when tired

Expected output is noisy. Pattern matches, low-impact issues, and out-of-scope ideas are normal at this stage.

## Exploit Deep

Promote only promising leads into deep tracing.

For each lead, trace:

- attacker-controlled input
- reachable entry point
- trust boundary crossed
- state transition
- broken invariant
- concrete impact sink
- exact proof still missing

A lead must earn its way to impact such as fund loss, unauthorized mint, fund lock, chain crash/liveness break, proof soundness break, governance manipulation, or another program-rewarded outcome.

## Lead Bank Discipline

Maintain an adaptive lead bank:

- merge similar weak signals
- rank by expected value
- kill out-of-scope or non-impactful leads early
- send uncertain surfaces back to exploration
- promote only concrete paths into deepening

Do not spend equal effort on every lead.

## Verification Gate

Before submission, attack the candidate with these questions:

- Is it in scope?
- Is the entry point really attacker-accessible?
- Does it require privileged misuse or routine admin mistake?
- Is there an on-chain guard that kills the path?
- Is the attack economically feasible?
- Does the impact matter under the program's severity rules?
- Can it be reproduced end to end?
- Can the auditor personally explain and defend the finding?

If the answer is weak, the candidate should not be submitted.

## What Did Not Work

Too many simple bug patterns can make Codex see bugs everywhere. They create shallow analogies and scanner-like noise.

Use pattern libraries as triggers and checklists, not as conclusions.

Workflow changes need an evaluation set. If every prompt change is tested on a new target, different output can feel like improvement even when it is only different.

## Practical Rule For Our Agent

For bounty work, optimize for one real high-impact bug, not broad audit completeness. For full audits, broad file coverage still remains the user's responsibility and must not be replaced by bounty-style lead hunting.

The correct loop:

- explore wide
- exploit deep
- kill aggressively
- verify manually
- submit only if the finding survives scope, impact, duplicate, and reproduction gates

