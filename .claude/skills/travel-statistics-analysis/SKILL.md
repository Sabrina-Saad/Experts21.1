---
name: travel-statistics-analysis
description: "Reads and interprets NTTO, State Dept passport, OTA and survey data, and keeps series that measure different things apart. Use when working with outbound travel volumes, passport counts, OTA bookings, or traveler survey results."
---

# Travel statistics analysis

Reads and interprets NTTO, State Dept passport, OTA and survey data, and keeps series that measure different things apart.

**Skill ID:** SK-02 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when working with outbound travel volumes, passport counts, OTA bookings, or traveler survey results.

## Procedure

1. Identify exactly what each series measures (people vs. trips vs. departures; air only vs. all modes; citizens vs. residents; books vs. passport cards).
2. Pull the latest period and the same period one year earlier and in 2019 (pre-pandemic baseline).
3. Compute growth rates and shares; show the formula for anything derived.
4. For surveys, note sample size, population, date and who paid for it. Treat sponsor surveys (e.g., language-app or insurer surveys) as directional.
5. State what the data means for the product in one or two sentences.

## Output

- A small table: metric, value, period, source, what it measures.
- A 'so what' paragraph.
- Caveats.

## Project context

- Baselines in `docs/01-market.md`: 107.7M U.S. resident outbound air trips (2024, NTTO), ~48% passport holders (CRS, 2024), 27.3M passports issued FY2025, $108.5B U.S. OTA gross bookings (2024).
- Survey evidence on travel anxiety is in `docs/02-target-customers.md`.

## Guardrails

- Don't add numbers from different definitions together.
- Passport *count* is not passport *holders* (one person can hold a book and a card).
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
