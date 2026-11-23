---
name: resilient-system-architecture
description: "Designs scalable systems with abstraction layers and fallbacks so no single supplier is critical. Use when designing or reviewing the platform architecture, or any feature that depends on an outside provider."
---

# System architecture & multi-provider design

Designs scalable systems with abstraction layers and fallbacks so no single supplier is critical.

**Skill ID:** SK-16 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when designing or reviewing the platform architecture, or any feature that depends on an outside provider.

## Procedure

1. Write the requirements: users, traffic, latency, offline needs, data sensitivity, budget.
2. Put every travel supplier behind an internal interface (flights, lodging, eSIM, insurance, tours) with at least one fallback.
3. Cache fare and content data; set budgets for API and LLM spend.
4. Plan for failure: timeouts, retries, circuit breakers, graceful degradation (show cached deals rather than an error).
5. Document decisions as short ADRs (context, decision, consequences).

## Output

- Architecture diagram (text or Mermaid).
- ADRs.
- Cost and scaling estimate.

## Project context

- Risk #4 (`docs/08`): API dependency, e.g., Amadeus Self-Service shutdown. Monthly cost ranges in `docs/04`.

## Guardrails

- Keep payment data out of our systems where possible (hosted payments, small PCI scope).
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
