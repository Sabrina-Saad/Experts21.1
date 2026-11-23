---
name: expert-orchestration
description: "Routes a question to the right expert agents, runs them in parallel, has them challenge each other, and returns one combined answer. Use when the consultant asks any question that needs more than one expert, or asks 'ask the experts'."
argument-hint: "[question for the expert team]"
---

# Expert orchestration

Routes a question to the right expert agents, runs them in parallel, has them challenge each other, and returns one combined answer.

**Skill ID:** SK-45 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when the consultant asks any question that needs more than one expert, or asks 'ask the experts'.

## Procedure

1. Restate the question and the decision it supports. If it is ambiguous, state your interpretation and proceed.
2. Pick 2–6 experts from the roster in `docs/expert-roster.md` (agent file names are in the 'Agent' column). Always include: a finance expert if money is involved, a legal expert if rules or claims are involved, `entry-safety-expert` if traveler safety is involved, `insurance-risk-manager` for big decisions.
3. Write each expert a self-contained brief: the question, the context from `docs/`, the specific angle you want from them, the output format, and 'flag disagreements with other functions'.
4. Run the experts in parallel with the Agent tool (`subagent_type` = the agent's name). If the Agent tool is not available to you, return the routing plan and briefs so the main conversation can run them.
5. Cross-examine: send the key conflicts back to the relevant experts (e.g., growth plan vs. CFO's CAC ceiling vs. consumer-protection counsel) for one round of response.
6. Synthesize with `executive-synthesis`: one recommendation, reasons with the expert behind each, disagreements and how resolved, risks, next steps, sources.
7. If the answer produces a lasting deliverable, save it to `docs/deliverables/<date>-<topic>.md`.

## Output

- **Answer** (recommendation first).
- **Experts consulted** and what each contributed.
- **Where they disagreed**.
- **Risks & open questions**.
- **Next steps**.
- **Sources**.

## Project context

- When invoked directly as `/expert-orchestration <question>`, the question is: $ARGUMENTS
- Team roster and skill map: `docs/expert-roster.md`. Team guide: `CLAUDE.md`.

## Guardrails

- Don't consult experts that add nothing; more is not better.
- Never drop a safety or legal warning from an expert in the final answer.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
