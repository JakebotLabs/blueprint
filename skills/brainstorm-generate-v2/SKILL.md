---
name: brainstorm-generate-v2
description: End the brainstorm-v2 Q&A phase and write the requirements doc. Use after brainstorm-v2 has gathered enough scope clarity.
---

## Brainstorm-v2 — Write requirements

End the WHAT-only Q&A and persist `requirements.md`.

### Step 1: Generate slug

Create a concise 2-5 word kebab-case slug (max 50 chars) for the feature. Sanitize: lowercase, alphanumeric + hyphens only, no leading/trailing hyphens. If `blueprint/<slug>` already exists, append `-2`, `-3`, etc.

The slug lives under the same `blueprint/` directory as `/blueprint`-style plans, so a feature can later receive a `plan-<slug>.md` next to its `requirements.md`.

### Step 2: Create the feature directory

```bash
mkdir -p blueprint/<slug>
```

### Step 3: Synthesize the most recent refined requirements

Use the most recent refined requirements from the Q&A conversation. If for any reason it wasn't shown in the most recent round, regenerate now per [refine-requirements.md](../brainstorm-v2/references/refine-requirements.md).

### Step 4: Write requirements.md

See [references/write-requirements.md](references/write-requirements.md) for assembly instructions and [references/requirements-template.md](references/requirements-template.md) for the canonical section structure.

Output path: `blueprint/<slug>/requirements.md`.

Append this progress line at the end of every message during Step 4:

```
✓ Explore  ✓ Scope  ● Write
```

Place the line after all other content, separated by a blank line.

### Step 5: Hand off

After writing, tell the user:
- The requirements file path (in a code block so it's easy to copy)
- That they can run `/plan-v2` (when available) or `/blueprint` against this doc for implementation planning
- That the requirements doc is durable — they can edit it directly, or re-run `/brainstorm-v2` to refine

Do NOT enter a refinement phase. Brainstorm-v2 keeps termination clean. If the user wants to refine, they invoke `/brainstorm-v2` again with the existing requirements as context.

After Step 5, the skill exits — no more progress lines.
