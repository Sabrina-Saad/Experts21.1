# Expert Roster — Advisory Agents for the "First Trip Abroad" Travel Platform

> **Purpose:** The experts a consultant needs around them to advise on this project. Each one is built as a Claude Code subagent in `.claude/agents/<agent>.md`, and each skill as a project skill in `.claude/skills/<skill>/SKILL.md`. Built from the research in this folder ([README](README.md), [01 Market](01-market.md), [02 Target Customers](02-target-customers.md), [03 Competitors](03-competitors.md), [04 Costs](04-startup-and-operating-costs.md), [05 Permits & Licenses](05-permits-and-licenses.md), [06 Staffing](06-staffing.md), [07 Marketing](07-marketing.md), [08 Risks](08-risks.md)). See [`CLAUDE.md`](../CLAUDE.md) for how to use the team.

**41 agents · 47 skills.** Skills are shared: each skill is written once and preloaded into every agent that lists it in its `skills:` field.

## How to read this file

- **Part 1** lists every expert agent: roster ID, agent name (= file name and subagent type), one-line job description, the docs it reads first, and its skills.
- **Part 2** defines each skill and shows every agent that uses it.
- **Part 3** ranks skills by how many agents share them.

**Doc codes:** 01 Market · 02 Target Customers · 03 Competitors · 04 Costs · 05 Permits & Licenses · 06 Staffing · 07 Marketing · 08 Risks · ROSTER this file.

**Ground rules for every agent:**
- Cite sources, and prefer official ones (State Dept, NTTO, DOT, FTC, state attorneys general) for anything about traveler safety or compliance.
- Label estimates and assumptions; carry forward the *(verify)* flags from the research docs.
- Legal and financial agents give research and options, not final legal or tax advice; a licensed human signs off.
- Anything traveler-facing escalates to a human for emergencies, safety, medical, and visa or legal edge cases.

## Part 1 — Expert agents

### Coordination (2)

| ID | Agent | Expert | One-line job description | Primary docs | Skills |
|---|---|---|---|---|---|
| ORC-01 | `orchestrator` | **Orchestrator** | Takes any question, decides which experts to bring in, has them work together, and returns one combined answer. | README, ROSTER | `expert-orchestration`, `executive-synthesis`, `source-verification` |
| META-01 | `team-builder` | **Team Builder (meta agent)** | Creates new expert agents and skills and improves existing ones, keeping the roster, wiring and CLAUDE.md in sync. | ROSTER | `agent-skill-authoring` |

### Business & Strategy (8)

