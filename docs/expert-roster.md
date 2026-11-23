# Expert Roster — Advisory Agents for the "First Trip Abroad" Travel Platform

> **Purpose:** The experts a consultant needs around them to advise on this project, each designed to become an AI agent. Built from the research in this folder ([README](README.md), [01 Market](01-market.md), [02 Target Customers](02-target-customers.md), [03 Competitors](03-competitors.md), [04 Costs](04-startup-and-operating-costs.md), [05 Permits & Licenses](05-permits-and-licenses.md), [06 Staffing](06-staffing.md), [07 Marketing](07-marketing.md), [08 Risks](08-risks.md)).

**39 agents · 44 skills.** Skills are shared: each skill is written once and attached to every agent that needs it.

## How to read this file

- **Part 1** lists every expert agent with a one-line job description, the docs it should read first, and its skills (by skill ID).
- **Part 2** defines each skill and shows every agent that uses it.
- **Part 3** shows how many agents share each skill, which helps decide which skills to build first.

**Doc codes:** 01 Market · 02 Target Customers · 03 Competitors · 04 Costs · 05 Permits & Licenses · 06 Staffing · 07 Marketing · 08 Risks.

**Ground rules for every agent** (from the research):
- Cite sources, and prefer official ones (State Dept, NTTO, DOT, FTC, state attorneys general) for anything about traveler safety or compliance.
- Label estimates and assumptions; carry forward the *(verify)* flags from the research docs.
- Legal and financial agents give research and options, not final legal or tax advice; a licensed human signs off.
- Anything traveler-facing escalates to a human for emergencies, safety, medical, and visa or legal edge cases.

## Part 1 — Expert agents

### Business & Strategy (8)

| ID | Expert agent | One-line job description | Primary docs | Skills |
|---|---|---|---|---|
| BIZ-01 | **Engagement Lead / Orchestrator** | Turns the consultant's questions into tasks, sends each to the right experts, reconciles conflicting advice and returns one recommendation. | README | SK-01, SK-07, SK-09, SK-18, SK-27, SK-36, SK-44 |
| BIZ-02 | **Business Strategist** | Owns positioning, business-model choices (affiliate → partner booking → merchant of record) and the phased roadmap. | 01, 03, 04, 08 | SK-02, SK-03, SK-04, SK-07, SK-08, SK-09, SK-28, SK-30, SK-36 |
| BIZ-03 | **Market Research Analyst** | Sizes and tracks U.S. outbound travel demand (NTTO, passport issuance, OTA volumes) and keeps the TAM/SAM/SOM current. | 01 | SK-01, SK-02, SK-03 |
| BIZ-04 | **Customer Insights Researcher** | Validates the personas and their travel fears through surveys and interviews, and turns findings into jobs-to-be-done. | 02 | SK-01, SK-02, SK-05, SK-06 |
| BIZ-05 | **Competitive Intelligence Analyst** | Monitors OTAs, Google Flights, deal clubs, AI planners and language apps, and flags moves that threaten our position. | 03 | SK-01, SK-04 |
| BIZ-06 | **Travel Industry & Distribution Expert** | Explains how airlines, hotels, OTAs, GDS/NDC, host agencies and affiliate networks make money and what they will let us do. | 03, 04, 05 | SK-01, SK-07, SK-10, SK-32, SK-43 |
| BIZ-07 | **Partnerships & Business Development Lead** | Builds affiliate, insurance, eSIM, language-app, university, credit-union and employer partnerships. | 04, 07 | SK-10, SK-35, SK-43 |
| BIZ-08 | **Product Manager** | Defines the MVP (fare alerts, readiness checklist, survival language, touristy-vs-local guides) and prioritizes the backlog against user value. | 02, README | SK-04, SK-05, SK-06, SK-08, SK-20, SK-21, SK-29 |

### Travel Domain (4)

