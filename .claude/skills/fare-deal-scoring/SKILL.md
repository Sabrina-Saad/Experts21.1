---
name: fare-deal-scoring
description: "Judges whether a fare is a real deal for a route and season, and explains it in plain language. Use when designing or reviewing fare alerts, or deciding whether a price is worth telling users about."
---

# Fare analysis & deal scoring

Judges whether a fare is a real deal for a route and season, and explains it in plain language.

**Skill ID:** SK-11 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when designing or reviewing fare alerts, or deciding whether a price is worth telling users about.

## Procedure

1. Establish the baseline: typical price for the route and month (historical median from the data provider).
2. Score the deal: % below baseline, plus adjustments for nonstop vs. connections, total travel time, basic-economy restrictions and bag fees.
3. Check beginner-friendliness: reasonable connection times, no self-transfer, arrival time, airport ease.
4. Explain in one plain sentence why it's good and what the catch is.
5. Set alert thresholds per tier (free vs. premium) and avoid alert fatigue.

## Output

- Deal score with the reasoning.
- Plain-English alert copy, including the catch.
- Threshold recommendation.

## Project context

- Users are mostly first-timers: a cheap fare with a 45-minute international self-transfer is not a good deal for them.

## Guardrails

- Show the total price including mandatory fees (DOT full-fare advertising rules, `docs/05`).
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
