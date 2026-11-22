---
name: customer-research
description: Multi-source research on a customer question or topic with source attribution. Use when a customer asks something you need to look up, investigating whether a bug has been reported before, checking what was previously told to a specific account, or gathering background before drafting a response.
argument-hint: "<question or topic>"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- Search `dokturek-docs` (STAV.md, SLOVNIK.md, the register) and closed GitHub Issues before the web. Official sources for state services: SÚKL, ČSSZ, MZČR / NCEZ.

# Customer research

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Multi-source research on a customer question, product topic, or account-related inquiry. Synthesizes findings from all available sources with clear attribution and confidence scoring.

## Usage

```
/customer-support:customer-research <question or topic>
```

## Workflow

### 1. Parse the Research Request

Identify what type of research is needed:
- **Customer question**: Something a customer has asked that needs an answer (e.g., „Umí Doktůrek přihlášení s dvoufázovým ověřením?“ — answer only from `dokturek-docs` or code)
- **Issue investigation**: Background on a reported problem (e.g., "Has this bug been reported before? What's the known workaround?")
- **Account context**: History with a specific customer (e.g., „Co jsme této ordinaci naposledy psali k předplatnému?“)
- **Topic research**: General topic relevant to support work (e.g., "Best practices for webhook retry logic")

Before searching, clarify what you're actually trying to find:
- Is this a factual question with a definitive answer?
- Is this a contextual question requiring multiple perspectives?
- Is this an exploratory question where the scope is still being defined?
- Who is the audience for the answer (internal team, customer, leadership)?

### 2. Search Available Sources

Search systematically through the source tiers below, adapting to what is connected. Don't stop at the first result — cross-reference across sources.

**Tier 1 — Official Internal Sources (highest confidence):**
- ~~knowledge base (if connected): product docs, runbooks, FAQs, policy documents
- Uploaded files: documents the user attached in this conversation (internal specs, guides, past research)
- Product roadmap (internal-facing): feature timelines, priorities

**Tier 2 — Organizational Context:**
- ~~CRM notes: account notes, activity history, previous answers, opportunity details
- ~~support platform (if connected): previous resolutions, known issues, workarounds
- Meeting notes: previous discussions, decisions, commitments

**Tier 3 — Team Communications:**
- ~~chat: search for the topic in relevant channels; check if teammates have discussed or answered this before
- ~~email: search for previous correspondence on this topic
- Calendar notes: meeting agendas and post-meeting notes

**Tier 4 — External Sources:**
- Web search: official documentation, blog posts, community forums
- Public knowledge bases, help centers, release notes
- Third-party documentation: integration partners, complementary tools

