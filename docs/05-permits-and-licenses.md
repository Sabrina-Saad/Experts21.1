# 05 — Permits, Licenses & Regulatory Compliance

> ⚠️ **Not legal advice.** This is a research map for the team. Engage a travel-industry attorney before launch — especially before taking payment for travel or selling insurance.

The regulatory burden depends almost entirely on **which business model we run**:

| Model | Regulatory weight |
|---|---|
| **A. Content + guidance + subscription + affiliate links** (recommended launch) | Light — general business, consumer protection, privacy, affiliate disclosure, subscription/auto-renew laws |
| **B. Sell travel via a partner as agent (Duffel/host agency is ticketing agent)** | Medium — seller-of-travel registrations likely, DOT ticket-agent rules |
| **C. Merchant of record, own ARC/IATAN accreditation** | Heavy — bonds, trust accounts, refund liability, PCI scope |

## 1. General business (all models)

| Requirement | Notes |
|---|---|
| Entity formation (LLC or Delaware C-corp) | C-corp if raising venture capital |
| EIN (IRS) | Free |
| State foreign qualification | Where we have employees/offices; Florida requires out-of-state sellers of travel to be authorized with the FL Secretary of State |
| Local business license | City/county where headquartered |
| Sales tax | Subscriptions/digital services are taxable in some states — use a tax engine (Stripe Tax/Avalara) |
| Trademark | Clear name before launch (USPTO) |

## 2. Seller-of-Travel (SOT) laws — the "Big Four" (+ others)

State SOT laws are **extraterritorial**: they apply to any business selling travel **to residents of that state**, even if we are based elsewhere.

| State | Agency | Key requirements (verify current) |
|---|---|---|
| **California** | Attorney General | Register before doing business; **$100/yr per business location**; trust account or bond; Travel Consumer Restitution Fund participation; registration # displayed in ads; fees can't be paid from trust account |
| **Florida** | Dept. of Agriculture & Consumer Services (FDACS) | Annual registration (**~$300/yr** per older sources); bond/security may be required; disclosures; penalties for non-compliance |
| **Washington** | Dept. of Licensing | Registration; trust account/bond; IC exemption if contracted with a registered seller |
| **Hawaii** | Dept. of Commerce & Consumer Affairs | Registration + client trust account; **no IC exemption** |
| Others | e.g., Iowa, Nevada, Delaware, Massachusetts, Ohio, Oregon, Rhode Island, Virginia, Louisiana have registration or bonding rules of varying scope | Check list annually |

**Does a pure affiliate/content site need SOT registration?** Generally SOT laws trigger on *selling, offering for sale or arranging* travel for consideration. Pure referral/affiliate links where the supplier/OTA is the seller often fall outside — **but California's definition is broad**. Get a written opinion from counsel before Model B.

## 3. Airline ticketing (Model B / C)

| Requirement | Notes |
|---|---|
| **ARC accreditation** (U.S. agencies issuing airline tickets) | Requires bond or letter of credit (commonly **$20K+**), qualifying experience, fees; vendor estimates ~$3K+ to obtain. Avoid at launch |
| **IATAN** accreditation | U.S. equivalent of IATA accreditation; notarized application, references, training certification. Mainly for agent ID/credibility |
| **Alternative: Duffel's accredited agency network / host agency** | Sell flights using partner's accreditation — no ARC needed |
| **DOT ticket-agent rules** (14 CFR Part 399 etc.) | Full-fare advertising (total price incl. taxes/fees), baggage-fee disclosure, code-share disclosure |
| **DOT refund rule (Apr 2024)** | Ticket agents who are **merchant of record** must give prompt refunds on request when airlines cancel or significantly change flights. Confirm current compliance dates/status |

## 4. Consumer protection & advertising

| Rule | Relevance |
|---|---|
| **FTC Act §5** (unfair/deceptive practices) | All claims — "cheapest," "safe," savings claims must be substantiated |
| **FTC Endorsement Guides** (2023) | Creator/influencer and affiliate links must be clearly disclosed; no fake reviews |
| **FTC Rule on Unfair or Deceptive Fees** ("junk fees") — effective **May 12, 2025** | Covers **short-term lodging** and live-event tickets, including third-party platforms and travel agents: must show **total price** upfront. Applies if we display lodging prices |
| **FTC Fake Reviews Rule** (2024) | Bans fake/incentivized reviews — important for our "hidden gems" community content |
| **Auto-renewal / subscription laws** | FTC "Click-to-Cancel" rule was vacated by a federal appeals court in 2025, **but state laws remain** — California ARL (strictest), NY, CO, VA, etc.: clear terms, affirmative consent, easy online cancellation, renewal reminders. Also ROSCA (federal) still applies |
| **CAN-SPAM / TCPA** | Email & SMS fare alerts — opt-in, unsubscribe; TCPA requires prior express written consent for marketing texts |

