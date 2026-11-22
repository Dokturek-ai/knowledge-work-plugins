---
name: triage-nda
description: Rapidly triage an incoming NDA under Czech law and classify it as GREEN (recommend signing), YELLOW (points to resolve) or RED (do not sign as is); every result is a recommendation to Honza, nothing is signed without him. Use when a new NDA arrives from a practice, an AIS vendor, a partner or an investor, or when screening for embedded non-solicits, non-competes or missing carveouts.
argument-hint: "<NDA file or text>"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- The Doktůrek party is **Clementine Solutions s.r.o.** Typical counterparties: practices, AIS vendors, integration partners, investors.
- An NDA that touches patient data is not an NDA case: route it to a DPA review (`review-contract`).
- No lawyer is engaged yet: YELLOW and RED go to Honza with the list of points for an external lawyer.
- **GREEN is a recommendation to Honza, not an approval.** Nothing is signed without him; there is no delegation of signing authority.
- **No local NDA playbook exists** (there is no `legal.local.md`). Use the Czech defaults in Step 2; for anything touching personal data, the reference is [`dpa-revision-brief.md`](https://github.com/Dokturek-ai/dokturek-docs/blob/main/04-pravo-a-regulatorika/dpa-revision-brief.md).
- A contractual penalty (smluvní pokuta, § 2048 OZ) is common in Czech NDAs: treat it as YELLOW and check its amount, whether it is mutual and whether it excludes damages beyond the penalty.

# /triage-nda -- NDA Pre-Screening

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Triage the NDA: $ARGUMENTS

Rapidly triage incoming NDAs against standard screening criteria. Classify the NDA as a recommendation to Honza: sign, resolve specific points, or do not sign as is.

**Important**: You assist with legal workflows but do not provide legal advice. All analysis should be reviewed by qualified legal professionals before being relied upon.

## Invocation

```
/legal:triage-nda <NDA file or text>
```

## Workflow

### Step 1: Accept the NDA

Accept the NDA in any format:
- **File upload**: PDF, DOCX, or other document format
- **URL**: Link to the NDA in a document system
- **Pasted text**: NDA text pasted directly

If no NDA is provided, prompt the user to supply one.

### Step 2: Apply Czech Defaults

Doktůrek has no local NDA playbook (no `legal.local.md`); do not look for one. Apply these defaults and say in the report that they were used ([P], to be confirmed by a lawyer):
  - Mutual obligations required (unless Clementine Solutions s.r.o. is only disclosing)
  - Term: 2-3 years standard, up to 5 years for trade secrets (obchodní tajemství, § 504 OZ)
  - Standard carveouts required: independently developed, publicly available, rightfully received from third party, required by law
  - No non-solicitation or non-compete provisions
  - No residuals clause (or narrowly scoped if present)
  - A contractual penalty (smluvní pokuta, § 2048 OZ) is acceptable if proportionate and mutual; flag it YELLOW for Honza
  - Czech law and Czech courts

### Step 3: Quick Screen

Evaluate the NDA against each screening criterion systematically.

#### 1. Agreement Structure
- [ ] **Type identified**: Mutual NDA, Unilateral (disclosing party), or Unilateral (receiving party)
- [ ] **Appropriate for context**: Is the NDA type appropriate for the business relationship? (e.g., mutual for exploratory discussions, unilateral for one-way disclosures)
- [ ] **Standalone agreement**: Confirm the NDA is a standalone agreement, not a confidentiality section embedded in a larger commercial agreement

#### 2. Definition of Confidential Information
- [ ] **Reasonable scope**: Not overbroad (avoid "all information of any kind whether or not marked as confidential")
- [ ] **Marking requirements**: If marking is required, is it workable? (Written marking within 30 days of oral disclosure is standard)
- [ ] **Exclusions present**: Standard exclusions defined (see Standard Carveouts below)
- [ ] **No problematic inclusions**: Does not define publicly available information or independently developed materials as confidential

#### 3. Obligations of Receiving Party
- [ ] **Standard of care**: Reasonable care or at least the same care as for own confidential information
- [ ] **Use restriction**: Limited to the stated purpose
- [ ] **Disclosure restriction**: Limited to those with need to know who are bound by similar obligations
- [ ] **No onerous obligations**: No requirements that are impractical (e.g., encrypting all communications, maintaining physical logs)

#### 4. Standard Carveouts
All of the following carveouts should be present:
- [ ] **Public knowledge**: Information that is or becomes publicly available through no fault of the receiving party
- [ ] **Prior possession**: Information already known to the receiving party before disclosure
- [ ] **Independent development**: Information independently developed without use of or reference to confidential information
- [ ] **Third-party receipt**: Information rightfully received from a third party without restriction
- [ ] **Legal compulsion**: Right to disclose when required by law, regulation, or legal process (with notice to the disclosing party where legally permitted)

#### 5. Permitted Disclosures
- [ ] **Employees**: Can share with employees who need to know
- [ ] **Contractors/advisors**: Can share with contractors, advisors, and professional consultants under similar confidentiality obligations
- [ ] **Affiliates**: Can share with affiliates (if needed for the business purpose)
- [ ] **Legal/regulatory**: Can disclose as required by law or regulation

#### 6. Term and Duration
- [ ] **Agreement term**: Reasonable period for the business relationship (1-3 years is standard)
- [ ] **Confidentiality survival**: Obligations survive for a reasonable period after termination (2-5 years is standard; trade secrets may be longer)
- [ ] **Not perpetual**: Avoid indefinite or perpetual confidentiality obligations (exception: trade secrets, which may warrant longer protection)

#### 7. Return and Destruction
- [ ] **Obligation triggered**: On termination or upon request
- [ ] **Reasonable scope**: Return or destroy confidential information and all copies
- [ ] **Retention exception**: Allows retention of copies required by law, regulation, or internal compliance/backup policies
- [ ] **Certification**: Certification of destruction is reasonable; sworn affidavit is onerous

#### 8. Remedies
- [ ] **Injunctive relief**: Acknowledgment that breach may cause irreparable harm and equitable relief may be appropriate is standard
- [ ] **Contractual penalty (smluvní pokuta, § 2048 OZ)**: Common in Czech NDAs. Check the amount in Kč, whether it applies per breach, whether it is mutual, and whether the parties excluded damages beyond the penalty (§ 2050 OZ). A disproportionate penalty can be reduced by a court (§ 2051 OZ); whether that applies ověří právník
- [ ] **Not one-sided**: Remedies provisions apply equally to both parties (in mutual NDAs)

#### 9. Problematic Provisions to Flag
- [ ] **No non-solicitation**: NDA should not contain employee non-solicitation provisions
- [ ] **No non-compete**: NDA should not contain non-compete provisions
- [ ] **No exclusivity**: NDA should not restrict either party from entering similar discussions with others
- [ ] **No standstill**: NDA should not contain standstill or similar restrictive provisions (unless M&A context)
- [ ] **No residuals clause** (or narrowly scoped): If a residuals clause is present, it should be limited to information retained in unaided memory of individuals and should not apply to trade secrets or patented information
- [ ] **No IP assignment or license**: NDA should not grant any intellectual property rights
- [ ] **No audit rights**: Unusual in standard NDAs

#### 10. Governing Law and Jurisdiction
- [ ] **Reasonable jurisdiction**: A well-established commercial jurisdiction
- [ ] **Consistent**: Governing law and jurisdiction should be in the same or related jurisdictions
- [ ] **No mandatory arbitration** (in standard NDAs): Litigation is generally preferred for NDA disputes

### Step 4: Classify

Based on the screening results, assign a classification:

#### GREEN -- Recommend Signing

**All** of the following must be true:
- NDA is mutual (or unilateral in the appropriate direction)
- All standard carveouts are present
- Term is within standard range (1-3 years, survival 2-5 years)
- No non-solicitation, non-compete, or exclusivity provisions
- No residuals clause, or residuals clause is narrowly scoped
- Reasonable governing law jurisdiction
- Standard remedies (no contractual penalty, or none beyond what is flagged YELLOW)
- Permitted disclosures include employees, contractors, and advisors
- Return/destruction provisions include retention exception for legal/compliance
- Definition of confidential information is reasonably scoped

**Routing**: Recommendation to Honza. Nothing is signed without him.
- **Action**: Send the triage report to Honza with the recommendation to sign; mention anything a lawyer should glance at

#### YELLOW -- Points to Resolve

**One or more** of the following are present, but the NDA is not fundamentally problematic:
- Definition of confidential information is broader than preferred but not unreasonable
- Term is longer than standard but within market range (e.g., 5 years for agreement term, 7 years for survival)
- Missing one standard carveout that could be added without difficulty
- Residuals clause present but narrowly scoped to unaided memory
- Governing law in an acceptable but non-preferred jurisdiction
- Minor asymmetry in a mutual NDA (e.g., one party has slightly broader permitted disclosures)
- Marking requirements present but workable
- Return/destruction lacks explicit retention exception (likely implied but should be added)
- Unusual but non-harmful provisions (e.g., obligation to notify of potential breach)
- Contractual penalty (smluvní pokuta) or liquidated damages, if proportionate and not one-sided

**Routing**: Flag specific issues for Honza with proposed redlines and the points for an external lawyer.
- **Action**: Honza decides whether to negotiate the points or have a lawyer look at them

#### RED -- Significant Issues

**One or more** of the following are present:
- **Unilateral when mutual is required** (or wrong direction for the relationship)
- **Missing critical carveouts** (especially independent development or legal compulsion)
- **Non-solicitation or non-compete provisions** embedded in the NDA
- **Exclusivity or standstill provisions** without appropriate business context
- **Unreasonable term** (10+ years, or perpetual without trade secret justification)
- **Overbroad definition** that could capture public information or independently developed materials
- **Broad residuals clause** that effectively creates a license to use confidential information
- **IP assignment or license grant** hidden in the NDA
- **Disproportionate or one-sided contractual penalty** (e.g., a penalty that only Clementine Solutions s.r.o. pays, or an amount out of all proportion to the purpose)
- **Audit rights** without reasonable scope or notice requirements
- **Highly unfavorable jurisdiction** with mandatory arbitration
- **The document is not actually an NDA** (contains substantive commercial terms, exclusivity, or other obligations beyond confidentiality)

**Routing**: Recommend not signing as is. Honza decides between negotiation, a counterproposal and rejection; points for an external lawyer attached.
- **Action**: Do not sign as is; requires negotiation or counterproposal

### Step 5: Generate Triage Report

Output a structured report:

```
## NDA Triage Report

**Classification**: [GREEN / YELLOW / RED]
**Parties**: [party names]
**Type**: [Mutual / Unilateral (disclosing) / Unilateral (receiving)]
**Term**: [duration]
**Governing Law**: [jurisdiction]
**Review Basis**: Czech defaults (no local playbook)

## Screening Results

| Criterion | Status | Notes |
|-----------|--------|-------|
| Mutual Obligations | [PASS/FLAG/FAIL] | [details] |
| Definition Scope | [PASS/FLAG/FAIL] | [details] |
| Term | [PASS/FLAG/FAIL] | [details] |
| Standard Carveouts | [PASS/FLAG/FAIL] | [details] |
| [etc.] | | |

## Issues Found

### [Issue 1 -- YELLOW/RED]
**What**: [description]
**Risk**: [what could go wrong]
**Suggested Fix**: [specific language or approach]

[Repeat for each issue]

## Recommendation to Honza

[Specific recommendation: sign, resolve the listed points, or counter/reject. Nothing is signed without Honza.]

## Next Steps

1. [Action item 1]
2. [Action item 2]
```

### Step 6: Routing Suggestion

Based on the classification, recommend the appropriate next step:

| Classification | Recommended Action | Typical Timeline |
|---|---|---|
| GREEN | Recommendation to Honza to sign | Honza decides |
| YELLOW | To Honza with the flagged points and proposed redlines | Honza decides |
| RED | To Honza with a recommendation not to sign as is; points for an external lawyer | Honza decides |

Do not promise a turnaround time. For YELLOW and RED classifications:
- Include a brief summary of issues Honza can read in a minute
- Include the list of points for an external lawyer (no lawyer is engaged yet)
- No Doktůrek standard-form NDA is documented; do not claim one exists

## Common NDA Issues and Standard Positions

### Issue: Overbroad Definition of Confidential Information
**Standard position**: Confidential information should be limited to non-public information disclosed in connection with the stated purpose, with clear exclusions.
**Redline approach**: Narrow the definition to information that is marked or identified as confidential, or that a reasonable person would understand to be confidential given the nature of the information and circumstances of disclosure.

### Issue: Missing Independent Development Carveout
**Standard position**: Must include a carveout for information independently developed without reference to or use of the disclosing party's confidential information.
**Risk if missing**: Could create claims that internally-developed products or features were derived from the counterparty's confidential information.
**Redline approach**: Add standard independent development carveout.

### Issue: Non-Solicitation of Employees
**Standard position**: Non-solicitation provisions do not belong in NDAs. They are appropriate in employment agreements, M&A agreements, or specific commercial agreements.
**Redline approach**: Delete the provision entirely. If the counterparty insists, limit to targeted solicitation (not general recruitment) and set a short term (12 months).

### Issue: Broad Residuals Clause
**Standard position**: Resist residuals clauses. If required, limit to: (a) general ideas, concepts, know-how, or techniques retained in the unaided memory of individuals who had authorized access; (b) explicitly exclude trade secrets and patentable information; (c) does not grant any IP license.
**Risk if too broad**: Effectively grants a license to use the disclosing party's confidential information for any purpose.

### Issue: Perpetual Confidentiality Obligation
**Standard position**: 2-5 years from disclosure or termination, whichever is later. Trade secrets may warrant protection for as long as they remain trade secrets.
**Redline approach**: Replace perpetual obligation with a defined term. Offer a trade secret carveout for longer protection of qualifying information.

## Notes

- If the document is not actually an NDA (e.g., it's labeled as an NDA but contains substantive commercial terms), flag this immediately as a RED and recommend full contract review instead
- For NDAs that are part of a larger agreement (e.g., confidentiality section in an MSA), note that the broader agreement context may affect the analysis
- Always note that this is a screening tool, that GREEN is a recommendation and not an approval, and that a lawyer should review any items the user is uncertain about