| ID | Agent | Expert | One-line job description | Primary docs | Skills |
|---|---|---|---|---|---|
| BIZ-01 | `engagement-lead` | **Engagement Lead** | Runs the consulting engagement: scope, workplan, decision log, deliverables and status reports for the consultant. | README, ROSTER, 08 | `source-verification`, `business-model-evaluation`, `executive-synthesis`, `llm-guardrails-engineering`, `hiring-org-design`, `risk-assessment-insurance`, `pr-crisis-comms`, `expert-orchestration` |
| BIZ-02 | `business-strategist` | **Business Strategist** | Owns positioning, business-model choices (affiliate → partner booking → merchant of record) and the phased roadmap. | 01, 03, 04, 08 | `travel-statistics-analysis`, `market-sizing`, `competitor-tracking`, `business-model-evaluation`, `roadmap-prioritization`, `executive-synthesis`, `financial-modeling`, `fundraising-materials`, `risk-assessment-insurance` |
| BIZ-03 | `market-research-analyst` | **Market Research Analyst** | Sizes and tracks U.S. outbound travel demand (NTTO, passport issuance, OTA volumes) and keeps the TAM/SAM/SOM current. | 01 | `source-verification`, `travel-statistics-analysis`, `market-sizing`, `currency-exchange-rates` |
| BIZ-04 | `customer-insights-researcher` | **Customer Insights Researcher** | Validates the personas and their travel fears through surveys and interviews, and turns findings into jobs-to-be-done. | 02 | `source-verification`, `travel-statistics-analysis`, `survey-interview-design`, `persona-jtbd-mapping` |
| BIZ-05 | `competitive-intelligence-analyst` | **Competitive Intelligence Analyst** | Monitors OTAs, Google Flights, deal clubs, AI planners and language apps, and flags moves that threaten our position. | 03 | `source-verification`, `competitor-tracking` |
| BIZ-06 | `travel-distribution-expert` | **Travel Industry & Distribution Expert** | Explains how airlines, hotels, OTAs, GDS/NDC, host agencies and affiliate networks make money and what they will let us do. | 03, 04, 05 | `source-verification`, `business-model-evaluation`, `travel-distribution-economics`, `travel-regulatory-compliance`, `partnership-negotiation` |
| BIZ-07 | `partnerships-lead` | **Partnerships & Business Development Lead** | Builds affiliate, insurance, eSIM, language-app, university, credit-union and employer partnerships. | 04, 07 | `travel-distribution-economics`, `contract-drafting-review`, `partnership-negotiation` |
| BIZ-08 | `product-manager` | **Product Manager** | Defines the MVP (fare alerts, readiness checklist, survival language, touristy-vs-local guides) and prioritizes the backlog against user value. | 02, README | `competitor-tracking`, `survey-interview-design`, `persona-jtbd-mapping`, `roadmap-prioritization`, `accessible-calm-ux`, `product-analytics-experiments`, `pricing-subscription-design` |

### Travel Domain (4)

| ID | Agent | Expert | One-line job description | Primary docs | Skills |
|---|---|---|---|---|---|
| DOM-01 | `destination-expert` | **Destination & Local Experiences Expert** | Curates first-timer-friendly destinations and the 'touristy vs. off-the-path' picks, and manages the local contributor network. | 02, 06 | `source-verification`, `persona-jtbd-mapping`, `destination-curation`, `editorial-freshness`, `contractor-management`, `copywriting`, `currency-exchange-rates` |
| DOM-02 | `entry-safety-expert` | **Entry Requirements & Traveler Safety Expert** | Keeps passport, visa, UK ETA, EU EES/ETIAS, State Dept advisory, STEP and health guidance accurate and up to date. | 01, 08 | `source-verification`, `entry-requirements-monitoring`, `traveler-crisis-response`, `editorial-freshness` |
| DOM-03 | `language-learning-specialist` | **Language Learning Specialist** | Designs destination-specific survival-language packs and pronunciation practice, and runs native-speaker review. | 02, 03 | `survival-language-design`, `editorial-freshness` |
| DOM-04 | `fare-deals-expert` | **Flight Deals & Fare Expert** | Defines what counts as a 'good deal' per route and season, and how fare alerts should be scored and explained to beginners. | 03, 07 | `source-verification`, `travel-distribution-economics`, `fare-deal-scoring`, `lifecycle-marketing`, `currency-exchange-rates` |

### Technical (7)

