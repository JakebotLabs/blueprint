# Trace — what `/blueprint` would ask

Mental-model walkthrough using the actual SKILL.md flow.

## Step 1-2: Template selection

`/blueprint` would offer the user "Default" or "Concise". Both templates carry HOW sections (Implementation plan, Implementation phases, Changes). Neither has a WHAT-only mode.

Probable pick: **Default** (broader feature with multiple touchpoints).

## Step 3: Codebase exploration

`/blueprint` would Read:
- `app/services/title_analysis.py`
- `app/services/mortgage_estimator.py`
- `app/services/lien_graph.py`
- `app/services/criteria_matcher.py`
- `app/services/enrichment.py` (the `enrich_property_core` seam)
- `app/services/batch_enrichment.py`
- `tests/test_cross_tab_parity.py` (if it exists)
- `scripts/audit_service_composition.py` (if it exists)

Plus PR #176 diff to understand what was already fixed.

## Step 4: Round 1 — 3-5 clarifying questions

Given the Default template's HOW-bias and the genuinely-fuzzy scope, the questions would likely come out mixed. Plausible round 1:

> Q1. **Which drift do we fix in this PR?**
> a) The remaining items from the original #169 audit (if any)
> b) New drift surfaced since April (e.g. #253-related)
> c) Both, sequenced — old first then new
> d) Other
>
> Q2. **Where does the new wiring land?**
> a) In `enrich_property_core` (single seam)
> b) In each consumer path independently
> c) Behind a new `EnrichmentOrchestrator` class
> d) Other
>
> Q3. **Test strategy?**
> a) Extend `test_cross_tab_parity.py`
> b) New `test_drift_invariants.py`
> c) Both
> d) Other
>
> Q4. **Rollback if parity test fails on real data?**
> a) Per-analyzer feature flag
> b) Revert the whole PR
> c) Other
>
> Q5. **Should we add the G2 audit script (mechanical orphan detection) in scope?**
> a) Yes, ship it in this PR
> b) Separate PR, this cycle
> c) Out of scope this cycle
> d) Other

## Classification of round-1 questions

| Q | Type | Defensible without WHAT-lock? |
|---|---|---|
| Q1 | WHAT | The skill conflates this with HOW |
| Q2 | HOW | Cannot answer until Q1 picks which drift |
| Q3 | HOW | Test choice depends on Q1 answer |
| Q4 | HOW | Premature — rollback scope depends on Q1/Q2 |
| Q5 | WHAT | Scope question disguised as a checklist item |

**Mix: 2/5 WHAT, 3/5 HOW.** The HOW questions are pre-committed to assumptions the WHAT questions are still resolving — they retrofit answers to make Q2-Q4 work.

## Step 5: Continue Q&A

If round 1 answers were `1a, 2a, 3a, 4a, 5c` (defensible defaults), round 2 might be:

> Q6. Which of the original 6 items from #169 are actually still un-wired today?
> Q7. Does `lien_graph.analyze()` already run in `enrich_property_core` since PR #176? (Re-check before plumbing.)
> Q8. Cross-tab parity test fixtures — synthetic parcels or anonymised real?
> ...

By round 2, the skill is patching scope holes it should have caught in round 1.

## Best case: how many rounds to a clean plan?

If the user is sharp and pushes back on early HOW questions, ~3 rounds. If they answer in good faith, scope keeps moving and 5-7 rounds is plausible.

## Worst-case symptom from the retrofit

Compare with `canonical-grounding-guard` (the closest analog in the existing blueprint output dir): 40+ revision rounds visible in breadcrumbs. Many of them caught WHAT-shaped problems (what does "verified" prove, what's the host-identity contract, what's "live enforcement") that the early Q&A let slip through.

That's the failure mode `/blueprint` is vulnerable to here.