| ID | Expert agent | One-line job description | Primary docs | Skills |
|---|---|---|---|---|
| DOM-01 | **Destination & Local Experiences Expert** | Curates first-timer-friendly destinations and the 'touristy vs. off-the-path' picks, and manages the local contributor network. | 02, 06 | SK-01, SK-06, SK-13, SK-24, SK-26, SK-38 |
| DOM-02 | **Entry Requirements & Traveler Safety Expert** | Keeps passport, visa, UK ETA, EU EES/ETIAS, State Dept advisory, STEP and health guidance accurate and up to date. | 01, 08 | SK-01, SK-12, SK-15, SK-24 |
| DOM-03 | **Language Learning Specialist** | Designs destination-specific survival-language packs and pronunciation practice, and runs native-speaker review. | 02, 03 | SK-14, SK-24 |
| DOM-04 | **Flight Deals & Fare Expert** | Defines what counts as a 'good deal' per route and season, and how fare alerts should be scored and explained to beginners. | 03, 07 | SK-01, SK-10, SK-11, SK-42 |

### Technical (7)

| ID | Expert agent | One-line job description | Primary docs | Skills |
|---|---|---|---|---|
| TEC-01 | **Solutions Architect** | Designs the overall system, including a provider-agnostic layer so no single travel API can take the product down. | 04, 08 | SK-08, SK-16, SK-17, SK-18, SK-19, SK-22 |
| TEC-02 | **Travel API & Integrations Engineer** | Integrates Duffel, affiliate networks, lodging, eSIM, insurance and tour APIs, and builds the fare-tracking engine. | 04 | SK-10, SK-11, SK-16, SK-17 |
| TEC-03 | **AI / ML Engineer** | Builds the trip-planning assistant, personalization and translation features, with guardrails and human escalation. | 06, 08 | SK-11, SK-12, SK-14, SK-18 |
| TEC-04 | **Full-Stack & Mobile Engineer** | Builds the web app, mobile apps and offline features (phrasebook, emergency card, guides). | 04 | SK-16, SK-17, SK-19, SK-39 |
| TEC-05 | **UX / UI Designer** | Designs a calm, accessible experience that works for nervous 22-year-olds and 65-year-olds alike. | 02 | SK-05, SK-06, SK-08, SK-19, SK-20 |
| TEC-06 | **Data & Analytics Engineer** | Builds tracking, dashboards and experiments for funnel, retention, CAC/LTV and affiliate earnings. | 04, 07, 08 | SK-21, SK-34, SK-39, SK-41 |
| TEC-07 | **Security & Privacy Engineer** | Protects passport numbers, location and payment data, and keeps PCI scope small. | 05 | SK-16, SK-22, SK-34 |

### Operations (5)

| ID | Expert agent | One-line job description | Primary docs | Skills |
|---|---|---|---|---|
| OPS-01 | **Operations Manager** | Runs day-to-day operations, vendors and processes, and the playbooks for travel disruptions and crises. | 06, 08 | SK-15, SK-23, SK-26, SK-32, SK-36 |
| OPS-02 | **Traveler Support & Emergency Escalation Lead** | Runs the 'Trip Guide' support team and the 24/7 escalation path for travelers who are stuck, scared or in danger. | 06, 08 | SK-12, SK-15, SK-18, SK-23, SK-37, SK-44 |
| OPS-03 | **Content Operations & Editorial QA Lead** | Enforces editorial standards and 'last verified' freshness on every guide, checklist and language pack. | 06, 08 | SK-12, SK-13, SK-14, SK-24, SK-26 |
| OPS-04 | **Trust & Safety / Community Moderator** | Moderates community and user content, and blocks fake reviews, scams and unsafe 'hidden gem' recommendations. | 05, 08 | SK-25, SK-33 |
| OPS-05 | **People & Talent Partner** | Plans hiring by phase, sets compensation bands, and contracts freelance writers, local experts and native speakers. | 06 | SK-26, SK-27 |

### Finance (4)

| ID | Expert agent | One-line job description | Primary docs | Skills |
|---|---|---|---|---|
| FIN-01 | **CFO / Financial Modeler** | Owns the financial model, burn, runway, unit economics and break-even plan. | 04 | SK-03, SK-07, SK-09, SK-27, SK-28, SK-30, SK-31, SK-36 |
| FIN-02 | **Pricing & Monetization Strategist** | Designs free vs. premium tiers, subscription pricing, concierge pricing and the affiliate revenue mix. | 03, 04 | SK-04, SK-10, SK-21, SK-28, SK-29, SK-33 |
| FIN-03 | **Fundraising & Investor Relations Advisor** | Prepares the pitch, data room and seed raise ($1.5M–$3M) and manages investor communications. | 01, 04, README | SK-02, SK-03, SK-09, SK-28, SK-30, SK-43 |
| FIN-04 | **Accounting & Tax Advisor** | Handles bookkeeping, sales tax on digital subscriptions, app-store revenue accounting and entity tax matters. | 04, 05 | SK-01, SK-31 |

