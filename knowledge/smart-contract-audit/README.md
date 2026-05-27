# Smart Contract Audit Knowledge Base

Use this directory as a reusable audit memory for smart contract and Web3 security work.

When the user provides a rejected report, X post, article, accepted bug report, Solodit item, C4/Cantina/HackenProof/Sherlock report, or similar source, distill it into a concise pattern note. Do not copy large source text. Capture the reusable attack pattern, invariant, false-positive filters, and PoC shape.

## Directory Guide

- `bug-patterns/`: reusable vulnerability patterns independent of one source.
- `report-patterns/`: distilled lessons from accepted public bug reports.
- `x-post-lessons/`: lessons from X posts and short social content; mark unverified claims clearly.
- `article-lessons/`: lessons from longer articles, blogs, research posts, and writeups.
- `workflows/`: repeatable audit workflows and operating procedures.
- `rejected-findings/`: rejected Codex/user findings and the reason they failed triage.
- `finding-library.md`: strong findings found or submitted by the user.
- `miss-library.md`: good findings the user missed, plus why they were missed.
- `dead-branches.md`: investigated ideas that were killed before submission.
- `invariant-library.md`: reusable invariants by protocol family.
- `protocol-patterns.md`: common design patterns and risk zones by protocol type.
- `triage-rejection-patterns.md`: recurring reasons triagers reject reports.

## Distillation Rule

Save the lesson, not the whole content.

Every note should answer:

- What is the bug pattern?
- What invariant breaks?
- Where does it appear in code?
- What is the exploit shape?
- What false-positive checks matter?
- How would we prove it next time?

## Audit Workflow

For serious audits, use `workflows/mythos-inspired-audit-workflow.md` as the local multi-pass workflow. Use `templates/audit-coverage-ledger.md` to track in-scope file coverage and `templates/candidate-verification-card.md` to verify or kill candidate findings.
