---
name: competitor-tracking
description: "Maintains the competitor list and matrix, tracks pricing and launches, and assesses threats. Use when a question involves a competitor, a substitute product, a pricing benchmark, or 'what if X launches Y'."
---

# Competitor tracking & feature comparison

Maintains the competitor list and matrix, tracks pricing and launches, and assesses threats.

**Skill ID:** SK-04 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when a question involves a competitor, a substitute product, a pricing benchmark, or 'what if X launches Y'.

## Procedure

1. Place the player in a category from `docs/03-competitors.md` (OTA, metasearch, deal subscription, AI planner, content/guide, language app, human advisor, tour operator).
2. Check their current product, pricing and recent announcements (official site, press releases, earnings, app-store listing).
3. Update the capability matrix: fare alerts, first-trip checklist, trip-specific language, touristy vs. off-the-path, fear/safety support, human help, booking.
4. Assess threat: likelihood they move into our space × impact on us. Name the trigger to watch.
5. Recommend a response: ignore, monitor, differentiate, or partner.

## Output

- Competitor snapshot (what, price, strengths, weaknesses vs. us).
- Updated matrix row(s).
- Threat level + recommended response.

## Project context

- Biggest substitutes: Google Flights (free fare tracking) and general AI planners. Closest model: Going (deal alerts). Closest spirit for 50+: Rick Steves.
- Defensibility levers in `docs/03`: brand of reassurance, verified content, community, lifecycle ownership, data.

## Guardrails

- Don't copy competitor content or branding. Use only public information.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
