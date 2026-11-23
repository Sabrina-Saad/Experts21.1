---
name: consumer-protection-law
description: "Applies FTC Act Section 5, endorsement guides, the fake-reviews rule, junk-fee total pricing, ROSCA and state auto-renewal laws, CAN-SPAM and TCPA. Use when reviewing ads, creator posts, claims, prices, subscriptions, emails or texts."
---

# Consumer protection & advertising law

Applies FTC Act Section 5, endorsement guides, the fake-reviews rule, junk-fee total pricing, ROSCA and state auto-renewal laws, CAN-SPAM and TCPA.

**Skill ID:** SK-33 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when reviewing ads, creator posts, claims, prices, subscriptions, emails or texts.

## Procedure

1. Claims: is every claim ('cheapest', 'safe', '% off') true and substantiated?
2. Endorsements: creator and affiliate relationships clearly disclosed; no fake or incentivized reviews.
3. Pricing: total price shown up front for lodging (FTC junk-fees rule, effective May 12, 2025); airfare total price (DOT).
4. Subscriptions: clear terms, affirmative consent, easy online cancellation, renewal reminders (ROSCA + state laws such as California's ARL; the FTC click-to-cancel rule was vacated in 2025 but state laws remain).
5. Email/SMS: CAN-SPAM opt-out; TCPA prior express written consent for marketing texts.

## Output

- Pass / fix list with the rule behind each item.
- Corrected copy or flow.

## Project context

- Rules summarized in `docs/05`. Verify current status of each rule before relying on it.

## Guardrails

- Not legal advice; escalate uncertain items to a human lawyer.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
