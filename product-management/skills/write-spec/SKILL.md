---
name: write-spec
description: Write a spec for a non-clinical Doktůrek feature or process (practice onboarding, subscription and billing, migration from an incumbent AIS, internal processes, the website) from a problem statement or idea. Use when turning a vague idea or request into a structured document, scoping with goals and non-goals, defining success metrics and acceptance criteria, or phasing a big ask. Clinical EHR screens, workflows and PRDs belong to the ehr-design plugin (ehr-prd).
argument-hint: "<feature or problem statement>"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- Clinical EHR screens and workflows go to `ehr-design` (`ehr-prd`, `ehr-user-stories`). Use this skill for non-clinical specs: onboarding of a practice, billing and subscription, migration, internal processes, the website. A spec for an AI or decision-support feature also needs `cz-health-ai` (`ai-feature-readiness`).
- Check the day-one scope in [`01-produkt/prvni-den-2027.md`](https://github.com/Dokturek-ai/dokturek-docs/blob/main/01-produkt/prvni-den-2027.md) and the register before you add scope. Scope decisions are Honza's.
- A spec that changes product behaviour lives in `dokturek-docs`; a code PR without the linked docs PR goes back from review (R-nový-G).

# Write Spec

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Write a feature specification or product requirements document (PRD).

## Usage

```
/product-management:write-spec $ARGUMENTS
```

## Workflow

### 1. Understand the Feature

Ask the user what they want to spec. Accept any of:
- A feature name ("pozvánky do týmu ordinace")
- A problem statement ("Practices migrating from PC Doktor need to know which data comes over")
- A user request ("The founding admin wants to download the subscription invoices")
- A vague idea ("Onboarding of a new practice should take less of the doctor's time")

### 2. Gather Context

Ask the user for the following. Be conversational — do not dump all questions at once. Ask the most important ones first and fill in gaps as you go:

- **User problem**: What problem does this solve? Who experiences it?
- **Target users**: Which user segment(s) does this serve?
- **Success metrics**: How will we know this worked?
- **Constraints**: Technical constraints, timeline, regulatory requirements, dependencies
- **Prior art**: Has this been attempted before? Are there existing solutions?

### 3. Pull Context from Connected Tools

If **~~project tracker** is connected:
- Search for related tickets, epics, or features
- Pull in any existing requirements or acceptance criteria
- Identify dependencies on other work items

If **~~knowledge base** is connected:
- Search for related research documents, prior specs, or design docs
- Pull in relevant user research findings
- Find related meeting notes or decision records

If **~~design** is connected:
- Pull related mockups, wireframes, or design explorations
- Search for design system components relevant to the feature

If these tools are not connected, work entirely from what the user provides. Do not ask the user to connect tools — just proceed with available information.

### 4. Generate the PRD

Produce a structured PRD with these sections. See **PRD Structure** below for detailed guidance on what each section should contain.

- **Problem Statement**: The user problem, who is affected, and impact of not solving it (2-3 sentences)
- **Goals**: 3-5 specific, measurable outcomes tied to user or business metrics
- **Non-Goals**: 3-5 things explicitly out of scope, with brief rationale for each
- **User Stories**: Standard format ("As a [user type], I want [capability] so that [benefit]"), grouped by persona
- **Requirements**: Categorized as Must-Have (P0), Nice-to-Have (P1), and Future Considerations (P2), each with acceptance criteria
- **Success Metrics**: Leading indicators (change quickly) and lagging indicators (change over time), with specific targets
- **Open Questions**: Unresolved questions tagged with the owner who needs to answer
- **Timeline Considerations**: Hard deadlines, dependencies, and phasing

### 5. Review and Iterate

After generating the PRD:
- Ask the user if any sections need adjustment
- Offer to expand on specific sections
- Offer to create follow-up artifacts (design brief, engineering ticket breakdown, stakeholder pitch)

## PRD Structure

### Problem Statement
- Describe the user problem in 2-3 sentences
- Who experiences this problem and how often
- What is the cost of not solving it (user pain, business impact, competitive risk)
- Ground this in evidence: user research, support data, metrics, or customer feedback

### Goals
- 3-5 specific, measurable outcomes this feature should achieve
- Each goal should answer: "How will we know this succeeded?"
- Distinguish between user goals (what users get) and business goals (what the company gets)
- Goals should be outcomes, not outputs ("reduce time to first value by 50%" not "build onboarding wizard")

### Non-Goals
- 3-5 things this feature explicitly will NOT do
- Adjacent capabilities that are out of scope for this version
- For each non-goal, briefly explain why it is out of scope (not enough impact, too complex, separate initiative, premature)
- Non-goals prevent scope creep during implementation and set expectations with stakeholders

### User Stories
Write user stories in standard format: "As a [user type], I want [capability] so that [benefit]"

Guidelines:
- The user type should be specific enough to be meaningful ("enterprise admin" not just "user")
- The capability should describe what they want to accomplish, not how
- The benefit should explain the "why" — what value does this deliver
- Include edge cases: error states, empty states, boundary conditions
- Include different user types if the feature serves multiple personas
- Order by priority — most important stories first

Example:
- "As the founding admin of a practice, I want to invite a nurse by e-mail so that she can start working in our practice"
- "As an invited nurse, I want the invitation to tell me in Czech what to do next so that I can sign in without calling support"
- "As the founding admin, I want to see pending invitations so that I can resend or cancel one"

### Requirements

**Must-Have (P0)**: The feature cannot ship without these. These represent the minimum viable version of the feature. Ask: "If we cut this, does the feature still solve the core problem?" If no, it is P0.

**Nice-to-Have (P1)**: Significantly improves the experience but the core use case works without them. These often become fast follow-ups after launch.

**Future Considerations (P2)**: Explicitly out of scope for v1 but we want to design in a way that supports them later. Documenting these prevents accidental architectural decisions that make them hard later.

For each requirement:
- Write a clear, unambiguous description of the expected behavior
- Include acceptance criteria (see below)
- Note any technical considerations or constraints
- Flag dependencies on other teams or systems

### Open Questions
- Questions that need answers before or during implementation
- Tag each with the owner from the team table (Honza product, Petr technology, Anna clinical); a question that needs a decision becomes a proposed Q entry for `10-rozhodnuti-a-otevrene-otazky.md`
- Distinguish between blocking questions (must answer before starting) and non-blocking (can resolve during implementation)

### Timeline Considerations
- Hard deadlines (contractual commitments, events, compliance dates)
- Dependencies on other teams' work or releases
- Suggested phasing if the feature is too large for one release

## User Stories, Priorities and Metrics

- Good user stories are independent, valuable, small and testable. Describe the need, not the UI widget; split anything that cannot be done in one weekly sprint.
- Prioritize requirements as P0/P1/P2 above; for MoSCoW and value-vs-effort see `roadmap-update`. Challenge every P0: "Would we really not ship without this?"
- Success metrics: prefer leading indicators that move within weeks (adoption, task completion, time to complete, error rate, support requests on the topic). Targets without data are assumptions: mark them [P] and say who set them, and define how and when they are measured.

## Acceptance Criteria

Write acceptance criteria in Given/When/Then format or as a checklist:

**Given/When/Then**:
- Given [precondition or context]
- When [action the user takes]
- Then [expected outcome]

Example:
- Given the founding admin is signed in to the practice
- When they invite a colleague by e-mail
- Then the colleague receives a Czech invitation and the invitation appears as pending

**Checklist format**:
- [ ] The admin can enter the colleague's e-mail and role
- [ ] A pending invitation can be resent or cancelled
- [ ] An expired or cancelled invitation shows a clear Czech message
- [ ] No patient data appears in the invitation

Cover the happy path, error cases and edge cases; describe behaviour, not implementation; include what should NOT happen; avoid words like "fast" or "intuitive" without a concrete meaning. Verify any product fact used in an example against `dokturek-docs` or the code before it goes into a real spec.

## Scope Management

- Write explicit non-goals in every spec.
- Any scope addition comes with a scope removal or a later phase; scope decisions are Honza's.
- Separate v1 from later phases clearly, and keep a parking lot for good ideas that are out of scope.

## Output Format

Use markdown with clear headers. Keep the document scannable — busy stakeholders should be able to read just the headers and bold text to get the gist.

## Tips

- Be opinionated about scope. It is better to have a tight, well-defined spec than an expansive vague one.
- If the user's idea is too big for one spec, suggest breaking it into phases and spec the first phase.
- Success metrics should be specific and measurable, not vague ("improve user experience").
- Non-goals are as important as goals. They prevent scope creep during implementation.
- Open questions should be genuinely open — do not include questions you can answer from context.
