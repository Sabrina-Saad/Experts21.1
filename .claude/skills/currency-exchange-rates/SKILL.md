---
name: currency-exchange-rates
description: "Gets current and historical exchange rates from the Frankfurter API (ECB reference rates, no key) and turns them into dollar costs, budgets and trends. Use when a question involves foreign prices, converting costs to or from U.S. dollars, trip budgets, or how a stronger or weaker dollar affects demand."
---

# Currency exchange rates (Frankfurter API)

Gets current and historical exchange rates from the Frankfurter API (ECB reference rates, no key) and turns them into dollar costs, budgets and trends.

**Skill ID:** SK-47 · See `docs/expert-roster.md` for the agents that use this skill.

## When to use

Use this skill when a question involves foreign prices, converting costs to or from U.S. dollars, trip budgets, or how a stronger or weaker dollar affects demand.

## Procedure

1. Use the project script if you have Bash: `python3 scripts/fx.py latest USD EUR,GBP,JPY`, `python3 scripts/fx.py convert 1500 USD EUR`, `python3 scripts/fx.py history USD JPY 2026-01-01 2026-11-20`, `python3 scripts/fx.py currencies`. Add `--json` for raw data.
2. Without Bash, fetch the API directly: `https://api.frankfurter.dev/v1/latest?base=USD&symbols=EUR,GBP` (latest), `https://api.frankfurter.dev/v1/2026-11-20?base=USD&symbols=EUR` (one date), `https://api.frankfurter.dev/v1/2026-01-01..2026-11-20?base=USD&symbols=EUR` (range), `https://api.frankfurter.dev/v1/currencies` (supported list).
3. Check coverage first: only about 30 currencies (AUD BRL CAD CHF CNY CZK DKK EUR GBP HKD HUF IDR ILS INR ISK JPY KRW MXN MYR NOK NZD PHP PLN RON SEK SGD THB TRY USD ZAR). Others (e.g., VND, COP, CRC, PEN, EGP, MAD) return 'not found': say so and use another clearly cited source.
4. State the rate date. Rates are ECB reference rates published once per working day; there are no weekend or holiday rates.
5. For traveler-facing budgets, add a margin: card and ATM rates are usually 1–3% worse than reference rates, and airport exchange counters are much worse.
6. For trends (dollar strength, which destinations got cheaper), compare the latest rate with 1 and 12 months earlier and show the % change.

## Output

- Amounts in both currencies, with the rate and its date.
- For trends: a small table of rate changes by destination currency.
- A note on coverage gaps and the card/ATM margin where relevant.

## Project context

- Strong-dollar periods make Europe, Japan and Latin America more affordable; currency swings are risk #13 in `docs/08-risks.md` and a demand driver in `docs/01-market.md`.
- Budget-first destination finder and 'What $1,500 gets you in…' content depend on current rates (`docs/02`, `docs/07`).
- API: https://api.frankfurter.dev (free, open source, no API key). Network access to it is allowed in the Experts21.1 cloud environment.

## Guardrails

- Reference rates are not the rate a traveler will get; never present them as a guaranteed price.
- Don't cache rates in content without the date.
- Follow the team ground rules in `CLAUDE.md` (cite sources, label estimates, escalate safety issues to a human).
