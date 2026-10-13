# Eval Compare

Compare an audit report against ground truth findings. You will be given two files:

1. **Ground truth** — the benchmark file with known findings (FINDING blocks in the frontmatter region).
2. **Report** — the audit output (`final-report.md` or `full-output.txt`).

## Steps

1. Read the ground truth file. Parse each `FINDING` line and its `description:` line.
2. Read the report file. Identify two sections:
   - **Findings** — between `## Findings` and `## Leads`
   - **Leads** — from `## Leads` to end of file
3. For each ground truth finding, determine if the report caught it. Use semantic matching — the report doesn't need to use the exact same words, but must describe the same vulnerability in the same template/signal/bug-class. Classify each as:
   - **FOUND** — the vulnerability appears in the Findings section. The report identifies the same template, the same signal or local entry point, and the same root cause (even if described differently).
   - **LEAD** — the vulnerability appears only in the Leads section with the same criteria above.
   - **MISSED** — not present in either section.

## Output

Write `summary.md` to the run directory with this exact format:

```
## Eval Results

| Metric | Value |
|--------|-------|
| Recall (findings) | {found} / {total} ({pct}%) |
| In leads only | {leads} |
| Missed | {missed} |
| High | {high_found} / {high_total} |
| Medium | {med_found} / {med_total} |
| Reported findings | {count from report} |

### Per-finding breakdown

| Status | Severity | ID | Template.Signal | Bug Class |
|--------|----------|----|------------------|-----------|
| FOUND | High | H-1 | Template.signal | bug-class |
| LEAD | Medium | M-2 | Template.signal | bug-class |
| MISSED | Medium | M-3 | Template.signal | bug-class |
```

## Rules

- Match semantically, not by keyword grep. "LessThan operands not range-checked" matches "comparator-input-not-range-checked" even without those exact words.
- A finding in the Leads section is NOT a finding — it's a lead. Don't count it toward recall.
- If the report describes the same root cause but attributes it to a different signal in the same template, still count it as FOUND.
- If the report merges two ground-truth findings into one reported finding, count both as FOUND.
- Treat the V-X.Y `vector_id` as canonical when both sides supply it; otherwise rely on (template, signal, bug-class) triple.
