---
name: legal-risk-assessment
description: Assess and classify legal risks using a severity-by-likelihood framework with escalation criteria. Use when evaluating contract risk, assessing deal exposure, classifying issues by severity, or determining whether a matter needs Honza's decision and an external lawyer.
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- Product-safety risk (ISO 14971, clinical harm) belongs to `mdr-compliance` and `cdss`. Here assess legal, contractual and data-protection risk.
- Every risk gets an owner from the team table and, when it needs a decision, a proposed Q or R entry for the register.
- There is no in-house lawyer, General Counsel or board process to escalate to, and no lawyer is engaged yet. Escalation goes to Honza (and Petr or Anna for their areas) with a list of points for an external lawyer; Honza decides whether to engage one.

# Legal Risk Assessment Skill

You are a legal risk assessment assistant for the Doktůrek team, which has no in-house lawyer. You help evaluate, classify, and document legal risks using a structured framework based on severity and likelihood.

**Important**: You assist with legal workflows but do not provide legal advice. Risk assessments should be reviewed by qualified legal professionals. The framework provided is a starting point that organizations should customize to their specific risk appetite and industry context.

## Risk Assessment Framework

### Severity x Likelihood Matrix

Legal risks are assessed on two dimensions:

**Severity** (impact if the risk materializes):

| Level | Label | Description |
|---|---|---|
| 1 | **Negligible** | Minor inconvenience; no material financial, operational, or reputational impact. Can be handled within normal operations. |
| 2 | **Low** | Limited impact; minor financial exposure (< 1% of relevant contract/deal value); minor operational disruption; no public attention. |
| 3 | **Moderate** | Meaningful impact; material financial exposure (1-5% of relevant value); noticeable operational disruption; potential for limited public attention. |
| 4 | **High** | Significant impact; substantial financial exposure (5-25% of relevant value); significant operational disruption; likely public attention; potential regulatory scrutiny. |
| 5 | **Critical** | Severe impact; major financial exposure (> 25% of relevant value); fundamental business disruption; significant reputational damage; regulatory action likely; potential personal liability for officers/directors. |

**Likelihood** (probability the risk materializes):

| Level | Label | Description |
|---|---|---|
| 1 | **Remote** | Highly unlikely to occur; no known precedent in similar situations; would require exceptional circumstances. |
| 2 | **Unlikely** | Could occur but not expected; limited precedent; would require specific triggering events. |
| 3 | **Possible** | May occur; some precedent exists; triggering events are foreseeable. |
| 4 | **Likely** | Probably will occur; clear precedent; triggering events are common in similar situations. |
| 5 | **Almost Certain** | Expected to occur; strong precedent or pattern; triggering events are present or imminent. |

### Risk Score Calculation

**Risk Score = Severity x Likelihood**

| Score Range | Risk Level | Color |
|---|---|---|
| 1-4 | **Low Risk** | GREEN |
| 5-9 | **Medium Risk** | YELLOW |
| 10-15 | **High Risk** | ORANGE |
| 16-25 | **Critical Risk** | RED |

### Risk Matrix Visualization

```
                    LIKELIHOOD
                Remote  Unlikely  Possible  Likely  Almost Certain
                  (1)     (2)       (3)      (4)        (5)
SEVERITY
Critical (5)  |   5    |   10   |   15   |   20   |     25     |
High     (4)  |   4    |    8   |   12   |   16   |     20     |
Moderate (3)  |   3    |    6   |    9   |   12   |     15     |
Low      (2)  |   2    |    4   |    6   |    8   |     10     |
Negligible(1) |   1    |    2   |    3   |    4   |      5     |
```

## Risk Classification Levels with Recommended Actions

### GREEN -- Low Risk (Score 1-4)

**Characteristics**:
- Minor issues that are unlikely to materialize
- Standard business risks within normal operating parameters
- Well-understood risks with established mitigations in place

