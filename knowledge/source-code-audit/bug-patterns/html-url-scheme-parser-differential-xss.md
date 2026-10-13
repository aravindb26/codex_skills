# HTML URL Scheme Parser Differential in Link Sanitizers

Source:
- Swiss Post E-Voting public work item, `RichTextPipe sanitizer bypass`, issue 45: <https://gitlab.com/swisspost-evoting/e-voting/e-voting/-/work_items/45>
- The work item links YesWeHack report 870334. Publicly available report summaries describe an HTML-character-reference bypass of a literal `javascript:` scheme check.

Source type:
- Publicly disclosed source-code report / duplicate-risk lead.

Status:
- The linked bounty report is not publicly accessible and its disposition is unknown. Treat this as a reported pattern, not as a confirmed accepted vulnerability.

Bug class:
- XSS / URL-scheme validation / parser differential.

Core idea:
- A sanitizer may inspect an href as a raw string, reject literal `javascript:` and then reconstruct trusted HTML. The browser subsequently parses character references in the attribute and interprets the decoded value as a dangerous URL. For example, a literal-scheme regex can miss an href whose `javascript:` spelling contains an HTML character reference such as `javascript&#58;` or `jav&#x61;script:`.
- The underlying defect is disagreement between the sanitizer's string-level interpretation and the browser's HTML/URL parsing, not the choice of one particular entity spelling.

Where to look:
- Custom rich-text or markdown renderers that extract anchors with regexes.
- Sanitizers that build an HTML string and return it as trusted/safe HTML.
- Templates using `innerHTML`, `bypassSecurityTrustHtml`, or equivalent trust APIs.
- Config, CMS, API, translation, or metadata fields that can reach clickable links.

Concrete checks:
- Trace each link-enabled sink back to an attacker-controlled source and determine whether the program threat model permits that actor.
- Test HTML character references in both scheme characters and punctuation, plus ASCII tabs/newlines and browser URL normalization where relevant.
- Validate a parsed/normalized URL against a strict protocol allowlist; do not rely on substring or raw-prefix blacklists.
- Escape all attribute syntax when reconstructing HTML, including ampersands and quotes, or use DOM APIs and a maintained sanitizer instead of string reconstruction.
- Confirm whether execution needs a user click and whether the actual application workflow presents a reachable clickable link.

False-positive and triage blockers:
- A similar public issue may already report the same parser-differential root; compare the exact sanitizer, trust boundary, attacker source, and impact before treating another entity spelling as a new variant.
- A sanitizer flaw alone is not a product finding when link rendering is disabled for the attacker-controlled field or the field is only trusted static configuration.
- A claimed XSS needs an attacker-reachable source-to-sink path and a safe local reproduction of the actual rendering path; browser parsing tests alone prove only the parser behavior.

PoC shape:
- In a local test application, feed an attacker-controlled href with an entity-obfuscated dangerous scheme through the production sanitizer and show the final DOM's parsed `href` and script execution after the documented user action. Include a normal safe-link control. Never test a production voter portal without explicit program authorization.
