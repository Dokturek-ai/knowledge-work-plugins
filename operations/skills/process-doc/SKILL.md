---
name: process-doc
description: Document a business process — flowcharts, RACI, and SOPs. Use when formalizing a process that lives in someone's head, building a RACI to clarify who owns what, writing an SOP for a handoff or audit, or capturing the exceptions and edge cases of how work actually gets done.
argument-hint: "<process name or description>"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- Operational guides and runbooks for engineers go to `technical-documentation`. Use this skill for business processes: onboarding a practice, support, vendor and authority communication.
- The SOP is a draft. Notion is a read-only archive: never create or edit a Notion page. The durable home is `dokturek-docs`, so propose a pull request there (target path, branch name and full text) and open it only after an explicit yes. Issues for improvement actions are drafts too: show the repository and exact text first.

# /process-doc

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Document a business process as a complete standard operating procedure (SOP).

## Usage

```
/operations:process-doc $ARGUMENTS
```

## How It Works

Walk me through the process — describe it, paste existing docs, or just tell me the name and I'll ask the right questions. I'll produce a complete SOP.

## Output

```markdown
## Process Document: [Process Name]
**Owner:** [Person/Team] | **Last Updated:** [Date] | **Review Cadence:** [Quarterly/Annually]

### Purpose
[Why this process exists and what it accomplishes]

### Scope
[What's included and excluded]

### RACI Matrix
| Step | Responsible | Accountable | Consulted | Informed |
|------|------------|-------------|-----------|----------|
| [Step] | [Who does it] | [Who owns it] | [Who to ask] | [Who to tell] |

### Process Flow
[ASCII flowchart or step-by-step description]

### Detailed Steps

#### Step 1: [Name]
- **Who**: [Role]
- **When**: [Trigger or timing]
- **How**: [Detailed instructions]
- **Output**: [What this step produces]

#### Step 2: [Name]
[Same format]

### Exceptions and Edge Cases
| Scenario | What to Do |
|----------|-----------|
| [Exception] | [How to handle it] |

### Metrics
| Metric | Target | How to Measure |
|--------|--------|----------------|
| [Metric] | [Target] | [Method] |

### Related Documents
- [Link to related process or policy]
```

## If Connectors Available

If **~~knowledge base** is connected:
- Search for existing process documentation (`dokturek-docs` first, Notion only as a read-only archive) to update rather than duplicate
- Propose the SOP as a pull request to `dokturek-docs`: show the target path and the exact text, and open the PR only after an explicit yes. Never write to Notion

If **~~project tracker** is connected:
- Link the process to related issues and workflows
- Draft issues for process improvement action items (GitHub Issues in `Dokturek-ai/dokturek-docs`); create them only after the user confirms the repository and the exact text of each

## Tips

1. **Start messy** — You don't need a perfect description. Tell me how it works today and I'll structure it.
2. **Include the exceptions** — "Usually we do X, but sometimes Y" is the most valuable part to document.
3. **Name the people** — Even if roles change, knowing who does what today helps get the process right.
