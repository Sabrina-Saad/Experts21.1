---
name: support-operations
description: "Designs support tiers, staffing, help-desk tooling, response-time targets and quality checks. Use when setting up or improving traveler support, the 'Trip Guide' team, or 24/7 coverage."
---

# Customer support operations

Designs support tiers, staffing, help-desk tooling, response-time targets and quality checks.

**Skill ID:** SK-23 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when setting up or improving traveler support, the 'Trip Guide' team, or 24/7 coverage.

## Procedure

1. Define tiers: self-serve help → AI assistant → human Trip Guide → emergency escalation.
2. Set response-time targets by tier and urgency (emergency in minutes, general within a business day).
3. Size staffing from ticket volume and time zones (travelers are abroad); consider an outsourced overnight partner.
4. Write macros and playbooks; tag tickets (including 'emergency' and 'wrong info').
5. Review quality weekly; feed content errors to content-ops-editor.

## Output

- Support model and staffing plan.
- SLA table.
- Playbook list and QA process.

## Project context

- Support costs and staffing in `docs/06` ($45K–$65K per agent, or BPO $15–$30/hr).

## Guardrails

- Emergencies always reach a human.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
