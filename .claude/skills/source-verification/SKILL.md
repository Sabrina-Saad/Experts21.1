---
name: source-verification
description: "Finds current information, prefers official sources, cross-checks figures and labels anything unverified. Use when any answer depends on a fact, number, rule, price or date that could be wrong or out of date."
---

# Web research & source verification

Finds current information, prefers official sources, cross-checks figures and labels anything unverified.

**Skill ID:** SK-01 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when any answer depends on a fact, number, rule, price or date that could be wrong or out of date.

## Procedure

1. Check the project research first (`docs/`) and note the research date. Anything older than ~6 months that affects safety, law or money must be re-checked.
2. Search for the current figure. Prefer primary sources in this order: government and regulators (State Dept, NTTO/trade.gov, DOT, FTC, state attorneys general, CDC, EU/UK official sites) → company filings and official pricing pages → reputable industry research (Phocuswright, Skift, PhocusWire) → press → vendor blogs.
3. Cross-check every important number with a second independent source. If sources disagree, report the range and say which you trust and why.
4. Keep different measures apart (e.g., NTTO air-traveler survey totals vs. monthly departure counts; Phocuswright OTA bookings vs. IMARC online-travel market).
5. Label each claim: **verified** (primary source, checked today), **secondary** (reputable but not primary), or **(verify)** (single weak source or estimate).
6. Record the date you checked and link every source.

## Output

- Answer first, then evidence.
- Each key claim tagged verified / secondary / (verify).
- A `Sources:` list of markdown links with the date checked.

## Project context

- The research docs carry *(verify)* flags (e.g., Florida SOT fee, Duffel per-order pricing, Going prices). Keep those flags until a primary source confirms the figure.
- Known moving targets: EU ETIAS launch date (repeatedly postponed), UK ETA fee, DOT refund rule status, FTC rules, API pricing.

## Guardrails

- Never invent a statistic or a source. If you can't find it, say so.
- Don't present a vendor's marketing number as fact.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
