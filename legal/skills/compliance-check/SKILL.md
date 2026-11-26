---
name: compliance-check
description: Run a Czech and EU compliance check (GDPR, Act 110/2019 Sb., Act 372/2011 Sb., Decree 444/2024 Sb., NIS2, DPA and DPIA status) on a proposed action, product feature or business initiative, surfacing applicable rules, required approvals and risk areas. Use when a feature or pilot touches personal or patient data, when marketing or product proposes something with regulatory implications, or when you need to know which approvals apply before proceeding.
argument-hint: "<action or initiative to check>"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- MDR, IVDR, AI Act and SaMD classification belong to the `mdr-compliance` plugin; qualifying a specific AI or software feature and SÚKL consultations belong to `cz-health-ai`. Here cover GDPR, DPA and DPIA status, health-records retention (Decree 444/2024 Sb.) and contractual obligations.
- Real patient data stays blocked until a signed DPA and a DPIA exist. Report that gate explicitly whenever a feature or a pilot touches real data.
- No lawyer and no DPO are engaged: say so whenever a requirement depends on them.
- Check the current state in [`04-pravo-a-regulatorika/README.md`](https://github.com/Dokturek-ai/dokturek-docs/blob/main/04-pravo-a-regulatorika/README.md) and the open questions in the register (for example Q-314, Q-745, Q-750, Q-753) before stating anything as settled.

# /compliance-check -- Compliance Review

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Run a compliance check on a proposed action, product feature, marketing campaign, or business initiative.

**Important**: This command assists with legal workflows but does not provide legal advice. Compliance assessments should be reviewed by qualified legal professionals. Regulatory requirements change frequently; always verify current requirements with authoritative sources.

## Usage

```
/legal:compliance-check <action or initiative>
```

Check: $ARGUMENTS

## What I Need From You

Describe what you're planning to do. Examples:
- "We want to run the first practice's pilot with real patient data"
- "We're adding a new vendor for OCR of scanned documents"
- "We want to migrate a practice's records from its current AIS"
- "Filip wants to send the newsletter to doctors from a purchased list"

## Output

```markdown
## Compliance Check: [Initiative]

### Summary
[Quick assessment: Proceed / Proceed with conditions / Requires further review]

### Applicable Regulations and Policies
| Regulation/Policy | Relevance | Key Requirements |
|-------------------|-----------|-----------------|
| [GDPR / 110/2019 Sb. / 372/2011 Sb. / 444/2024 Sb. / 264/2025 Sb. / etc.] | [How it applies] | [What you need to do] |

### Requirements
| # | Requirement | Status | Action Needed |
|---|-------------|--------|---------------|
| 1 | [Requirement] | [Met / Not Met / Unknown] | [What to do] |

### Risk Areas
| Risk | Severity | Mitigation |
|------|----------|------------|
| [Risk] | [High/Med/Low] | [How to address] |

### Recommended Actions
1. [Most important action]
2. [Second priority]
3. [Third priority]

### Approvals Needed
| Approver | Why | Status |
|----------|-----|--------|
| [Person/Team] | [Reason] | [Pending] |

### Further Review Recommended
[Points for an external lawyer, for Lukáš Peter (GDPR) and handovers to `mdr-compliance`]
```

## Privacy Regulation Overview

### GDPR (General Data Protection Regulation)

**Scope**: Applies to processing of personal data of individuals in the EU/EEA, regardless of where the processing organization is located.

**Key Obligations** (Doktůrek is the processor for practices; the practice is the controller):
- **Lawful basis**: Identify and document lawful basis for each processing activity (consent, contract, legitimate interest, legal obligation, vital interest, public task)
- **Data subject rights**: The controller responds to access, rectification, erasure, portability, restriction, and objection requests within one month of receipt, extendable by two further months where necessary (Art. 12(3)); the processor assists under Art. 28(3)(e)
- **Data protection impact assessments (DPIAs)**: Required for processing likely to result in high risk to individuals
- **Breach notification**: The controller notifies ÚOOÚ within 72 hours of becoming aware of a personal data breach and affected individuals without undue delay if high risk; the processor notifies the controller without undue delay (contractually 24 h per the DPA brief)
- **Records of processing**: Maintain Article 30 records of processing activities
- **International transfers**: Ensure appropriate safeguards for transfers outside EEA (SCCs, adequacy decisions, BCRs)
- **DPO requirement**: Appoint a Data Protection Officer if required (public authority, large-scale processing of special categories, large-scale systematic monitoring). Clementine Solutions s.r.o. has no DPO; whether one is required is open [N] and ověří právník

**Common Doktůrek Touchpoints**:
- Reviewing sub-processor terms (see `vendor-check`)
- Privacy by design in product features (with Petr)
- Assisting practices with data-subject requests (see `legal-response`)
- Keeping all processing in the EU/EEA

### Czech and EU Requirements

| Item | What to check | Source or owner |
|---|---|---|
| **Act 110/2019 Sb.** (zákon o zpracování osobních údajů) | Czech rules implementing GDPR; cited as a legal basis in the DPA brief, where the reference is marked [N] | `dpa-revision-brief.md` §3; ověří právník |
| **ÚOOÚ** (Úřad pro ochranu osobních údajů) | Supervisory authority: breach notification by the controller within 72 h, complaints, inquiries | GDPR Art. 33, 77 |
| **Act 372/2011 Sb.** (zákon o zdravotních službách) | Medical records (zdravotnická dokumentace) and who may access them and obtain copies; access requests are the provider's duty, Doktůrek assists | Exact provisions ověří právník |
| **Decree 444/2024 Sb.** | Retention of medical records: 10 years from change of registering provider or death; record of destruction kept 40 years [Z] | `04-pravo-a-regulatorika/README.md` |
| **NIS2: Act 264/2025 Sb.** (cybersecurity) | Whether Clementine Solutions s.r.o. falls under the Act and in which regime is open | Q-739 (Petr) |
| **DPA and DPIA** | Signed DPA and documented DPIA assessment before any real patient data | Q-745; `04-pravo-a-regulatorika/README.md` |
| **DPO** | No DPO is appointed; whether Art. 37 GDPR requires one for Clementine Solutions s.r.o. is open [N] | ověří právník |
| **EHDS** (EU) 2025/327 | Applicability to the product is open | Q-740 |
| **MDR, AI Act** | Not covered here | `mdr-compliance` plugin; AI feature qualification `cz-health-ai` |

## DPA Review Checklist

When reviewing a Data Processing Agreement or Data Processing Addendum, verify the following:

### Required Elements (GDPR Article 28)

- [ ] **Subject matter and duration**: Clearly defined scope and term of processing
- [ ] **Nature and purpose**: Specific description of what processing will occur and why
- [ ] **Type of personal data**: Categories of personal data being processed
- [ ] **Categories of data subjects**: Whose personal data is being processed
- [ ] **Controller obligations and rights**: Controller's instructions and oversight rights

### Processor Obligations

- [ ] **Process only on documented instructions**: Processor commits to process only per controller's instructions (with exception for legal requirements)
- [ ] **Confidentiality**: Personnel authorized to process have committed to confidentiality
- [ ] **Security measures**: Appropriate technical and organizational measures described (Article 32 reference)
- [ ] **Sub-processor requirements**:
  - [ ] Written authorization requirement (general or specific)
  - [ ] If general authorization: notification of changes with opportunity to object
  - [ ] Sub-processors bound by same obligations via written agreement
  - [ ] Processor remains liable for sub-processor performance
- [ ] **Data subject rights assistance**: Processor will assist controller in responding to data subject requests
- [ ] **Security and breach assistance**: Processor will assist with security obligations, breach notification, DPIAs, and prior consultation
- [ ] **Deletion or return**: On termination, delete or return all personal data (at controller's choice) and delete existing copies unless legal retention required
- [ ] **Audit rights**: Controller has right to conduct audits and inspections (or accept third-party audit reports)
- [ ] **Breach notification**: Processor will notify controller of personal data breaches without undue delay (contractually within 24 hours per the DPA brief; must enable controller to meet the 72-hour deadline towards ÚOOÚ)

### International Transfers

- [ ] **Transfer mechanism identified**: SCCs, adequacy decision, BCRs, or other valid mechanism
- [ ] **SCCs version**: Using current EU SCCs (June 2021 version) if applicable
- [ ] **Correct module**: Appropriate SCC module selected (C2P, C2C, P2P, P2C)
- [ ] **Transfer impact assessment**: Completed if transferring to countries without adequacy decisions
- [ ] **Supplementary measures**: Technical, organizational, or contractual measures to address gaps identified in transfer impact assessment

### Practical Considerations

- [ ] **Liability**: DPA liability provisions align with (or don't conflict with) the main services agreement
- [ ] **Termination alignment**: DPA term aligns with the services agreement
- [ ] **Data locations**: Processing locations specified and acceptable
- [ ] **Security standards**: Specific security standards or certifications required (SOC 2, ISO 27001, etc.)
- [ ] **Insurance**: Adequate insurance coverage for data processing activities

### Common DPA Issues

| Issue | Risk | Standard Position |
|---|---|---|
| Blanket sub-processor authorization without notification | Loss of control over processing chain | Require notification with right to object |
| Breach notification timeline > 72 hours | May prevent timely regulatory notification | Require notification within 24 hours (DPA brief) |
| No audit rights (or audit rights only via third-party reports) | Cannot verify compliance | Accept SOC 2 Type II + right to audit upon cause |
| Data deletion timeline not specified | Data retained indefinitely | Require deletion within 30-90 days of termination |
| No data processing locations specified | Data could be processed anywhere | Require disclosure of processing locations |
| Outdated SCCs | Invalid transfer mechanism | Require current EU SCCs (2021 version) |

## Data Subject Request Handling

### Request Intake

Doktůrek is the processor: a request that reaches Doktůrek is forwarded to the practice (controller) without undue delay, and Doktůrek assists (Art. 28(3)(e) GDPR; draft the hand-over with `legal-response`). The steps below describe what the practice does and what Doktůrek must be able to support.

When a data subject request is received:

1. **Identify the request type**:
   - Access (copy of personal data)
   - Rectification (correction of inaccurate data)
   - Erasure / deletion ("right to be forgotten")
   - Restriction of processing
   - Data portability (structured, machine-readable format)
   - Objection to processing

2. **Identify the controller and the applicable rules**:
   - Which practice is the controller?
   - GDPR with Act 110/2019 Sb.; for access to medical records also Act 372/2011 Sb.
   - What are the specific requirements and timelines?

3. **Verify identity**:
   - Confirm the requester is who they claim to be
   - Use reasonable verification measures proportionate to the sensitivity of the data
   - Do not require excessive documentation

4. **Log the request**:
   - Date received
   - Request type
   - Requester identity
   - Applicable regulation
   - Response deadline
   - Assigned handler

### Response Timelines

| Regulation | Initial Acknowledgment | Substantive Response | Extension |
|---|---|---|---|
| GDPR Art. 12(3) | Not specified (best practice: promptly) | One month from receipt | Two further months where necessary, with the data subject told within the first month |

### Exemptions and Exceptions

Before fulfilling a request, check whether any exemptions apply:

**Common exemptions across regulations**:
- Legal claims defense or establishment
- Legal obligations requiring retention
- Public interest or official authority
- Freedom of expression and information (for erasure requests)
- Archiving in the public interest or scientific/historical research

**Doktůrek-specific considerations**:
- Medical records retention: Decree 444/2024 Sb. sets mandatory retention, so erasure requests for medical records usually cannot be fulfilled in full; the practice decides
- Other regulatory retention: accounting and employment records have their own periods
- Third-party rights: Fulfilling the request might adversely affect the rights of others

### Response Process

1. Gather all personal data of the requester across systems
2. Apply any exemptions and document the basis
3. Prepare response: fulfill the request or explain why (in whole or part) it cannot be fulfilled
4. If denying (in whole or part): cite the specific legal basis for denial
5. Inform the requester of their right to lodge a complaint with the supervisory authority
6. Document the response and retain records of the request and response

## Regulatory Monitoring Basics

### What to Monitor

Maintain awareness of developments in:
- **Regulatory guidance**: New or updated guidance from ÚOOÚ, the EDPB, NÚKIB, SÚKL and MZČR
- **Enforcement actions**: Fines, orders, and settlements that signal regulatory priorities
- **Legislative changes**: New privacy laws, amendments to existing laws, implementing regulations
- **Industry standards**: Updates to ISO 27001, SOC 2, NIST frameworks, and sector-specific requirements
- **Cross-border transfer developments**: Adequacy decisions, SCC updates, data localization requirements

### Monitoring Approach

1. **Subscribe to regulatory authority communications** (newsletters, RSS feeds, official announcements)
2. **Track relevant legal publications** for analysis of new developments
3. **Review industry association updates** for sector-specific guidance
4. **Maintain a regulatory calendar** of known upcoming deadlines, effective dates, and compliance milestones
5. **Brief Honza and Petr** on material developments that affect Doktůrek's processing; a decision goes to the register as a proposal

### Escalation Criteria

Escalate regulatory developments to Honza and Petr (with points for an external lawyer) when:
- A new regulation or guidance directly affects the organization's core business activities
- An enforcement action in the organization's sector signals heightened regulatory scrutiny
- A compliance deadline is approaching that requires organizational changes
- A data transfer mechanism the organization relies on is challenged or invalidated
- A regulatory authority initiates an inquiry or investigation involving the organization

## Tips

1. **Be specific** — "We want to email all our users" is better than "marketing campaign."
2. **Say whether real patient data is involved** — Real patient data stays blocked until a signed DPA and a documented DPIA assessment exist.
3. **Mention the data** — What personal data is involved? This drives most compliance requirements.
