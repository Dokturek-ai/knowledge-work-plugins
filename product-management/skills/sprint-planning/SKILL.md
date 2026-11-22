---
name: sprint-planning
description: Plan a sprint — scope work, estimate capacity, set goals, and draft a sprint plan. Use when kicking off a new sprint, sizing a backlog against team availability (accounting for PTO and meetings), deciding what's P0 vs. stretch, or handling carryover from the last sprint.
argument-hint: "[sprint name or date range]"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- Sprints are weekly GitHub milestones in `Dokturek-ai/dokturek-docs`; tasks are GitHub Issues there with an owner, expected output, spec and due date.
- Use the triage labels `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. Check for an existing issue first, and create or edit issues only after the user confirms the exact list.
- Create issues and milestones only after the user confirms the exact list: in Claude Code with `gh issue create --repo Dokturek-ai/dokturek-docs` (and `--milestone`, `--label`, `--assignee`), in claude.ai through the GitHub connector.
- Capacity and shared milestones come from [`03-implementacni-plan/plan-prvni-ordinace.md`](https://github.com/Dokturek-ai/dokturek-docs/blob/main/03-implementacni-plan/plan-prvni-ordinace.md). Never assign work to Adrian on your own.

# Sprint planning

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Plan a sprint by scoping work, estimating capacity, and setting clear goals.

## Usage

```
/product-management:sprint-planning $ARGUMENTS
```

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                    SPRINT PLANNING                                 │
├─────────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                       │
│  ✓ Define sprint goals and success criteria                     │
│  ✓ Estimate team capacity (accounting for PTO, meetings)        │
│  ✓ Scope and prioritize backlog items                           │
│  ✓ Identify dependencies and risks                              │
│  ✓ Generate sprint plan document                                │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                      │
│  + Project tracker: Pull backlog; draft milestone and issues    │
│  + Calendar: Account for PTO and meetings in capacity           │
│  + Chat: Draft a sprint-plan post (sent after you confirm)      │
└─────────────────────────────────────────────────────────────────┘
```

## What I Need From You

- **Team**: Who's on the team and their availability this sprint?
- **Sprint length**: How many days/weeks?
- **Backlog**: What's prioritized? (Pull from tracker, paste, or describe)
- **Carryover**: Anything unfinished from last sprint?
- **Dependencies**: Anything blocked on other teams?

## Output

```markdown
## Sprint Plan: [Sprint Name]
**Dates:** [Start] — [End] | **Team:** [X] engineers
**Sprint Goal:** [One clear sentence about what success looks like]

### Capacity
| Person | Available Days | Allocation | Notes |
|--------|---------------|------------|-------|
| [Name] | [X] of [Y] | [X] points/hours | [PTO, on-call, etc.] |
| **Total** | **[X]** | **[X] points** | |

### Sprint Backlog
| Priority | Item | Estimate | Owner | Dependencies |
|----------|------|----------|-------|--------------|
| P0 | [Must ship] | [X] pts | [Person] | [None / Blocked by X] |
| P1 | [Should ship] | [X] pts | [Person] | [None] |
| P2 | [Stretch] | [X] pts | [Person] | [None] |

### Planned Capacity: [X] points | Sprint Load: [X] points ([X]% of capacity)

### Risks
| Risk | Impact | Mitigation |
|------|--------|------------|
| [Risk] | [What happens] | [What to do] |

### Definition of Done
- [ ] Code reviewed and merged
- [ ] Tests passing
- [ ] Documentation updated (if applicable)
- [ ] Product sign-off

### Key Dates
| Date | Event |
|------|-------|
| [Date] | Sprint start |
| [Date] | Mid-sprint check-in |
| [Date] | Sprint end / Demo |
| [Date] | Retro |
```

## After the Plan

Offer, as drafts only:
- The list of issues to create or edit in `Dokturek-ai/dokturek-docs` (title, owner, labels, milestone, expected output). After an explicit yes: `gh issue create --repo Dokturek-ai/dokturek-docs --title "…" --body "…" --milestone "…" --label "…" --assignee "…"` in Claude Code, or the GitHub connector in claude.ai.
- A ~~chat post with the sprint plan; show the exact channel and text and post only after an explicit yes.

## Tips

1. **Leave buffer** — Plan to 70-80% capacity. You will get interrupts.
2. **One clear sprint goal** — If you can't state it in one sentence, the sprint is unfocused.
3. **Identify stretch items** — Know what to cut if things take longer than expected.
4. **Carry over honestly** — If something didn't ship, understand why before re-committing.
