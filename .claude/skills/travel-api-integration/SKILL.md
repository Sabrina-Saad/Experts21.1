---
name: travel-api-integration
description: "Integrates Duffel, affiliate, lodging, eSIM, insurance and tour APIs, including caching and error handling. Use when connecting to a travel data or booking provider, or building the fare-tracking engine."
---

# Travel API integration

Integrates Duffel, affiliate, lodging, eSIM, insurance and tour APIs, including caching and error handling.

**Skill ID:** SK-17 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when connecting to a travel data or booking provider, or building the fare-tracking engine.

## Procedure

1. Read the provider's current docs, pricing and terms (rate limits, caching rules, display requirements, attribution).
2. Build behind the internal provider interface (`resilient-system-architecture`).
3. Handle auth via environment secrets, never hard-coded keys.
4. Add caching, retries with backoff, and monitoring (error rate, latency, cost per call).
5. Write contract tests with recorded responses; test the fallback path.

## Output

- Integration plan or code.
- Provider comparison (coverage, cost, terms).
- Monitoring checklist.

## Project context

- Options in `docs/04`: affiliate deep links (launch), Duffel (~$2–3/order, verify) for phase 2, Kiwi/AirLabs/Ignav for data. No public Google Flights API; don't scrape it.

## Guardrails

- Respect providers' terms; no scraping that violates them.
- Never commit API keys.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
