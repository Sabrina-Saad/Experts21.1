---
name: travel-distribution-economics
description: "Knows how OTAs, GDS/NDC, host agencies, metasearch and affiliate networks work, including commission rates and cookie terms. Use when a question involves how travel is sold, who pays whom, commissions, booking APIs or supplier relationships."
---

# Travel distribution & affiliate economics

Knows how OTAs, GDS/NDC, host agencies, metasearch and affiliate networks work, including commission rates and cookie terms.

**Skill ID:** SK-10 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when a question involves how travel is sold, who pays whom, commissions, booking APIs or supplier relationships.

## Procedure

1. Map the money flow: traveler → seller of record → supplier, and where we sit (referrer, agent, or merchant).
2. List the revenue per product: lodging ~4–6%, insurance ~10–30%, eSIM ~10–20%, tours ~8%, flights ~$0–10 via metasearch CPC (`docs/04`, verify current rates).
3. Check program terms: cookie window, attribution, payout timing, brand-bidding and content restrictions.
4. Note dependencies and concentration risk (one OTA or API supplying most revenue).

## Output

- Money-flow diagram or table.
- Revenue per trip estimate.
- Terms and risks to watch.

## Project context

- Amadeus Self-Service APIs shut down July 17, 2026; Duffel's accredited agency network lets us sell flights without our own ARC accreditation (`docs/04`).

## Guardrails

- Commission rates change; mark them (verify) unless confirmed from the program's current terms.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
