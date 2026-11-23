---
name: pricing-subscription-design
description: "Designs tiers, trials, annual vs. monthly plans and price tests, and accounts for app-store fees. Use when setting or changing prices, tiers, trials, discounts, or the free vs. paid line."
---

# Pricing & subscription design

Designs tiers, trials, annual vs. monthly plans and price tests, and accounts for app-store fees.

**Skill ID:** SK-29 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when setting or changing prices, tiers, trials, discounts, or the free vs. paid line.

## Procedure

1. Benchmark: Going (~$49 / ~$199 yr, verify), deal clubs $50–$100/yr, Duolingo, concierge services (`docs/03`).
2. Define tiers by persona value: Free (deal alerts, basic checklist), Premium ($5–$10/mo or $49–$99/yr: full alerts, language packs, offline, human chat), Concierge ($149–$499/trip).
3. Model net revenue after app-store (15–30%) or web (Stripe ~2.9% + 30¢) fees.
4. Design trial and renewal flows that comply with auto-renewal laws (`consumer-protection-law`).
5. Plan price tests with clear success metrics.

## Output

- Tier table with features and prices.
- Net revenue per tier.
- Test plan.

## Project context

- Willingness to pay: low for young first-timers, highest for 50+ (`docs/02`). Risk #8 in `docs/08`.

## Guardrails

- Clear terms, easy cancellation, renewal reminders, no hidden fees.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