### Legal & Risk (5)

| ID | Expert agent | One-line job description | Primary docs | Skills |
|---|---|---|---|---|
| LEG-01 | **Travel Regulatory Counsel** | Advises on seller-of-travel laws (CA, FL, WA, HI and others), ARC/IATAN and DOT ticket-agent and refund rules for each business model. | 05 | SK-01, SK-07, SK-32, SK-35 |
| LEG-02 | **Consumer Protection & Advertising Counsel** | Keeps marketing, pricing and subscriptions compliant with FTC rules (endorsements, fake reviews, junk fees), auto-renewal laws, CAN-SPAM and TCPA. | 05, 07 | SK-01, SK-25, SK-33, SK-35 |
| LEG-03 | **Privacy & Data Protection Counsel** | Advises on CCPA/CPRA and other state privacy laws, COPPA and GDPR exposure for traveler data. | 05 | SK-01, SK-22, SK-34 |
| LEG-04 | **Corporate, Contracts & IP Counsel** | Handles entity formation, founder and investor documents, partner and contributor contracts, and trademarks. | 04, 05, 06 | SK-26, SK-35 |
| LEG-05 | **Insurance & Risk Manager** | Maintains the risk register, arranges E&O, cyber and general liability cover, and checks travel-insurance referral licensing. | 05, 08 | SK-09, SK-15, SK-32, SK-36 |

### Marketing (6)

| ID | Expert agent | One-line job description | Primary docs | Skills |
|---|---|---|---|---|
| MKT-01 | **Brand Strategist** | Owns the 'first trip abroad, without the fear' positioning, brand voice and visual identity. | 07 | SK-04, SK-06, SK-20, SK-37, SK-38, SK-40, SK-44 |
| MKT-02 | **Growth & Performance Marketer** | Runs paid tests, referral loops and funnel optimization, and keeps blended CAC under target. | 04, 07 | SK-21, SK-28, SK-33, SK-41, SK-42 |
| MKT-03 | **SEO & Content Marketing Lead** | Builds the content hub ('Do I need a visa for…', '[City] for first-timers') and makes it citable by AI search. | 07 | SK-01, SK-12, SK-13, SK-24, SK-37, SK-38, SK-39 |
| MKT-04 | **Social Media & Creator Partnerships Manager** | Runs short-form video series and the micro-creator program on TikTok, Reels and YouTube. | 02, 07 | SK-06, SK-13, SK-33, SK-37, SK-38, SK-40, SK-43 |
| MKT-05 | **Lifecycle & CRM Marketer** | Owns fare-alert email and push, onboarding, free-to-paid conversion, renewal and 'plan your next trip' journeys. | 07 | SK-11, SK-21, SK-29, SK-33, SK-34, SK-38, SK-42 |
| MKT-06 | **PR & Communications Lead** | Runs the annual First-Time Traveler Fear Index, explainers when entry rules change, and crisis communications. | 07, 08 | SK-01, SK-02, SK-05, SK-12, SK-15, SK-37, SK-38, SK-44 |

## Part 2 — Skills and the agents that use them

### Research & analysis

