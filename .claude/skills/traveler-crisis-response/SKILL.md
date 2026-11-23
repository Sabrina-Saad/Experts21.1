---
name: traveler-crisis-response
description: "Follows the playbooks for lost passports, cancellations, medical issues and unrest, and knows when to hand off to a human. Use when a traveler is in trouble, or the team is designing emergency features, support playbooks or crisis plans."
---

# Traveler emergency & crisis response

Follows the playbooks for lost passports, cancellations, medical issues and unrest, and knows when to hand off to a human.

**Skill ID:** SK-15 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when a traveler is in trouble, or the team is designing emergency features, support playbooks or crisis plans.

## Procedure

1. Triage: is anyone in immediate danger? If yes, the first instruction is the local emergency number and the nearest U.S. embassy/consulate. Escalate to a human immediately.
2. Identify the situation and use its playbook: lost/stolen passport, flight cancelled/missed, medical issue, theft/scam, natural disaster/unrest, arrest/legal trouble.
3. Give short, calm, numbered steps. Include phone numbers and addresses from official sources.
4. Point to the user's travel insurance assistance line and STEP enrollment.
5. Log the incident and follow up after it's resolved.

## Output

- Calm numbered steps for the traveler.
- Escalation note for the human team.
- For design work: the playbook with triggers, steps and owners.

## Project context

- Emergency card is part of the MVP (`docs/README`). Risk #3 in `docs/08`: inaccurate guidance can harm a traveler.

## Guardrails

- AI never handles a life-safety, medical or legal emergency alone; always escalate to a human.
- No medical or legal advice beyond pointing to official help.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
