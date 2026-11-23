---
name: risk-assessment-insurance
description: "Maintains the risk register (likelihood × impact), early-warning metrics and insurance coverage. Use when evaluating a decision's downside, updating the risk register, or checking insurance needs."
---

# Risk assessment & insurance

Maintains the risk register (likelihood × impact), early-warning metrics and insurance coverage.

**Skill ID:** SK-36 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when evaluating a decision's downside, updating the risk register, or checking insurance needs.

## Procedure

1. Start from the 16 ranked risks in `docs/08-risks.md`.
2. For a new decision or event: which risks does it raise or lower? Add new risks if needed.
3. Score likelihood × impact; name an owner, a mitigation and an early-warning metric.
4. Check insurance: general liability, E&O/professional, cyber; more if offering guides or meetups.
5. Report changes to the top 3 board-level risks.

## Output

- Updated risk register rows.
- Top-3 risk summary.
- Insurance gaps.

## Project context

- Top 3 board risks: CAC vs. LTV, AI commoditization, guidance accuracy (`docs/08`).

## Guardrails

- Be explicit about uncertainty; don't downplay safety risks.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