| ID | Agent | Expert | One-line job description | Primary docs | Skills |
|---|---|---|---|---|---|
| TEC-01 | `solutions-architect` | **Solutions Architect** | Designs the overall system, including a provider-agnostic layer so no single travel API can take the product down. | 04, 08 | `roadmap-prioritization`, `resilient-system-architecture`, `travel-api-integration`, `llm-guardrails-engineering`, `app-development-offline`, `security-privacy-engineering` |
| TEC-02 | `travel-api-engineer` | **Travel API & Integrations Engineer** | Integrates Duffel, affiliate networks, lodging, eSIM, insurance and tour APIs, and builds the fare-tracking engine. | 04 | `travel-distribution-economics`, `fare-deal-scoring`, `resilient-system-architecture`, `travel-api-integration`, `currency-exchange-rates` |
| TEC-03 | `ai-ml-engineer` | **AI / ML Engineer** | Builds the trip-planning assistant, personalization and translation features, with guardrails and human escalation. | 06, 08 | `fare-deal-scoring`, `entry-requirements-monitoring`, `survival-language-design`, `llm-guardrails-engineering`, `currency-exchange-rates` |
| TEC-04 | `fullstack-mobile-engineer` | **Full-Stack & Mobile Engineer** | Builds the web app, mobile apps and offline features (phrasebook, emergency card, guides). | 04 | `resilient-system-architecture`, `travel-api-integration`, `app-development-offline`, `seo-ai-search` |
| TEC-05 | `ux-ui-designer` | **UX / UI Designer** | Designs a calm, accessible experience that works for nervous 22-year-olds and 65-year-olds alike. | 02 | `survey-interview-design`, `persona-jtbd-mapping`, `roadmap-prioritization`, `app-development-offline`, `accessible-calm-ux` |
| TEC-06 | `data-analytics-engineer` | **Data & Analytics Engineer** | Builds tracking, dashboards and experiments for funnel, retention, CAC/LTV and affiliate earnings. | 04, 07, 08 | `product-analytics-experiments`, `privacy-law-compliance`, `seo-ai-search`, `paid-acquisition` |
| TEC-07 | `security-privacy-engineer` | **Security & Privacy Engineer** | Protects passport numbers, location and payment data, and keeps PCI scope small. | 05 | `resilient-system-architecture`, `security-privacy-engineering`, `privacy-law-compliance` |

### Operations (5)

| ID | Agent | Expert | One-line job description | Primary docs | Skills |
|---|---|---|---|---|---|
| OPS-01 | `operations-manager` | **Operations Manager** | Runs day-to-day operations, vendors and processes, and the playbooks for travel disruptions and crises. | 06, 08 | `traveler-crisis-response`, `support-operations`, `contractor-management`, `travel-regulatory-compliance`, `risk-assessment-insurance` |
| OPS-02 | `traveler-support-lead` | **Traveler Support & Emergency Escalation Lead** | Runs the 'Trip Guide' support team and the 24/7 escalation path for travelers who are stuck, scared or in danger. | 06, 08 | `entry-requirements-monitoring`, `traveler-crisis-response`, `llm-guardrails-engineering`, `support-operations`, `brand-voice`, `pr-crisis-comms` |
| OPS-03 | `content-ops-editor` | **Content Operations & Editorial QA Lead** | Enforces editorial standards and 'last verified' freshness on every guide, checklist and language pack. | 06, 08 | `entry-requirements-monitoring`, `destination-curation`, `survival-language-design`, `editorial-freshness`, `contractor-management` |
| OPS-04 | `trust-safety-moderator` | **Trust & Safety / Community Moderator** | Moderates community and user content, and blocks fake reviews, scams and unsafe 'hidden gem' recommendations. | 05, 08 | `content-moderation`, `consumer-protection-law` |
| OPS-05 | `people-talent-partner` | **People & Talent Partner** | Plans hiring by phase, sets compensation bands, and contracts freelance writers, local experts and native speakers. | 06 | `contractor-management`, `hiring-org-design` |

### Finance (4)

| ID | Agent | Expert | One-line job description | Primary docs | Skills |
|---|---|---|---|---|---|
| FIN-01 | `cfo` | **CFO / Financial Modeler** | Owns the financial model, burn, runway, unit economics and break-even plan. | 04 | `market-sizing`, `business-model-evaluation`, `executive-synthesis`, `hiring-org-design`, `financial-modeling`, `fundraising-materials`, `accounting-tax`, `risk-assessment-insurance`, `currency-exchange-rates` |
| FIN-02 | `pricing-strategist` | **Pricing & Monetization Strategist** | Designs free vs. premium tiers, subscription pricing, concierge pricing and the affiliate revenue mix. | 03, 04 | `competitor-tracking`, `travel-distribution-economics`, `product-analytics-experiments`, `financial-modeling`, `pricing-subscription-design`, `consumer-protection-law`, `currency-exchange-rates` |
| FIN-03 | `fundraising-advisor` | **Fundraising & Investor Relations Advisor** | Prepares the pitch, data room and seed raise ($1.5M–$3M) and manages investor communications. | 01, 04, README | `travel-statistics-analysis`, `market-sizing`, `executive-synthesis`, `financial-modeling`, `fundraising-materials`, `partnership-negotiation` |
| FIN-04 | `accounting-tax-advisor` | **Accounting & Tax Advisor** | Handles bookkeeping, sales tax on digital subscriptions, app-store revenue accounting and entity tax matters. | 04, 05 | `source-verification`, `accounting-tax` |