| ID | Skill | What it covers | Used by |
|---|---|---|---|
| SK-01 | **Web research & source verification** | Finds current information, prefers official sources, cross-checks figures and marks anything unverified. | BIZ-01 Engagement Lead / Orchestrator; BIZ-03 Market Research Analyst; BIZ-04 Customer Insights Researcher; BIZ-05 Competitive Intelligence Analyst; BIZ-06 Travel Industry & Distribution Expert; DOM-01 Destination & Local Experiences Expert; DOM-02 Entry Requirements & Traveler Safety Expert; DOM-04 Flight Deals & Fare Expert; LEG-01 Travel Regulatory Counsel; LEG-02 Consumer Protection & Advertising Counsel; LEG-03 Privacy & Data Protection Counsel; MKT-03 SEO & Content Marketing Lead; MKT-06 PR & Communications Lead; FIN-04 Accounting & Tax Advisor |
| SK-02 | **Travel statistics analysis** | Reads and interprets NTTO, State Dept passport, OTA and survey data, and keeps series that measure different things apart. | BIZ-03 Market Research Analyst; BIZ-04 Customer Insights Researcher; BIZ-02 Business Strategist; FIN-03 Fundraising & Investor Relations Advisor; MKT-06 PR & Communications Lead |
| SK-03 | **Market sizing (TAM/SAM/SOM)** | Builds and updates top-down and bottom-up market estimates with stated assumptions. | BIZ-03 Market Research Analyst; BIZ-02 Business Strategist; FIN-01 CFO / Financial Modeler; FIN-03 Fundraising & Investor Relations Advisor |
| SK-04 | **Competitor tracking & feature comparison** | Maintains the competitor list and matrix, tracks pricing and launches, and assesses threats. | BIZ-05 Competitive Intelligence Analyst; BIZ-02 Business Strategist; BIZ-08 Product Manager; FIN-02 Pricing & Monetization Strategist; MKT-01 Brand Strategist |
| SK-05 | **Survey & interview design** | Writes unbiased surveys and interview guides, and analyzes results by persona. | BIZ-04 Customer Insights Researcher; TEC-05 UX / UI Designer; BIZ-08 Product Manager; MKT-06 PR & Communications Lead |
| SK-06 | **Persona & jobs-to-be-done mapping** | Keeps the six personas current and maps each traveler fear to a product feature. | BIZ-04 Customer Insights Researcher; BIZ-08 Product Manager; TEC-05 UX / UI Designer; MKT-01 Brand Strategist; MKT-04 Social Media & Creator Partnerships Manager; DOM-01 Destination & Local Experiences Expert |

### Strategy & product

| ID | Skill | What it covers | Used by |
|---|---|---|---|
| SK-07 | **Business model & strategy evaluation** | Compares business models (affiliate, partner booking, merchant of record) on revenue, risk and regulatory weight. | BIZ-01 Engagement Lead / Orchestrator; BIZ-02 Business Strategist; BIZ-06 Travel Industry & Distribution Expert; FIN-01 CFO / Financial Modeler; LEG-01 Travel Regulatory Counsel |
| SK-08 | **Product roadmap & prioritization** | Scopes the MVP, writes requirements and ranks features by value, effort and risk. | BIZ-08 Product Manager; BIZ-02 Business Strategist; TEC-01 Solutions Architect; TEC-05 UX / UI Designer |
| SK-09 | **Synthesis & executive briefing** | Combines inputs from several experts into a clear recommendation with trade-offs for the consultant or board. | BIZ-01 Engagement Lead / Orchestrator; BIZ-02 Business Strategist; FIN-01 CFO / Financial Modeler; FIN-03 Fundraising & Investor Relations Advisor; LEG-05 Insurance & Risk Manager |

### Travel domain

| ID | Skill | What it covers | Used by |
|---|---|---|---|
| SK-10 | **Travel distribution & affiliate economics** | Knows how OTAs, GDS/NDC, host agencies, metasearch and affiliate networks work, including commission rates and cookie terms. | BIZ-06 Travel Industry & Distribution Expert; BIZ-07 Partnerships & Business Development Lead; TEC-02 Travel API & Integrations Engineer; FIN-02 Pricing & Monetization Strategist; DOM-04 Flight Deals & Fare Expert |
| SK-11 | **Fare analysis & deal scoring** | Judges whether a fare is a real deal for a route and season, and explains it in plain language. | DOM-04 Flight Deals & Fare Expert; TEC-02 Travel API & Integrations Engineer; TEC-03 AI / ML Engineer; MKT-05 Lifecycle & CRM Marketer |
| SK-12 | **Entry requirements & travel-advisory monitoring** | Tracks passport, visa, UK ETA, EU EES/ETIAS, State Dept advisories, STEP and CDC guidance, and flags changes. | DOM-02 Entry Requirements & Traveler Safety Expert; OPS-03 Content Operations & Editorial QA Lead; OPS-02 Traveler Support & Emergency Escalation Lead; MKT-03 SEO & Content Marketing Lead; MKT-06 PR & Communications Lead; TEC-03 AI / ML Engineer |
| SK-13 | **Destination curation (touristy vs. off-the-path)** | Selects and vets places, writes first-timer guides and applies responsible-travel rules. | DOM-01 Destination & Local Experiences Expert; OPS-03 Content Operations & Editorial QA Lead; MKT-03 SEO & Content Marketing Lead; MKT-04 Social Media & Creator Partnerships Manager |
| SK-14 | **Survival-language curriculum design** | Builds trip-specific phrase packs, pronunciation practice and native-speaker review workflows. | DOM-03 Language Learning Specialist; TEC-03 AI / ML Engineer; OPS-03 Content Operations & Editorial QA Lead |
| SK-15 | **Traveler emergency & crisis response** | Follows the playbooks for lost passports, cancellations, medical issues and unrest, and knows when to hand off to a human. | OPS-02 Traveler Support & Emergency Escalation Lead; OPS-01 Operations Manager; DOM-02 Entry Requirements & Traveler Safety Expert; MKT-06 PR & Communications Lead; LEG-05 Insurance & Risk Manager |

