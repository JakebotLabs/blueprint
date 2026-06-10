# Retrofit — existing `/blueprint` outputs

Plan said retrofit against "last 3 `/blueprint` sessions." Workspace has 5: `canonical-grounding-guard`, `jakebot-coder-rails`, `pantheon-ceo-agent`, `pantheon-ceo-phase-2a`, `pantheon-ceo-phase-2b`. Sampled 3 across domains.

Signal hunted: did the FINAL PLAN show evidence of having retrofitted scope into a HOW frame under pressure? Or did it show clean scope-first reasoning?

## Sample 1 — `canonical-grounding-guard`

**Verdict: SEVERE WHAT-vs-HOW conflation.**

Plan went through 40+ revision rounds visible in breadcrumbs. Many were caught by Jakebot, not surfaced in original Q&A:

- Round 17: "Plugin-owned smoke's claim is narrowed honestly" — what does the smoke actually prove? (WHAT escaping HOW disguise.)
- Round 21: "WindowsBot lane now has the same three-layer proof model as BOTASAURUS" — what counts as proof? (WHAT.)
- Round 24-32: a long arc of "verified" semantics — what does verified actually mean? Hardcoded probes vs cap-row declared, single artifact vs three-layer, etc.
- Round 35-41: GH API specifics — HOW-shape failures, but rooted in the WHAT-uncertainty about what the verifier should accept as proof.

The WHAT churn (what's the proof model, what's the host-identity contract) dominated. A `/brainstorm-v2` round would have surfaced "what does 'verified' mean for this capability — single proof or three-layer? Per-host or fleet-wide? Bound to which artifacts?" up front. The HOW arc would then have been ~5 rounds, not 40.

**This plan exhibits the failure mode v2-split targets.**

## Sample 2 — `jakebot-coder-rails`

**Verdict: NO strong conflation.**

The visible refined-prompt block shows a 5-question Q&A with shorthand answers:
- Q1 (scope): `b` — targeted tightening, not refactor. **WHAT.**
- Q2 (source of truth): `a` — `botasaurus-heartbeat/scripts/grok-coder.py`. **HOW boundary.**
- Q3 (failure modes in scope): `a+b+c+d` — explicit in-scope/out-of-scope list. **WHAT.**
- Q4 (coordination with `pr_reviewer.py`): `d` — separate, contract doc. **HOW.**
- Q5 (migration timing): `a` — land on BOTASAURUS now. **HOW.**

3/5 WHAT, 2/5 HOW. The skill happened to lead with WHAT (Q1, Q3) before HOW (Q2, Q4, Q5). Plan landed clean.

**This plan did NOT exhibit the failure mode** — but only because the user (or model) happened to order questions well. Not a structural defense.

## Sample 3 — `pantheon-ceo-phase-2a`

**Verdict: NO conflation visible — but only because Phase 1 pre-locked the WHAT.**

The plan opens with seven "locked Phase-1 decision" bullets:
- "CEO is the orchestrator, not the operator"
- "3-hour escalation timer from DETECTED"
- "P0-beyond-scope keyword classifier at ingest"
- "PROPOSE flow uses the lead twice"
- "Phase split to keep the round-2 PR shippable"
- "Cold-start full reconciliation"
- "Director ↔ Kathy is conversational"

These are pure WHAT — locked by an earlier blueprint session (Phase 1) and inherited here. Phase 2a's Q&A could focus entirely on HOW because the WHAT was already pinned.

This is exactly what `/brainstorm-v2` would produce — a durable WHAT artifact that subsequent `/plan-v2` runs consume. **The pattern v2-split formalizes is already emergent in Jake's workflow** — he does it manually by phase-splitting.

## Cross-sample summary

| Sample | WHAT-vs-HOW conflation? | Why |
|---|---|---|
| canonical-grounding-guard | YES (severe) | No WHAT-lock; semantics churned through 40+ rounds |
| jakebot-coder-rails | No | Q&A happened to order well; no structural defense |
| pantheon-ceo-phase-2a | No | Phase 1 already produced the WHAT-lock; emergent split |

**1/3 strong build signal. 1/3 weak (lucky). 1/3 already does the pattern manually.**

Plan threshold: ">=1/3 had this problem → build." Met.

## Adjacent observation

The pantheon-ceo Phase 1→2a→2b sequence IS the v2-split pattern, done by hand. Phase 1 was the WHAT lock; Phases 2a/2b consumed it. The 12-rounds-vs-round-1 evidence from `feedback_preflight_internal_reads.md` is also a Phase-1-locked-WHAT story.

This is what shifts the decision from "build" toward "build, but carefully." The pattern works manually. Formalizing it adds friction unless the skills bake in the discovery — e.g., `/plan-v2` invoked without `requirements.md` could prompt the user to run `/brainstorm-v2` first when the feature description is thin.
