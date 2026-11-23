---
name: executive-synthesis
description: "Combines inputs from several experts into a clear recommendation with trade-offs for the consultant or board. Use when several inputs must be turned into one decision-ready answer."
---

# Synthesis & executive briefing

Combines inputs from several experts into a clear recommendation with trade-offs for the consultant or board.

**Skill ID:** SK-09 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when several inputs must be turned into one decision-ready answer.

## Procedure

1. Restate the question and the decision to be made.
2. Lead with the recommendation in one or two sentences.
3. Give the 3–5 reasons, each tied to evidence and to the expert it came from.
4. Show where experts disagreed and how you resolved it (or that it's still open).
5. List risks, open questions, and the next 3 actions with owners.
6. Keep it short: one screen if possible; details go in an appendix.

## Output

- **Recommendation** → **Why** → **Disagreements** → **Risks** → **Next steps** → **Sources**.

## Project context

- Board-level risks to always check: CAC vs. LTV, AI commoditization, guidance accuracy (`docs/08`).

## Guardrails

- Don't hide disagreement or uncertainty to make the answer look cleaner.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
