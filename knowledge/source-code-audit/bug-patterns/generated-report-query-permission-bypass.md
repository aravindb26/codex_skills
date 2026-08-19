# Generated Report Or Query Permission Bypass

Source:
- Z.ai CVD Ledger: <https://cvd.z.ai/>
- Example public finding family: Frappe prepared/query report permission bypasses.

Source type:
- Public OSS/source-code vulnerability disclosure.

Status:
- Public pattern, use as a lead source only.

Bug class:
- Authorization bypass / row-level permission bypass / generated artifact access control.

Core idea:
- A reporting/query subsystem correctly checks permissions when creating or viewing a normal object, but a generated report, cached prepared report, query result, export, chart, or background job output bypasses the same object/row/owner constraints.

Where to look:
- Report builders.
- Prepared/cached reports.
- Query report endpoints.
- CSV/PDF/export generation.
- Dashboard widgets and charts.
- Background jobs that materialize user-visible data.
- Saved searches, filters, kanban boards, and views.

Search terms:
```text
report query prepared export csv pdf dashboard chart filter view owner permission has_permission row_level get_all get_list sql raw_query background job cache
```

Concrete checks:
- Compare permissions on the source object with permissions on the generated artifact.
- Check whether query builders use raw SQL or broad `get_all`-style helpers that skip row-level rules.
- Verify owner, tenant, role, sharing, and field-level checks are applied before caching and before retrieval.
- Check whether a user can request another user's report ID, job ID, view ID, saved filter, or export URL.
- Verify cached artifacts are scoped by user, tenant, role, filter set, and permission version.
- Check whether permission changes invalidate old generated artifacts.

False-positive blockers:
- The report is intentionally public and contains only public data.
- The generated artifact lookup is unguessable and bound to the requesting user/session.
- Source query and artifact retrieval both enforce the same canonical permission check.
- The exposed data is not sensitive and creates no meaningful boundary break.

PoC shape:
- Create or locate data visible to user A but not user B.
- Generate a report/export/cache entry as user A or an authorized role.
- Access or trigger the generated artifact as user B.
- Prove user B receives data they cannot access through the normal object/API path.

Audit routing:
- Use this note during Web2/source-code audits of enterprise apps, SaaS dashboards, low-code frameworks, ERP/CRM systems, analytics features, and any system with reports or exports.
