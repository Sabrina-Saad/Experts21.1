---
name: security-privacy-engineering
description: "Protects sensitive traveler data, handles access control and incident response, and minimizes PCI scope. Use when handling passport numbers, location, payments, accounts, or any personal data."
---

# Security, privacy engineering & PCI

Protects sensitive traveler data, handles access control and incident response, and minimizes PCI scope.

**Skill ID:** SK-22 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when handling passport numbers, location, payments, accounts, or any personal data.

## Procedure

1. Classify the data: sensitive (passport, precise location, health, payment) vs. personal vs. public.
2. Minimize: don't collect what you don't need; set retention limits.
3. Protect: encryption in transit and at rest, least-privilege access, secrets management, audit logs.
4. Use hosted payment fields (Stripe/Duffel) to keep PCI scope small.
5. Threat-model new features; keep an incident response plan with notification steps.

## Output

- Data inventory and classification.
- Security requirements for the feature.
- Threat model / incident plan.

## Project context

- Privacy laws in `docs/05` (CCPA/CPRA and other state laws; passport numbers and location are sensitive).

## Guardrails

- Never put secrets in code, docs or chat.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
