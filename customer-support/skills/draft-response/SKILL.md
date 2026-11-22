---
name: draft-response
description: Draft a reply to a support request from a practice that already uses Doktůrek (doctor, nurse or practice staff), tailored to the situation. Use when answering a product question, responding to an outage or a failed eRecept or eNeschopenka, delivering bad news like a delay or won't-fix, declining a feature request, or replying about the subscription. Sales follow-ups go to sales:call-summary, first contact with a prospect to sales:draft-outreach.
argument-hint: "<situation description>"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- Doctors and practice staff: Czech, vykání, calm and concrete. Describe the real state and the next step. No timelines, prices or clinical advice that the team has not confirmed.
- Draft only; the user sends it. Never write that something was logged, escalated, corrected or discussed unless the user confirms it happened.
- Escalation itself is `customer-escalation`; this skill only drafts the reply to the practice.

# Draft response

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Draft a professional, customer-facing response tailored to the situation, customer relationship, and communication context.

## Usage

```
/customer-support:draft-response <context about the customer question, issue, or request>
```

Examples:
- `/customer-support:draft-response Ordinace se ptá, proč se eRecept neodeslal a co má říct pacientovi`
- `/customer-support:draft-response Lékaři nejde přihlášení přes Keycloak a je rozladěný`
- `/customer-support:draft-response Odpověď na přání funkce, kterou Honza zatím nezařadil`
- `/customer-support:draft-response Ordinace se ptá na fakturu za předplatné`

## Workflow

### 1. Understand the Context

Parse the user's input to determine:

- **Customer**: Who is the communication for? Look up account context if available.
- **Situation type**: Question, issue, escalation, announcement, negotiation, bad news, good news, follow-up
- **Urgency**: Is this time-sensitive? How long has the customer been waiting?
- **Channel**: Email, support ticket, chat, or other (adjust formality accordingly)
- **Relationship stage**: New customer, established, frustrated/escalated
- **Stakeholder level**: End user, manager, executive, technical, business

### 2. Research Context

Gather relevant background from available sources:

**~~email:**
- Previous correspondence with this customer on this topic
- Any commitments or timelines previously shared
- Tone and style of the existing thread

**~~chat:**
- Internal discussions about this customer or topic
- Any guidance from product, engineering, or leadership
- Similar situations and how they were handled

**~~CRM (if connected):**
- Account details and plan level
- Contact information and key stakeholders
- Previous escalations or sensitive issues

**~~support platform (if connected):**
- Related tickets and their resolution
- Known issues or workarounds
- What was already told to the practice (there is no SLA; never invent a response time)

**~~knowledge base:**
- Official documentation or help articles to reference
- Product roadmap information (if shareable)
- Policy or process documentation

### 3. Generate the Draft

Produce a response tailored to the situation:

```
## Draft Response

**To:** [Customer contact name]
**Re:** [Subject/topic]
**Channel:** [Email / Ticket / Chat]
**Tone:** [Empathetic / Professional / Technical / Celebratory / Candid]

---

[Draft response text]

---

### Notes for You (internal — do not send)
- **Why this approach:** [Rationale for tone and content choices]
- **Things to verify:** [Any facts or commitments to confirm before sending]
- **Risk factors:** [Anything sensitive about this response]
- **Follow-up needed:** [Actions to take after sending]
- **Escalation note:** [If this should be reviewed by someone else first]
```

### 4. Run Quality Checks

Before presenting the draft, verify:

- [ ] Tone matches the situation and relationship
- [ ] No commitments beyond what's authorized
- [ ] No product roadmap details that shouldn't be shared externally
- [ ] Accurate references to previous conversations
- [ ] Clear next steps and ownership
- [ ] Appropriate for the stakeholder level (not too technical for executives, not too vague for engineers)
- [ ] Length is appropriate for the channel (shorter for chat, fuller for email)

### 5. Offer Iterations

