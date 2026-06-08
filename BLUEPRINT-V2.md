# Blueprint v2 — WHAT-vs-HOW split (JakebotLabs fork)

This fork adds two skills alongside the upstream `/blueprint` + `/blueprint-generate` pair:

| Skill | Purpose |
|---|---|
| `brainstorm-v2 <description>` | WHAT-only scope-locking Q&A. Produces a durable `requirements.md`. |
| `brainstorm-generate-v2` | End the Q&A and write `blueprint/<slug>/requirements.md`. |

## Why

Upstream `/blueprint` runs one Q&A loop that mixes scope questions (problem, personas, success criteria) with implementation questions (files, tests, rollback). When scope is fuzzy, implementation questions arrive too early and answers retrofit the scope — manifesting as 10+ revision rounds on the final plan.

`brainstorm-v2` produces a durable scope artifact BEFORE any implementation planning. The artifact is reviewable and version-controlled on its own.

## How the two pairs coexist

```text
Use case                         | Recommended flow
---------------------------------|-------------------------------------
Clear scope, mostly HOW left     | /blueprint (unchanged)
Fuzzy scope, no spec yet         | /brainstorm-v2 → /blueprint
Re-plan after scope shift        | /brainstorm-v2 (new scope) → /blueprint
```

`/plan-v2` (a HOW-only counterpart to `/brainstorm-v2`) is **deliberately not shipped in this PR.** Whether to ship it is gated on real usage of `/brainstorm-v2` — see `validation/04-comparison.md`.

## Output layout

Both skill pairs write under the same `blueprint/<slug>/` directory:

```text
blueprint/
└── my-feature/
    ├── requirements.md   # from brainstorm-generate-v2
    └── plan-my-feature.md  # from blueprint-generate (later, optional)
```

A feature can have just a requirements doc, just a plan doc, or both.

## Validation

The decision to build v2 was preceded by a side-by-side validation against three real `/blueprint` outputs. The artifacts live in `validation/`:

- `00-context.md` — chosen validation feature
- `01-blueprint-trace.md` — mental-model of what `/blueprint` would ask
- `02-v2-trace.md` — mental-model of what `/brainstorm-v2` then `/plan-v2` would ask
- `03-retrofit.md` — findings from retrofitting against three existing plans
- `04-comparison.md` — analysis + recommendation to build Stage 1 only

Verdict: 1/3 sampled plans (`canonical-grounding-guard`) showed severe WHAT-vs-HOW conflation (40+ revision rounds). The other two avoided it for reasons unrelated to skill design — lucky question ordering, or manual phase-splitting. v2-split formalizes the phase-splitting pattern.

## Install (same as upstream)

```bash
bash install-skills.sh
```

This symlinks all four skills (`/blueprint`, `/blueprint-generate`, `/brainstorm-v2`, `/brainstorm-generate-v2`) into `~/.claude/skills/`.
