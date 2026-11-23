---
name: product-analytics-experiments
description: "Sets up event tracking, dashboards, A/B tests and funnel and cohort analysis. Use when measuring a feature or campaign, designing an experiment, or answering 'is it working?'."
---

# Product analytics & experimentation

Sets up event tracking, dashboards, A/B tests and funnel and cohort analysis.

**Skill ID:** SK-21 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when measuring a feature or campaign, designing an experiment, or answering 'is it working?'.

## Procedure

1. Define the metric and its exact formula (e.g., CAC = spend ÷ new activated users in the period).
2. Specify the events and properties needed; check privacy rules before collecting.
3. For experiments: hypothesis, primary metric, guardrail metrics, sample size, duration; don't stop early.
4. Analyze by cohort and persona; report effect size with confidence intervals.
5. Recommend a decision: ship, iterate, or stop.

## Output

- Metric definitions.
- Event spec.
- Experiment plan or results with a decision.

## Project context

- Year-1 KPI targets in `docs/07`: CAC < $10–$15 per active, activation > 40%, free→paid 5–10%, 12-month paid retention > 50%, NPS > 50.
- Early-warning metrics in `docs/08`.

## Guardrails

- Collect only what's needed; honor opt-outs.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
