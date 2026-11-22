---
name: email-sequence
description: Design and draft multi-email sequences for a list or segment of doctors and practices (newsletter subscribers, demo sign-ups, pre-order leads) with full copy, timing, branching logic and exit conditions. Use when building onboarding, lead nurture, re-engagement, educational or product launch flows, or mapping a sequence end-to-end with a flow diagram. A message to one named practice belongs to sales:draft-outreach.
argument-hint: "[sequence type]"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- Recipients are doctors: Czech, vykání, short. Each email has one call to action (demo, pre-order, call). Include an unsubscribe line. Draft only; Filip sends.
- No discounts, incentives, limited-time offers, "last chance" deadlines, upsell or win-back pressure. Price only as a link to `https://dokturek.ai/cenik`.
- No case studies, testimonials or results from practices before 1 January 2027 unless the user provides them.

# Email Sequence

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Design and draft complete email sequences with full copy, timing, branching logic, and performance benchmarks for any lifecycle or campaign use case.

## Trigger

User runs `/marketing:email-sequence` or asks to create, design, build, or draft an email sequence, drip campaign, nurture flow, or onboarding series.

## Inputs

Gather the following from the user. If not provided, ask before proceeding:

1. **Sequence type** — one of:
   - Onboarding
   - Lead nurture
   - Re-engagement
   - Product launch
   - Event follow-up
   - Educational drip

2. **Goal** — what the sequence should achieve (e.g., get doctors to try the demo, turn demo users into pre-orders, drive webinar attendance, explain a day-one feature)

3. **Audience** — who receives this sequence, what stage they are at, and any relevant segmentation details (role, industry, behavior triggers, lifecycle stage)

4. **Number of emails** (optional) — if not specified, recommend a count based on the sequence type using the templates in the Sequence Type Templates section below

5. **Timing/cadence preferences** (optional) — desired spacing between emails (e.g., "every 3 days", "weekly", "aggressive first week then taper off")

