---
name: tech-debt
description: Triage a known technical-debt item or deferred piece of work and propose a row for the Doktůrek registers (technicky-dluh.md in dokturek-docs, or the dokturek-platform pre-production checklist). Use when someone reports a shortcut, workaround or postponed task that should be recorded, or asks to re-prioritise rows already in those registers. Not for code review or refactoring, which belong to the development plugins.
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- Doktůrek keeps technical debt in `dokturek-docs:02-architektura/medplum-rozhodnuti/technicky-dluh.md` and deferred work in `dokturek-platform:docs/pre-production-checklist.md`. Propose rows there instead of a new register.
- Output is a proposed row (or edit to an existing row) in the register's own columns, with the source and [Z]/[P]/[N] marks. Adding it is a `dokturek-docs` or `dokturek-platform` pull request that you open only after an explicit yes. Petr owns technical priorities.
- Do not audit code, review pull requests or plan refactors here; route that to the development plugins (`medplum`, `medplum-engineering` in the `dokturek-team` marketplace).

# Tech Debt Management

Systematically identify, categorize, and prioritize technical debt.

## Categories

| Type | Examples | Risk |
|------|----------|------|
| **Code debt** | Duplicated logic, poor abstractions, magic numbers | Bugs, slow development |
| **Architecture debt** | Monolith that should be split, wrong data store | Scaling limits |
| **Test debt** | Low coverage, flaky tests, missing integration tests | Regressions ship |
| **Dependency debt** | Outdated libraries, unmaintained dependencies | Security vulns |
| **Documentation debt** | Missing runbooks, outdated READMEs, tribal knowledge | Onboarding pain |
| **Infrastructure debt** | Manual deploys, no monitoring, no IaC | Incidents, slow recovery |

## Prioritization Framework

Score each item on:
- **Impact**: How much does it slow the team down? (1-5)
- **Risk**: What happens if we don't fix it? (1-5)
- **Effort**: How hard is the fix? (1-5, inverted — lower effort = higher priority)

Priority = (Impact + Risk) x (6 - Effort)

## Output

Produce a prioritized list with estimated effort, business justification for each item, and a phased remediation plan that can be done alongside feature work.
