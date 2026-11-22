---
name: ticket-triage
description: Triage and prioritize a support request from a practice using Doktůrek. Use when a new request comes in and needs categorization, assigning P1-P4 priority, deciding which Doktůrek owner should handle it, or checking whether it's a duplicate or known issue before routing.
argument-hint: "<ticket or issue description>"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- Doktůrek has no agreed SLA or support tiers: never promise a response or resolution time to a practice. P1–P4 below only orders the internal queue.
- Tickets about a failed or unclear eRecept or eNeschopenka are urgent and go to the incident path (operations `incident-response`). Never tell a doctor to simply resend.
- Remove patient identifiers from the ticket text before analysis; ask the practice to send an anonymised description.

# Ticket triage

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Categorize, prioritize, and route an incoming support ticket or customer issue. Produces a structured triage assessment with a suggested initial response.

## Usage

```
/customer-support:ticket-triage <ticket text, customer message, or issue description>
```

Examples:
- `/customer-support:ticket-triage Ordinace hlásí, že eRecept se neodeslal a lékař nevidí žádnou chybovou hlášku`
- `/customer-support:ticket-triage "Sestře nejde přihlášení přes Keycloak, po zadání hesla se vrací na přihlašovací stránku"`
- `/customer-support:ticket-triage Lékař se ptá, kde najde dekurz, který uložil včera`
- `/customer-support:ticket-triage Přání ordinace: tisk seznamu objednaných pacientů na další den`

## Workflow

### 1. Parse the Issue

Read the input and extract:

- **Core problem**: What is the customer actually experiencing?
- **Symptoms**: What specific behavior or error are they seeing?
- **Customer context**: Who is this? Any account details, plan level, or history available?
- **Urgency signals**: Are they blocked? Is this production? How many users affected?
- **Emotional state**: Frustrated, confused, matter-of-fact, escalating?

### 2. Categorize and Prioritize

Using the category taxonomy and priority framework below:

- Assign a **primary category** (bug, how-to, feature request, billing, account, integration, security, data, performance) and an optional secondary category
- Assign a **priority** (P1–P4) based on impact and urgency
- Identify the **product area** the issue maps to

### 3. Check for Duplicates and Known Issues

Before routing, check available sources:

- **~~support platform**: Search for similar open or recently resolved tickets
- **~~knowledge base**: Check for known issues or existing documentation
- **~~project tracker**: Check if there's an existing bug report or feature request

Apply the duplicate detection process below.

### 4. Determine Routing

Using the routing rules below, recommend which Doktůrek owner should handle this based on category and complexity. A failed or unclear eRecept or eNeschopenka goes to operations `incident-response` first.

### 5. Generate Triage Output

```
## Triage: [One-line issue summary]

**Category:** [Primary] / [Secondary if applicable]
**Priority:** [P1-P4] — [Brief justification]
**Product area:** [Area/team]

### Issue Summary
[2-3 sentence summary of what the customer is experiencing]

### Key Details
- **Customer:** [Name/account if known]
- **Impact:** [Who and what is affected]
- **Workaround:** [Available / Not available / Unknown]
- **Related tickets:** [Links to similar issues if found]
- **Known issue:** [Yes — link / No / Checking]

### Routing Recommendation
**Route to:** [Owner from the routing table, or operations `incident-response`]
**Why:** [Brief reasoning]

### Suggested Initial Response
[Draft first reply in Czech: acknowledge the issue, ask for
missing details, give a verified workaround if one exists, name
the next step without a date. Start from the templates below.
Draft only; the user sends it after confirming.]

### Internal Notes
- [Any additional context for the agent picking this up]
- [Reproduction hints if it's a bug]
- [Escalation triggers to watch for]
```

### 6. Offer Next Steps

After presenting the triage:
- "Want me to draft a full response to the customer?"
- "Should I search for more context on this issue?"
- "Want me to check if this is a known bug in the tracker?"
- "Should I escalate this? I can package it with `customer-escalation`."

---

## Category Taxonomy

Assign every ticket a **primary category** and optionally a **secondary category**:

| Category | Description | Signal Words |
|----------|-------------|-------------|
| **Bug** | Product is behaving incorrectly or unexpectedly | Error, broken, crash, not working, unexpected, wrong, failing |
| **How-to** | Customer needs guidance on using the product | How do I, can I, where is, setting up, configure, help with |
| **Feature request** | Customer wants a capability that doesn't exist | Would be great if, wish I could, any plans to, requesting |
| **Billing** | Payment, subscription, invoice, or pricing issues | Charge, invoice, payment, subscription, refund, upgrade, downgrade |
| **Account** | Account access, permissions, settings, or user management | Login, password, access, permission, Keycloak, locked out, can't sign in |
| **Integration** | Issues connecting to third-party tools or APIs | API, webhook, integration, connect, OAuth, sync, third-party |
| **Security** | Security concerns, data access, or compliance questions | Data breach, unauthorized, compliance, GDPR, SOC 2, vulnerability |
| **Data** | Data quality, migration, import/export issues | Missing data, export, import, migration, incorrect data, duplicates |
| **Performance** | Speed, reliability, or availability issues | Slow, timeout, latency, down, unavailable, degraded |

### Category Determination Tips

- If the customer reports **both** a bug and a feature request, the bug is primary
- If they can't log in due to a bug, category is **Bug** (not Account) — root cause drives the category
- "It used to work and now it doesn't" = **Bug**
- "I want it to work differently" = **Feature request**
- "How do I make it work?" = **How-to**
- When in doubt, lean toward **Bug** — it's better to investigate than dismiss

## Priority Framework

### P1 — Critical
**Criteria:** Production system down, data loss or corruption, security breach, all or most users affected.

- The customer cannot use the product at all
- Data is being lost, corrupted, or exposed
- A security incident is in progress
- The issue is worsening or expanding in scope
- A failed or unclear eRecept or eNeschopenka (route to operations `incident-response`)

### P2 — High
**Criteria:** Major feature broken, significant workflow blocked, many users affected, no workaround.

- A core workflow is broken but the product is partially usable
- Multiple users are affected or a key account is impacted
- The issue is blocking time-sensitive work
- No reasonable workaround exists

### P3 — Medium
**Criteria:** Feature partially broken, workaround available, single user or small team affected.

- A feature isn't working correctly but a workaround exists
- The issue is inconvenient but not blocking critical work
- A single user or small team is affected
- The customer is not escalating urgently

### P4 — Low
**Criteria:** Minor inconvenience, cosmetic issue, general question, feature request.

- Cosmetic or UI issues that don't affect functionality
- Feature requests and enhancement ideas
- General questions or how-to inquiries
- Issues with simple, documented solutions

### Priority Escalation Triggers

Automatically bump priority up when:
- The practice has been blocked for a long time without an update
- Multiple customers report the same issue (pattern detected)
- The customer explicitly escalates or mentions executive involvement
- A workaround that was in place stops working
- The issue expands in scope (more users, more data, new symptoms)

## Routing Rules

Doktůrek has no support tiers or specialist teams. Route to a named owner (team table in the Doktůrek context):

| Route to | When |
|----------|------|
| **You (the user), with a drafted reply** | How-to questions with an answer documented in `dokturek-docs`, known issues with a verified workaround |
| **Operations `incident-response`** | A failed or unclear eRecept or eNeschopenka, an outage affecting practices |
| **Petr Sovadina** | Confirmed bugs, architecture, state integrations, data access or security concerns |
| **Jan Rožánek** | Integration details of eRecept, registries or eNeschopenka (via Petr when unsure) |
| **Jakub Sekula (Kuba)** | Environments, deploys, availability, performance, monitoring |
| **Martin Marhold** | Login, Keycloak, identity, gov-gateway |
| **MUDr. Anna Chromcová** | Anything clinical: content, safety, wording for doctors |
| **Jan Chromec (Honza)** | Subscription, price, contract or relationship questions; feature requests and priorities |

## Duplicate Detection

Before creating a new ticket or routing, check for duplicates:

1. **Search by symptom**: Look for tickets with similar error messages or descriptions
2. **Search by customer**: Check if this customer has an open ticket for the same issue
3. **Search by product area**: Look for recent tickets in the same feature area
4. **Check known issues**: Compare against documented known issues

**If a duplicate is found**, propose, do not act:
- Draft a link or comment that ties the new report to the existing issue, show the target issue and exact text, and post only after an explicit yes
- Draft a reply telling the practice this is a known problem, with the next step and no fix date
- List new information from this report that belongs in the existing issue
- Suggest a higher priority to the owner if the new report adds urgency (more practices affected, etc.)

## Initial Reply Templates (Czech)

Rules for every template: vykání, a concrete next step without a date, no claim that something was already logged, escalated or fixed unless the user confirms it happened, and no patient identifiers. Replace the bracketed parts; drop lines that do not apply.

### Chyba (bug)
```
Dobrý den,

děkujeme za popis. Rozumíme, že [konkrétní dopad, např. „nejde uložit dekurz“] Vám komplikuje práci.

Abychom mohli chybu prověřit, pošlete nám prosím [čas, kdy se to stalo; přesný text hlášky; snímek obrazovky bez údajů pacienta].
[Jen ověřené náhradní řešení: „Mezitím můžete [postup].“]

Dalším krokem je prověření chyby. Ozveme se Vám, až budeme vědět víc.

S pozdravem
[jméno], Doktůrek
```

### Dotaz „jak na to“ (how-to)
```
Dobrý den,

[přímá odpověď v jedné až dvou větách, ověřená v dokturek-docs]

Postup:
1. [krok]
2. [krok]

Pokud se na některém kroku zastavíte, napište nám prosím, na kterém.

S pozdravem
[jméno], Doktůrek
```

### Přání nové funkce (feature request)
```
Dobrý den,

děkujeme za podnět. Chápeme, proč by Vám [funkce] pomohla při [jejich práce].

Váš podnět předáme k posouzení. Zda a kdy funkci zařadíme, zatím slíbit nemůžeme.
[Jen ověřená alternativa: „Zatím můžete [postup].“]

S pozdravem
[jméno], Doktůrek
```

### Předplatné a platby
```
Dobrý den,

děkujeme za zprávu. Abychom mohli [platbu / fakturu / předplatné] prověřit, pošlete nám prosím [číslo faktury, datum platby].
Zveřejněný ceník předplatného najdete na https://dokturek.ai/cenik.

S pozdravem
[jméno], Doktůrek
```
Individual terms, refunds and exceptions belong to Honza; the reply never offers them.

### eRecept nebo eNeschopenka
```
Dobrý den,

děkujeme za rychlé upozornění. Problém s [eReceptem / eNeschopenkou] řešíme jako naléhavý.

Pošlete nám prosím čas odeslání a přesný text hlášky, bez jména a rodného čísla pacienta.
Další postup Vám napíšeme, jakmile ověříme stav dokladu.

S pozdravem
[jméno], Doktůrek
```
Do not advise resending; the next step for the patient comes from the incident owner.

### Bezpečnost nebo přístup k datům
```
Dobrý den,

děkujeme, že jste nám to dali vědět. Bereme to vážně a předáme to technickému vlastníkovi systému.

Prosíme, do další zprávy nevkládejte údaje pacientů. Pošlete nám jen [co jste viděli, kdy a pod jakým účtem].

S pozdravem
[jméno], Doktůrek
```
Add a protective recommendation only when Petr has confirmed it.

## Triage Best Practices

1. Read the full ticket before categorizing — context in later messages often changes the assessment
2. Categorize by **root cause**, not just the symptom described
3. When in doubt on priority, err on the side of higher — it's easier to de-escalate than to recover from a missed urgent case
4. Always check for duplicates and known issues before routing
5. Write internal notes that help the next person pick up context quickly
6. Include what you've already checked or ruled out to avoid duplicate investigation
7. Flag patterns — if you're seeing the same issue repeatedly, escalate the pattern even if individual tickets are low priority
