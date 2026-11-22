---
name: brand-review
description: Review Doktůrek marketing and sales texts (web, newsletter, social posts, emails, sales materials) against the brand voice in DESIGN.md and the Doktůrek context, flagging deviations by severity with specific before/after fixes. Use when checking a draft before it ships, auditing copy for voice and terminology, or screening for unsubstantiated clinical, AI, certification or compliance claims. Product UI copy belongs to design:ux-copy.
argument-hint: "<content to review>"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- The brand authority is [`05-design/Doktůrek-brand/DESIGN.md`](https://github.com/Dokturek-ai/dokturek-docs/blob/main/05-design/Doktůrek-brand/DESIGN.md): voice, vocabulary, colours (teal #1e7f74), typography (Geist, Roboto Mono). The generated OpenDesign templates are marked as not valid.
- Flag every claim about AI, diagnosis, certification or compliance that the documents do not prove.

# Brand Review

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Review marketing content against brand voice, style guidelines, and messaging standards. Flag deviations and provide specific improvement suggestions.

## Trigger

User runs `/marketing:brand-review` or asks to review, check, or audit content against brand guidelines.

## Inputs

1. **Content to review** — accept content in any of these forms:
   - Pasted directly into the conversation
   - A file path or ~~knowledge base reference (e.g. a file in `dokturek-docs`; Notion is a read-only archive)
   - A URL to a published page
   - Multiple pieces for batch review

2. **Brand guidelines source** (fixed):
   - Always review against `dokturek-docs` → `05-design/Doktůrek-brand/DESIGN.md` and the Voice section of the Doktůrek context; the context wins where they differ on wording rules
   - If DESIGN.md is not reachable, say so and review against the Voice section and the Czech conventions below

## Review Process

### Brand Dimensions

Evaluate the content against each of these dimensions:

#### Voice and Tone
- Does the content match the defined brand voice attributes?
- Is the tone appropriate for the content type and audience?
- Are there shifts in voice that feel inconsistent?
- Flag specific sentences or phrases that deviate with an explanation of why

#### Terminology and Language
- Are preferred brand terms used correctly?
- Are any "avoid" terms or phrases present?
- Is jargon level appropriate for the target audience?
- Are product names, feature names, and branded terms used correctly (capitalization, formatting)?

#### Messaging Pillars
- Does the content align with defined messaging pillars or value propositions?
- Are claims consistent with approved messaging?
- Is the content reinforcing or contradicting brand positioning?

#### Style Guide Compliance
- Czech grammar and punctuation (see Czech Conventions below)
- Formatting conventions (headers, lists, emphasis)
- Number, date and time formatting per Czech Conventions
- Acronym usage (defined on first use?)

### General Quality (Always Checked)

Evaluate the content for:

#### Clarity
- Is the main message clear within the first paragraph?
- Are sentences concise and easy to understand?
- Is the structure logical and easy to follow?
- Are there ambiguous statements or unclear references?

#### Consistency
- Is the tone consistent throughout?
- Are terms used consistently (no switching between synonyms for the same concept)?
- Is formatting consistent (headers, lists, capitalization)?

#### Professionalism
- Is the content free of typos, grammatical errors, and awkward phrasing?
- Is the tone appropriate for the intended audience?
- Are claims supported or substantiated?

### Legal and Compliance Flags (Always Checked)

Regardless of whether brand guidelines are configured, flag:
- **Unsubstantiated claims** — superlatives ("best", "fastest", "only") without evidence or qualification
- **Missing disclaimers** — financial claims, health claims, or guarantees that may need legal disclaimers
- **Comparative claims** — comparisons to competitors that could be challenged
- **Regulatory language** — content that may need compliance review (financial services, healthcare, etc.)
- **Testimonial issues** — quotes or endorsements without attribution or approval; any testimonial, case study or result from a practice before 1 January 2027 that the user did not provide
- **Doktůrek claims** — clinical statements without Anna's confirmation; MDR, certification or compliance claims the documents do not prove (Q-750, Q-753); "AI rozhodla" or anything that lets the system decide instead of the doctor; prices other than a link to `dokturek.ai/cenik`; discounts or incentives
- **Copyright concerns** — content that appears to be closely paraphrased from other sources

## Brand Voice Reference

Use these frameworks to evaluate content against brand standards or to help the user document their brand voice.

### Brand Voice Documentation Framework

A complete brand voice document should cover these areas:

1. **Brand Personality** — Define the brand as if it were a person. Example: "If our brand were a person, they would be a knowledgeable colleague who explains complex things simply, celebrates your wins genuinely, and never talks down to you."
2. **Voice Attributes** — 3-5 attributes that define how the brand communicates, each defined with what it means in practice, what it does NOT mean (to prevent misinterpretation), and an example.
3. **Audience Awareness** — Who the brand is speaking to (primary and secondary), what they care about, their level of expertise, and how they expect to be addressed.
4. **Core Messaging Pillars** — 3-5 key themes the brand consistently communicates, the hierarchy of these messages, and how each pillar connects to audience needs.
5. **Tone Spectrum** — How the voice adapts across contexts while remaining recognizably the same brand.
6. **Style Rules** — Specific grammar, formatting, and language rules.
7. **Terminology** — Preferred and avoided terms.

### Voice Attribute Spectrums

When defining or evaluating brand voice, position attributes on a spectrum:

| Spectrum | One End | Other End |
|----------|---------|-----------|
| Formality | Formal, institutional | Casual, conversational |
| Authority | Expert, authoritative | Peer-level, collaborative |
| Emotion | Warm, empathetic | Direct, matter-of-fact |
| Complexity | Technical, precise | Simple, accessible |
| Energy | Bold, energetic | Calm, measured |
| Humor | Playful, witty | Serious, earnest |
| Innovation | Cutting-edge, forward-looking | Established, proven |

For each chosen attribute, document it in this format:

**[Attribute name]**
- **We are**: [what this means in practice]
- **We are not**: [common misinterpretation to avoid]
- **This sounds like**: [example sentence demonstrating the attribute]
- **This does NOT sound like**: [example sentence violating the attribute]

Example:

**Approachable**
- **We are**: friendly, clear, jargon-free, welcoming to beginners and experts alike
- **We are not**: dumbed-down, overly casual, or lacking substance
- **This sounds like**: "Here's how to get started — it takes about five minutes."
- **This does NOT sound like**: "Yo! This is super easy, even a noob can do it lol."

### Tone Adaptation Across Channels and Contexts

The brand voice stays consistent, but tone adapts to context. Tone is the emotional inflection applied to the voice.

#### Tone by Channel

| Channel | Tone Adaptation | Example |
|---------|----------------|---------|
| Blog | Informative, conversational, educational | "Let's walk through how this works and why it matters for your team." |
| Social media (LinkedIn) | Professional, thought-provoking, concise | "Three things we learned from running 50 campaigns this quarter." |
| Social media (Twitter/X) | Punchy, direct, sometimes witty | "Your landing page has 3 seconds. Make them count." |
| Email marketing | Personal, helpful, action-oriented | "We put together something we think you'll find useful." |
| Sales collateral | Confident, benefit-driven, verifiable | "Víc času na pacienty, míň na papíry." (no unsourced numbers) |
| Support/Help docs | Clear, patient, step-by-step | "If you see this error, here's how to fix it." |
| Press release | Formal, factual, newsworthy | "The company today announced the launch of..." |
| Error messages | Empathetic, helpful, blame-free | "Something went wrong on our end. We're looking into it." |

#### Tone by Situation

| Situation | Tone Adaptation |
|-----------|----------------|
| Product launch | Excited, confident, forward-looking |
| Incident or outage | Transparent, empathetic, accountable |
| Customer success story | Celebratory, specific, crediting the customer |
| Thought leadership | Authoritative, nuanced, evidence-based |
| Onboarding | Welcoming, encouraging, clear |
| Bad news (price increase, deprecation) | Honest, respectful, solution-oriented |
| Competitive comparison | Confident but fair, fact-based, not disparaging |

#### Tone Adaptation Rule
The voice attributes remain fixed. Tone dials them up or down based on context. For example, if a brand is "bold and warm":
- In a product launch, dial up boldness
- In an incident response, dial up warmth
- Neither attribute disappears; the balance shifts

### Czech Conventions

Apply these unless DESIGN.md says otherwise:

| Rule | Convention | Example |
|------|-----------|---------|
| E-mail | With a hyphen | "e-mail", not "email" |
| Date | Day. month. year with spaces | "22. 11. 2026" |
| Time | 24-hour | "15:00", not "3:00 PM" |
| Headings | Sentence case | "Jak začít", not "Jak Začít" |
| Numbers | Space as thousands separator, decimal comma | "1 000 Kč", "2,5 %" |
| Percent | Space before % ("50 procent"); no space only in the adjective form ("50%" = padesátiprocentní) | "50 %" |
| Quotation marks | Czech quotes | „ordinace“ |
| Dash | En dash with spaces for a pause, hyphen inside words | "kartotéka – přehled", "e-mail" |
| Address | Vykání; capitalised Vy/Vám in a letter to one person, lowercase vy in texts for many readers | "Děkujeme Vám" (one doctor), "vyzkoušejte" (newsletter) |
| Brand | Doktůrek with diacritics, without ".ai" in running text | "Doktůrek", not "Dokturek" |
| Line breaks | No single-letter preposition or conjunction at the end of a line on web and print (v, k, s, z, o, u, a, i) | non-breaking space after "v" |

#### Punctuation and Emphasis
- Exclamation mark policy (limited use, never more than one)
- ALL CAPS policy (avoid; use bold for emphasis instead)
- Emoji usage by channel (professional channels: minimal or none; social: where appropriate)

### Terminology Management

#### Preferred Terms

From the Voice section of the Doktůrek context; DESIGN.md adds to it:

| Use This | Not This | Notes |
|----------|----------|-------|
| Doktůrek | Dokturek, Doktůrek.ai | ".ai" only in the domain |
| přihlásit se | zalogovat se, login (verb) | |
| předplatné | subscription | |
| koncept, uloženo | draft, saved | |
| ordinace, kartotéka, pacient | | Preferred everyday words |
| Systém navrhuje, lékař rozhoduje | AI rozhodla, garantovaná diagnóza | Clinical decisions stay with the doctor |
| ambulantní informační systém (AIS) | EHRko | |
| (plain description) | revoluce, hotovo bez ověření | |

#### Product and Feature Names
- Official capitalization for product names
- When to use the full product name vs. shorthand
- Whether to use "the" before product names
- How to handle versioning in copy
- Trademark and registration symbols (when required and when to omit)

#### Inclusive Language
- Avoid ableist language and idioms that exclude readers
- Use "jednoduše" or "přehledně" carefully: what is easy varies by person

#### Industry Jargon Management
- Define which technical terms the audience understands without explanation
- List jargon that should always be defined or replaced with plain language
- Specify which acronyms need to be spelled out on first use
- Audience-specific glossary for terms that mean different things to different readers

#### Competitor and Category Terms
- How to refer to your product category (use your preferred framing)
- How to refer to competitors (by name or generically)
- Terms competitors have coined that you should avoid (to prevent reinforcing their positioning)
- Your preferred differentiation language

## Output Format

Present the review as:

### Summary
- Overall assessment: how well the content aligns with brand standards (or general quality)
- 1-2 sentence summary of the biggest strengths
- 1-2 sentence summary of the most important improvements

### Detailed Findings

For each issue found, provide:

| Issue | Location | Severity | Suggestion |
|-------|----------|----------|------------|

Where severity is:
- **High** — contradicts brand voice, contains compliance risk, or significantly undermines messaging
- **Medium** — inconsistent with guidelines but not damaging
- **Low** — minor style or preference issue

### Revised Sections

For the top 3-5 highest-severity issues, provide a before/after showing the original text and a suggested revision.

### Legal/Compliance Flags

List any legal or compliance concerns separately with recommended actions.

## After Review

Ask: "Would you like me to:
- Revise the full content with these suggestions applied?
- Focus on fixing just the high-severity issues?
- Review additional content against the same guidelines?
- Propose text for a change to DESIGN.md (you file it in `dokturek-docs`)?"