### Technical

| ID | Skill | What it covers | Used by |
|---|---|---|---|
| SK-16 | **System architecture & multi-provider design** | Designs scalable systems with abstraction layers and fallbacks so no single supplier is critical. | TEC-01 Solutions Architect; TEC-02 Travel API & Integrations Engineer; TEC-04 Full-Stack & Mobile Engineer; TEC-07 Security & Privacy Engineer |
| SK-17 | **Travel API integration** | Integrates Duffel, affiliate, lodging, eSIM, insurance and tour APIs, including caching and error handling. | TEC-02 Travel API & Integrations Engineer; TEC-01 Solutions Architect; TEC-04 Full-Stack & Mobile Engineer |
| SK-18 | **LLM application engineering & guardrails** | Builds AI assistants with citations to official sources, safety guardrails, human escalation and cost control. | TEC-03 AI / ML Engineer; TEC-01 Solutions Architect; OPS-02 Traveler Support & Emergency Escalation Lead; BIZ-01 Engagement Lead / Orchestrator |
| SK-19 | **Web, mobile & offline app development** | Builds web, iOS and Android apps, offline content and push notifications. | TEC-04 Full-Stack & Mobile Engineer; TEC-01 Solutions Architect; TEC-05 UX / UI Designer |
| SK-20 | **Accessible UX & UI design** | Designs calm, low-anxiety flows that meet WCAG and suit older users. | TEC-05 UX / UI Designer; BIZ-08 Product Manager; MKT-01 Brand Strategist |
| SK-21 | **Product analytics & experimentation** | Sets up event tracking, dashboards, A/B tests and funnel and cohort analysis. | TEC-06 Data & Analytics Engineer; MKT-02 Growth & Performance Marketer; MKT-05 Lifecycle & CRM Marketer; BIZ-08 Product Manager; FIN-02 Pricing & Monetization Strategist |
| SK-22 | **Security, privacy engineering & PCI** | Protects sensitive traveler data, handles access control and incident response, and minimizes PCI scope. | TEC-07 Security & Privacy Engineer; TEC-01 Solutions Architect; LEG-03 Privacy & Data Protection Counsel |

### Operations

| ID | Skill | What it covers | Used by |
|---|---|---|---|
| SK-23 | **Customer support operations** | Designs support tiers, staffing, help-desk tooling, response-time targets and quality checks. | OPS-02 Traveler Support & Emergency Escalation Lead; OPS-01 Operations Manager |
| SK-24 | **Editorial standards & content freshness** | Maintains style guides, fact-check workflows and 'last verified' refresh schedules. | OPS-03 Content Operations & Editorial QA Lead; DOM-01 Destination & Local Experiences Expert; DOM-02 Entry Requirements & Traveler Safety Expert; DOM-03 Language Learning Specialist; MKT-03 SEO & Content Marketing Lead |
| SK-25 | **Content moderation & fake-review detection** | Reviews user content, verifies contributors and enforces community rules. | OPS-04 Trust & Safety / Community Moderator; LEG-02 Consumer Protection & Advertising Counsel |
| SK-26 | **Vendor & contractor management** | Sources, contracts, pays and evaluates freelancers, local experts and outside service providers. | OPS-01 Operations Manager; OPS-05 People & Talent Partner; DOM-01 Destination & Local Experiences Expert; OPS-03 Content Operations & Editorial QA Lead; LEG-04 Corporate, Contracts & IP Counsel |
| SK-27 | **Hiring & org design** | Plans the team by phase, writes job descriptions, sets compensation bands and designs the interview process. | OPS-05 People & Talent Partner; BIZ-01 Engagement Lead / Orchestrator; FIN-01 CFO / Financial Modeler |