## 5. Privacy & data

| Law | Notes |
|---|---|
| **CCPA/CPRA (California)** and ~20 other state privacy laws | Privacy notice, opt-out of sale/sharing, data-subject requests. Passport numbers & location = sensitive data |
| **COPPA** | Don't market to under-13s; student persona is 18+ |
| **PCI DSS** | Minimize scope by using Stripe/Duffel hosted payments |
| **GDPR** | Applies if we target EU residents or have EU staff/contributors processing data; likely minimal at launch |

## 6. Insurance referrals

Recommending/selling **travel insurance** can require a **producer license or limited-lines travel insurance license** in many states. Safer path at launch: pure affiliate referral to marketplaces (e.g., Squaremouth) without discussing specific coverage terms, or partner with a licensed agency. Confirm per-state with counsel.

## 7. Language-learning & content

- Use licensed or original content; native-speaker audio needs contributor IP assignment agreements.
- Map data, photos — license properly (Unsplash, own photography, licensed APIs).
- Health guidance (vaccines, meds) — link to CDC Travelers' Health; avoid giving medical advice.

## 8. Contributors, guides & marketplace (phase 2)

- Local guides abroad as **independent contractors** — contracts, local-law compliance, payout tools (e.g., Stripe Connect/Wise). Guiding is licensed in some countries (e.g., Italy, Greece, France for certain sites) — vet partners.

## 9. Compliance checklist by phase

**Pre-launch (Model A):** entity, EIN, ToS/privacy, affiliate disclosures, subscription terms compliant with CA ARL, CAN-SPAM, E&O + cyber insurance, trademark.

**Phase 2 (Model B):** counsel opinion on SOT; register CA/FL/WA/HI (+others as needed); DOT advertising compliance; Duffel/host-agency agreement; junk-fee total-price display.

**Phase 3 (Model C, optional):** ARC bond, trust accounts, refund operations, PCI program.

## Sources

- [California AG — Seller of Travel FAQs](https://www.oag.ca.gov/travel/reg-faqs)
- [California AG — Form JUS 8771](https://oag.ca.gov/system/files/media/jus-8771.pdf)
- [Travel Weekly (Pestronk) — Seller-of-travel requirements vary state to state](https://www.travelweekly.com/Mark-Pestronk/Seller-travel-requirements-vary-from-state-state)
- [Travel Weekly — Five states vary in rules for exemption from IC registration](https://www.travelweekly.com/Mark-Pestronk/Five-states-vary-in-rules-for-exemption-from-IC-registration)
- [Travel Weekly — Updated state regulations: who requires what](https://www.travelweekly.com/Travel-News/Travel-Agent-Issues/Updated-State-Regulations-Who-requires-what)
- [Host Agency Reviews — Travel agent license + SOT registration 2025](https://hostagencyreviews.com/blog/travel-agent-license-seller-of-travel-license)
- [ARC — Become an ARC-accredited agent](https://www2.arccorp.com/products-participation/travel-agencies/become-an-arc-accredited-agent)
- [SuretyBonds — ARC accreditation guide](https://www.suretybonds.com/guide/federal/arc-accreditation)
- [IATAN — Accreditation requirements (PDF)](https://www.iata.org/globalassets/iatan/documents/iatan-accreditation-requirements.pdf)
- [Duffel — Accredited agency network](https://duffel.com/blog/benefits-of-using-duffel-content-services-duffels-accredited-agency-network)
- [DOT — Refunds final rule (April 2024)](https://www.transportation.gov/airconsumer/refundsfinalruleapril2024)
- [DOT — Refund rule small business compliance guidance](https://www.transportation.gov/sites/dot.gov/files/2024-12/Refund%20Final%20Rule%20Small%20Business%20Compliance%20Guidance.pdf)
- [Barnes & Thornburg — FTC junk fees rule effective May 12, 2025](https://btlaw.com/en/insights/alerts/2025/ftc-finalizes-junk-fees-rule-new-pricing-disclosure-requirements-take-effect-may-12-2025)
- [Foley — FTC final junk fees rule (short-term lodging)](https://www.foley.com/insights/publications/2025/01/ftc-final-junk-fees-rule-live-event-tickets-short-term-lodging/)
