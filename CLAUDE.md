# Experts21.1 — Expert Advisory Team for a "First Trip Abroad" Travel Platform

This project is an advisory team of Claude Code subagents. The team helps a consultant plan and build a travel platform for Americans who want to travel internationally but feel unprepared or nervous. The platform covers fare tracking and deals, step-by-step trip guidance, survival language, and touristy and off-the-beaten-path places.

The team has **41 agents** and **46 skills**, all stored inside this project.

## What's where

| Path | What it is |
|---|---|
| `docs/README.md` | Index and summary of the research (market, customers, competitors, costs, licenses, staffing, marketing, risks) |
| `docs/01-…08-*.md` | One research file per topic. The agents' shared knowledge base |
| `docs/expert-roster.md` | **The team directory:** every agent, its job, its docs and skills, and which agents use each skill |
| `docs/deliverables/` | Where agents save lasting outputs (analyses, plans, the decision log) |
| `.claude/agents/<name>.md` | One subagent per expert (YAML frontmatter plus a system prompt) |
| `.claude/skills/<name>/SKILL.md` | One shared skill per capability. An agent preloads every skill listed in its `skills:` field |
| `scripts/validate_team.py` | Checks that agents, skills, the roster and this file all agree |

## The team

| Domain | Agents |
|---|---|
| **Coordination** | `orchestrator` (routes any question to the right experts and combines their answers), `team-builder` (meta agent: creates and improves agents and skills) |
| **Business & Strategy** | `engagement-lead`, `business-strategist`, `market-research-analyst`, `customer-insights-researcher`, `competitive-intelligence-analyst`, `travel-distribution-expert`, `partnerships-lead`, `product-manager` |
| **Travel Domain** | `destination-expert`, `entry-safety-expert`, `language-learning-specialist`, `fare-deals-expert` |
| **Technical** | `solutions-architect`, `travel-api-engineer`, `ai-ml-engineer`, `fullstack-mobile-engineer`, `ux-ui-designer`, `data-analytics-engineer`, `security-privacy-engineer` |
| **Operations** | `operations-manager`, `traveler-support-lead`, `content-ops-editor`, `trust-safety-moderator`, `people-talent-partner` |
| **Finance** | `cfo`, `pricing-strategist`, `fundraising-advisor`, `accounting-tax-advisor` |
| **Legal & Risk** | `travel-regulatory-counsel`, `consumer-protection-counsel`, `privacy-counsel`, `corporate-ip-counsel`, `insurance-risk-manager` |
| **Marketing** | `brand-strategist`, `growth-marketer`, `seo-content-lead`, `social-creator-manager`, `lifecycle-crm-marketer`, `pr-communications-lead` |

Each agent's one-line job description and its skills are in `docs/expert-roster.md`.

## How to use the team

### Ask the whole team a question (recommended)

Use either of these:

- **Run the orchestrator as your main session.** This is the most reliable way, because the orchestrator can launch the experts itself:
  ```bash
  claude --agent orchestrator
  ```
  Then ask any question, for example: "Should we launch with a subscription or free plus affiliates?"
- **In a normal session, use the orchestration skill:**
  ```
  /expert-orchestration Should we sell flights directly in year one?
  ```
  Claude then follows the orchestration procedure in your conversation: it picks the experts, runs them in parallel, has them respond to each other's conflicts, and returns one combined answer.

You can also say "use the orchestrator subagent to …". When the orchestrator runs as a subagent, it may not be able to launch other subagents. In that case it returns a routing plan with a brief for each expert, and the main conversation runs those experts.

### Ask one expert

- Name the expert: "Use the cfo subagent to estimate runway at $150K/month burn."
- Or @-mention it: `@agent-entry-safety-expert what does a first-timer need for Portugal?`
- Claude also delegates automatically, based on each agent's `description`. Several agents are marked "use proactively": `orchestrator`, `entry-safety-expert`, `cfo`, `travel-regulatory-counsel`, `consumer-protection-counsel`, `insurance-risk-manager` and `traveler-support-lead`.

### Use a skill directly

Every skill is also a slash command, for example `/market-sizing`, `/consumer-protection-law` or `/fare-deal-scoring`.

### Grow or fix the team

Ask the meta agent:

- "Use team-builder to add a visa-services expert."
- "Use team-builder to improve the pricing-strategist; its last answer ignored app-store fees."

The team-builder edits `.claude/agents/`, `.claude/skills/` and `docs/expert-roster.md`, updates the counts in this file, and runs the validator.

## Ground rules for every agent

1. **Cite sources.** Prefer official sources (State Dept, NTTO/trade.gov, DOT, FTC, state attorneys general, CDC) for anything about traveler safety or compliance. Include the date checked for anything time-sensitive.
2. **Label estimates and assumptions.** Keep the *(verify)* flags from the research until a primary source confirms the figure.
3. **Not final legal, tax or investment advice.** Legal and finance agents give research and options; a licensed human signs off.
4. **Human escalation for travelers.** Anything traveler-facing escalates to a human for emergencies, safety, medical, and visa or legal edge cases.
5. **Stay in your lane, and hand off.** Each expert gives its own view and names who else should weigh in.
6. **No secrets in the repo.** Never write API keys or credentials into files. Don't commit or push unless the user asks.

## Key facts every agent should know (from `docs/`, research date Nov 2026)

- U.S. residents made a record **107.7M** outbound air trips in 2024. About **48%** of Americans hold a passport, and **27.3M** passports were issued in FY2025.
- **Positioning:** "Your first trip abroad, without the fear."
- **Launch model:** content, subscription and affiliate booking. Partner booking through Duffel comes in phase 2. Avoid merchant-of-record selling early.
- **Amadeus Self-Service APIs shut down on July 17, 2026.**
- **Economics:** blended ARPU target is $20–$45 per user per year, so growth must come mostly from organic channels. Keep LTV:CAC at 3:1 or better.
- **Top 3 risks:** CAC vs. LTV, commoditization by Google and AI planners, and the accuracy of safety and entry guidance.

## Maintaining the team

Run this after any change to agents, skills or the roster:

```bash
python3 scripts/validate_team.py
```

The validator checks:
- agent names match their file names, are lowercase-hyphen and contain no `:`
- every skill an agent lists exists
- every skill's `name` matches its folder, and its description is within 1,536 characters
- the team stays between 10 and 50 agents, and `orchestrator` and `team-builder` are present
- `docs/expert-roster.md` matches the files exactly
- the counts in this file are correct

Format reference: [subagents](https://code.claude.com/docs/en/sub-agents) · [skills](https://code.claude.com/docs/en/skills).