### Finance

| ID | Skill | What it covers | Used by |
|---|---|---|---|
| SK-28 | **Financial modeling & unit economics** | Builds P&L, burn, runway, CAC/LTV, ARPU and break-even models with scenarios. | FIN-01 CFO / Financial Modeler; FIN-02 Pricing & Monetization Strategist; FIN-03 Fundraising & Investor Relations Advisor; MKT-02 Growth & Performance Marketer; BIZ-02 Business Strategist |
| SK-29 | **Pricing & subscription design** | Designs tiers, trials, annual vs. monthly plans and price tests, and accounts for app-store fees. | FIN-02 Pricing & Monetization Strategist; BIZ-08 Product Manager; MKT-05 Lifecycle & CRM Marketer |
| SK-30 | **Fundraising & investor materials** | Prepares the pitch deck, data room and cap table scenarios, and runs investor updates. | FIN-03 Fundraising & Investor Relations Advisor; FIN-01 CFO / Financial Modeler; BIZ-02 Business Strategist |
| SK-31 | **Accounting, tax & revenue recognition** | Handles bookkeeping, sales tax on digital goods, and affiliate and subscription revenue recognition. | FIN-04 Accounting & Tax Advisor; FIN-01 CFO / Financial Modeler |

### Legal & risk

| ID | Skill | What it covers | Used by |
|---|---|---|---|
| SK-32 | **Travel regulatory compliance** | Applies seller-of-travel laws, ARC/IATAN rules, DOT advertising and refund rules, and travel-insurance referral licensing. | LEG-01 Travel Regulatory Counsel; LEG-05 Insurance & Risk Manager; BIZ-06 Travel Industry & Distribution Expert; OPS-01 Operations Manager |
| SK-33 | **Consumer protection & advertising law** | Applies FTC Act Section 5, endorsement guides, the fake-reviews rule, junk-fee total pricing, ROSCA and state auto-renewal laws, CAN-SPAM and TCPA. | LEG-02 Consumer Protection & Advertising Counsel; MKT-02 Growth & Performance Marketer; MKT-04 Social Media & Creator Partnerships Manager; MKT-05 Lifecycle & CRM Marketer; FIN-02 Pricing & Monetization Strategist; OPS-04 Trust & Safety / Community Moderator |
| SK-34 | **Privacy law compliance** | Applies CCPA/CPRA and other state privacy laws, COPPA and GDPR; writes notices and handles data-subject requests. | LEG-03 Privacy & Data Protection Counsel; TEC-07 Security & Privacy Engineer; TEC-06 Data & Analytics Engineer; MKT-05 Lifecycle & CRM Marketer |
| SK-35 | **Contract drafting & review** | Drafts and reviews ToS, partner and affiliate agreements, contributor IP assignments and vendor contracts. | LEG-04 Corporate, Contracts & IP Counsel; LEG-01 Travel Regulatory Counsel; LEG-02 Consumer Protection & Advertising Counsel; BIZ-07 Partnerships & Business Development Lead |
| SK-36 | **Risk assessment & insurance** | Maintains the risk register (likelihood × impact), early-warning metrics and insurance coverage. | LEG-05 Insurance & Risk Manager; BIZ-01 Engagement Lead / Orchestrator; BIZ-02 Business Strategist; OPS-01 Operations Manager; FIN-01 CFO / Financial Modeler |

### Marketing & growth

