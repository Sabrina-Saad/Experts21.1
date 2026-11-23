---
name: financial-modeling
description: "Builds P&L, burn, runway, CAC/LTV, ARPU and break-even models with scenarios. Use when any question about money: costs, revenue, runway, break-even, unit economics or financial impact of a decision."
---

# Financial modeling & unit economics

Builds P&L, burn, runway, CAC/LTV, ARPU and break-even models with scenarios.

**Skill ID:** SK-28 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when any question about money: costs, revenue, runway, break-even, unit economics or financial impact of a decision.

## Procedure

1. Start from the cost and revenue tables in `docs/04-startup-and-operating-costs.md`.
2. Build monthly: users (by channel), conversion, ARPU by stream (subscription, affiliate, concierge, B2B), costs by category, cash.
3. Compute CAC, LTV, LTV:CAC, payback months, gross margin, burn, runway, break-even users.
4. Run low/base/high scenarios and a sensitivity on the top 3 drivers.
5. Show formulas and assumptions; never bury them.

## Output

- Summary table (base case).
- Scenarios.
- Assumptions list.
- Optionally a spreadsheet file in `docs/deliverables/`.

## Project context

- Reference points: seed burn ~$120K–$300K/month; break-even ~90K actives at $30 ARPU and ~80% margin; LTV:CAC ≥ 3:1 target (`docs/04`).

## Guardrails

- Label estimates; this is planning analysis, not accounting or investment advice.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
