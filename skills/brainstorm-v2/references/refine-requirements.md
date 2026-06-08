# Refine requirements

Synthesize the Q&A conversation into an evolving requirements snapshot. Display in a blockquote so the user sees scope locking in.

Structure as a draft of the eventual `requirements.md` — Problem, Personas, Success Criteria, Out of Scope, Open Questions. Mark sections as `_(not yet asked)_` if the Q&A hasn't touched them yet.

Rules:
- Use the user's original feature description as the seed for `Problem`
- ONLY incorporate decisions the user has actively answered — never invent
- Mark unresolved scope as `_(open — TBD)_` rather than guessing
- Keep it short — bullet points, not paragraphs
- Each Q&A round should crispen one or two sections; not every section moves every round
- Do not add explanations or commentary
- If anchor docs (`project_*.md`) were honored, cite them by name in the relevant section

Example shape after round 1:

```
> # <Feature> — refined requirements (round 1)
>
> ## Problem
> - <restate from feature description>
> - <one decision the user made this round>
>
> ## Personas
> - **<persona> (role)** — what they need
>
> ## Success criteria
> _(open — TBD)_
>
> ## Out of scope
> - <explicit non-goal from this round>
>
> ## Open questions
> - <unresolved scope item flagged for next round>
```
