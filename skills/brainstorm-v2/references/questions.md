# Questions

Output a numbered question list in the conversation (NOT in any file):

```
> Answer with shorthand like `1a, 2b, 3e` or write freely.

---

**Q1. [Question text]**

_Context: [1-2 line snippet from the evolving requirements or anchor docs]_

a) Option A
b) Option B
c) Option C
d) Other (describe)


**Q2. [Question text]** (select all that apply)

_Context: [1-2 line snippet]_

a) Option A
b) Option B
c) Other (describe)


**Q3. [Open-ended question text]**

_Context: [1-2 line snippet]_
```

Leave two blank lines between questions. Leave a blank line between question text, context line, and options.

For questions with clear enumerable scope options, provide lettered choices. Always include a final "Other (describe)" option. If a question is better answered with free text, omit choices.

Each question must answer ONE of four scope dimensions:
- **Problem** — what we're solving / failure mode if we don't
- **Personas** — who's affected and how
- **Success criteria** — what does done look like, observably
- **Out of scope** — what stays out this cycle

Do NOT ask:
- Which files to touch
- Test strategy
- Rollback approach
- PR sequencing
- Architectural patterns
- Any question whose answer is a code shape

If a question is genuinely ambiguous between WHAT and HOW, ask the WHAT version. ("What's the rollback model?" is HOW. "What does it mean for this feature to be reversible by the user?" is WHAT.)
