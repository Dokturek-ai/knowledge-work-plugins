---
name: roadmap-update
description: Update, create, or reprioritize your product roadmap. Use when adding a new initiative and deciding what moves to make room, shifting priorities after new information comes in, moving timelines due to a dependency slip, or building a Now/Next/Later view from scratch.
argument-hint: "<update description>"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- The roadmap lives in [`01-produkt/produktova-roadmapa.md`](https://github.com/Dokturek-ai/dokturek-docs/blob/main/01-produkt/produktova-roadmapa.md). Output a proposed diff to that file, not a new roadmap document.
- Day one is 1 January 2027 with the scope confirmed in R-nový-L. CDS co-pilot, patient portal and white-label CDS are possible future extensions without a date: do not schedule them.

# Roadmap Update

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Update, create, or reprioritize a product roadmap.

## Usage

```
/product-management:roadmap-update $ARGUMENTS
```

## Workflow

### 1. Understand Current State

If **~~project tracker** is connected:
- Pull current roadmap items with their statuses, assignees, and dates
- Identify items that are overdue, at risk, or recently completed
- Surface any items without clear owners or dates

If no project management tool is connected:
- Ask the user to describe their current roadmap or paste/upload it
- Accept any format: list, table, spreadsheet, screenshot, or prose description

### 2. Determine the Operation

Ask what the user wants to do:

**Add item**: New feature, initiative, or work item to the roadmap
- Gather: name, description, priority, estimated effort, target timeframe, owner, dependencies
- Suggest where it fits based on current priorities and capacity

**Update status**: Change status of existing items
- Options: not started, in progress, at risk, blocked, completed, cut
- For "at risk" or "blocked": ask for the blocker and mitigation plan

**Reprioritize**: Change the order or priority of items
- Ask what changed (new information, strategy shift, resource change, customer feedback)
- Apply a prioritization framework if helpful — see **Prioritization** below for MoSCoW and value-vs-effort
- Show before/after comparison
- A priority change is a proposal for Honza; a change to the day-one scope is a decision proposal for the register `10-rozhodnuti-a-otevrene-otazky.md`

**Move timeline**: Shift dates for items
- Ask why (scope change, dependency slip, resource constraint)
- Identify downstream impacts on dependent items
- Flag items that move past hard deadlines, above all 1 January 2027

**Create new roadmap**: Build a roadmap from scratch
- Ask about timeframe (quarter, half, year)
- Use the structure of `01-produkt/produktova-roadmapa.md`; Now/Next/Later below only when the user asks for a summary view
- Gather the list of initiatives to include

### 3. Generate Roadmap Summary

Produce a roadmap view with:

#### Status Overview
Quick summary: X items in progress, Y completed this period, Z at risk.

#### Roadmap Items
For each item, show:
- Name and one-line description
- Status indicator (on track / at risk / blocked / completed / not started)
- Target timeframe or date
- Owner
- Key dependencies

Group items by:
- Timeframe (Now / Next / Later) or quarter, depending on format
- Or by theme/goal if the user prefers

#### Risks and Dependencies
- Items that are blocked or at risk, with details
- Cross-team dependencies and their status
- Items approaching hard deadlines

#### Changes This Update
If this is an update to an existing roadmap, summarize what changed:
- Items added, removed, or reprioritized
- Timeline shifts
- Status changes

### 4. Follow Up

After generating the roadmap:
- Offer to format for a specific audience (executive summary, engineering detail, customer-facing)
- Offer to draft communication about roadmap changes
- If ~~project tracker is connected, propose issue status changes as a list (issue, current status, proposed status, reason); change nothing until the user confirms that exact list

## Roadmap Frameworks

### Now / Next / Later
- **Now**: committed work, high confidence in scope and timing.
- **Next**: planned work, good confidence in what, less in when.
- **Later**: direction only; scope and timing flexible. Possible future extensions from the roadmap stay here without a date.

Good for communicating to leadership or externally because it avoids false precision on dates.

## Prioritization

### MoSCoW
- **Must have**: the release fails without these (for day one: the scope in R-nový-L).
- **Should have**: important, but delivery is viable without them.
- **Could have**: only if capacity allows.
- **Won't have**: explicitly out of scope for this period (for day one, e.g. offline mode).

### Value vs Effort
- **High value, low effort**: do first. **High value, high effort**: scope carefully.
- **Low value, low effort**: fill-ins. **Low value, high effort**: propose removing.

Estimates of value and effort are assumptions: mark them [P] and name who gave them.

## Dependencies

- List technical, team and external dependencies explicitly (state services such as SÚKL, ČSSZ, MZČR are external).
- Give each one an owner from the team table and a "need by" date.
- Flag dependencies on state integrations early; they are the highest-risk items.
- Capacity comes from `03-implementacni-plan/plan-prvni-ordinace.md`, not from a generic allocation rule. When adding to the roadmap, ask: "What comes off?"

## Communicating Roadmap Changes

1. State what is changing and why (the new information).
2. Show the tradeoff: what moves or comes off.
3. Show the proposed diff to `01-produkt/produktova-roadmapa.md`.
4. Name who is affected and who must confirm (Honza for priorities, Petr for technical sequencing).

Do not change the roadmap for every piece of new information; batch changes unless something is urgent.

## Output Format

Use a clear, scannable format. Tables work well for roadmap items. Use text status labels: **Done**, **On Track**, **At Risk**, **Blocked**, **Not Started**.

## Tips

- A roadmap is a communication tool, not a project plan. Keep it at the right altitude — themes and outcomes, not tasks.
- When reprioritizing, always ask what changed. Priority shifts should be driven by new information, not whim.
- Flag capacity issues early. If the roadmap has more work than the team can handle, say so.
- Dependencies are the biggest risk to roadmaps. Surface them explicitly.
- If the user asks to add something, always ask what comes off or moves. Roadmaps are zero-sum against capacity.
