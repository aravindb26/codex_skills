# Sl4x0: AI Bug Bounty System Architecture

Source: [How I Built My AI Bug Bounty Hunting System (And How You Can Build Yours)](https://x.com/sl4x0/status/2115791008747135067), by Abdelrhman Allam (@sl4x0), 2026-10-29.

Use this as an architecture and knowledge-curation reference for AI-assisted security research. The article describes the author's system and lessons; it is not an independent benchmark or a drop-in Codex implementation.

## Useful Design Lessons

- Separate model context from durable workflow state. Build a small, task-relevant context pack from persistent scope, assets, hypotheses, prior results, evidence, pending work, and validation status instead of replaying the entire history.
- Treat model claims as proposals, not evidence. A claimed test or request is not proof until the operation actually ran and its command, response/result, and provenance are recorded.
- Do not let the model be the only authority on completion. Check outstanding files, hypotheses, tests, validation, and report obligations against durable audit state before calling work complete. In our Codex workflow, Program Memory, the coverage ledger, and the audit gate receipt provide procedural checks; `AGENTS.md` alone is not a programmatic tool sandbox or an independently enforced supervisor.
- Keep technical validity separate from reportability. A reproducible behavior still needs scope fit, reachability, meaningful impact, deployment relevance, and sufficient evidence.
- Separate experience records from reusable techniques and skills. Preserve target-specific findings, dead ends, and observations with their source and confidence. Generalize the reason a technique worked only after validation across relevant cases, and review it before promoting it into a durable skill. Do not mistake a single observation for a universal rule.
- Evaluate changes to prompts, skills, guards, or context assembly against a stable, representative regression set where possible. Different output on a different target is not proof that the workflow improved.

## Fit With Our Existing Setup

Program Memory, selective skill loading, the coverage ledger, candidate verification, evidence requirements, reportability checks, and the audit gate receipt already cover most of the article's workflow ideas. Use this note only for the distinctions above; do not duplicate those procedures or install the author's runtime, MCP servers, or framework as part of an audit.