### Legal & Risk (5)

| ID | Agent | Expert | One-line job description | Primary docs | Skills |
|---|---|---|---|---|---|
| LEG-01 | `travel-regulatory-counsel` | **Travel Regulatory Counsel** | Advises on seller-of-travel laws (CA, FL, WA, HI and others), ARC/IATAN and DOT ticket-agent and refund rules for each business model. | 05 | `source-verification`, `business-model-evaluation`, `travel-regulatory-compliance`, `contract-drafting-review` |
| LEG-02 | `consumer-protection-counsel` | **Consumer Protection & Advertising Counsel** | Keeps marketing, pricing and subscriptions compliant with FTC rules (endorsements, fake reviews, junk fees), auto-renewal laws, CAN-SPAM and TCPA. | 05, 07 | `source-verification`, `consumer-protection-law`, `contract-drafting-review` |
| LEG-03 | `privacy-counsel` | **Privacy & Data Protection Counsel** | Advises on CCPA/CPRA and other state privacy laws, COPPA and GDPR exposure for traveler data. | 05 | `source-verification`, `security-privacy-engineering`, `privacy-law-compliance` |
| LEG-04 | `corporate-ip-counsel` | **Corporate, Contracts & IP Counsel** | Handles entity formation, founder and investor documents, partner and contributor contracts, and trademarks. | 04, 05, 06 | `contractor-management`, `contract-drafting-review` |
| LEG-05 | `insurance-risk-manager` | **Insurance & Risk Manager** | Maintains the risk register, arranges E&O, cyber and general liability cover, and checks travel-insurance referral licensing. | 05, 08 | `executive-synthesis`, `traveler-crisis-response`, `travel-regulatory-compliance`, `risk-assessment-insurance` |

### Marketing (6)

| ID | Agent | Expert | One-line job description | Primary docs | Skills |
|---|---|---|---|---|---|
| MKT-01 | `brand-strategist` | **Brand Strategist** | Owns the 'first trip abroad, without the fear' positioning, brand voice and visual identity. | 07 | `competitor-tracking`, `persona-jtbd-mapping`, `accessible-calm-ux`, `brand-voice`, `copywriting`, `creator-program`, `pr-crisis-comms` |
| MKT-02 | `growth-marketer` | **Growth & Performance Marketer** | Runs paid tests, referral loops and funnel optimization, and keeps blended CAC under target. | 04, 07 | `product-analytics-experiments`, `financial-modeling`, `consumer-protection-law`, `paid-acquisition`, `lifecycle-marketing` |
| MKT-03 | `seo-content-lead` | **SEO & Content Marketing Lead** | Builds the content hub ('Do I need a visa for…', '[City] for first-timers') and makes it citable by AI search. | 07 | `source-verification`, `entry-requirements-monitoring`, `destination-curation`, `editorial-freshness`, `brand-voice`, `copywriting`, `seo-ai-search`, `currency-exchange-rates` |
| MKT-04 | `social-creator-manager` | **Social Media & Creator Partnerships Manager** | Runs short-form video series and the micro-creator program on TikTok, Reels and YouTube. | 02, 07 | `persona-jtbd-mapping`, `destination-curation`, `consumer-protection-law`, `brand-voice`, `copywriting`, `creator-program`, `partnership-negotiation` |
| MKT-05 | `lifecycle-crm-marketer` | **Lifecycle & CRM Marketer** | Owns fare-alert email and push, onboarding, free-to-paid conversion, renewal and 'plan your next trip' journeys. | 07 | `fare-deal-scoring`, `product-analytics-experiments`, `pricing-subscription-design`, `consumer-protection-law`, `privacy-law-compliance`, `copywriting`, `lifecycle-marketing` |
| MKT-06 | `pr-communications-lead` | **PR & Communications Lead** | Runs the annual First-Time Traveler Fear Index, explainers when entry rules change, and crisis communications. | 07, 08 | `source-verification`, `travel-statistics-analysis`, `survey-interview-design`, `entry-requirements-monitoring`, `traveler-crisis-response`, `brand-voice`, `copywriting`, `pr-crisis-comms` |

