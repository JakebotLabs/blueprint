---
name: brainstorm-v2
description: Start a WHAT-only scope-locking session for a new feature. Produces a durable requirements doc through multi-round Q&A. Hand off to /plan-v2 or /blueprint for implementation planning.
---

## Brainstorm-v2 — Lock scope before implementation

Start a WHAT-only Q&A session. The goal is to produce a `requirements.md` artifact that locks the feature's PROBLEM / PERSONAS / SUCCESS CRITERIA / OUT OF SCOPE / OPEN QUESTIONS before any implementation planning. Implementation questions belong in `/plan-v2` (or in a `/blueprint` run that consumes this requirements doc) — DO NOT ask them here.

### Step 1: Parse the feature description

Parse the user's message for the feature description. If empty or under ~10 words, ask for a longer description before proceeding — under-specified scope is the failure mode this skill exists to prevent.

### Step 2: Light-touch grounding

Scan the workspace for:
- `project_*.md` files in the user's memory directory that match the feature area (these are anchor docs — read them as authoritative product context)
- Open Issues and recent merged PRs referencing the feature name (for state-of-the-world)
- The repo's CLAUDE.md and any user-facing README (for personas and product framing)

DO NOT do deep source-file reading here. That's `/plan-v2`'s job. Grounding here is enough to ask informed WHAT questions, no more.

If anchor docs exist, lead the first question round with: "Anchor docs found: `[list]`. I'll honor these unless your answers contradict them."

### Step 3: Ask 3-5 scope-only questions

Cover four scope dimensions across the questions:
- **Problem** — what are we actually solving?
- **Personas** — who's the user, who's affected?
- **Success criteria** — what does "done" look like, observably?
- **Out of scope** — what stays out this cycle?

Format per [references/questions.md](references/questions.md). Always include the shorthand hint before the questions:

```
> Answer with shorthand like `1a, 2b, 3e` or write freely.
```

And the generate-skill reminder after:

```
Once you're done answering, I'll follow up with more questions. When you're ready, invoke the brainstorm-generate-v2 skill to end the Q&A and write the requirements doc.
```

DO NOT ask implementation questions:
- "Which file should we touch?" — NO. That's /plan-v2.
- "Test strategy?" — NO. That's /plan-v2.
- "Rollback approach?" — NO. That's /plan-v2.
- "Single PR or multiple?" — NO. That's /plan-v2.

If you catch yourself drafting a HOW question, drop it and ask the underlying WHAT question instead. ("What's the rollback model?" → "What does it mean for this feature to be reversible?")

### Step 4: Continue Q&A — round-by-round refinement

Accept answers in any format (shorthand, prose, mixed). When the user answers:
- Acknowledge briefly
- Show the updated **refined requirements** — see [references/refine-requirements.md](references/refine-requirements.md). Display in a blockquote so the user sees scope locking in.
- ALWAYS ask 3-5 more questions. These may be follow-ups or new scope dimensions. Use the same format as Step 3.
- Keep going round-by-round until the user invokes the brainstorm-generate-v2 skill.

IMPORTANT: Do NOT stop asking questions on your own. Only the user terminates by invoking brainstorm-generate-v2. Do NOT write any files. Do NOT modify code.

### Progress indicator

After Step 1 succeeds (feature description provided), append a progress line at the end of every message:

```
✓ Explore  ● Scope  ○ Write
```

`Explore` completes after Step 2 (light grounding). Place the line after all other content, separated by a blank line.

DO NOT show the progress line before Step 1 succeeds (e.g. when asking for a longer feature description).
