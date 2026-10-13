# Findings

This directory holds two kinds of reports:

- **Reports from previous `/circom-auditor` runs** — written automatically as `{project-name}-zksec-circom-audit-report-{timestamp}.md` each time the skill runs with `--file-output`.
- **External audit reports** — drop any third-party or manual audit `.md` files here.

On each run the orchestrator builds a `prior-findings` bundle from the markdown files in this directory and re-verifies those issues against the current code during the final dedup/output pass.

- Issues still present are carried forward with a `Previously reported — still present` note.
- Issues that are no longer present are silently skipped.
- Revalidation works best for reports already in the skill's own markdown format, but the orchestrator also makes a best-effort pass over other markdown audit reports.