## Part 2 — Skills and the agents that use them

| ID | Skill | Name | What it covers | Used by |
|---|---|---|---|---|
| SK-01 | `source-verification` | **Web research & source verification** | Finds current information, prefers official sources, cross-checks figures and labels anything unverified. | `orchestrator`, `engagement-lead`, `market-research-analyst`, `customer-insights-researcher`, `competitive-intelligence-analyst`, `travel-distribution-expert`, `destination-expert`, `entry-safety-expert`, `fare-deals-expert`, `accounting-tax-advisor`, `travel-regulatory-counsel`, `consumer-protection-counsel`, `privacy-counsel`, `seo-content-lead`, `pr-communications-lead` |
| SK-02 | `travel-statistics-analysis` | **Travel statistics analysis** | Reads and interprets NTTO, State Dept passport, OTA and survey data, and keeps series that measure different things apart. | `business-strategist`, `market-research-analyst`, `customer-insights-researcher`, `fundraising-advisor`, `pr-communications-lead` |
| SK-03 | `market-sizing` | **Market sizing (TAM/SAM/SOM)** | Builds and updates top-down and bottom-up market estimates with stated assumptions. | `business-strategist`, `market-research-analyst`, `cfo`, `fundraising-advisor` |
| SK-04 | `competitor-tracking` | **Competitor tracking & feature comparison** | Maintains the competitor list and matrix, tracks pricing and launches, and assesses threats. | `business-strategist`, `competitive-intelligence-analyst`, `product-manager`, `pricing-strategist`, `brand-strategist` |
| SK-05 | `survey-interview-design` | **Survey & interview design** | Writes unbiased surveys and interview guides, and analyzes results by persona. | `customer-insights-researcher`, `product-manager`, `ux-ui-designer`, `pr-communications-lead` |
| SK-06 | `persona-jtbd-mapping` | **Persona & jobs-to-be-done mapping** | Keeps the six personas current and maps each traveler fear to a product feature. | `customer-insights-researcher`, `product-manager`, `destination-expert`, `ux-ui-designer`, `brand-strategist`, `social-creator-manager` |
| SK-07 | `business-model-evaluation` | **Business model & strategy evaluation** | Compares business models (affiliate, partner booking, merchant of record) on revenue, risk and regulatory weight. | `engagement-lead`, `business-strategist`, `travel-distribution-expert`, `cfo`, `travel-regulatory-counsel` |
| SK-08 | `roadmap-prioritization` | **Product roadmap & prioritization** | Scopes the MVP, writes requirements and ranks features by value, effort and risk. | `business-strategist`, `product-manager`, `solutions-architect`, `ux-ui-designer` |
| SK-09 | `executive-synthesis` | **Synthesis & executive briefing** | Combines inputs from several experts into a clear recommendation with trade-offs for the consultant or board. | `orchestrator`, `engagement-lead`, `business-strategist`, `cfo`, `fundraising-advisor`, `insurance-risk-manager` |
| SK-10 | `travel-distribution-economics` | **Travel distribution & affiliate economics** | Knows how OTAs, GDS/NDC, host agencies, metasearch and affiliate networks work, including commission rates and cookie terms. | `travel-distribution-expert`, `partnerships-lead`, `fare-deals-expert`, `travel-api-engineer`, `pricing-strategist` |
| SK-11 | `fare-deal-scoring` | **Fare analysis & deal scoring** | Judges whether a fare is a real deal for a route and season, and explains it in plain language. | `fare-deals-expert`, `travel-api-engineer`, `ai-ml-engineer`, `lifecycle-crm-marketer` |
| SK-12 | `entry-requirements-monitoring` | **Entry requirements & travel-advisory monitoring** | Tracks passport, visa, UK ETA, EU EES/ETIAS, State Dept advisories, STEP and CDC guidance, and flags changes. | `entry-safety-expert`, `ai-ml-engineer`, `traveler-support-lead`, `content-ops-editor`, `seo-content-lead`, `pr-communications-lead` |
| SK-13 | `destination-curation` | **Destination curation (touristy vs. off-the-path)** | Selects and vets places, writes first-timer guides and applies responsible-travel rules. | `destination-expert`, `content-ops-editor`, `seo-content-lead`, `social-creator-manager` |
| SK-14 | `survival-language-design` | **Survival-language curriculum design** | Builds trip-specific phrase packs, pronunciation practice and native-speaker review workflows. | `language-learning-specialist`, `ai-ml-engineer`, `content-ops-editor` |
| SK-15 | `traveler-crisis-response` | **Traveler emergency & crisis response** | Follows the playbooks for lost passports, cancellations, medical issues and unrest, and knows when to hand off to a human. | `entry-safety-expert`, `operations-manager`, `traveler-support-lead`, `insurance-risk-manager`, `pr-communications-lead` |
| SK-16 | `resilient-system-architecture` | **System architecture & multi-provider design** | Designs scalable systems with abstraction layers and fallbacks so no single supplier is critical. | `solutions-architect`, `travel-api-engineer`, `fullstack-mobile-engineer`, `security-privacy-engineer` |
| SK-17 | `travel-api-integration` | **Travel API integration** | Integrates Duffel, affiliate, lodging, eSIM, insurance and tour APIs, including caching and error handling. | `solutions-architect`, `travel-api-engineer`, `fullstack-mobile-engineer` |
| SK-18 | `llm-guardrails-engineering` | **LLM application engineering & guardrails** | Builds AI assistants with citations to official sources, safety guardrails, human escalation and cost control. | `engagement-lead`, `solutions-architect`, `ai-ml-engineer`, `traveler-support-lead` |
| SK-19 | `app-development-offline` | **Web, mobile & offline app development** | Builds web, iOS and Android apps, offline content and push notifications. | `solutions-architect`, `fullstack-mobile-engineer`, `ux-ui-designer` |
| SK-20 | `accessible-calm-ux` | **Accessible UX & UI design** | Designs calm, low-anxiety flows that meet WCAG and suit older users. | `product-manager`, `ux-ui-designer`, `brand-strategist` |
| SK-21 | `product-analytics-experiments` | **Product analytics & experimentation** | Sets up event tracking, dashboards, A/B tests and funnel and cohort analysis. | `product-manager`, `data-analytics-engineer`, `pricing-strategist`, `growth-marketer`, `lifecycle-crm-marketer` |
| SK-22 | `security-privacy-engineering` | **Security, privacy engineering & PCI** | Protects sensitive traveler data, handles access control and incident response, and minimizes PCI scope. | `solutions-architect`, `security-privacy-engineer`, `privacy-counsel` |
| SK-23 | `support-operations` | **Customer support operations** | Designs support tiers, staffing, help-desk tooling, response-time targets and quality checks. | `operations-manager`, `traveler-support-lead` |
| SK-24 | `editorial-freshness` | **Editorial standards & content freshness** | Maintains style guides, fact-check workflows and 'last verified' refresh schedules. | `destination-expert`, `entry-safety-expert`, `language-learning-specialist`, `content-ops-editor`, `seo-content-lead` |
| SK-25 | `content-moderation` | **Content moderation & fake-review detection** | Reviews user content, verifies contributors and enforces community rules. | `trust-safety-moderator` |
| SK-26 | `contractor-management` | **Vendor & contractor management** | Sources, contracts, pays and evaluates freelancers, local experts and outside service providers. | `destination-expert`, `operations-manager`, `content-ops-editor`, `people-talent-partner`, `corporate-ip-counsel` |
| SK-27 | `hiring-org-design` | **Hiring & org design** | Plans the team by phase, writes job descriptions, sets compensation bands and designs the interview process. | `engagement-lead`, `people-talent-partner`, `cfo` |
| SK-28 | `financial-modeling` | **Financial modeling & unit economics** | Builds P&L, burn, runway, CAC/LTV, ARPU and break-even models with scenarios. | `business-strategist`, `cfo`, `pricing-strategist`, `fundraising-advisor`, `growth-marketer` |
| SK-29 | `pricing-subscription-design` | **Pricing & subscription design** | Designs tiers, trials, annual vs. monthly plans and price tests, and accounts for app-store fees. | `product-manager`, `pricing-strategist`, `lifecycle-crm-marketer` |
| SK-30 | `fundraising-materials` | **Fundraising & investor materials** | Prepares the pitch deck, data room and cap table scenarios, and runs investor updates. | `business-strategist`, `cfo`, `fundraising-advisor` |
| SK-31 | `accounting-tax` | **Accounting, tax & revenue recognition** | Handles bookkeeping, sales tax on digital goods, and affiliate and subscription revenue recognition. | `cfo`, `accounting-tax-advisor` |
| SK-32 | `travel-regulatory-compliance` | **Travel regulatory compliance** | Applies seller-of-travel laws, ARC/IATAN rules, DOT advertising and refund rules, and travel-insurance referral licensing. | `travel-distribution-expert`, `operations-manager`, `travel-regulatory-counsel`, `insurance-risk-manager` |
| SK-33 | `consumer-protection-law` | **Consumer protection & advertising law** | Applies FTC Act Section 5, endorsement guides, the fake-reviews rule, junk-fee total pricing, ROSCA and state auto-renewal laws, CAN-SPAM and TCPA. | `trust-safety-moderator`, `pricing-strategist`, `consumer-protection-counsel`, `growth-marketer`, `social-creator-manager`, `lifecycle-crm-marketer` |
| SK-34 | `privacy-law-compliance` | **Privacy law compliance** | Applies CCPA/CPRA and other state privacy laws, COPPA and GDPR; writes notices and handles data-subject requests. | `data-analytics-engineer`, `security-privacy-engineer`, `privacy-counsel`, `lifecycle-crm-marketer` |
| SK-35 | `contract-drafting-review` | **Contract drafting & review** | Drafts and reviews ToS, partner and affiliate agreements, contributor IP assignments and vendor contracts. | `partnerships-lead`, `travel-regulatory-counsel`, `consumer-protection-counsel`, `corporate-ip-counsel` |
| SK-36 | `risk-assessment-insurance` | **Risk assessment & insurance** | Maintains the risk register (likelihood × impact), early-warning metrics and insurance coverage. | `engagement-lead`, `business-strategist`, `operations-manager`, `cfo`, `insurance-risk-manager` |
| SK-37 | `brand-voice` | **Brand positioning & voice** | Applies the brand promise and a warm, plain-English tone to every touchpoint. | `traveler-support-lead`, `brand-strategist`, `seo-content-lead`, `social-creator-manager`, `pr-communications-lead` |
| SK-38 | `copywriting` | **Copywriting & content creation** | Writes guides, landing pages, scripts, emails and ad copy in the brand voice. | `destination-expert`, `brand-strategist`, `seo-content-lead`, `social-creator-manager`, `lifecycle-crm-marketer`, `pr-communications-lead` |
| SK-39 | `seo-ai-search` | **SEO & AI-search optimization** | Handles keyword research, programmatic pages, schema markup and getting cited by AI answer engines. | `fullstack-mobile-engineer`, `data-analytics-engineer`, `seo-content-lead` |
| SK-40 | `creator-program` | **Social video & creator program management** | Plans short-form series, recruits and briefs creators, and manages disclosures and revenue share. | `brand-strategist`, `social-creator-manager` |
| SK-41 | `paid-acquisition` | **Paid acquisition & attribution** | Runs Meta, TikTok, Google and Apple Search Ads tests, tracks attribution and enforces the LTV:CAC 3:1 rule. | `data-analytics-engineer`, `growth-marketer` |
| SK-42 | `lifecycle-marketing` | **Lifecycle, email & push marketing** | Builds onboarding, fare-alert, trial-conversion, renewal and referral journeys. | `fare-deals-expert`, `growth-marketer`, `lifecycle-crm-marketer` |
| SK-43 | `partnership-negotiation` | **Partnership development & negotiation** | Prospects, pitches and negotiates B2B2C, affiliate and co-marketing deals. | `travel-distribution-expert`, `partnerships-lead`, `fundraising-advisor`, `social-creator-manager` |
| SK-44 | `pr-crisis-comms` | **PR, media relations & crisis communications** | Writes press releases, runs the data-led PR survey, handles rapid-response explainers and crisis statements. | `engagement-lead`, `traveler-support-lead`, `brand-strategist`, `pr-communications-lead` |
| SK-45 | `expert-orchestration` | **Expert orchestration** | Routes a question to the right expert agents, runs them in parallel, has them challenge each other, and returns one combined answer. | `orchestrator`, `engagement-lead` |
| SK-46 | `agent-skill-authoring` | **Agent & skill authoring** | Creates, updates and validates project subagents and skills so the expert team stays consistent. | `team-builder` |
| SK-47 | `currency-exchange-rates` | **Currency exchange rates (Frankfurter API)** | Gets current and historical exchange rates from the Frankfurter API (ECB reference rates, no key) and turns them into dollar costs, budgets and trends. | `market-research-analyst`, `destination-expert`, `fare-deals-expert`, `travel-api-engineer`, `ai-ml-engineer`, `cfo`, `pricing-strategist`, `seo-content-lead` |

