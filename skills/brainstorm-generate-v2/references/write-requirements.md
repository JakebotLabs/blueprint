# Write requirements

Write `blueprint/<slug>/requirements.md`.

Use the refined requirements from the Q&A as the source of truth. Before writing:
- Re-read any anchor docs identified during brainstorm-v2 to ensure the requirements doc honors them
- Cross-check the Q&A for any open questions the user explicitly flagged

Follow [requirements-template.md](requirements-template.md) for the structure.

CRITICAL:
- Never write implementation code or implementation-shaped content (file paths, function names, class designs)
- If a Q&A answer leaked into HOW (e.g., "we'll wire it into `enrich_property_core`"), drop the HOW detail and capture only the WHAT it implies (e.g., "Solution integrates at the single canonical enrichment seam, wherever that lives today")
- Keep it tight — bullet points throughout, no paragraphs
- The Open Questions section is non-empty by default; perfect WHAT-lock is impossible
