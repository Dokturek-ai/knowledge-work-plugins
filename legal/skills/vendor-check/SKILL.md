---
name: vendor-check
description: Check a vendor as a sub-processor of Clementine Solutions s.r.o. under Art. 28(2) and 28(4) GDPR — prior written authorisation by the practices, a processing contract with the same obligations, processing location in the EU/EEA, presence in the DPA sub-processor annex, and SCC with a transfer impact assessment if anything leaves the EEA. Use when adding or renewing a vendor that touches personal or patient data, or when checking the sub-processor list before a DPA is signed.
argument-hint: "[vendor name]"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- Doktůrek sub-processors named in the documents include Hetzner (hosting), Mistral (OCR) and Langfuse (disabled). The DPA review lists them as missing from the template: check that every vendor that touches personal data appears in the DPA annex.
- Only EU/EEA processing is acceptable for clinical data (DPA revision brief).
- The reference is [`dpa-revision-brief.md`](https://github.com/Dokturek-ai/dokturek-docs/blob/main/04-pravo-a-regulatorika/dpa-revision-brief.md) §1 (sub-processors) and §2 (transfers). No CLM, CRM or document-storage connector ships with this plugin: work from the documents and links the user provides and from `dokturek-docs`.

# /vendor-check -- Sub-processor Check

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Check whether a vendor can act as a sub-processor of Clementine Solutions s.r.o. for the practices' data, and what is missing. Doktůrek is the processor; the practices are the controllers.

**Important**: This command assists with legal workflows but does not provide legal advice. Findings should be verified against the original documents; no lawyer is engaged yet, so open points go to Honza and Petr with a list for an external lawyer.

## Invocation

```
/legal:vendor-check [vendor name]
```

Vendor: $ARGUMENTS

If no vendor name is provided, prompt the user to specify which vendor to check.

## Workflow

### Step 1: Identify the Vendor and What It Does

- Full legal name, seat (country) and the trade name, for example a parent and a subsidiary with different seats
- Which service Doktůrek uses (hosting, OCR, monitoring, e-mail, identity, etc.) and in which environment (production, test, demo)
- Whether the vendor touches personal data at all, and whether that includes patient health data. A vendor that only ever sees synthetic data is not a sub-processor today; note when that would change

Ask the user to clarify if the vendor or the service is ambiguous.

### Step 2: Collect the Sources

Work from what is available and list what was not checked:
- The vendor's data processing terms (DPA) and its own sub-processor list, from links or files the user provides
- `dokturek-docs`: `04-pravo-a-regulatorika/dpa-template.md` (sub-processor annex), `dpa-review.md`, `dpa-revision-brief.md`, `STAV.md`
- Infrastructure facts (region, data centre, self-hosted or cloud) from Petr or Kuba; mark anything not documented [N]

### Step 3: Check the Sub-processor Requirements

| # | Requirement | Basis | Status |
|---|---|---|---|
| 1 | **Prior written authorisation**: the practices (controllers) authorised the sub-processor, specifically or generally; with general authorisation, the practice was informed of the change and could object (the brief proposes 30 days' notice) | Art. 28(2) GDPR; brief §1 | [Met / Missing / Unknown] |
| 2 | **Same obligations flow down**: a contract with the vendor imposes the same data protection obligations as the DPA with the practice, including security measures | Art. 28(4) GDPR; brief §1 | |
| 3 | **Doktůrek remains liable** to the practice for the sub-processor's performance | Art. 28(4) GDPR | |
| 4 | **Processing location** in the EU/EEA, including support access, backups and the vendor's own sub-processors | brief §2 | |
| 5 | **Listed in the DPA annex** (sub-processor list as a separate annex, kept current) | brief §1; `dpa-template.md` | |
| 6 | **Transfers outside the EEA**: if any, a separate decision of the controller, EU SCC (the correct module), a transfer impact assessment and supplementary measures | Chapter V GDPR; brief §2 | [Not applicable / Met / Missing] |
| 7 | **Breach notice** from the vendor fast enough for Doktůrek to inform the practice within 24 h | brief §8 | |
| 8 | **Return and deletion** at the end of the contract in line with the brief (30 / 60 / 90 days) | brief §10 | |
| 9 | **No use of the data for AI/ML training** without written consent | brief §4 | |

### Step 4: Generate Report

```
## Sub-processor Check: [Vendor Name]

**Date**: [today's date]
**Vendor**: [full legal name, seat]
**Service**: [what Doktůrek uses it for, environment]
**Personal data**: [none / personal data / patient health data] [Z/P/N]
**Sources checked**: [documents and links]
**Not checked**: [what was not available]

## Requirements

| # | Requirement | Status | Evidence | Gap |
|---|---|---|---|---|
| 1 | Prior written authorisation (Art. 28(2)) | | | |
| 2 | Same obligations flow down (Art. 28(4)) | | | |
| ... | | | | |

## Gaps and Next Steps

- [Gap] -- [owner from the team table] -- [what is needed]

## Points for a Lawyer

- [Questions an external lawyer must answer]
```

## Notes

- Never claim a DPA, SCC or authorisation exists unless a document shows it; mark it [N] otherwise
- The sub-processors named in the documents (Hetzner, Mistral, Langfuse) are missing from the DPA template annex according to the DPA review; report that as a gap until the annex exists
- Cloud versus self-hosted Medplum and the location of other sub-processors are open in the brief; do not resolve them here
- Do not contact the vendor; draft any question for the user to send after confirmation
