---
name: app-development-offline
description: "Builds web, iOS and Android apps, offline content and push notifications. Use when building or reviewing app features, offline mode, or notifications."
---

# Web, mobile & offline app development

Builds web, iOS and Android apps, offline content and push notifications.

**Skill ID:** SK-19 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when building or reviewing app features, offline mode, or notifications.

## Procedure

1. Pick the delivery: web/PWA first where possible (avoids 15–30% app-store fees for subscriptions where permitted), native apps for push and offline.
2. Make the in-trip essentials work offline: phrasebook, emergency card, downloaded guides, saved bookings.
3. Implement push and email for fare alerts with user-controlled frequency.
4. Meet accessibility (`accessible-calm-ux`) and performance budgets on low-end phones and slow networks.
5. Instrument analytics events defined in the spec.

## Output

- Implementation plan or code.
- Offline data plan.
- Test checklist (devices, offline, accessibility).

## Project context

- App-store dependency is risk #14 (`docs/08`).

## Guardrails

- Store passport numbers and location only if needed, encrypted (`security-privacy-engineering`).
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