After presenting the draft:
- "Want me to adjust the tone? (more formal, more casual, more empathetic, more direct)"
- "Should I add or remove any specific points?"
- "Want me to make this shorter/longer?"
- "Should I draft a version for a different stakeholder?"
- "Should I package the escalation with `customer-escalation`?"
- "Should I prepare a follow-up message to send after [X days] if no response?"

---

## Customer Communication Best Practices

### Core Principles

1. **Lead with empathy**: Acknowledge the customer's situation before jumping to solutions
2. **Be direct**: Get to the point — customers are busy. Bottom-line-up-front.
3. **Be honest**: Never overpromise, never mislead, never hide bad news in jargon
4. **Be specific**: Use concrete details and names — avoid vague language. No dates the owner has not confirmed
5. **Own it**: Take responsibility when appropriate. "We" not "the system" or "the process"
6. **Close the loop**: Every response should have a clear next step or call to action
7. **Match their energy**: If they're frustrated, be empathetic first. If they're excited, be enthusiastic.

### Response Structure

For most customer communications, follow this structure:

```
1. Acknowledgment / Context (1-2 sentences)
   - Acknowledge what they said, asked, or are experiencing
   - Show you understand their situation

2. Core Message (1-3 paragraphs)
   - Deliver the main information, answer, or update
   - Be specific and concrete
   - Include relevant details they need

3. Next Steps (1-3 bullets)
   - What happens next on our side (no date unless the owner confirmed it)
   - What THEY need to do (if anything)

4. Closing (1 sentence)
   - Warm but professional sign-off
   - Reinforce you're available if needed
```

### Length Guidelines

- **Chat/IM**: 1-4 sentences. Get to the point immediately.
- **Support ticket response**: 1-3 short paragraphs. Structured and scannable.
- **Email**: 3-5 paragraphs max. Respect their inbox.
- **Escalation response**: As long as needed to be thorough, but well-structured with headers.
- **Executive communication**: Shorter is better. 2-3 paragraphs max. Data-driven.

## Tone and Style Guidelines

### Tone Spectrum

| Situation | Tone | Characteristics |
|-----------|------|----------------|
| Good news / wins | Celebratory | Enthusiastic, warm, congratulatory, forward-looking |
| Routine update | Professional | Clear, concise, informative, friendly |
| Technical response | Precise | Accurate, detailed, structured, patient |
| Delayed delivery | Accountable | Honest, apologetic, action-oriented, specific |
| Bad news | Candid | Direct, empathetic, solution-oriented, respectful |
| Issue / outage | Urgent | Immediate, transparent, actionable, reassuring |
| Escalation | Executive | Composed, ownership-taking, plan-presenting, confident |
| Billing / account | Precise | Clear, factual, empathetic, resolution-focused |

### Tone Adjustments by Relationship Stage