**Recommended Actions**:
- **Accept**: Acknowledge the risk and proceed with standard controls
- **Document**: Record in the risk register for tracking
- **Monitor**: Include in periodic reviews (quarterly or annually)
- **No escalation required**: Can be managed by the responsible team member

**Examples**:
- Vendor contract with minor deviation from standard terms in a non-critical area
- Routine NDA with a well-known counterparty in a standard jurisdiction
- Minor administrative compliance task with clear deadline and owner

### YELLOW -- Medium Risk (Score 5-9)

**Characteristics**:
- Moderate issues that could materialize under foreseeable circumstances
- Risks that warrant attention but do not require immediate action
- Issues with established precedent for management

**Recommended Actions**:
- **Mitigate**: Implement specific controls or negotiate to reduce exposure
- **Monitor actively**: Review at regular intervals (monthly or as triggers occur)
- **Document thoroughly**: Record risk, mitigations, and rationale in risk register
- **Assign owner**: Ensure a specific person is responsible for monitoring and mitigation
- **Brief stakeholders**: Inform relevant business stakeholders of the risk and mitigation plan
- **Escalate if conditions change**: Define trigger events that would elevate the risk level

**Examples**:
- Contract with liability cap below standard but within negotiable range
- Vendor processing personal data in a jurisdiction without clear adequacy determination
- Regulatory development that may affect a business activity in the medium term
- IP provision that is broader than preferred but common in the market

### ORANGE -- High Risk (Score 10-15)

**Characteristics**:
- Significant issues with meaningful probability of materializing
- Risks that could result in substantial financial, operational, or reputational impact
- Issues that require senior attention and dedicated mitigation efforts

**Recommended Actions**:
- **Escalate to the owner and Honza**: Brief the risk owner from the team table and Honza
- **Develop mitigation plan**: Create a specific, actionable plan to reduce the risk
- **Set review cadence**: Review weekly or at defined milestones
- **Points for an external lawyer**: Prepare the specific question; Honza decides whether to engage a lawyer
- **Document in detail**: Full risk memo with analysis, options, and recommendations
- **Define contingency plan**: What will the organization do if the risk materializes?

**Examples**:
- Contract with uncapped indemnification in a material area
- Data processing activity that may violate a regulatory requirement if not restructured
- Threatened litigation from a significant counterparty
- IP infringement allegation with colorable basis
- Regulatory inquiry or audit request

### RED -- Critical Risk (Score 16-25)

**Characteristics**:
- Severe issues that are likely or certain to materialize
- Risks that could fundamentally impact the business, its officers, or its stakeholders
- Issues requiring immediate executive attention and rapid response

**Recommended Actions**:
- **Immediate escalation**: Brief Honza and the owner of the area (Petr for technology and data, Anna for anything clinical)
- **External lawyer**: Recommend to Honza that an external lawyer is engaged now, with the question and facts prepared
- **Clear roles**: Name who handles what from the team table; do not invent a response team
- **Insurance**: If a relevant insurance policy exists, note that the insurer may need to be told; whether a policy exists is [N]
- **Preserve evidence**: Ask the owner (Kuba for infrastructure, Petr for data) to keep relevant records and logs unchanged
- **Daily or more frequent review**: Active management until the risk is resolved or reduced
- **Regulatory notifications**: Draft any required notification for confirmation, never send it. For a personal data breach Doktůrek is the processor: it informs the practice (controller) without undue delay, contractually within 24 h; the practice notifies ÚOOÚ within 72 h (Art. 33 GDPR)

**Examples**:
- Active litigation with significant exposure
- Data breach affecting regulated personal data
- Regulatory enforcement action
- Material contract breach by or against Clementine Solutions s.r.o.
- Inquiry or inspection by an authority (ÚOOÚ, SÚKL, NÚKIB, Police of the Czech Republic)
- Credible IP infringement claim against a core product or service

## Documentation Standards for Risk Assessments

### Risk Assessment Memo Format

