# Research Docs — "First Trip Abroad" Travel Platform

**Product vision:** One place where Americans go for *everything* about traveling internationally — fare tracking & deals, step-by-step guidance, survival language, touristy *and* off-the-beaten-path places — built especially for people who are new to it, nervous, or don't know where to start.

**Purpose of this folder:** Shared context for the team of expert agents (and humans) who will build the business. Each file covers one topic; agents should read this index first, then the files relevant to their role.

**Research date:** November 2026. Figures marked *(verify)* come from secondary sources and should be re-checked before external use. This is research, not legal or financial advice.

## Index

| # | File | What's inside | Primary agent |
|---|---|---|---|
| 01 | [Market](01-market.md) | Outbound travel volumes, passport data, OTA market size, TAM/SAM/SOM, demand drivers & headwinds | Market analyst |
| 02 | [Target Customers](02-target-customers.md) | Evidence of travel anxiety, 6 personas, jobs-to-be-done → features | Customer insight / product |
| 03 | [Competitors](03-competitors.md) | OTAs, metasearch, deal subscriptions, AI planners, language apps, guides; competitive matrix; moats | Competitive intel |
| 04 | [Startup & Operating Costs](04-startup-and-operating-costs.md) | One-time & monthly costs, travel API options, revenue model, unit economics, break-even | Finance |
| 05 | [Permits & Licenses](05-permits-and-licenses.md) | Business model vs. regulatory weight, seller-of-travel laws, ARC/IATAN, DOT, FTC, privacy, insurance | Compliance |
| 06 | [Staffing](06-staffing.md) | Team by phase, salaries, contributor network, expert-agent ↔ human-owner map | Org / hiring |
| 07 | [Marketing](07-marketing.md) | Positioning, channels, partnerships, funnel, KPIs, seasonal calendar | Marketing & content |
| 08 | [Risks](08-risks.md) | 16 ranked risks with mitigations, top-3 board risks, early-warning metrics | Risk |
| — | [Expert Roster](expert-roster.md) | 41 expert agents (39 advisors + orchestrator + team-builder) with job descriptions, 47 shared skills, and which agents use each skill. Built as `.claude/agents/` and `.claude/skills/` — see [`CLAUDE.md`](../CLAUDE.md) | All agents |
| — | [Deliverables](deliverables/README.md) | Where agents save lasting outputs and the decision log | All agents |

## Executive summary

1. **Demand is real and growing.** U.S. residents made a record **107.7M** outbound air trips in 2024; monthly departures in 2025 exceeded 2019 levels. Yet only **~48%** of Americans hold a passport, and **27.3M** passports were issued in FY2025 — a large, measurable pool of new travelers.
2. **The unmet need is confidence, not booking.** Booking is dominated by Expedia and Booking Holdings ($108.5B U.S. OTA gross bookings, 2024). Surveys show heavy anxiety among new travelers (e.g., 69% of Gen Z changed/canceled plans due to anxiety and unpreparedness; ~1/3 of Americans anxious about language barriers).
3. **Positioning:** "Your first trip abroad, without the fear" — fare alerts + trip-readiness checklist + survival language + touristy/local picks + human help, in one place.
4. **Launch model:** content + subscription + affiliate booking. Avoids ARC bonds, refund liability and most seller-of-travel exposure. Add direct booking via **Duffel** (no own ARC accreditation needed) in phase 2. Note: **Amadeus Self-Service APIs shut down July 2026** — don't plan around them.
5. **Economics:** Lean launch ~**$30K**; seed-funded build ~**$280K–$450K** upfront and **$120K–$300K/month** burn. Blended ARPU target **$20–$45/user/yr** → acquisition must be mostly organic (creators, SEO, community, partnerships).
6. **Biggest risks:** CAC vs. LTV, commoditization by Google/AI planners, and accuracy of safety/entry guidance.

## Recommended MVP scope
- Fare deal alerts from the user's home airport.
- Personalized "Trip Readiness" checklist (passport → ETA/ETIAS → insurance → phone → money → packing → arrival).
- Survival-language packs for the first 20 destinations.
- "Touristy vs. Off-the-path" guides for 20 first-timer-friendly cities.
- Emergency card + human chat (premium).

## Conventions for agents
- Cite sources; prefer official sources (State Dept, NTTO/trade.gov, DOT, FTC, state AGs) for facts that affect traveler safety or compliance.
- Mark estimates and assumptions explicitly.
- When updating a file, update the research date and the executive summary here if conclusions change.
