---
name: market-sizing
description: "Builds and updates top-down and bottom-up market estimates with stated assumptions. Use when someone asks how big the opportunity is, or a plan, pitch or model needs TAM/SAM/SOM."
---

# Market sizing (TAM/SAM/SOM)

Builds and updates top-down and bottom-up market estimates with stated assumptions.

**Skill ID:** SK-03 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when someone asks how big the opportunity is, or a plan, pitch or model needs TAM/SAM/SOM.

## Procedure

1. Define the customer and the unit (people, trips, or dollars) before estimating anything.
2. Top-down: start from population/passport/outbound-trip data and narrow with stated filters.
3. Bottom-up: reachable users × conversion × revenue per user, using the unit economics in `docs/04-startup-and-operating-costs.md`.
4. Reconcile the two; explain any gap greater than 2×.
5. List every assumption with a low/base/high value and how to validate it (survey, pilot, partner data).

## Output

- TAM / SAM / SOM table with units and logic.
- Assumption table (low/base/high, validation method).
- Sensitivity: which assumption moves the answer most.

## Project context

- Working model in `docs/01-market.md`: TAM ~100M+ people; SAM ~15–25M novice/early overseas travelers; SOM yr-3 150K–400K actives, 15K–40K paying.
- Blended ARPU target $20–$45/user/yr (`docs/04`).

## Guardrails

- Mark assumptions clearly; never present an assumption as a measured fact.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
