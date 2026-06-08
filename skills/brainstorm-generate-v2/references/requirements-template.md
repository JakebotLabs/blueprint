# Requirements template

The canonical structure for `requirements.md`. All sections required. Order is fixed. Bullet points throughout — no paragraphs.

---

## Section: Problem

2-5 bullets describing what's broken, who hurts, and the cost of inaction.

If any `project_*.md` anchor doc was honored, cite it explicitly in this section.

---

## Section: Personas

Each persona on its own bullet. Format:

- **Name (role)** — what they need from this feature, and why

Include both human and bot personas if relevant. Out-of-scope personas should be explicit ("Future devs are NOT a primary persona this cycle").

---

## Section: Success criteria

2-5 observable criteria. Each must be checkable without reading the implementation. Prefer concrete metrics (counts, latencies, pass/fail tests, user-visible behaviors) over subjective language.

- BAD: "User experience is improved"
- GOOD: "Cross-tab consistency test passes on 20 real parcels with mismatch under 1%"

---

## Section: Out of scope

Bulleted list of explicit non-goals. Each bullet includes WHY (cost, scope creep, deferred). This section is load-bearing — its absence is how scope creeps.

---

## Section: Open questions

Each unresolved scope question on a bullet. Format:

- **Q:** the question
- **Status:** one of: decision deferred to /plan-v2 / blocked on Director / surfaced but unanswered / requires user research

This section is non-empty by default. Perfect WHAT-lock is impossible — surface what's still open so /plan-v2 (or `/blueprint`) inherits the right uncertainty.
