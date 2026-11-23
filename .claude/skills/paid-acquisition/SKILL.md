---
name: paid-acquisition
description: "Runs Meta, TikTok, Google and Apple Search Ads tests, tracks attribution and enforces the LTV:CAC 3:1 rule. Use when planning, running or judging paid marketing."
---

# Paid acquisition & attribution

Runs Meta, TikTok, Google and Apple Search Ads tests, tracks attribution and enforces the LTV:CAC 3:1 rule.

**Skill ID:** SK-41 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when planning, running or judging paid marketing.

## Procedure

1. Set the target: max CAC per activated user from the financial model (LTV:CAC ≥ 3:1).
2. Start with small tests per channel and audience; one variable at a time.
3. Set up attribution (UTMs, app attribution, post-purchase survey) and define CAC on activated users, not installs.
4. Kill or scale weekly based on CAC and early retention.
5. Report blended vs. paid CAC.

## Output

- Test plan with budgets.
- Weekly results with kill/scale decisions.

## Project context

- Benchmarks in `docs/04`/`docs/07`: travel CAC up ~35% 2022→2025; mobile CPI ~$4.70 iOS / ~$3.70 Android. Paid should be ≤ 30–40% of acquisition.

## Guardrails

- Ad claims must pass `consumer-protection-law`.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
