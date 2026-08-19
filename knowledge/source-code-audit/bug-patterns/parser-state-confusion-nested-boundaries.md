# Parser State Confusion Across Nested Boundaries

Source:
- Z.ai CVD Ledger: <https://cvd.z.ai/>
- Example public finding: Suricata SMTP MIME `message/rfc822` state-reset bug, CVE-2026-57229.

Source type:
- Public OSS/source-code vulnerability disclosure.

Status:
- Public pattern, use as a lead source only.

Bug class:
- Parser state confusion / stale nested-state inheritance / detection bypass.

Core idea:
- A parser enters a nested or embedded object but carries outer-object metadata into the inner object.
- The inner object is then decoded, classified, logged, or enforced using stale filename, encoding, boundary, content type, trust flag, or policy state.

Where to look:
- MIME/email parsers.
- Archive parsers.
- Multipart upload handlers.
- JSON/YAML/XML nested object parsers.
- Protocol decoders with recursive frames or submessages.
- Import/export pipelines with nested attachments, manifests, or metadata.

Search terms:
```text
parse decode nested embedded recursive message/rfc822 multipart boundary filename content-type encoding state reset clear child parent part attachment
```

Concrete checks:
- Does entering a nested object reset all state that should be scoped to one object or part?
- Are filename, content type, transfer encoding, security labels, and policy flags stored per node/part instead of globally?
- Do error paths, early returns, and recursion exits restore parser state?
- Can attacker-controlled outer metadata change enforcement for inner attacker-controlled content?
- Do logs/UI/detection rules rely on stale parsed metadata while raw payload checks see different content?
- Does validation happen before or after decoding, canonicalization, or nested object construction?

False-positive blockers:
- The relevant standard intentionally inherits the state and the code follows that standard.
- The inner object cannot be attacker-controlled.
- Stale state affects only diagnostics and has no security, policy, routing, or detection impact.
- Enforcement uses independent canonical state, not the stale parser fields.

PoC shape:
- Build an outer object with benign metadata.
- Embed an inner object with malicious or policy-relevant content.
- Prove the engine enforces/logs/classifies the inner object using the outer metadata.

Audit routing:
- Use this note when a source-code audit includes parsers, importers, file analyzers, malware detectors, WAF/proxy decoders, archive processing, or nested message formats.
