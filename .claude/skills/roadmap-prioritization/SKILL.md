---
name: roadmap-prioritization
description: "Scopes the MVP, writes requirements and ranks features by value, effort and risk. Use when deciding what to build next, cutting scope, or writing a feature spec."
---

# Product roadmap & prioritization

Scopes the MVP, writes requirements and ranks features by value, effort and risk.

**Skill ID:** SK-08 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when deciding what to build next, cutting scope, or writing a feature spec.

## Procedure

1. Tie each candidate feature to a persona job (`persona-jtbd-mapping`) and a metric.
2. Score with RICE (reach, impact, confidence, effort) or value vs. effort, and add a risk column (safety, legal, dependency).
3. Protect the MVP: fare alerts, trip-readiness checklist, survival language for 20 destinations, touristy vs. off-the-path guides for 20 cities, emergency card + human chat (premium).
4. Write requirements as user stories with acceptance criteria and the analytics events needed.
5. Sequence into now / next / later with dependencies.

## Output

- Ranked feature table.
- Now / next / later roadmap.
- Spec: user stories, acceptance criteria, events, open questions.

## Project context

- Risk #15 in `docs/08`: the 'full travel system' scope is the main execution risk. Keep the MVP narrow.

## Guardrails

- Any traveler-facing safety feature needs a human escalation path.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
