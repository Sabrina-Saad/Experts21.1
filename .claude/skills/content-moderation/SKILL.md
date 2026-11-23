---
name: content-moderation
description: "Reviews user content, verifies contributors and enforces community rules. Use when handling community posts, reviews, user tips or contributor submissions."
---

# Content moderation & fake-review detection

Reviews user content, verifies contributors and enforces community rules.

**Skill ID:** SK-25 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when handling community posts, reviews, user tips or contributor submissions.

## Procedure

1. Apply community rules: no harassment, no unsafe advice, no private addresses, no undisclosed promotion.
2. Detect fake or incentivized reviews (bursts, copied text, new accounts, undisclosed incentives).
3. Check safety of 'hidden gem' submissions before publishing.
4. Act proportionately: edit, hide, warn, remove, ban; log decisions.
5. Report trends to trust & safety and legal.

## Output

- Moderation decision with reason.
- Trend report.

## Project context

- FTC Fake Reviews Rule (2024) applies (`docs/05`). Risk #10 in `docs/08`.

## Guardrails

- Never publish content that could put a traveler or a local resident at risk.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
