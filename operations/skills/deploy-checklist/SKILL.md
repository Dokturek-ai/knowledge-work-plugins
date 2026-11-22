---
name: deploy-checklist
description: Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migrations or feature flags, verifying CI status and approvals before going to production, or documenting rollback triggers ahead of time.
argument-hint: "[service or release name]"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- Coolify deploys `main`. Each service repo has its own runbook in `deploy/coolify/README.md`; Keycloak releases follow `dokturek-keycloak:docs/release-gate.md`.
- Before anything touches real patient data, check `dokturek-platform:docs/pre-production-checklist.md` and "Podmínky zahájení provozu" in `dokturek-docs` → `01-produkt/prvni-den-2027.md`. In short: `app.prod` wired to test backends (R-nový-M) is not a separate clinical production; real data need documented legal conditions, clinical approval and technical acceptance through gates G01–G10 in `47-audit-healthcare-2026-11-16/03-plan-overeni.md` (section 2), and project configuration, green unit tests or a published certificate do not by themselves allow operation. Add an unchecked line for each gate the release touches and name its owner from that table; never tick a gate yourself.
- The checklist is for the person who deploys; you do not deploy. Notifications and ticket changes in the checklist are drafts: show the exact target and text, and act only after an explicit yes.
- Doktůrek has no on-call rotation or canary releases, and no monitoring tool is documented (see CONNECTORS.md). Name the real owner instead (Kuba for Coolify and deploys, Martin Marhold for Keycloak and gov-gateway).

# /deploy-checklist

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Generate a pre-deployment checklist to verify readiness before shipping.

## Usage

```
/operations:deploy-checklist $ARGUMENTS
```

## Output

```markdown
## Deploy Checklist: [Service/Release]
**Date:** [Date] | **Deployer:** [Name]

### Pre-Deploy
- [ ] All tests passing in CI
- [ ] Code reviewed and approved
- [ ] No known critical bugs in release
- [ ] Database migrations tested (if applicable)
- [ ] Feature flags configured (if applicable)
- [ ] Rollback plan documented
- [ ] Owner of the affected service knows the deploy time (Kuba / Martin Marhold)
- [ ] Real-data gates touched by this release listed with owners (G01–G10, `prvni-den-2027.md`)

### Deploy
- [ ] Deploy to staging and verify
- [ ] Run smoke tests
- [ ] Deploy to production through Coolify (`main`)
- [ ] Watch logs and health checks for 15 min (manually; no monitoring tool is connected)
- [ ] Verify key user flows

### Post-Deploy
- [ ] Confirm metrics are nominal
- [ ] Update release notes / changelog
- [ ] Draft the stakeholder note (sent only after explicit confirmation)
- [ ] Propose which related issues to close (closed only after explicit confirmation)

### Rollback Triggers
- Error rate exceeds [X]%
- P50 latency exceeds [X]ms
- [Critical user flow] fails
```

## Customization

Tell me about your deploy and I'll customize the checklist:
- "We use feature flags" → adds flag verification steps
- "This includes a database migration" → adds migration-specific checks
- "This is a breaking API change" → adds consumer notification steps

## If Connectors Available

If **~~source control** is connected:
- Pull the release diff and list of changes
- Verify all PRs are approved and merged

If **~~CI** is connected:
- Check build and test status automatically
- Verify pipeline is green before deploy

If **~~monitoring** is connected:
- Pre-fill rollback trigger thresholds from current baselines
- Propose a post-deploy check (which metrics, how long). Do not create alerts, dashboards or watches yourself; show the exact configuration and let the owner set it up after an explicit yes

## Tips

1. **Run before every deploy** — Even routine ones. Checklists prevent "I forgot to..."
2. **Customize per service** — Start from the service's `deploy/coolify/README.md` runbook; describe the stack again in each session, nothing is remembered between sessions.
3. **Include rollback criteria** — Decide when to roll back before you deploy, not during.
