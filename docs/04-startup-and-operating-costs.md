# 04 — Startup & Operating Costs

> **Recommended model:** *Content + guidance + fare alerts + affiliate booking* (no merchant-of-record ticketing at launch). This avoids ARC/IATAN bonds, airline-refund liability and most seller-of-travel exposure, and keeps burn low. Add direct booking later (via Duffel or a host agency) once demand is proven.

All figures are **planning estimates in USD** for a U.S.-based startup. Ranges reflect a lean bootstrap (low) vs. a seed-funded team (high).

## 1. One-time startup costs (first ~6 months)

| Item | Lean | Seed-funded | Notes |
|---|---|---|---|
| Company formation (Delaware C-corp or state LLC), registered agent, EIN | $500 | $2,000 | Use Stripe Atlas / Clerky for C-corp if raising VC |
| Legal: ToS, privacy policy, affiliate disclosures, subscription terms, founder agreements | $2,000 | $15,000 | Travel-specific counsel recommended (see `05-permits-and-licenses.md`) |
| Trademark search + filing (1–2 classes) | $700 | $3,000 | USPTO fee ~$350/class + attorney |
| Seller-of-travel registrations (if/when needed) | $0 | $3,000–$25,000 | Only if we sell travel; CA/FL/WA/HI. Bond/trust costs may apply. Affiliate-only model likely exempt — confirm with counsel |
| Brand/design (logo, design system) | $500 | $15,000 | |
| MVP product build (web + mobile, fare alerts, checklists, language packs) | $15,000 (founder-built + freelancers) | $150,000–$300,000 | 3–6 months, 2–4 engineers |
| Initial content (50 destination guides, 20 language packs, checklists) | $5,000 | $40,000 | Freelance writers + native-speaker reviewers @ $150–$500/guide |
| Launch marketing | $5,000 | $50,000 | Creator seeding, PR, paid tests |
| **Total** | **~$29K** | **~$280K–$450K** | |

## 2. Monthly operating costs

| Category | Lean (pre-revenue) | Seed (yr 1–2) | Notes |
|---|---|---|---|
| **Payroll** | $0–$10K | $80K–$150K | See `06-staffing.md` |
| Cloud hosting (AWS/GCP/Vercel/Supabase) | $100–$500 | $2K–$8K | Fare-scanning workloads drive cost |
| **Flight data / APIs** | $0–$1K | $3K–$20K | See API section below — the most important variable cost |
| LLM / AI API usage (trip-planning assistant, translation) | $200–$1K | $3K–$15K | Scales with users; cache aggressively |
| Email/SMS/push (fare alerts) | $50–$300 | $1K–$5K | SMS is expensive — prefer push/email |
| Subscription billing (App Store/Play 15–30% cut; Stripe ~2.9% + 30¢ on web) | variable | variable | Push web checkout where allowed to avoid store fees |
| Customer support tooling (Intercom/Zendesk) | $0–$100 | $500–$2K | |
| Analytics, monitoring, error tracking | $0–$200 | $1K–$3K | |
| Insurance (GL, E&O/professional, cyber) | $150 | $500–$2K | E&O is important for advice-giving; cyber for user data |
| Legal/accounting retainer | $300 | $3K–$8K | |
| Content updates (entry rules change constantly) | $500 | $5K–$15K | |
| Marketing (paid + creators) | $1K–$3K | $20K–$80K | See `07-marketing.md` |
| **Total monthly burn** | **~$3K–$17K** | **~$120K–$300K** | |

## 3. Travel data & booking APIs (key decision)