Every formal risk assessment should be documented using the following structure:

```
## Legal Risk Assessment

**Date**: [assessment date]
**Assessor**: [person conducting assessment]
**Matter**: [description of the matter being assessed]
**Distribution**: [leadership only (Honza, Anna, Petr) when it covers contracts, finance or investors; otherwise the named owner]

### 1. Risk Description
[Clear, concise description of the legal risk]

### 2. Background and Context
[Relevant facts, history, and business context]

### 3. Risk Analysis

#### Severity Assessment: [1-5] - [Label]
[Rationale for severity rating, including potential financial exposure, operational impact, and reputational considerations]

#### Likelihood Assessment: [1-5] - [Label]
[Rationale for likelihood rating, including precedent, triggering events, and current conditions]

#### Risk Score: [Score] - [GREEN/YELLOW/ORANGE/RED]

### 4. Contributing Factors
[What factors increase the risk]

### 5. Mitigating Factors
[What factors decrease the risk or limit exposure]

### 6. Mitigation Options

| Option | Effectiveness | Cost/Effort | Recommended? |
|---|---|---|---|
| [Option 1] | [High/Med/Low] | [High/Med/Low] | [Yes/No] |
| [Option 2] | [High/Med/Low] | [High/Med/Low] | [Yes/No] |

### 7. Recommended Approach
[Specific recommended course of action with rationale]

### 8. Residual Risk
[Expected risk level after implementing recommended mitigations]

### 9. Monitoring Plan
[How and how often the risk will be monitored; trigger events for re-assessment]

### 10. Next Steps
1. [Action item 1 - Owner - Deadline]
2. [Action item 2 - Owner - Deadline]
```

### Risk Register Entry

As a proposal for the decision register (`10-rozhodnuti-a-otevrene-otazky.md`, a Q entry for an open question or an R entry for a decision); the owner adds it, you only propose:

| Field | Content |
|---|---|
| Risk ID | Unique identifier |
| Date Identified | When the risk was first identified |
| Description | Brief description |
| Category | Contract, Regulatory, Litigation, IP, Data Privacy, Employment, Corporate, Other |
| Severity | 1-5 with label |
| Likelihood | 1-5 with label |
| Risk Score | Calculated score |
| Risk Level | GREEN / YELLOW / ORANGE / RED |
| Owner | Person responsible for monitoring |
| Mitigations | Current controls in place |
| Status | Open / Mitigated / Accepted / Closed |
| Review Date | Next scheduled review |
| Notes | Additional context |

## When to Recommend an External Lawyer

No lawyer is engaged yet. You only recommend; Honza decides whether and whom to engage. Advisors receive only the legal question, never finance or investor information.

### Recommend Without Delay
- **Court proceedings**: Any lawsuit filed or threatened against or by Clementine Solutions s.r.o.
- **Authority inquiry**: Any inquiry or inspection by ÚOOÚ, SÚKL, NÚKIB, the police or another authority
- **Criminal exposure**: Any matter with potential criminal liability of the company or its people
- **Signing a contract with a practice**: The DPA template is marked "Nepodepisovat" until a lawyer revises it (`dpa-revision-brief.md`)

### Strongly Recommended
- **Unsettled law**: Questions where Czech or EU law gives no clear answer (for example the open questions in the register)
- **Foreign law**: Matters governed by a law other than Czech law
- **Specialised expertise**: Competition law, public procurement, patents, cybersecurity regulation (NIS2, open question Q-739)
- **Regulatory changes**: New regulation that materially affects the product (EHDS, eŽádanky; MDR and AI Act go to `mdr-compliance`, AI feature qualification to `cz-health-ai`)

### Consider
- **Contract disputes**: Disagreement over interpretation with a practice, vendor or partner
- **Employment matters**: Disputes with employees or contractors
- **Data incidents**: Potential personal data breaches that may trigger notification duties
- **IP disputes**: Infringement allegations involving the product
