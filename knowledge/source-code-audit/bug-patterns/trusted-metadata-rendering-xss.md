# Trusted Metadata Rendered Without Escaping

Source:
- Z.ai CVD Ledger: <https://cvd.z.ai/>
- Example public finding: Joomla `com_installer` update-list stored XSS, CVE-2026-48952.

Source type:
- Public OSS/source-code vulnerability disclosure.

Status:
- Public pattern, use as a lead source only.

Bug class:
- Stored XSS / supply-chain metadata trust / admin-context script execution.

Core idea:
- A product ingests metadata from a trusted-looking external source, stores it, then renders it in a privileged UI without correct escaping or sanitization.
- The metadata may come from update manifests, package registries, extension feeds, plugin descriptors, marketplace listings, webhooks, imports, CI annotations, or generated reports.

Where to look:
- Package/plugin/extension update pages.
- Admin dashboards that render third-party metadata.
- Marketplace integrations.
- CI/CD annotations and security scan results.
- Import/export preview pages.
- Webhook event viewers.
- Report/query builders that render titles, descriptions, links, or markdown.

Search terms:
```text
description detailsurl details_url update manifest package plugin extension marketplace markdown html raw innerHTML dangerouslySetInnerHTML render_template safe escape sanitize
```

Concrete checks:
- Identify every externally supplied metadata field rendered in an authenticated or admin UI.
- Check whether text, URL, markdown, and HTML fields use context-correct escaping.
- Check whether links validate scheme and host before rendering as clickable anchors.
- Confirm the rendering path treats third-party update feeds and package manifests as untrusted.
- Check whether stored metadata is sanitized on ingest, escaped on output, or both.
- Check whether an attacker can control a feed, package, extension manifest, or update source without owning the target site.

False-positive blockers:
- Metadata source is not attacker-controllable in any realistic deployment.
- Output is escaped in the final template, even if intermediate variables look raw.
- The field is rendered only in inert text contexts.
- Admin-only self-XSS with no realistic external metadata/control path.

PoC shape:
- Control or simulate an external metadata feed.
- Store a payload in a description, URL, changelog, title, or markdown field.
- Load the privileged UI and prove script execution or unsafe HTML rendering.

Audit routing:
- Use this note for Web2/source-code audits involving update systems, marketplaces, registries, plugin managers, admin consoles, generated reports, and any UI rendering data from external feeds.
