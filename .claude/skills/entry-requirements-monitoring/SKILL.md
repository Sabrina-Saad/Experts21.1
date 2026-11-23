---
name: entry-requirements-monitoring
description: "Tracks passport, visa, UK ETA, EU EES/ETIAS, State Dept advisories, STEP and CDC guidance, and flags changes. Use when any question about documents, entry rules, advisories, vaccinations, or what an American needs to enter a country."
---

# Entry requirements & travel-advisory monitoring

Tracks passport, visa, UK ETA, EU EES/ETIAS, State Dept advisories, STEP and CDC guidance, and flags changes.

**Skill ID:** SK-12 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when any question about documents, entry rules, advisories, vaccinations, or what an American needs to enter a country.

## Procedure

1. Start from official sources: travel.state.gov country pages, the destination's official immigration site, gov.uk for the UK ETA, the official EU ETIAS/EES site, CDC Travelers' Health.
2. Check: passport validity rules (e.g., 6-month rule), blank pages, visa or e-authorization, fees, processing times, onward ticket, minors' consent letters.
3. Check the current State Dept advisory level and any specific regional warnings.
4. Record the date verified and link the source on every statement.
5. If something changed, list affected destinations and users, and alert content-ops-editor and lifecycle-crm-marketer.

## Output

- Checklist per destination with source links and 'last verified' date.
- Change alerts: what changed, from when, who is affected.

## Project context

- As of Nov 2026: UK ETA £16; EU EES operational since April 2026; ETIAS €20, launch date not confirmed (`docs/01`, `docs/08`). Re-verify before use.

## Guardrails

- Never guess an entry rule. If unsure, say so and point to the official source.
- Medical questions → link CDC and advise seeing a doctor; don't give medical advice.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
