# Validation context — Vantacq service-composition drift fix

**Date:** 2026-06-07
**Director input (hypothetical):** "Fix the Vantacq service-composition drift."

## Why this feature was chosen

Plan doc named three candidates (Pantheon CEO Phase 2b, Sidekick orb, Vantacq drift). Director picked Vantacq drift for highest scope-fuzziness — strongest test of whether the WHAT-vs-HOW split adds value.

## State of the underlying work (verified 2026-06-07)

- Issue #169 (original drift audit) **CLOSED 2026-04-23**, fixed by PR #176 (5-item punch list).
- Memory entry `project_service_composition_drift.md` is **46 days old** (system reminder flagged it).
- Active drift-ish PRs since the audit:
  - PR #226 merged 2026-05-31 — `refactor(enrichment): shared arv_from_assessed + estimate_repairs helpers`
  - PR #235 merged 2026-05-31 — `fix(title): share release-aware open-mortgage logic; net request-time exposure (#228)`
  - PR #248 merged 2026-06-02 — `fix(enrichment): distinguish PIN-filter-empty from authoritative-empty (#247) [P0]`
- Open issue #253 (updated 2026-06-03) — `Preserve four ingress points in refresh orchestration; share only post-parcel enrichment`

## What's genuinely fuzzy

If Director said "fix the drift" today, the unanswered questions are all WHAT-level:

1. Is there NEW drift since April, or are remnants from the original six un-wired?
2. Does "fix" mean wire each composition? Add guardrails (G2 audit script)? Both?
3. Is the four-ingress-point work in #253 part of "the drift fix" or its own thing?
4. What's "fixed" — zero un-wired analyzers, or "no false signals reaching prod"?
5. Out of scope: is `enrichment_monitor` orphan triage in this cycle?

Every one of those is a scope question. Implementation questions (which file, what test, rollback) can't be answered until they are.