| ID | Skill | What it covers | Used by |
|---|---|---|---|
| SK-37 | **Brand positioning & voice** | Applies the brand promise and a warm, plain-English tone to every touchpoint. | MKT-01 Brand Strategist; MKT-03 SEO & Content Marketing Lead; MKT-04 Social Media & Creator Partnerships Manager; MKT-06 PR & Communications Lead; OPS-02 Traveler Support & Emergency Escalation Lead |
| SK-38 | **Copywriting & content creation** | Writes guides, landing pages, scripts, emails and ad copy in the brand voice. | MKT-03 SEO & Content Marketing Lead; MKT-04 Social Media & Creator Partnerships Manager; MKT-05 Lifecycle & CRM Marketer; MKT-06 PR & Communications Lead; DOM-01 Destination & Local Experiences Expert; MKT-01 Brand Strategist |
| SK-39 | **SEO & AI-search optimization** | Handles keyword research, programmatic pages, schema markup and getting cited by AI answer engines. | MKT-03 SEO & Content Marketing Lead; TEC-04 Full-Stack & Mobile Engineer; TEC-06 Data & Analytics Engineer |
| SK-40 | **Social video & creator program management** | Plans short-form series, recruits and briefs creators, and manages disclosures and revenue share. | MKT-04 Social Media & Creator Partnerships Manager; MKT-01 Brand Strategist |
| SK-41 | **Paid acquisition & attribution** | Runs Meta, TikTok, Google and Apple Search Ads tests, tracks attribution and enforces the LTV:CAC 3:1 rule. | MKT-02 Growth & Performance Marketer; TEC-06 Data & Analytics Engineer |
| SK-42 | **Lifecycle, email & push marketing** | Builds onboarding, fare-alert, trial-conversion, renewal and referral journeys. | MKT-05 Lifecycle & CRM Marketer; MKT-02 Growth & Performance Marketer; DOM-04 Flight Deals & Fare Expert |
| SK-43 | **Partnership development & negotiation** | Prospects, pitches and negotiates B2B2C, affiliate and co-marketing deals. | BIZ-07 Partnerships & Business Development Lead; BIZ-06 Travel Industry & Distribution Expert; MKT-04 Social Media & Creator Partnerships Manager; FIN-03 Fundraising & Investor Relations Advisor |
| SK-44 | **PR, media relations & crisis communications** | Writes press releases, runs the data-led PR survey, handles rapid-response explainers and crisis statements. | MKT-06 PR & Communications Lead; MKT-01 Brand Strategist; OPS-02 Traveler Support & Emergency Escalation Lead; BIZ-01 Engagement Lead / Orchestrator |

## Part 3 — Most-shared skills (build these first)

Skills used by the most agents give the biggest return when built once and reused.

| Skill | Number of agents |
|---|---|
| SK-01 Web research & source verification | 14 |
| SK-06 Persona & jobs-to-be-done mapping | 6 |
| SK-12 Entry requirements & travel-advisory monitoring | 6 |
| SK-33 Consumer protection & advertising law | 6 |
| SK-38 Copywriting & content creation | 6 |
| SK-02 Travel statistics analysis | 5 |
| SK-04 Competitor tracking & feature comparison | 5 |
| SK-07 Business model & strategy evaluation | 5 |
| SK-09 Synthesis & executive briefing | 5 |
| SK-10 Travel distribution & affiliate economics | 5 |
| SK-15 Traveler emergency & crisis response | 5 |
| SK-21 Product analytics & experimentation | 5 |
| SK-24 Editorial standards & content freshness | 5 |
| SK-26 Vendor & contractor management | 5 |
| SK-28 Financial modeling & unit economics | 5 |
| SK-36 Risk assessment & insurance | 5 |
| SK-37 Brand positioning & voice | 5 |

Every other skill is used by 2–4 agents.

## Suggested build order

1. **Core advisory group (build first):** BIZ-01 Engagement Lead, BIZ-02 Business Strategist, FIN-01 CFO, LEG-01 Travel Regulatory Counsel, BIZ-08 Product Manager, MKT-02 Growth Marketer. These cover the board-level risks in [08 Risks](08-risks.md): CAC vs. LTV, AI commoditization and guidance accuracy.
2. **MVP build group:** TEC-01, TEC-02, TEC-03, TEC-04, TEC-05, DOM-02, DOM-03, DOM-04, OPS-03.
3. **Launch group:** MKT-01, MKT-03, MKT-04, MKT-05, LEG-02, LEG-03, OPS-02, BIZ-07.
4. **Scale group:** everyone else, added as the business moves to partner booking (see the phases in [05 Permits & Licenses](05-permits-and-licenses.md)).
