---
name: legal-response
description: Draft a text response to a common legal inquiry, with escalation checks for situations that need Honza or a lawyer. Use when a patient's data-subject request reaches Doktůrek and must be handed over to the practice (controller), or for vendor legal questions, NDA requests, privacy questions from practices and insurance notifications. Output is text for review; nothing is sent.
argument-hint: "[inquiry-type]"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- Doktůrek is the processor for practices. A data-subject request from a patient goes to the practice (controller); draft the hand-over and the processor's assistance, not a direct answer to the patient.
- Requests from authorities (SÚKL, ČSSZ, MZČR, ÚOOÚ) and from practices are external: draft only, and Honza confirms before anything is sent.
- **No local templates exist** (there is no `legal.local.md`). Use the default structures below; the reference for processor duties is [`dpa-revision-brief.md`](https://github.com/Dokturek-ai/dokturek-docs/blob/main/04-pravo-a-regulatorika/dpa-revision-brief.md) §6 and §8.
- The plugin has no email or calendar connector: the output is text the user copies, plus a list of deadlines to note. Never create email drafts, send messages or set reminders.

# /legal-response -- Draft a Response to a Legal Inquiry

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Draft a response to a common legal inquiry from the default structures below. Customize it with the specific details and check escalation triggers for situations that should not get a routine reply.

**Important**: This command assists with legal workflows but does not provide legal advice. Generated responses should be reviewed before being sent; no lawyer is engaged yet, so regulated communications go to Honza with the points for an external lawyer.

## Invocation

```
/legal:legal-response [inquiry-type]
```

Common inquiry types:
- `dsr` or `data-subject-request` -- A patient's request (access, rectification, erasure, restriction, portability, objection) that reached Doktůrek: hand-over to the practice
- `vendor` or `vendor-question` -- Vendor legal questions
- `nda` or `nda-request` -- NDA requests
- `privacy` or `privacy-inquiry` -- Privacy questions from a practice (where data is processed, sub-processors, security measures)
- `insurance` -- Insurance claim notifications (whether a relevant policy exists is [N])
- `custom` -- Another inquiry, built from the closest structure

Requests from an authority or the police, court documents and anything threatening proceedings are not routine inquiries: stop, tell the user, and route the matter to Honza with a recommendation to engage an external lawyer (see `legal-risk-assessment`).

If no inquiry type is provided, ask the user what type of response they need and show available categories.

## Workflow

### Step 1: Identify Inquiry Type

Accept the inquiry type from the user. If the type is ambiguous, show available categories and ask for clarification.

### Step 2: Load the Default Structure

There is no local template library (no `legal.local.md`); do not look for one. Use the structure for the inquiry type in "Response Categories" below and say in the output that a default structure was used.

### Step 3: Check Escalation Triggers

Before generating any response, evaluate whether this situation has characteristics that should NOT get a routine reply.

#### Universal Escalation Triggers (Apply to All Categories)
- The matter involves potential court proceedings or an inquiry by an authority (ÚOOÚ, SÚKL, ČSSZ, MZČR, NÚKIB, police)
- The response could create a binding legal commitment or waiver
- The matter involves potential criminal liability
- Media attention is involved or likely
- The situation is unprecedented (no prior handling by the team)
- The matter involves law other than Czech and EU law

#### Data Subject Request Escalation Triggers
- Request involves a minor's data, or is from/on behalf of a minor
- Request is from an authority (not an individual)
- The practice (controller) cannot be identified, or the requester is not a patient of a Doktůrek practice
- Requester is a current or former employee of Clementine Solutions s.r.o. with an active dispute
- Request asks Doktůrek itself to delete or change records: the practice decides, and medical records have a retention period under Decree 444/2024 Sb.
- Request asks for access to medical records under Act 372/2011 Sb.: that is the provider's duty, not Doktůrek's

#### Vendor Question Escalation Triggers
- The question involves a dispute or potential breach
- The vendor is threatening litigation or termination
- The question involves regulatory compliance (not just contract terms)
- The response could create a binding commitment or waiver
- Response could affect ongoing negotiation

#### NDA Request Escalation Triggers
- The counterparty is a competitor (for example an incumbent AIS vendor)
- The business context suggests the NDA is for an investment or acquisition
- The request involves unusual subject matter (AI training data, patient data, etc.); anything with patient data is a DPA case (`review-contract`)

**When an escalation trigger is detected:**
1. **Stop**: Do not generate a routine response
2. **Alert**: Inform the user that an escalation trigger has been detected
3. **Explain**: Describe which trigger was detected and why it matters
4. **Recommend**: Name the owner from the team table (Honza for contracts and customers, Petr for data and technology, Anna for anything clinical) and list the points for an external lawyer
5. **Offer**: Provide a draft clearly marked "KONCEPT – K POSOUZENÍ, NEODESÍLAT" rather than a final response

### Step 4: Gather Specific Details

Prompt the user for the details needed to customize the response:

**Data Subject Request (hand-over to the practice):**
- Which practice is the controller, and its contact person
- Date and channel through which Doktůrek received the request
- Which right is exercised (Art. 15–22 GDPR)
- A reference number only: never copy the patient's name, birth number, insurance number or health data into the draft
- What technical assistance Doktůrek can offer (export, correction, restriction in the product) and who does it (Petr names the person)
- The relevant DPA article, if a DPA with that practice is signed (DPA status is [N] until documented)

**Vendor Question:**
- Vendor name
- Reference agreement (if applicable)
- Specific question being addressed
- Relevant contract provisions

**NDA Request:**
- Requesting team member
- Counterparty name
- Purpose of the NDA
- Mutual or unilateral
- Any special requirements

### Step 5: Generate Response

Fill the structure with the gathered details. Ensure the response:
- Is in Czech, addresses the reader formally (vykání) and uses a calm, concrete tone
- Includes all required legal elements for the response type
- References specific dates, deadlines, and obligations
- Provides clear next steps for the recipient
- Names Clementine Solutions s.r.o. as the party, not "Doktůrek.ai"

Present the draft response to the user as text. Nothing is sent: the user copies it, and anything external needs Honza's confirmation.

#### Customization Guidelines

**Required customization** — Every response MUST be customized with:
- Correct names, dates, and reference numbers
- Specific facts of the situation
- Correct deadlines based on when the inquiry was received
- Appropriate signature block (a real person the user names; never an AI persona such as "Vojtěch")

**Tone adjustment** — Adjust tone based on:
- **Audience**: Internal vs. external, practice vs. vendor vs. authority
- **Relationship**: New counterparty vs. existing partner vs. adversarial party
- **Sensitivity**: Routine inquiry vs. contentious matter
- **Urgency**: Standard timeline vs. expedited response needed

## Response Categories

### 1. Data Subject Requests: Hand-over to the Controller

Doktůrek is the processor. It does not answer the patient on the merits; it forwards the request to the practice without undue delay and assists the practice under Art. 28(3)(e) GDPR (`dpa-revision-brief.md` §6).

**Sub-categories**:
- Hand-over of the request to the practice
- Description of the technical assistance Doktůrek can provide
- Optional short note to the requester that the request was passed to their practice ([P]: whether and how Doktůrek may contact the requester depends on the DPA; ověří právník)

**Key elements**:
- Reference to Art. 28(3)(e) GDPR and the DPA article, if signed
- The right exercised and the date and channel of receipt
- The controller's deadline under Art. 12(3) GDPR: one month from receipt of the request, extendable by two further months where necessary, with the data subject informed of the extension within the first month. How the deadline counts when the request first reached the processor ověří právník
- What Doktůrek can do technically and by when it can do it (only what the owner confirms; no promised turnaround)
- Contact person at Clementine Solutions s.r.o.

**Example structure** (write the output in Czech):
```
Subject: Data subject request handed over to the controller - Ref. {{request_id}}

Dear {{practice_contact}},

On {{received_date}} Clementine Solutions s.r.o., as your processor, received via {{channel}} a request from a person who states they are a patient of your practice. Under Art. 28(3)(e) GDPR [and Article {{dpa_article}} of our data processing agreement] we are passing it to you as the controller. We have not answered the request on the merits.

Right exercised: {{right}} (Art. {{article}} GDPR)
Attached: the request as received (by a secure channel, not in this message)
Deadline for your answer: Art. 12(3) GDPR, one month from receipt, extendable by two months

We can assist with: {{technical_assistance}}

Contact: {{contact_person}}
```

### 2. Privacy Inquiries from Practices

**Sub-categories**:
- Where data is processed (EU/EEA only, per the DPA brief)
- Sub-processors (see `vendor-check`)
- Security measures (TOM; RPO and RTO targets in the brief are targets, not proven)
- Incident notification (processor to controller without undue delay, contractually 24 h; controller to ÚOOÚ 72 h)

**Key elements**:
- Specific answers from `dokturek-docs`, marked [Z], [P] or [N]
- No claim of certification or compliance the documents do not prove
- Contact person at Clementine Solutions s.r.o.

### 3. Vendor Legal Questions

**Sub-categories**:
- Contract status inquiry response
- Amendment request response
- Compliance certification requests
- Audit request responses

**Key elements**:
- Reference to the applicable agreement
- Specific response to the vendor's question
- Any required caveats or limitations
- Next steps

### 4. NDA Requests

**Sub-categories**:
- Accepting a counterparty's NDA (with markup; triage it first with `triage-nda`)
- Declining an NDA request with explanation
- NDA renewal or extension

No Doktůrek standard-form NDA is documented; do not claim one exists.

**Key elements**:
- Purpose of the NDA
- Summary of terms
- Who signs (Honza decides)

### 5. Insurance Notifications

Only if the user confirms a relevant policy exists.

**Sub-categories**:
- Initial claim notification
- Supplemental information

**Key elements**:
- Policy number and coverage period
- Description of the matter or incident
- Timeline of events
- Requested coverage confirmation

## Reusable Templates

If the user wants a reusable template, draft it with: use case, escalation triggers, required variables (`{{requester_name}}`, `{{response_deadline}}`), body and follow-up steps. Propose it as a change to `dokturek-docs` for the owner to accept; do not save it to local settings.

## Output Format

```
## Draft Response: [Inquiry Type]

**To**: [recipient]
**Subject**: [subject line]
**Structure used**: [default structure / custom]

---

[Response body in Czech]

---

### Escalation Check
[Confirmation that no escalation triggers were detected, OR flagged triggers with the owner and points for a lawyer]

### Deadlines to Note
- [Deadline, what it is, legal basis]

### Next Steps
1. [Who confirms the text (Honza for anything external)]
2. [Who sends it, through which channel]
```

## Notes

- Always present the draft as text for the user to review; never send it, create an email draft or set a calendar reminder
- For data-subject requests, always state the Art. 12(3) GDPR deadline and that it is the controller's deadline
- Never put patient identifiers or health data into a draft; use a reference number