## Part 3 — Most-shared skills

| Skill | Number of agents |
|---|---|
| `source-verification` | 15 |
| `currency-exchange-rates` | 8 |
| `persona-jtbd-mapping` | 6 |
| `executive-synthesis` | 6 |
| `entry-requirements-monitoring` | 6 |
| `consumer-protection-law` | 6 |
| `copywriting` | 6 |
| `travel-statistics-analysis` | 5 |
| `competitor-tracking` | 5 |
| `business-model-evaluation` | 5 |
| `travel-distribution-economics` | 5 |
| `traveler-crisis-response` | 5 |
| `product-analytics-experiments` | 5 |
| `editorial-freshness` | 5 |
| `contractor-management` | 5 |
| `financial-modeling` | 5 |
| `risk-assessment-insurance` | 5 |
| `brand-voice` | 5 |

Every other skill is used by 1–4 agents.

## Suggested build order

1. **Core advisory group:** `orchestrator`, `engagement-lead`, `business-strategist`, `cfo`, `travel-regulatory-counsel`, `product-manager`, `growth-marketer`. These cover the board-level risks in [08 Risks](08-risks.md): CAC vs. LTV, AI commoditization and guidance accuracy.
2. **MVP build group:** `solutions-architect`, `travel-api-engineer`, `ai-ml-engineer`, `fullstack-mobile-engineer`, `ux-ui-designer`, `entry-safety-expert`, `language-learning-specialist`, `fare-deals-expert`, `content-ops-editor`.
3. **Launch group:** `brand-strategist`, `seo-content-lead`, `social-creator-manager`, `lifecycle-crm-marketer`, `consumer-protection-counsel`, `privacy-counsel`, `traveler-support-lead`, `partnerships-lead`.
4. **Scale group:** everyone else, as the business moves to partner booking (see the phases in [05 Permits & Licenses](05-permits-and-licenses.md)).