**New Customer (0-3 months):**
- More formal and professional
- Extra context and explanation (don't assume knowledge)
- Proactively offer help and resources
- Build trust through reliability and responsiveness

**Established Customer (3+ months):**
- Warm and collaborative
- Can reference shared history and previous conversations
- More direct and efficient communication
- Show awareness of their goals and priorities

**Frustrated or Escalated Customer:**
- Extra empathy and acknowledgment
- A concrete next step and the owner handling it
- Only commitments the owner has confirmed

### Writing Style Rules

**DO:**
- Use active voice ("We'll investigate" not "This will be investigated")
- Use "I" for personal commitments and "we" for team commitments
- Name the real owner from the team table when the user agrees to it, never a generic team
- Use the customer's terminology, not your internal jargon
- Leave out dates and times for an answer or fix unless the owner confirmed them in writing
- Break up long responses with headers or bullet points

**DON'T:**
- Use corporate jargon or buzzwords ("synergy", "leverage", "paradigm shift")
- Deflect blame to other teams, systems, or processes
- Use passive voice to avoid ownership ("Mistakes were made")
- Include unnecessary caveats or hedging that undermines confidence
- CC people unnecessarily — only include those who need to be in the conversation
- Use exclamation marks excessively (one per email max, if any)

## Situation-Specific Approaches

**Answering a product question:**
- Lead with the direct answer
- Provide relevant documentation links
- Offer to connect them with the right resource if needed
- If you don't know the answer: say so honestly and say you will find out, without a timeline

**Responding to an issue or bug:**
- Acknowledge the impact on their work
- State what you know about the issue and its status
- Provide a verified workaround if available
- Name the next step, without a resolution date

**Handling an escalation:**
- Acknowledge the severity and their frustration
- Take ownership (no deflecting or excuse-making)
- Name the next step, without a timeline unless the owner confirmed one
- Identify the person accountable for resolution (from the team table)
- Offer a meeting or call if appropriate for the severity

**Delivering bad news (feature sunset, delay, can't-fix):**
- Be direct — don't bury the news
- Explain the reasoning honestly
- Acknowledge the impact on them specifically
- Offer alternatives or mitigation
- Provide a clear path forward

**Sharing good news (feature launch, milestone, recognition):**
- Lead with the positive outcome
- Connect it to their specific goals or use case
- Suggest next steps to capitalize on the good news
- Express genuine enthusiasm

**Declining a request (feature request, price exception, other exception):**
- Acknowledge the request and its reasoning
- Be honest about the decision (only one Honza or the owner has actually made)
- Explain the why without being dismissive
- Offer alternatives when possible
- Leave the door open for future conversation

## Reply Templates (Czech)

Rules for every template: vykání, a concrete next step without a date, no claim that something was already logged, escalated, corrected or discussed unless the user confirms it happened, no patient identifiers, and the brand written as Doktůrek. Replace the bracketed parts; drop lines that do not apply.

### Potvrzení chyby
```
Dobrý den,

děkujeme za popis. Rozumíme, že [konkrétní dopad] Vám komplikuje práci.

Co zatím víme:
- [co se děje]
- [příčina, jen pokud je ověřená]
- [náhradní postup, jen pokud je ověřený]

Dalším krokem je [prověření chyby / oprava]. Ozveme se Vám, až budeme vědět víc.

S pozdravem
[jméno], Doktůrek
```

### Předplatné nebo faktura
```
Dobrý den,

děkujeme za zprávu. Podle podkladů, které máme, [věcné vysvětlení, co se stalo].

Abychom to mohli dořešit, pošlete nám prosím [číslo faktury, datum platby].
Zveřejněný ceník předplatného najdete na https://dokturek.ai/cenik.

S pozdravem
[jméno], Doktůrek
```
Refunds, individual terms and exceptions belong to Honza; the reply never offers them.

### Funkce, kterou zatím neplánujeme
Use only after Honza decided it; otherwise use the feature-request template in `ticket-triage`.
```
Dobrý den,

děkujeme za podnět. Chápeme, proč by Vám [funkce] pomohla při [jejich práce].

Tuto funkci teď do vývoje nezařazujeme. Důvod: [stručné a věcné vysvětlení].

Zatím můžete:
- [ověřená alternativa]

Pokud se priorita změní, dáme Vám vědět.

S pozdravem
[jméno], Doktůrek
```

### Výpadek nebo incident
```
Dobrý den,

chceme Vás informovat o problému, který se týká [služba nebo funkce].

Co se děje: [srozumitelné vysvětlení]
Dopad na Vaši ordinaci: [konkrétně]
Stav: [prověřujeme / známe příčinu / opravujeme / vyřešeno]
[Jen ověřený náhradní postup: „Mezitím můžete [postup].“]

Další zprávu Vám pošleme, jakmile se stav změní.

Omlouváme se za komplikace při práci.
[jméno], Doktůrek
```
Statements about state services (SÚKL, ČSSZ) come from the incident owner, not from guesses.

### Připomenutí po odmlčení
```
Dobrý den,

[datum] jsme Vám psali ohledně [téma]. Ozýváme se pro jistotu, kdyby zpráva zapadla.

[Co od Vás potřebujeme, nebo co Vám nabízíme.]

S pozdravem
[jméno], Doktůrek
```

When the situation needs an escalation rather than a reply, package it with `customer-escalation`.