6. **Brand voice** — always use `dokturek-docs` → [`05-design/Doktůrek-brand/DESIGN.md`](https://github.com/Dokturek-ai/dokturek-docs/blob/main/05-design/Doktůrek-brand/DESIGN.md) and the Voice section of the Doktůrek context. Tell the user which source you applied; if DESIGN.md is not reachable, say so and use the Voice section.

7. **Additional context** (optional):
   - CTAs or landing pages to link to
   - Content assets available (blog posts, videos, guides; case studies only if the user provides them)
   - Product features to highlight
   - Competitor differentiators to reference

## Process

### 1. Sequence Strategy

Before drafting any emails, define the overall sequence architecture:

- **Narrative arc** — what story does this sequence tell across all emails? What is the emotional and logical progression from first email to last?
- **Journey mapping** — map each email to a stage of the buyer or user journey (awareness, consideration, decision, activation, expansion)
- **Progression** — how does the value of each email build on the previous one?
- **Success definition** — what specific action signals that the sequence has done its job and the recipient should exit?

### 2. Individual Email Design

For each email in the sequence, produce:

#### Subject Line
- Provide 2-3 options per email
- Vary approaches: curiosity, benefit-driven, personalization, question-based (no artificial urgency)
- Keep under 50 characters where possible; note preview behavior on mobile

#### Preview Text
- 40-90 characters that complement (not repeat) the subject line
- Should add context or intrigue that increases open likelihood

#### Email Purpose
- One sentence explaining why this email exists and what it moves the recipient toward

#### Body Copy
- Full draft ready to use
- Clear hierarchy: hook, body, CTA
- Short paragraphs (2-3 sentences max)
- Scannable formatting with bold key phrases where appropriate
- Personalization tokens where relevant (e.g., title and surname, practice name)

#### Primary CTA
- Button text and destination
- One primary CTA per email (secondary CTA only if appropriate for the sequence stage)

#### Timing
- Days after the trigger event or after the previous email
- Note if timing should adjust based on engagement (e.g., "send sooner if they opened but did not click")

#### Segment/Condition Notes
- Who receives this email vs. who skips it
- Any behavioral or attribute-based conditions (e.g., "only send to users who have not completed setup")

### 3. Sequence Logic

Define the flow control for the sequence:

- **Branching conditions** — alternate paths based on engagement. For example:
  - "If opened email 2 but did not click CTA, send email 2b (softer re-ask) instead of email 3"
  - "If clicked CTA in email 1, skip email 2 and go directly to email 3"
- **Exit conditions** — when a recipient converts (completes the desired action), remove them from the sequence. Define what "conversion" means for this sequence.
- **Re-entry rules** — can someone re-enter the sequence? Under what conditions? (e.g., "a demo user who already finished onboarding does not re-enter it")
- **Suppression rules** — do not send if the recipient is already in another active sequence, has unsubscribed from marketing, or has contacted support in the last 48 hours

### 4. Targets

Doktůrek has no email benchmarks of its own yet. Ask the user for targets or past newsletter results. If you quote a general industry figure, name its source and mark it [N]; never present it as an expectation for Czech doctors.

## Sequence Type Templates

Use these as starting frameworks. Adapt length and content based on the user's goal and audience.

**Onboarding (5-7 emails over 14-21 days):**
Welcome and set expectations -- Quick win to demonstrate value -- Core feature deep dive -- Advanced feature or integration -- Check-in and feedback request -- Next steps

**Lead Nurture (4-6 emails over 3-4 weeks):**
Value-first educational content -- Pain point identification -- Solution positioning with facts verified in `dokturek-docs` -- Soft CTA (demo, resource) -- Direct CTA (pre-order, book a call)

**Re-engagement (2-3 emails over 2-3 weeks):**
What is new in Doktůrek -- Value reminder -- Simple question whether they still want to hear from us, with an easy unsubscribe

**Product Launch (4-6 emails over 2-3 weeks):**
Teaser or pre-announcement -- Launch announcement with full details -- Feature spotlight or use case -- Practical how-to or FAQ -- Reminder with the same CTA

**Event Follow-up (3-4 emails over 7-10 days):**
Thank you with key takeaways or recordings -- Resource roundup from the event -- Next step (demo, call) -- Feedback survey

**Educational Drip (5-8 emails over 4-6 weeks):**
Introduction and what they will learn -- Lesson 1: foundational concept -- Lesson 2: intermediate concept -- Lesson 3: advanced concept -- Practical application or exercise -- Resource roundup -- Graduation and next steps

## Tool Integration

### If ~~email marketing is connected
- Reference how to set up the sequence as a flow or automation in the platform
- Note any platform-specific features to use (e.g., smart send time, conditional splits, A/B testing)
- Map the branching logic to the platform's visual flow builder concepts
- Creating or activating the flow is a change: show the exact setup and wait for an explicit yes

### If ~~marketing automation or ~~CRM is connected
- Reference lead scoring data to inform segmentation and exit conditions
- Use lifecycle stage data to tailor messaging per segment
- Note how to set enrollment triggers based on CRM properties or list membership

### If no tools are connected
- Deliver all email content in copy-paste-ready format
- Include a setup checklist the user can follow in any email platform:
  1. Create the automation or flow
  2. Set the enrollment trigger
  3. Add each email with the specified delays
  4. Configure branching and exit conditions
  5. Set up tracking for the recommended metrics

## Output

Present the complete sequence with the following sections:

### Sequence Overview Table

| # | Subject Line | Purpose | Timing | Primary CTA | Condition |
|---|-------------|---------|--------|-------------|-----------|

### Full Email Drafts
Each email with subject line options, preview text, purpose, body copy, CTA, timing, and segment notes.

### Sequence Flow Diagram
A text-based diagram showing the email flow, branching paths, and exit points. Use a clear format such as:

```
[Trigger] --> Email 1 (Day 0)
                |
          Opened? --Yes--> Email 2 (Day 3)
                |              |
                No        Clicked CTA? --Yes--> [EXIT: Converted]
                |              |
                v              No
          Email 1b (Day 2)     |
                |              v
                +--------> Email 3 (Day 7)
                               |
                               v
                          Email 4 (Day 10)
                               |
                          [EXIT: Sequence complete]
```

### Branching Logic Notes
Summary of all conditions, exits, and suppressions in a reference list.

### A/B Test Suggestions
- 2-3 recommended A/B tests (subject lines, CTA text, send time, email length)
- What to test, how to split, and how to measure the winner

### Metrics to Track
- Primary conversion metric for the sequence
- Per-email metrics: open rate, CTR, unsubscribe rate
- Sequence-level metrics: overall conversion rate, time to conversion, drop-off points
- Recommended review cadence (e.g., "Review performance weekly for the first month, then monthly")

## After the Sequence

Ask: "Would you like me to:
- Revise the copy or tone for any specific email?
- Add a branching path for a specific scenario?
- Create a variation of this sequence for a different audience segment?
- Draft the A/B test variants for the subject lines?
- Build a companion sequence (e.g., a follow-up after a demo sign-up)?"