| Option | Use | Cost model | Notes |
|---|---|---|---|
| **Affiliate/metasearch links** (Skyscanner, Kayak, Expedia, Booking.com, Travelpayouts, CJ/Impact networks) | Deep-link users to book | Free; we *earn* CPC or commission | Fastest path; no licensing burden |
| **Duffel** (NDC/GDS flight API) | Search & sell airline tickets directly | Per-order fee reported **~$2–$3 per confirmed order** plus % fees on some content/payments *(verify at duffel.com/pricing)*. Duffel's accredited agency network lets us sell **without our own ARC/IATA accreditation** | Best option for in-app booking in phase 2 |
| **Amadeus Self-Service APIs** | — | **Shut down July 17, 2026.** Enterprise contracts only now | Don't plan around it |
| **Kiwi Tequila, AirLabs, Ignav, others** | Search data, flight status | Varies; some free tiers | AirLabs/Ignav published Amadeus migration guides |
| **Google Flights** | — | No public API | Can't legally scrape at scale |
| **Hotel APIs** (Booking.com/Expedia Rapid affiliate, Hotelbeds, LiteAPI) | Lodging | Commission-based | Expedia Rapid requires approval |
| **Activities** (Viator, GetYourGuide, Klook affiliates) | Tours | ~8% commission | |
| **Frankfurter** (api.frankfurter.dev) | Currency exchange rates for budgets, price display and dollar-strength trends | **Free, no key** (open source; ECB reference rates, ~30 currencies, updated each working day) | In use by the expert team (`scripts/fx.py`). Doesn't cover some destination currencies (e.g., VND, COP, CRC, PEN), so a second source is needed for those |
| **eSIM** (Airalo, Holafly affiliate) | Connectivity | ~10–20% commission | High conversion for first-timers |
| **Travel insurance** (SafetyWing, World Nomads, Squaremouth, Faye affiliates) | Insurance | ~10–30% commission | Insurance referral may need a license in some states — see licenses doc |

## 4. Revenue model & unit economics (illustrative)

| Stream | Assumption | Revenue |
|---|---|---|
| Subscription (Premium) | $59/yr; 8% of actives convert | ~$4.70 per active user/yr |
| Affiliate per trip | ~$60–$150 per completed trip (lodging + insurance + eSIM + tours) | 25% of actives book a trip/yr → ~$15–$38 per active/yr |
| Concierge / human planning | $149–$499 per trip; 0.5% of actives | ~$1–$2.50 per active/yr |
| B2B (universities, employers, credit unions) | Licensed "first trip" program | Upside |

**Blended ARPU target:** ~$20–$45 per active user/yr.

**CAC benchmarks:** travel CAC rose ~35% from 2022→2025 (Adobe); mobile CPI ~$4.70 iOS / ~$3.70 Android (Adapty 2025); travel paid CAC per *customer* often $100–$800 (vendor estimate). **Implication:** paid acquisition alone won't work at our ARPU — we must lean on organic content, creators, community and referrals to keep blended CAC < $15 per active and **LTV:CAC ≥ 3:1**.

## 5. Break-even sketch (seed scenario)

- Burn ~$180K/month → needs ~$2.2M/yr gross margin.
- At $30 blended ARPU and ~80% gross margin → **~90K active users** to break even.
- Plausible by month 24–36 if organic growth works. Raise **$1.5M–$3M seed** for ~18–24 months runway.

## 6. Cost-control recommendations
1. Launch affiliate-only; avoid merchant-of-record risk.
2. Web-first subscription checkout to avoid 15–30% app-store fees where permitted.
3. Use AI for first-draft content + human native-speaker/local verification.
4. Cache fare data; use push/email over SMS.
5. Contract local contributors per guide rather than full-time staff.

## Sources

- [Duffel — Pricing](https://duffel.com/pricing)
- [Duffel — Accredited agency network](https://duffel.com/blog/benefits-of-using-duffel-content-services-duffels-accredited-agency-network)
- [PricingSaaS — Duffel pricing history](https://pricingsaas.com/companies/duffel)
- [PhocusWire — Amadeus to shut down self-service APIs portal](https://www.phocuswire.com/amadeus-shut-down-self-service-apis-portal-developers)
- [Amadeus — Statement on developers portal](https://amadeus.com/en/industry-messaging/statement-regarding-amadeus-for-developers-portal)
- [Ignav — Amadeus Self-Service Shutdown migration guide](https://ignav.com/docs/amadeus-self-service-shutdown)
- [AirLabs — Amadeus Self-Service API shutdown](https://airlabs.co/amadeus-self-service-api-shutdown)
- [Adapty — Customer acquisition cost benchmarks](https://adapty.io/blog/customer-acquisition-cost/)
- [Adobe — Customer acquisition and retention in an imperfect world](https://business.adobe.com/assets/pdfs/resources/sdk/customer-acquisition-and-retention-in-an-imperfect-world/customer-acquisition-and-retention-in-an-imperfect-world.pdf)
- [Rework — Customer acquisition cost in travel](https://resources.rework.com/libraries/travel-tour-growth/customer-acquisition-cost-in-travel)
- [PhocusWire — Addressing rising customer acquisition costs](https://www.phocuswire.com/addressing-rising-customer-acquisition-costs-travel)
