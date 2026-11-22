---
name: draft-content
description: Draft Doktůrek content for public channels (web and landing pages, newsletter, social media, blog, press releases) with channel-specific formatting and SEO recommendations. Use when writing marketing content for many readers, when you need headline or subject line options, or when adapting a message for a specific platform and audience. An asset for one named practice belongs to sales:create-an-asset.
argument-hint: "<content type and topic>"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- Audience: Czech GPs and practice staff. Czech, vykání, the Doktůrek voice. Prices only from `dokturek.ai/cenik`; no MDR or certification claims, no "AI rozhodla".
- Clinical statements need Anna's confirmation; screenshots only with synthetic data.
- No case studies, testimonials, customer quotes or results before 1 January 2027 unless the user provides them with the person's approval.

# Draft Content

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Generate marketing content drafts tailored to a specific content type, audience, and brand voice.

## Trigger

User runs `/marketing:draft-content` or asks to draft, write, or create marketing content.

## Inputs

Gather the following from the user. If not provided, ask before proceeding:

1. **Content type** — one of:
   - Blog post
   - Social media post (specify platform: LinkedIn, Twitter/X, Instagram, Facebook)
   - Email newsletter
   - Landing page copy
   - Press release
   - Case study (only from material the user provides)

2. **Topic** — the subject or theme of the content

3. **Target audience** — who this content is for (role, industry, seniority, pain points)

4. **Key messages** — 2-4 main points or takeaways to communicate

5. **Tone** — e.g., authoritative, conversational, inspirational, technical, witty (optional; the Doktůrek voice is the default)

6. **Length** — target word count or format constraint (e.g., "1000 words", "280 characters", "3 paragraphs")

## Brand Voice

- Always use `dokturek-docs` → [`05-design/Doktůrek-brand/DESIGN.md`](https://github.com/Dokturek-ai/dokturek-docs/blob/main/05-design/Doktůrek-brand/DESIGN.md) and the Voice section of the Doktůrek context. Tell the user which source you applied; if DESIGN.md is not reachable, say so and use the Voice section.
- Apply the tone consistently throughout the draft.

## Content Generation by Type

### Blog Post
- Engaging headline (provide 2-3 options)
- Introduction with a hook (question, sourced statistic, or story)
- 3-5 organized sections with descriptive subheadings
- Supporting points, examples, or data references in each section
- Conclusion with a clear call to action
- SEO considerations: suggest a primary keyword, include it in the headline and first paragraph, use related keywords in subheadings

### Social Media Post
- Platform-appropriate format and length
- Hook in the first line
- Hashtag suggestions (3-5 relevant hashtags)
- Call to action or engagement prompt
- Emoji usage appropriate to brand and platform
- If LinkedIn: professional framing, paragraph breaks for readability
- If Twitter/X: concise, punchy, within character limit
- If Instagram: visual-first language, story-driven, hashtag block

### Email Newsletter
- Subject line (provide 2-3 options with open-rate considerations)
- Preview text
- Greeting
- Body sections with clear hierarchy
- Call to action button text
- Sign-off
- Unsubscribe note reminder

### Landing Page Copy
- Headline and subheadline
- Hero section copy
- Value propositions (3-4 benefit-driven bullets or sections)
- No social proof before 1 January 2027 unless the user provides it; leave a marked placeholder [N] instead of inventing a testimonial or number
- Primary and secondary CTAs
- FAQ section suggestions
- SEO: meta title and meta description suggestions

### Press Release
- Headline following press release conventions
- Dateline and location
- Lead paragraph (who, what, when, where, why)
- Supporting quotes (provide placeholder guidance)
- Company boilerplate placeholder
- Media contact placeholder
- Standard press release formatting

### Case Study
- Title emphasizing the result
- Write only from material the user provides (before 1 January 2027 there are no paying practices to describe)
- Practice overview (type, size, challenge), with the practice's approval to be named
- Challenge section
- Solution section (what was implemented)
- Results section with metrics from the user; mark anything unverified [N]
- Quote only if the user provides it with the person's approval
- Call to action

## SEO Considerations (for web content)

For blog posts, landing pages, and other web-facing content:
- Suggest a primary keyword based on the topic
- Recommend keyword placement: headline, first paragraph, subheadings, meta description
- Suggest internal and external linking opportunities
- Recommend a meta description (under 160 characters)
- Note image alt text opportunities

## Output

Present the draft with clear formatting. After the draft, include:
- A brief note on what brand voice and tone were applied
- Any SEO recommendations (for web content)
- Suggestions for next steps (e.g., "Review with Filip", "Confirm clinical statements with Anna", "Pair with a visual")

Ask: "Would you like me to revise any section, adjust the tone, or create a variation for a different channel?"
