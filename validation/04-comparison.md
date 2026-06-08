# Comparison + recommendation

## Time-to-clarity

For the Vantacq drift feature:

| | `/blueprint` | `/brainstorm-v2` + `/plan-v2` |
|---|---|---|
| Rounds to a defensible plan (estimate) | 5-7 | 2 (brainstorm) + 1-2 (plan) = 3-4 |
| Rounds wasted on retroactive scope-patching | 2-4 | 0 |
| Mid-stream scope-change cost | High — patch the plan | Low — re-run brainstorm, plan untouched |
| Output durability | 1 plan file | 1 requirements file + 1 plan file (requirements survives plan rewrites) |

Net: v2-split saves ~2-3 rounds on the validation feature.

## Retrofit verdict

3 samples: 1 severe conflation (`canonical-grounding-guard`), 1 lucky-clean (`jakebot-coder-rails`), 1 already-doing-the-pattern-manually (`pantheon-ceo-phase-2a`).

Plan's stated threshold (`>=1/3 had the problem → build`) is met.

## What v2-split formalizes

The retrofit's most important finding: Jake already does the WHAT-vs-HOW split MANUALLY in high-stakes work (Pantheon CEO phase-split, the pre-flight reads discipline, the Phase 1→2a→2b cadence). The v2-split skills would formalize and lower-friction-ize that pattern, making it available without manually staging a phase split.

## Recommendation: **BUILD, but in two stages**

### Stage 1 — ship `/brainstorm-v2` + `/brainstorm-generate-v2` only

Lowest-risk piece. Produces `requirements.md`. Existing `/blueprint` continues to work; users who want HOW after `/brainstorm-v2` can pass the requirements file as input to `/blueprint`.

Why this stage alone is high-value:
- Even without `/plan-v2`, having a durable WHAT artifact unblocks better `/blueprint` runs (the requirements doc IS the feature description, scope is pre-locked).
- Single skill addition is reversible. If `requirements.md` artifacts don't show up in real workflow within 2-3 weeks, kill it cleanly.
- Adoption signal lives in `~/.claude/projects/.../blueprint/<slug>/requirements.md` files. Easy to grep for usage.

### Stage 2 — gate on usage signal

Ship `/plan-v2` + `/plan-generate-v2` only if:
1. Stage 1 sees real `requirements.md` files written for ≥3 features within ~2 weeks, AND
2. Subsequent `/blueprint` runs against those requirements docs still show HOW-shaped pain (slow rounds, scope-bleed, plan rewrites).

If `/brainstorm-v2` alone is enough, Stage 2 is pure ceremony and we don't ship it.

### Defer `/plan-v2`'s "auto-invoke brainstorm when fuzzy" prompt

The plan doc raised this as an open question. Defer to Stage 2 — premature without Stage 1 usage data.

## What changes from the original v2-split plan

| Plan doc said | This validation says |
|---|---|
| Build both `/brainstorm-v2` and `/plan-v2` together | Build `/brainstorm-v2` first, gate `/plan-v2` on usage signal |
| "No skill code written until comparison says yes" | Comparison says yes for stage 1; conditional yes for stage 2 |
| Validate by retrofitting last 3 sessions | Done — 1/3 severe, 1/3 lucky, 1/3 already-emergent |
| Risk: cognitive overhead of two skills | Mitigated by sequencing — overhead only paid if stage 2 ships |

## Director gate

Per plan doc: "No skill code written until that comparison says yes." Comparison done. **Director sign-off required before Stage 1 build.**

If Stage 1 approved, scope is:
- `~/repos/blueprint-v2/skills/brainstorm-v2/SKILL.md` (new)
- `~/repos/blueprint-v2/skills/brainstorm-generate-v2/SKILL.md` (new)
- `~/repos/blueprint-v2/skills/brainstorm-v2/references/` (questions template, requirements-template.md, etc.)
- README addition explaining the v2 pair coexists with original `/blueprint`
- Install instructions for adding the new skills alongside existing `/blueprint` install

Estimated effort: ~4-6 hours focused work in this same worktree.
