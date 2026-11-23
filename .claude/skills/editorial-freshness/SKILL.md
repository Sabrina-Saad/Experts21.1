---
name: editorial-freshness
description: "Maintains style guides, fact-check workflows and 'last verified' refresh schedules. Use when creating, reviewing, or refreshing any guide, checklist, or language pack."
---

# Editorial standards & content freshness

Maintains style guides, fact-check workflows and 'last verified' refresh schedules.

**Skill ID:** SK-24 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when creating, reviewing, or refreshing any guide, checklist, or language pack.

## Procedure

1. Apply the style guide: plain English, warm, specific, no jargon, prices with date and currency.
2. Fact-check every rule, price, phone number and address against a source (`source-verification`).
3. Stamp a 'last verified' date; set the refresh interval (entry rules: monthly; city guides: quarterly; evergreen: yearly).
4. Disclose affiliate links and any paid relationship.
5. Track overdue content; overdue safety content is a release blocker.

## Output

- Review checklist with pass/fail.
- Freshness report (items past their refresh date).

## Project context

- Early-warning metric in `docs/08`: % of guides past refresh date.

## Guardrails

- No paid placement without a clear disclosure (FTC Endorsement Guides).
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
