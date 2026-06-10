# Trace — what `/brainstorm-v2` + `/plan-v2` would each ask

Mental-model walkthrough per the v2-split plan spec.

## Part A — `/brainstorm-v2`

### Honor strategic anchor docs

Per the plan, `/brainstorm-v2` would notice `project_service_composition_drift.md` in memory and the open issue #253. It would acknowledge prior context up front rather than re-discover it.

### Round 1 — 3-5 scope-only questions

> Q1. **What problem are we actually solving today?**
> a) False signals reaching prod (correctness)
> b) Cross-tab inconsistency (UX)
> c) Hidden compute waste — analyzers loaded but skipped (efficiency)
> d) Future-proofing — recurrence prevention is the point
> e) Other
>
> Q2. **Who's the user?**
> a) Vantacq investor users (the dashboard)
> b) Internal bots running enrichment (the pipeline)
> c) Future devs adding services (recurrence prevention)
> d) All three
> e) Other
>
> Q3. **What does "fixed" look like, concretely?**
> a) `test_cross_tab_parity.py` passes on N real parcels
> b) Zero un-wired analyzers per a (re-run) audit script
> c) Director sign-off on a behavior diff between two enrichment runs
> d) Other
>
> Q4. **Is the April audit (#169 / PR #176) canonical for what was un-wired, or has new drift accumulated since?**
> a) April list is canonical, just re-verify each
> b) New drift exists (e.g. #253 four-ingress-point question) — survey first
> c) Other
>
> Q5. **Out of scope for this cycle?**
> a) G2 audit script (mechanical orphan detection)
> b) Minor orphans (`enrichment_monitor`, `auction_tracker`)
> c) Both
> d) Neither — ship it all
> e) Other

**All five are WHAT.** None retrofit assumptions about implementation.

### Output: `requirements.md`

After 1-2 rounds, the artifact looks like:

```markdown
# Vantacq service-composition drift — requirements

## Problem
Cross-tab inconsistency in investor signals (Q1=b) — same parcel shows different
criteria_signal / exposure / brrrr_roi depending on tab.

## Personas
- Vantacq investor users (Sally + prospective customers) — the primary visible-effect target
- Internal enrichment bots — secondary, but their behavior IS the bug surface
- Future devs — out of scope this cycle per Q5

## Success criteria
- `test_cross_tab_parity.py` passes on a curated set of 20 real parcels appearing
  in 2+ tabs, with exposure/criteria_signal matching within tolerance.
- A drift sweep of the original six #169 items shows 0 regressions and any
  newly-identified un-wired compositions are documented (not necessarily fixed).

## Out of scope
- G2 audit script (mechanical orphan detection) — separate cycle.
- `enrichment_monitor` / `auction_tracker` orphans — minor.
- Behavior changes beyond consistency — no new signals, no UI work.

## Open questions
- Is #253 (four-ingress-point) the SAME drift class, or a separate refactor?
  Surfacing in this brainstorm to feed plan-v2's scope.
```

This artifact is durable, reviewable, and version-controlled — even if `/plan-v2` is never run, the requirements doc has standalone value.

## Part B — `/plan-v2`

### Pre-condition: requirements.md exists

`/plan-v2` reads `requirements.md`. Scope is pinned. Codebase exploration runs (same as `/blueprint`'s Step 3).

### Round 1 — 3-5 technical-only questions

> Q1. **Single seam or per-path?**
> a) Wire missing analyzers into `enrich_property_core` (single seam)
> b) Per consumer path
> c) Behind a new `EnrichmentOrchestrator` class
>
> Q2. **Ordering invariant — where do we enforce `lien_graph` → `analyze_title`?**
> a) Hard-code call order in `enrich_property_core`
> b) Type-level dataclass dependency (TitleAnalysis takes lien_graph result as input)
> c) Both
>
> Q3. **Cross-tab parity test fixtures?**
> a) Synthetic parcels matched by hand
> b) Captured fixtures from prod (anonymised)
> c) Both — synthetic for invariants, real for regression
>
> Q4. **Rollback model?**
> a) Per-analyzer feature flag (e.g. `ENABLE_LIEN_GRAPH_IN_CORE`)
> b) Revert the whole PR
> c) Shadow comparison mode — log diffs without acting
>
> Q5. **PR size — single PR or per-item?**
> a) Single PR (5 changes, one parity-test gate)
> b) Per-#169-item PRs (5 PRs)
> c) Two PRs — wiring first, parity-test gate second

**All five are HOW.** Every one is answerable because Q1-Q5 in `/brainstorm-v2` already pinned scope.

### Output: `plan.md`

Standard plan with Approach / Files Touched / Sequence / Tests / Risks / Rollback. Crucially, Sequence and Rollback are symmetric (per the v2 plan spec) — every step in Sequence has a named undo step in Rollback.

## Comparing cognitive load

| | `/blueprint` | `/brainstorm-v2` + `/plan-v2` |
|---|---|---|
| Skills to learn | 2 (`/blueprint` + `/blueprint-generate`) | 4 (`brainstorm-v2` + `brainstorm-generate-v2` + `plan-v2` + `plan-generate-v2`) |
| Artifacts produced | 1 (`plan.md`) | 2 (`requirements.md` + `plan.md`) |
| Round-1 question diversity | Mixed WHAT/HOW | Pure WHAT, then pure HOW |
| Cognitive overhead | Low | Medium — user has to know which skill to invoke first |
| Recovery when scope shifts mid-Q&A | Retroactive — patch in later rounds | Re-run `/brainstorm-v2` (cheap because durable artifact) |
