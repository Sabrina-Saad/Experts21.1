---
name: llm-guardrails-engineering
description: "Builds AI assistants with citations to official sources, safety guardrails, human escalation and cost control. Use when building, reviewing or governing any AI feature, including the traveler-facing assistant and these expert agents."
---

# LLM application engineering & guardrails

Builds AI assistants with citations to official sources, safety guardrails, human escalation and cost control.

**Skill ID:** SK-18 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when building, reviewing or governing any AI feature, including the traveler-facing assistant and these expert agents.

## Procedure

1. Define what the assistant may and may not do; write it into the system prompt and tests.
2. Ground answers in verified content and official sources (retrieval), and show citations.
3. Add escalation triggers: emergencies, safety, medical, legal, visa edge cases, distress → hand to a human.
4. Evaluate with a test set of real traveler questions, including tricky and adversarial ones; track accuracy and refusal quality.
5. Control cost: caching, smaller models for simple tasks, token budgets.

## Output

- Assistant spec (scope, escalation rules, sources).
- Evaluation set and results.
- Cost estimate.

## Project context

- Moat is trust + human backup + verified content, not 'AI itinerary' (`docs/03`, risk #2 in `docs/08`). LLM API cost ranges in `docs/04`.

## Guardrails

- The assistant must never invent entry rules, prices or safety claims.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
