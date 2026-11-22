---
name: customer-escalation
description: Package an escalation for the right Doktůrek owner (Petr, Kuba, Martin Marhold, Anna, Honza) with full context. Use when a bug needs technical attention beyond normal support, multiple practices report the same issue, a practice is unhappy enough to leave, or an issue has sat unresolved too long. A failed eRecept or eNeschopenka goes to operations incident-response first.
argument-hint: "<issue summary> [customer name]"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- Escalation owners: technical and integrations → Petr; infrastructure and outages → Kuba; identity and gateway → Martin Marhold; clinical questions → Anna; contract, price or relationship → Honza.
- A failed or unclear eRecept or eNeschopenka is an incident, not a normal escalation: hand it to operations `incident-response` first and attach this brief there.
- Nothing is posted, sent or filed without confirmation of the exact channel or recipient and text. Reminders and follow-up nudges are OpenClaw's job, not this skill's.

# Customer escalation

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Package a support issue into a structured escalation brief for the right Doktůrek owner. Gathers context, structures reproduction steps, assesses impact on practices, and identifies the owner.

## Usage

```
/customer-support:customer-escalation <issue description> [practice name]
```

Examples:
- `/customer-support:customer-escalation Uložený dekurz se ordinaci po obnovení stránky nezobrazuje`
- `/customer-support:customer-escalation Tři ordinace tento týden hlásí, že nejde přihlášení přes Keycloak`
- `/customer-support:customer-escalation eNeschopenka se v jedné ordinaci opakovaně neodeslala`
- `/customer-support:customer-escalation Ordinace zvažuje odchod kvůli chybějící funkci`

## Workflow

### 1. Understand the Issue

Parse the input and determine:

- **What's broken or needed**: The core technical or product issue
- **Who's affected**: Specific customer(s), segment, or all users
- **How long**: When did this start? How long has the customer been waiting?
- **What's been tried**: Any troubleshooting or workarounds attempted
- **Why escalate now**: What makes this need attention beyond normal support

Use the "When to Escalate vs. Handle in Support" criteria below to confirm this warrants escalation.

### 2. Gather Context

Pull together relevant information from available sources:

- **~~support platform**: Related tickets, timeline of communications, previous troubleshooting
- **~~CRM** (if connected): Account details, key contacts, previous escalations
- **~~chat**: Internal discussions about this issue, similar reports from other customers
- **~~project tracker** (if connected): Related bug reports or feature requests, engineering status
- **~~knowledge base**: Known issues or workarounds, relevant documentation

### 3. Assess Business Impact

Using the impact dimensions below, quantify:

- **Breadth**: How many customers/users affected? Growing?
- **Depth**: Blocked vs. inconvenienced?
- **Duration**: How long has this been going on?
- **Day-one scope**: Does it touch eRecept, patient identification in the registries, eNeschopenka or dekurz storage?
- **Time pressure**: Hard deadline?

### 4. Determine Escalation Target

Using the escalation owners below, identify the right person. For a failed or unclear eRecept or eNeschopenka, stop here and hand over to operations `incident-response`.

### 5. Structure Reproduction Steps (for bugs)

If the issue is a bug, follow the reproduction step best practices below to document clear repro steps with environment details and evidence.

### 6. Generate Escalation Brief

```
## ESCALATION: [One-line summary]

**Severity:** [Critical / High / Medium]
**Owner:** [Name from the escalation owners table]
**Reported by:** [Your name/team]
**Date:** [Today's date]

### Impact
- **Customers affected:** [Who and how many]
- **Workflow impact:** [What they can't do]
- **Day-one scope touched:** [eRecept / registries / eNeschopenka / dekurz / none]
- **Time in queue:** [How long this has been an issue]

### Issue Description
[Clear, concise description of the problem — 3-5 sentences]

### What's Been Tried
1. [Troubleshooting step and result]
2. [Troubleshooting step and result]
3. [Troubleshooting step and result]

### Reproduction Steps
[If applicable — follow the format below]
1. [Step]
2. [Step]
3. [Step]
Expected: [X]
Actual: [Y]
Environment: [Details]

### Customer Communication
- **Last update to customer:** [Date and what was communicated]
- **Customer expectation:** [What they're expecting and by when]
- **Escalation risk:** [Will they escalate further if not resolved by X?]

### What's Needed
- [Specific ask — "investigate root cause", "prioritize fix",
  "make product decision on X", "approve exception for Y"]
- **Deadline:** [When this needs resolution or an update]

### Supporting Context
- [Related tickets or links]
- [Internal discussion threads]
- [Documentation or logs]
```

### 7. Offer Next Steps

After generating the escalation:
- "Want me to prepare this for a ~~chat channel? Tell me the channel; I will show the exact text and post only after your explicit yes."
- "Should I draft an interim reply to the practice (`draft-response`)?"
- "Should I draft a GitHub issue in `Dokturek-ai/dokturek-docs` from this brief? It is created only after you confirm."

---

## When to Escalate vs. Handle in Support

### Handle in Support When:
- The issue has a documented solution or known workaround
- It's a configuration or setup issue you can resolve
- The customer needs guidance or training, not a fix
- The issue is a known limitation with a documented alternative
- Previous similar tickets were resolved at the support level