**Tier 5 — Inferred or Analogical (use when direct sources don't yield answers):**
- Similar situations: how similar questions were handled before
- Analogous customers: what worked for comparable accounts
- General best practices: industry standards and norms

### 3. Synthesize Findings

Compile results into a structured research brief:

```
## Research: [Question/Topic]

### Answer
[Clear, direct answer to the question — lead with the bottom line]

**Confidence:** [High / Medium / Low]
[Explain what drives the confidence level]

### Key Findings

**From [Source 1]:**
- [Finding with specific detail]
- [Finding with specific detail]

**From [Source 2]:**
- [Finding with specific detail]

### Context & Nuance
[Any caveats, edge cases, or additional context that matters]

### Sources
1. [Source name/link] — [what it contributed]
2. [Source name/link] — [what it contributed]
3. [Source name/link] — [what it contributed]

### Gaps & Unknowns
- [What couldn't be confirmed]
- [What might need verification from a subject matter expert]

### Recommended Next Steps
- [Action if the answer needs to go to a customer]
- [Action if further research is needed]
- [Who to consult for verification if needed]
```

### 4. Handle Insufficient Sources

If no connected sources yield results:

- Perform web research on the topic
- Ask the user for internal context:
  - "I couldn't find this in connected sources. Do you have internal docs or knowledge base articles about this?"
  - "Has your team discussed this topic before? Any ~~chat channels I should check?"
  - "Is there a subject matter expert who would know the answer?"
- Be transparent about limitations:
  - "This answer is based on web research only — please verify against your internal documentation before sharing with the customer."
  - "I found a possible answer but couldn't confirm it from an authoritative internal source."

### 5. Customer-Facing Considerations

If the research is to answer a customer question:

- Flag if the answer involves product roadmap, pricing, legal, or security topics that may need review
- Note if the answer differs from what may have been communicated previously
- Suggest appropriate caveats for the customer-facing response
- Offer to draft the customer response: "Want me to draft a response to the customer based on these findings?"

### 6. Knowledge Capture

After research is complete, suggest capturing the knowledge:

- "Want me to draft a FAQ entry or article from this (`kb-article`)?"
- "Should I propose the exact text of a change to `dokturek-docs`?"

Propose text only: never write to a knowledge base, Notion or `dokturek-docs` yourself. The user applies the change after review.

---

## Source Prioritization and Confidence

### Confidence by Source Tier

| Tier | Source Type | Confidence | Notes |
|------|-------------|------------|-------|
| 1 | Official internal docs, KB, policies | **High** | Trust unless clearly outdated — check dates |
| 2 | CRM, support tickets, meeting notes | **Medium-High** | May be subjective or incomplete |
| 3 | Chat, email, calendar notes | **Medium** | Informal, may be out of context or speculative |
| 4 | Web, forums, third-party docs | **Low-Medium** | May not reflect your specific situation |
| 5 | Inference, analogies, best practices | **Low** | Clearly flag as inference, not fact |

### Confidence Levels

Always assign and communicate a confidence level:

**High Confidence:**
- Answer confirmed by official documentation or authoritative source
- Multiple sources corroborate the same answer
- Information is current (verified within a reasonable timeframe)
- "I'm confident this is accurate based on [source]."

**Medium Confidence:**
- Answer found in informal sources (chat, email) but not official docs
- Single source without corroboration
- Information may be slightly outdated but likely still valid
- "Based on [source], this appears to be the case, but I'd recommend confirming with [team/person]."

**Low Confidence:**
- Answer is inferred from related information
- Sources are outdated or potentially unreliable
- Contradictory information found across sources
- "I wasn't able to find a definitive answer. Based on [context], my best assessment is [answer], but this should be verified before sharing with the customer."

**Unable to Determine:**
- No relevant information found in any source
- Question requires specialized knowledge not available in sources
- "I couldn't find information about this. I recommend reaching out to [suggested expert/team] for a definitive answer."

### Handling Contradictions

When sources disagree:
1. Note the contradiction explicitly
2. Identify which source is more authoritative or more recent
3. Present both perspectives with context
4. Recommend how to resolve the discrepancy
5. If going to a customer: use the most conservative/cautious answer until resolved

## When to Escalate vs. Answer Directly

### Answer Directly When:
- Official documentation clearly addresses the question
- Multiple reliable sources corroborate the answer
- The question is factual and non-sensitive
- The answer doesn't involve commitments, timelines, or pricing
- You've answered similar questions before with confirmed accuracy

### Escalate or Verify When:
- The answer involves product roadmap commitments or timelines
- Pricing, legal terms, or contract-specific questions
- Security, compliance, or data handling questions
- The answer could set a precedent or create expectations
- You found contradictory information in sources
- The question involves a specific customer's custom configuration
- The answer requires specialized expertise you don't have
- The customer is at risk and the wrong answer could exacerbate the situation

### Who to Ask (team table in the Doktůrek context):
1. **Petr Sovadina**: technical questions, architecture, state integrations, data handling, bugs (Jan Rožánek for eRecept, registry and eNeschopenka details)
2. **Jakub Sekula (Kuba)**: environments, availability, deploys
3. **Martin Marhold**: login, Keycloak, gov-gateway
4. **MUDr. Anna Chromcová**: anything clinical
5. **Jan Chromec (Honza)**: roadmap commitments, price, subscription, contracts, exceptions
6. **Regulatory questions** (MDR, AI Act): the `mdr-compliance` plugin; no lawyer or DPO is engaged yet, so legal and privacy questions go to Honza as an open question

## Research Documentation for Team Knowledge Base

After completing research, capture the knowledge for future use.

### When to Document:
- Question has come up before or likely will again
- Research took significant effort to compile
- Answer required synthesizing multiple sources
- Answer corrects a common misunderstanding
- Answer involves nuance that's easy to get wrong

### Documentation Format:
```
## [Question/Topic]

**Last Verified:** [date]
**Confidence:** [level]

### Answer
[Clear, direct answer]

### Details
[Supporting detail, context, and nuance]

### Sources
[Where this information came from]

### Related Questions
[Other questions this might help answer]

### Review Notes
[When to re-verify, what might change this answer]
```

### Knowledge Base Hygiene:
- These entries are proposed text; the user files them (in `dokturek-docs` or the practice knowledge base once one exists). Never write to Notion.
- Date-stamp all entries
- Flag entries that reference specific product versions or features
- Review and update entries quarterly
- Archive entries that are no longer relevant
- Tag entries for searchability (by topic, product area, customer segment)
