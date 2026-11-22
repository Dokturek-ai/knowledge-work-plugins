---
name: campaign-plan
description: Generate a full campaign brief with objectives, audience, messaging, channel strategy, content calendar, and success metrics. Use when planning a product launch, lead-gen push, or awareness campaign, when you need a week-by-week content calendar with dependencies, or when translating a marketing goal into a structured, executable plan.
argument-hint: "<campaign objective or product>"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- Current motions: Meta ads to the landing page `get.dokturek.ai` (leads go to Pipedrive and Slack `#pr-and-outreach`), and Filip's newsletter inviting doctors to try the demo and pre-order, ahead of paid operation from 1 January 2027.
- Email campaigns need a lawful basis and an unsubscribe path under GDPR; flag any list without documented consent.

# Campaign Plan

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Generate a comprehensive marketing campaign brief with objectives, audience, messaging, channel strategy, content calendar, and success metrics.

## Trigger

User runs `/marketing:campaign-plan` or asks to plan, design, or build a marketing campaign.

## Inputs

Gather the following from the user. If not provided, ask before proceeding:

1. **Campaign goal** — the primary objective (e.g., get GPs to try the demo, collect pre-orders, generate leads from Meta ads, announce a day-one feature)

2. **Target audience** — who the campaign is aimed at (demographics, roles, industries, pain points, buying stage)

3. **Timeline** — campaign duration and any fixed dates (launch date, event date, seasonal deadline)

4. **Budget range** — the campaign budget the user gives (optional; if not provided, generate a channel-agnostic plan and note where budget allocation would matter). Never ask about or infer company revenue or finances: those are for leadership only

5. **Additional context** (optional):
   - Product or service being promoted
   - Key differentiators or value propositions
   - Previous campaign performance or learnings
   - Brand guidelines or constraints
   - Geographic focus

## Campaign Brief Structure

Generate a campaign brief with the following sections:

### 1. Campaign Overview
- Campaign name suggestion
- One-sentence campaign summary
- Primary objective with a specific, measurable goal
- Secondary objectives (if applicable)

### 2. Target Audience
- Primary audience segment with description
- Secondary audience segment (if applicable)
- Audience pain points and motivations
- Where they spend time (channels, communities, publications)
- Buying stage alignment (awareness, consideration, decision)

### 3. Key Messages
- Core campaign message (one sentence)
- 3-4 supporting messages tailored to audience pain points
- Message variations by channel (if different tones are needed)
- Proof points: only facts verifiable in `dokturek-docs`; no testimonials, case studies or results before 1 January 2027 unless the user provides them

### 4. Channel Strategy
Recommend channels based on audience and goal. For each channel, include:
- Why this channel fits the audience and objective
- Content format recommendations
- Estimated effort level (low, medium, high)
- Budget allocation suggestion (if budget was provided)

Consider channels from:
- Owned: blog, email, website, social media profiles
- Earned: PR, influencer partnerships, guest posts, community engagement
- Paid: search ads, social ads, display, sponsored content, events

### 5. Content Calendar
Create a week-by-week (or day-by-day for short campaigns) content calendar:
- What content to produce each week
- Which channel each piece targets
- Key milestones and deadlines
- Dependencies between pieces (e.g., "landing page must be live before paid ads launch")

Format as a table:

| Week | Content Piece | Channel | Owner/Notes | Status |
|------|--------------|---------|-------------|--------|

### 6. Content Pieces Needed
List every content asset required for the campaign:
- Asset name and type (blog post, email, social post, ad creative, landing page, etc.)
- Brief description of what it should contain
- Priority (must-have vs. nice-to-have)
- Suggested timeline for creation

### 7. Success Metrics
Define KPIs aligned to the campaign objective:
- Primary KPI with target number
- Secondary KPIs (3-5)
- How each metric will be tracked
- Reporting cadence recommendation

If ~~product analytics is connected, reference any available historical performance benchmarks to inform targets.

### 8. Budget Allocation (if budget provided)
- Breakdown by channel or activity
- Production costs vs. distribution costs
- Contingency recommendation (typically 10-15%)

### 9. Risks and Mitigations
- 2-3 potential risks (timeline, audience mismatch, channel underperformance)
- Mitigation strategy for each

### 10. Next Steps
- Immediate action items to kick off the campaign
- Stakeholder approvals needed
- Key decision points

## Planning Reference

### Objective, Audience, Message, Channel, Measure

- **Objective** — SMART, with the target number from the user. Example shape: "[N] demo sign-ups from GPs via `get.dokturek.ai` within 6 weeks."
- **Audience** — one-line profile: "[Role] in [type of practice] who struggles with [pain point] and wants [outcome]. They find solutions through [channels] and care most about [priorities]."
- **Message** — hierarchy: why should I care, what is the solution, why Doktůrek, what should I do. Use the messaging pillars from the Doktůrek context.
- **Channel** — where the audience is (see below).
- **Measure** — one primary KPI tied to the objective.

### Channels

| Channel | Best for | Metrics | Note |
|---------|----------|---------|------|
| Meta ads → `get.dokturek.ai` | Lead capture | Cost per lead, leads in Pipedrive "Inbound leads" | Running today |
| Newsletter (Filip) | Demo invitations, pre-orders | Opens, clicks, demo sign-ups, pre-orders | Running today |
| `dokturek.ai` web | SEO, price page `/cenik` | Organic traffic, conversions | See `seo-audit` |
| Social (organic), PR, professional events, webinars | Awareness, trust | Reach, registrations, leads | Mark as a new channel to be approved by Filip and Honza |

### Content Calendar

1. **Start with milestones**: launch dates, events, 1 January 2027
2. **Work backward**: what must be live when, and the production lead time
3. **Map content to funnel stages**: awareness, consideration, conversion
4. **Note dependencies**: e.g., the landing page must be live before ads launch; clinical statements need Anna's confirmation before publication

### Success Metrics

| Campaign type | Primary metrics |
|---------------|-----------------|
| Lead generation | Leads, cost per lead, lead-to-demo rate |
| Demo / pre-order push | Demo sign-ups, activated demo users, pre-orders |
| Launch of a feature | Reach, clicks, demo sign-ups, questions received |
| Event / webinar | Registrations, attendance rate, follow-up conversions |

Without historical data, targets are assumptions: mark them [P] and say who sets them.

## Output

Present the full campaign brief with clear headings and formatting. After the brief, ask:

"Would you like me to:
- Dive deeper into any section?
- Draft specific content pieces from the calendar?
- Create a competitive analysis to inform the messaging?
- Adjust the plan for a different budget or timeline?"