### Escalate When:
- **Technical**: Bug confirmed and needs a code fix, infrastructure investigation needed, data corruption or loss
- **Complexity**: Issue is beyond support's ability to diagnose, requires access support doesn't have, involves custom implementation
- **Impact**: Multiple customers affected, production system down, data integrity at risk, security concern
- **Business**: A practice is considering leaving, asks for a price or contract exception, or asks for Honza directly
- **Time**: The practice has been blocked or waiting unreasonably long, normal handling isn't progressing
- **Pattern**: Same issue reported by 3+ customers, recurring issue that was supposedly fixed, increasing severity over time

## Escalation Owners

Doktůrek has no support tiers, security team or leadership queue. Escalate to a named owner (team table in the Doktůrek context):

| Owner | When | What to include |
|-------|------|-----------------|
| **Operations `incident-response`** | Failed or unclear eRecept or eNeschopenka, outage affecting practices | Time, affected practices, exact error text, what the doctor did |
| **Petr Sovadina** | Confirmed bug, architecture, state integrations, data access or security concern | Reproduction steps, environment, logs, impact |
| **Jakub Sekula (Kuba)** | Infrastructure, environments, deploys, availability, performance | Time window, environment, symptoms, monitoring links |
| **Martin Marhold** | Login, Keycloak, identity, gov-gateway | Account (no patient data), time, exact error, browser |
| **MUDr. Anna Chromcová** | Anything clinical: content, safety, wording for doctors | The clinical question and the text concerned |
| **Jan Chromec (Honza)** | Contract, price, subscription, relationship, feature priority, a practice considering leaving | Practice, request, what was already said |

Security concerns skip any queue: go straight to Petr. Integration details of eRecept, registries or eNeschopenka can also involve Jan Rožánek; ask Petr when unsure.

## Business Impact Assessment

When escalating, quantify impact where possible:

### Impact Dimensions

| Dimension | Questions to Answer |
|-----------|-------------------|
| **Breadth** | How many customers/users are affected? Is it growing? |
| **Depth** | How severely are they impacted? Blocked vs. inconvenienced? |
| **Duration** | How long has this been going on? How long until it's critical? |
| **Day-one scope** | Does it touch eRecept, registries, eNeschopenka or dekurz storage? |
| **Reputation** | Could this become public? |
| **Clinical safety** | Could a doctor act on wrong or missing data? If yes, include Anna. |

### Severity Shorthand

- **Critical**: Production down, data at risk, security breach, failed eRecept or eNeschopenka, or several practices blocked. Needs immediate attention.
- **High**: Major functionality broken, a practice blocked in its daily work. Needs same-day attention.
- **Medium**: Significant issue with workaround, important but not urgent business impact. Needs attention this week.

## Writing Reproduction Steps

Good reproduction steps are the single most valuable thing in a bug escalation. Follow these practices:

1. **Start from a clean state**: Describe the starting point (account type, configuration, permissions)
2. **Be specific**: "Click the Export button in the top-right of the Dashboard page" not "try to export"
3. **Include exact values**: Use specific inputs, dates, IDs — not "enter some data"
4. **Note the environment**: Browser, OS, account type, feature flags, plan level
5. **Capture the frequency**: Always reproducible? Intermittent? Only under certain conditions?
6. **Include evidence**: Screenshots, error messages (exact text), network logs, console output
7. **Note what you've ruled out**: "Tested in Chrome and Firefox — same behavior" "Not account-specific — reproduced on test account"

## Follow-up Cadence After Escalation

Don't escalate and forget. Maintain ownership of the practice relationship. The rhythm below is internal only: never promise it to the practice. Reminders come from OpenClaw.

| Severity | Internal Follow-up | Customer Update |
|----------|-------------------|-----------------|
| **Critical** | Several times a day | When the state changes |
| **High** | Daily | When the state changes |
| **Medium** | Weekly | When there is news |

### Follow-up Actions
- Check with the receiving team for progress
- Update the customer even if there's no new information ("We're still investigating — here's what we know so far")
- Adjust severity if the situation changes (better or worse)
- Document all updates in the ticket for audit trail
- Close the loop when resolved: confirm with customer, update internal tracking, capture learnings

## De-escalation

Not every escalation stays escalated. De-escalate when:
- Root cause is found and it's a support-resolvable issue
- A workaround is found that unblocks the customer
- The issue resolves itself (but still document root cause)
- New information changes the severity assessment

When de-escalating:
- Draft a note for the owner you escalated to
- Draft the update for the issue (posted only after confirmation)
- Draft the reply to the practice (`draft-response`)
- Document what was learned for future reference

## Escalation Best Practices

1. Always quantify impact — vague escalations get deprioritized
2. Include reproduction steps for bugs — this is the #1 thing engineering needs
3. Be clear about what you need — "investigate" vs. "fix" vs. "decide" are different asks
4. State when you need an answer internally — but never pass it to the practice as a promise
5. Maintain ownership of the customer relationship even after escalating the technical issue
6. Follow up proactively — don't wait for the receiving team to come to you
7. Document everything — the escalation trail is valuable for pattern detection and process improvement
