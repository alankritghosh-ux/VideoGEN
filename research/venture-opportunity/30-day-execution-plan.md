# 30-day execution plan — F2 "Validate First", F1 probe, F3 watch

Prepared 2026-10-17 under the frame fixed in `research_notes/Venture scale opportunity search/decision_brief.md` §7. Week 1 starts Monday 2026-10-19; Day 30 = 2026-11-17, Day 60 = 2026-12-17, Day 90 = 2027-01-16. Amounts in ₹; "est." = my estimate, not a figure from the notes. Owners: **F** = founder; **E** = part-time tariff/regulatory expert or CA on retainer (optional, from Week 3, cost est.). The AI coding agent is a tool, not an owner.

## 1. Objective and the decision

Spend 30 days and under ₹1.5 lakh to produce two evidence-backed verdicts. **Verdict 1 — go/no-go on F2 pilots:** can 12 months of a Karnataka C&I open-access consumer's bills, SLDC/ESCOM energy-accounting and banking statements be recomputed under KERC tariff orders and the 2025 OA Regulations to find recoverable money ≥1.5% of the annual OA bill and ≥₹5 lakh/yr at ≥3 of 5 sites (F2-A), and will ≥4 of 10 consumers say they already pay someone for settlement or lost money to a dispute/lapse in 24 months, with ≥3 accepting a success-fee audit (F2-B)? Pass on both means paid pilots in Days 31–60. **Verdict 2 — kill/keep F1:** does CTUIL give written permission to reuse its published connectivity data commercially (F1-A0), and does a simple model on the 2023–2026 grant lists predict "effective within 12 months" with AUC ≥0.70 (F1-A)? Either failure kills F1 as a product and leaves the parser as an internal research tool. F3 gets no work: it is a 2027+ watch item tied to merchant-storage rules and the IEX data licence (red_team_counterevidence.md Q5–Q6).

## 2. Days 1–7

Cash for the week ≈₹6,000 (domain, cloud, printing, local travel); everything else is founder time (~60 hours).

### Day 1 — Mon 19 Oct: regulatory-document ingestion core (Karnataka)

| # | Action | Time | Output | Cost |
|---|---|---|---|---|
| 1 | Create the repo and `rules/karnataka/`: one versioned rule file per charge (wheeling, transmission, CSS, additional surcharge, banking, standby, SLDC operating charge, under-utilisation, relinquishment) with `effective_from/to`, `source_url`, `applies_to` (legacy WBA vs 2025 regime; captive vs non-captive; ESCOM; voltage). | 2 h | Rule schema | ₹0 |
| 2 | Download the primary documents: KERC OA Regulations 2025 (monthly banking, no carry-forward, 8% banking "or as decided", standby 125%, relinquishment = 3 months of charges — https://renewablewatch.in/2025/04/25/karnataka-announces-open-access-regulations-2025/ ), the 17 Aug 2023 directive (legacy annual 2% in-kind banking for 2018–2023 applicants — https://solarquarter.com/2023/08/17/kerc-issues-vital-directive-on-wheeling-charges-and-banking-for-renewable-power-projects/ ), the 31 Mar 2026 DERS order ( https://solarquarter.com/2026/04/02/kerc-extends-discounted-energy-rate-scheme-till-fy28-eases-open-access-rules-for-consumers-in-karnataka/ ) and the KERC tariff order of 27 Mar 2025 (FY26–FY28; f2_f3_commercial_facts.md notes it was never parsed). | 2 h | `docs/raw/` with hashes, dates | ₹0 |
| 3 | Build the PDF-to-text pipeline (layout-preserving, page-level provenance, table fallback); run on the four documents; flag pages needing hand-checks. | 3 h | Text + tables with page refs | ₹0 |
| 4 | Encode the first six rules from the text: banking (two regimes); additional surcharge ₹0.82/kWh FY26 → ₹0.40/kWh from Mar 2026, not on captive drawal ( https://solarquarter.com/2025/10/14/bescom-seeks-kerc-approval-to-levy-%e2%82%b91-65-per-unit-additional-surcharge-on-open-access-consumers-in-karnataka/ ); standby 125%; wheeling at 25% of normal transmission charges ( https://www.mercomindia.com/wheeling-charges-karnataka-five-fold ); CSS (only ~₹0.60/unit from a vendor blog — mark EST until the tariff order gives it). | 2 h | 6 rule files with source lines | ₹0 |
| 5 | Register a domain and professional email; set up a drive with folder-per-site and an access log. | 0.5 h | Working email | ₹1,500 (est.) |

### Day 2 — Tue 20 Oct: CTUIL permission email; scrape the queue; start the target list

| # | Action | Time | Output | Cost |
|---|---|---|---|---|
| 1 | Send the CTUIL permission email (text below) to the address on CTUIL's published contact page ( https://www.ctuil.in/ ); never guess an address. Diary a follow-up for Day 12. | 0.5 h | Email logged | ₹0 |
| 2 | Scrape the "Connectivity to be Made Effective" table (636 rows, filters, PDF/XLS export — https://ctuil.in/connectivity-effective-list ) and the GNA status page ( https://ctuil.in/nswsapi/gna ); store raw responses with timestamps. **Private research copy only; nothing is republished before permission** ( https://ctuil.in/copyright-policy ). | 3 h | `data/ctuil/effective_list_*.csv` | ₹0 |
| 3 | Download 2023–2026 PDFs: monthly "Details of Connectivity granted under GNA" tables (e.g. https://www.ctuil.in/uploads/assets/175747971577July%2025_Main-Connectivity%20under%20GNA.pdf ), the margin files and archive ( https://ctuil.in/renewable-energy ; every page stamped RESTRICTED, some streams corrupt), the 11/SM/2026 eligible-entities list ( https://ctuil.in/uploads/assets/178963420036Final%20List%20of%20eligible%20entities%20as%20per%2011SM2026_rev%2001.pdf ) and the compensation determination ( https://ctuil.in/uploads/assets/178645696705Compensation%20charges%20as%20per%20CERC%20order%20dtd%2003-08-2026%20to%20be%20uploaded%20on%20website.pdf ). | 2 h | ~40 PDFs catalogued | ₹0 |
| 4 | Start the F2 target list from the Karnataka SLDC W&B lists ( https://kptclsldc.in/WBUpload.aspx : BESCOM list 2,417 rows / 202 IPPs; CESC 435; MESCOM 229; ≈922 distinct consumer organisations; IPP sheet 556 IPPs / 4,924 MW with WBA dates, terms, captive flags). Tag each organisation with ESCOM, RR-number count, generator pairings, captive flag, WBA end date (renewal = regime switch). | 3 h | `targets_karnataka.csv` (~900 rows) | ₹0 |

**CTUIL email (sent as an individual; no claims about a company, customers or credentials):**

> Subject: Request for written permission to reuse published connectivity data (Copyright Policy)
>
> Dear Sir/Madam,
>
> I am an independent software developer based in Bengaluru. I am studying whether the connectivity and GNA information CTUIL publishes on ctuil.in can support an analytics and alerting service for renewable-energy and storage developers (for example, estimated time to effective connectivity, and alerts when margins, cluster declarations or eligible-entity lists change).
>
> CTUIL's Copyright Policy states that website contents may not be reproduced partially or fully without due permission from CTUIL, and the bay-wise and substation-wise margin files carry a "RESTRICTED" classification. Before going further I would like to ask, in writing:
>
> 1. Whether CTUIL permits use of the following published materials as inputs to a commercial analytics service, with source acknowledgement: the "Connectivity to be Made Effective" list, the monthly "Details of Connectivity granted under GNA" tables, the solar/non-solar-hour access and margin declarations, RE cluster declarations, and the eligible-entity lists under Petition 11/SM/2026.
> 2. Whether the answer differs between (a) verbatim reproduction of tables and (b) derived outputs such as estimates, summaries and change alerts that cite CTUIL as the source.
> 3. Whether an application form, fee or agreement is required, and which office to address it to.
>
> At present the data is used only for private, non-commercial analysis. I will not publish or distribute any CTUIL material until I have CTUIL's written response, and I would be glad to share the results of the analysis with CTUIL.
>
> Thank you for your time.
>
> [Name], [phone], [email], Bengaluru

### Day 3 — Wed 21 Oct: interview script, outreach material, routes

| # | Action | Time | Output | Cost |
|---|---|---|---|---|
| 1 | Write the F2 interview script (below), adapted from section F of f1_customers_and_buying.md: behaviour, cost, authority, urgency; no pitching before Q13. | 2 h | `interviews/script_f2.md` | ₹0 |
| 2 | Draft a one-page outreach note: the offer (free recomputation of 12 months of OA bills under KERC rules; nothing owed unless money is found), what is needed (bills, energy-accounting and banking statements, W&B agreement, PPA charge schedule), confidentiality (NDA on request; deletion on request). No claims about team, customers or track record. | 1.5 h | `outreach/one_pager.md` | ₹0 |
| 3 | Tier the ~900 rows: Tier A = multi-installation consumers within 40 km of Bengaluru (the notes name Shahi Exports ≥6 installations, Wipro entities, Infosys/Infosys Green Forum 40 MW, Bagmane, RMZ, Manyata, Biocon, Narayana Hrudayalaya, Sansera, Toyota Tsusho, Himatsingka); Tier B = GESCOM/HESCOM steel-cement-textile belt (Kirloskar Ferrous, Kalyani Steels, Mukand, Orient Cement); Tier C = rest. Fit reasons: f2_f3_commercial_facts.md Table F2. | 2 h | 40 Tier-A names | ₹0 |
| 4 | List public routes (routes, not contacts): KASSIA, Peenya Industries Association and the FKCCI energy committee (named in decision_brief.md §7); the largest generators in the BESCOM/CESC lists (Clean Max, Atria, Greenergy, Radiance, AMP Solar) as a second route to their consumers' energy managers. Take fees and event dates from public pages only. | 1.5 h | `outreach/routes.md` | ₹0 |

**F2 interview script (30 minutes; record who answered):**

1. Walk me through last month's bill: who received the ESCOM bill, the generator invoice, the SLDC/ESCOM energy-accounting statement and the banking statement, and what did each person do with them?
2. Who reconciles the three documents — a plant electrical engineer, accounts, the generator, a trader, a consultant? How many person-hours a month?
3. What do you pay anyone outside the company for open-access work today (generator's "free" advisory, trader, consultant, CA, lawyer)? Fee per year or per engagement?
4. In the last 24 months, any dispute with the ESCOM, SLDC or generator about a bill — banking lapse, additional surcharge on captive drawal, wrong CSS, standby at 125%, under-utilisation or relinquishment charges? Amount, and how resolved?
5. How much banked energy lapsed or was settled at a lower rate in the last 12 months? Did anyone quantify it?
6. Are you on a legacy wheeling-and-banking agreement (annual 2% in-kind banking) or the 2025 regime (monthly, no carry-forward)? When does the WBA expire and what changes then?
7. Did the FY26→FY27 additional-surcharge change (₹0.82 → ₹0.40/kWh) appear correctly from March 2026? Who checked?
8. Have you compared the Discounted Energy Rate Scheme with staying on open access? Who did the analysis?
9. Who signs a vendor engagement below ₹5 lakh at your plant, from which budget, and what onboarding steps apply?
10. Any subscription data, software or audit bought for energy in the last year (energy audit, IoT monitoring, market report)? Price, approver, time to approve?
11. If a third party found money in your last 12 months of bills, how would you want it back — ESCOM refund, bill adjustment, claim against the generator? Who inside runs that claim?
12. What is the one thing about your open-access bills you cannot verify today?
13. (Only now) Here is an anonymised recomputed bill. What is wrong or missing? What would you not trust?
14. Would you hand over 12 months of bills and statements for a recomputation on a success-fee basis — a share of verified recoveries, nothing otherwise? If not, what would have to be true?
15. Who else would need to agree, and who would object?


### Day 4 — Thu 22 Oct: first outreach wave; F1 parsing

| # | Action | Time | Output | Cost |
|---|---|---|---|---|
| 1 | Outreach wave 1: 25 Tier-A organisations via published website contact routes and company LinkedIn pages (no individual contacts exist in the notes; do not scrape personal data). Ask for 30 minutes with whoever sees the OA bill. | 3 h | 25 sent | ₹0 |
| 2 | Write to KASSIA, Peenya Industries Association and the FKCCI energy committee offering a free member briefing on "checking open-access bills under the 2025 regulations". | 1 h | 3 requests | ₹0 |
| 3 | Parse the CTUIL grant-list PDFs into one panel: application ID, applicant, submission date, region, type, MW, substation, in-principle/firm dates, effective status, document date. Label "effective within 12 months of in-principle grant" from successive monthly snapshots. | 4 h | `data/ctuil/grants_panel.csv` | ₹0 |
| 4 | Parse the margin PDFs (vision fallback for corrupt pages; flag them). | 1.5 h | `data/ctuil/margins_*.csv` | ₹0 |

### Day 5 — Fri 23 Oct: settlement engine v0 and proof pack

| # | Action | Time | Output | Cost |
|---|---|---|---|---|
| 1 | Settlement engine v0: inputs = monthly injection, drawal, banked, lapsed, standby units, contract demand, captive flag, regime flag, ESCOM, voltage; outputs = expected charge per line vs billed, with the rule citation per variance. Unit-test each rule on a hand-worked example. | 5 h | `engine/` with passing tests | ₹0 |
| 2 | Proof pack v0: an anonymised recomputed bill for a synthetic 5 MW BESCOM HT consumer on the 2025 regime — first line states it is synthetic until a real site replaces it. Show the three errors the notes make plausible: additional surcharge on captive drawal, wrong banking regime, standby above 125%. | 2.5 h | `proof_pack/v0.pdf` (2 pages) | ₹500 (est.) |

### Day 6 — Sat 24 Oct: F1-A model; legal templates

| # | Action | Time | Output | Cost |
|---|---|---|---|---|
| 1 | F1-A: base rate, logistic regression (region, substation, technology, MW, in-principle-to-firm gap, cluster flag) and a tree model, time-ordered cross-validation; report AUC for effective-within-12-months and MAE in months. Pass = AUC ≥0.70 over base rate. | 5 h | `f1/results.md` | ₹0 |
| 2 | Draft a mutual NDA and data-handling terms (what is collected, where stored, who sees it, deletion on request, no onward sharing, no cross-customer use); lawyer review in Week 2. | 2 h | `legal/*_draft.md` | ₹0 |
| 3 | Fill the Week-1 metrics file (section 6). | 0.5 h | `metrics/week01.md` | ₹0 |

### Day 7 — Sun 25 Oct: review; second wave

| # | Action | Time | Output | Cost |
|---|---|---|---|---|
| 1 | Review replies; book interviews for Days 8–14; if replies <3, shorten the ask ("15 minutes, I bring a recomputed example"). | 1 h | Interview calendar | ₹0 |
| 2 | Outreach wave 2: 25 Tier-A/B organisations plus the five largest generators in the lists (a route to statements, not a customer — see §7). | 2.5 h | 30 sent | ₹0 |
| 3 | Week-1 note: rule coverage (target ≥10 Karnataka rules with source pages), F1-A result, CTUIL status, outreach counts; decide whether to start the expert retainer in Week 3. | 1 h | `notes/week01.md` | ₹0 |

## 3. Weeks 2–4

| Week | Dates | Actions | Deliverables | Owner | Budget (est.) | Risks | Milestone |
|---|---|---|---|---|---|---|---|
| 2 | 26 Oct–1 Nov | First 4–6 interviews; collect the first 12-month statement sets (target 3 sites); extend rules to transmission/SLDC charges from the 27 Mar 2025 tariff order; run the engine on site 1 and replace the synthetic proof pack; lawyer review of NDA/data terms; wave 3 (30 orgs); one in-person visit to Peenya/Bommasandra/Jigani if an association or member agrees; CTUIL follow-up on Day 12; F1-A memo with AUC and a one-page "what survives if it survives" (alerting/interpretation layer, not data resale — red_team Q6). | 4–6 interview notes; site-1 variance table; rules v1 (≥15); signed NDA template; F1-A memo | F | ₹25,000 legal + ₹3,000 travel + ₹2,000 cloud | Statements not obtainable (the likeliest failure): offer to read bills on-site; interview no-shows | ≥3 interviews; ≥1 real site recomputed by Day 14 |
| 3 | 2–8 Nov | Interviews 7–10; sites 2–4 recomputed; start E (KERC-experienced tariff expert or CA, 4–6 h/week: check every variance line against the order and say which claims an ESCOM will accept); draft the success-fee engagement letter (20–25% of verified recoveries, the audit-firm structure, consistent with Zenatix's %-of-bill precedent — https://www.businesstoday.in/magazine/features/story/the-power-people-84654-2017-08-04 ); wave 4 to Tier B by email; Tamil Nadu rule skeleton (TNERC GEOA 2025: 8% in-kind banking in the billing cycle, 14%/12-month grandfathered wind, 75% buy-back, standby 125% — https://solarquarter.com/2025/09/26/tnerc-issues-new-regulations-2025-for-green-energy-open-access-2025-in-tamil-nadu ) only if Karnataka sites ≥3. | F2-B tally; 3–4 variance tables; E's first review memo; engagement-letter draft; TN skeleton (conditional) | F, E | ₹30,000 retainer + ₹5,000 travel + ₹2,000 cloud | E disagrees with the engine on regime identification (useful — that is the hardest question); KERC's FY27 additional-surcharge determination lands mid-pilot | Site 3 recomputed; ≥7 interviews by Day 21 |
| 4 | 9–15 Nov | Site 5 recomputed; compute the F2-A statistic (median recoverable % and ₹/yr, split "overcharge recoverable from ESCOM/generator" vs "avoidable lapse/standby/DERS loss"); give each site its one-page result and ask Q14 for real; Day-30 gate memo; F1 kill/keep from the CTUIL reply (or silence) and the AUC; note the 11/SM/2026 election window closing ~mid-Nov (f1_customers_and_buying.md §C) — if F1 is kept, the only action is a private memo, not outreach; lawyer's final pass on the engagement letter. | F2-A table; F2-B tally; pilot offers to ≥3 sites; gate memo; F1 memo | F, E | ₹30,000 retainer + ₹5,000 travel + ₹2,000 cloud + ₹10,000 legal | Recoveries real but small and lumpy (red_team Q2) — the gate handles it; founder bandwidth | Day-30 gate decided on evidence |

## 4. Gates

### Day 30 (2026-11-17)

| Test | Pass | Fail | Inconclusive | Action |
|---|---|---|---|---|
| **F2-A** (5 sites × 12 months) | Median recoverable ≥1.5% of annual OA bill AND ≥₹5 lakh/yr at ≥3 of 5 | <0.5% at 4 of 5 | <3 sites obtained, or 0.5–1.5% | Pass: offer paid pilots to the 3 best sites. Fail: the recurring value is bookkeeping — re-scope to procurement optimisation (DERS vs OA, group-captive vs third-party) and re-test in 30 days, or stop. Inconclusive: extend 14 days with travel-only spend; <3 sites by Day 44 = fail on access. |
| **F2-B** (10 interviews) | ≥4/10 pay someone or report a dispute/lapse loss in 24 months AND ≥3 accept a success-fee audit | <2 and none accept | <10 interviews, or 2–3 pay but none accept | Fail: stop F2. Inconclusive: 10 more interviews via associations in Days 31–44; same pattern = stop. |
| **F1-A0** (CTUIL permission) | Written permission, even conditional (attribution, derived outputs only) | Refusal, or silence after two follow-ups | Reply asks for a formal application | Pass with F1-A pass: keep F1 as a later module; no build before Day 90. Fail: F1 dead as a product; parser stays internal. Inconclusive: file; do not build. |
| **F1-A** (skill) | AUC ≥0.70 over base rate | AUC <0.70 | Too few labelled rows | Fail: F1 is aggregation only, which CTUIL already publishes — kill. |

**Stop conditions:** both F2 tests fail; or F2-B fails regardless of F2-A (money found, nobody will pay to find it); or <2 sites' statements after 110+ messages and three association requests (unreachable without a channel partner — a different plan).

### Day 60 (2026-12-17)

| Test | Pass | Fail | Inconclusive | Action |
|---|---|---|---|---|
| Pilot conversion | ≥2 signed success-fee letters, ≥1 claim filed with an ESCOM/generator | 0 signed | 1 signed, none filed | Pass: file claims; start the Maharashtra library (MERC-ordered wheeling refunds are documented — https://merc.gov.in/wp-content/uploads/2025/06/Final-Order-in-Case-Nos.-131-of-2024.pdf ). Fail: stop. Inconclusive: 30 more days, no new fixed spend. |
| First paid revenue | ≥₹1 invoiced (advance, fixed-fee recomputation, or first recovery share) | ₹0 and no claim in process | Claim awaiting ESCOM | Pass triggers the incorporation decision. |
| Rule coverage | Karnataka complete (every charge line in the FY26–FY28 order); TN skeleton | Karnataka incomplete | — | Fail here alone = bandwidth signal: buy more of E's hours first. |
| Incorporation | Incorporate (LLP or Pvt Ltd, est. ₹25–40k) only if ≥2 letters are signed and a counterparty needs an entity | Do not | — | Invoice as an individual until then; confirm GST/TDS position with the CA. |

**Stop conditions:** no signed letter; or the first claim is rejected on a ground the rule library got wrong and E confirms it was foreseeable (the core is wrong, not the market).

### Day 90 (2027-01-16)

| Test | Pass | Fail | Action |
|---|---|---|---|
| Revenue | ≥₹3 lakh invoiced, or ≥₹10 lakh verified recoverable under signed letters | <₹1 lakh invoiced and <₹5 lakh verified | Fail: stop or re-scope. |
| Rule coverage | 2–3 states (Karnataka complete; TN or Maharashtra usable on real bills) | Karnataka only | Needed to call it an engine rather than a Karnataka consultancy. |
| Repeatability | ≥1 site using the monthly settlement run, i.e. the ₹2–5 lakh/site/yr subscription case (f2_f3_commercial_facts.md F2-Q3) | None | Fail: it is an audit practice; decide if that is acceptable. |
| Raise vs bootstrap | Raise only with 5+ paying sites, a channel producing statements without cold outreach, and a credible 12-month path to ₹1 Cr ARR; otherwise stay bootstrapped on success fees | — | Nira Energy was profitable in year one on subscriptions ( https://www.latitudemedia.com/news/how-nira-energy-is-using-software-to-unclog-the-interconnection-queue ) — records-based products can bootstrap. |
| F1 / F3 | F1 (if kept): one-page alerting-module spec, built only after F2 revenue. F3: re-read only when CERC notifies market coupling, storage charging rules finalise, or an IEX licence price is known | — | No F1 build and no F3 work before Day 90 under any outcome. |

## 5. Budget (₹)

| Line item | Days 1–30 | Days 1–90 | Notes |
|---|---|---|---|
| Cloud, domain, email, storage | 6,000 | 15,000 | est. |
| Coding-agent subscription | 8,000 | 24,000 | Tool; est. |
| Data | 0 | 0 | F2 inputs are customer exports and public regulator PDFs; no weather data needed. JMK OA report (₹2 lakh + GST) not before Day 60. IEX licence is F3-only; not bought. |
| Travel within Karnataka/TN | 10,000 | 45,000 | Bengaluru industrial areas in Days 8–30; Koppal/Ballari and Hosur/Coimbatore only after Day 30; est. |
| Expert retainer (E) | 60,000 | 1,80,000 | ₹30k/month from Week 3; est. — the notes found no fee benchmark |
| Legal (NDA, data terms, engagement letter) | 35,000 | 60,000 | est. |
| Incorporation | 0 | 25,000–40,000 | Deferred to the Day-60 gate; est. |
| Printing, association/event fees, phone | 5,000 | 20,000 | Fees from associations' public pages; est. |
| Contingency (15%) | 19,000 | 60,000 | |
| **Total** | **≈1,43,000** | **≈4,70,000–4,85,000** | ≈₹5 lakh of the assumed ₹10 lakh stays unspent at Day 90, reserved for Maharashtra travel, a second expert or a first hire if the gate passes. |

## 6. Weekly metrics (update every Sunday in `metrics/`)

| Metric | Wk1 target | Wk2 | Wk3 | Wk4 | Definition |
|---|---|---|---|---|---|
| Outreach sent (orgs) | 55 | 85 | 115 | 125 | Distinct organisations via public routes |
| Replies | 5 | 12 | 20 | 25 | Any human response |
| Interviews done | 0–1 | 5 | 8 | 10 | Full script, notes filed |
| Statement sets obtained (sites) | 0 | 1–2 | 3–4 | 5 | 12 months of bills + accounting + banking statements |
| Sites recomputed | 0 | 1 | 3 | 5 | Variance table reviewed by E |
| Recoverable ₹ found (verified) | 0 | — | — | report | Overcharge vs avoidable loss |
| Median recoverable % of OA bill | — | — | — | report | F2-A statistic |
| Pilots agreed (verbal / signed) | 0 | 0 | 1 / 0 | 3 / 1 | Success-fee letters |
| ₹ invoiced | 0 | 0 | 0 | 0 | First invoice expected Days 31–60 |
| Karnataka rules encoded with source page | 10 | 15 | 20 | all | Count in `rules/karnataka/` |
| CTUIL permission status | sent | followed up | — | decided | sent / replied / refused / silent |
| Founder hours F2 / F1 | 45 / 12 | 50 / 5 | 55 / 0 | 55 / 2 | F1 under 20% in Week 1, ~0 after |

## 7. What NOT to do

- No satellite-imagery work (rejected entry wedge; decision_brief.md §1, §7).
- No forecasting-model work: no plant-level forecasting, weather feeds or QCA tooling (commoditised; a component, not a product).
- No incorporation before the Day-60 gate; no trademark, office or hire.
- No custom deals with OA developers or generators that turn the engine into free advisory for their sales — the market's existing failure mode ( https://www.openaccessexchange.com/ ; https://www.herofutureenergies.com/blog/solar-open-access-for-commercial-industrial-consumers-india/ ). Generators are a route to statements, not a customer, this month.
- No republishing, dashboarding or sharing of any CTUIL table or margin file before written permission ( https://ctuil.in/copyright-policy ); parsed copies stay private.
- No IEX data for commercial use (terms are personal, non-commercial — https://www.iexindia.com/terms-of-uses ); nothing on F3.
- No paid datasets before Day 60; no Maharashtra/TN rule work before three Karnataka sites are recomputed.
- No dashboard or UI; outputs are a variance table and a two-page proof pack.
- No pitching before Q13; no "would you use this" questions.

## 8. Risks and mitigations

| Risk | Evidence | Likelihood / impact | Mitigation |
|---|---|---|---|
| Incumbent bundles settlement at no visible fee once a consumer asks | Tata Power Trading sells OA reconciliation and DSM settlement ( https://tatapower.com/what-we-do-nav/energy-services/power-trading-2 ); Customized Energy Solutions staffs bill-settlement verification ( https://ces-ltd.com/service/consulting-services-india/ ); Open Access Exchange "zero upfront"; BridgeIT claims 1M+ bills validated | Medium / high | Position as the independent consumer-side auditor — the trader audits trades it arranged (f2_f3_commercial_facts.md F2-Q4); success fee displaces no budget line; Q3 in every interview learns what the bundle really covers. |
| Statements not obtainable | F2-A needs 3–5 sites' exports; no individual contacts in the notes; founder has no network | High / fatal for the gate | Three routes in parallel (direct, association, generator); read bills on-site; ask for 3 months first, then 12; accept redacted sets; extend to Day 44 before failing. |
| Over-billing is episodic and corrected in bulk by regulators | APTEL 366/2017 (23 consumers corrected in one order); MERC 2021 methodology proceeding (red_team Q2) | Medium / medium | The F2-A threshold prices this in; the overcharge vs avoidable-loss split gives the procurement re-scope its data on Day 30. |
| Rule changes mid-pilot | KERC FY27 additional-surcharge determination pending; legacy banking subject to a pending Supreme Court matter ( https://solarquarter.com/2023/08/17/kerc-issues-vital-directive-on-wheeling-charges-and-banking-for-renewable-power-projects/ ); MERC capacity-based banking proposal; Gujarat ₹1.50/unit cap | High / medium (also the recurring demand) | Versioned rules with effective dates; every variance line cites its order; E confirms which claims an ESCOM entertains. |
| Court/regulator timing on the F1 side | Karnataka HC stay of DSM 2024 regs for NSEFI petitioners; Delhi HC writ on DSM 2022 Reg 8(1) pending with interim orders kept (30 Sep 2026); GNA 4th amendment still draft; 11/SM/2026 window closing ~mid-Nov (red_team Q6; f1_customers_and_buying.md §C) | — | F1 gets 7 days and an email; nothing in F2 depends on these. Do not chase the mid-Nov window — it would pull the founder into F1 sales without permission in hand. |
| CTUIL silence rather than refusal | Policy requires permission; aggregators republish in practice; enforcement unknown (red_team Q5) | High / low for F2 | Silence after two follow-ups = no product; parser stays internal. |
| Founder bandwidth and credibility (21, no reputation, not a trained engineer) | Listed-company vendor onboarding runs 4–8 weeks (f1_customers_and_buying.md §B, inference) | High / medium | Lead with the proof pack, not a pitch; E's name on the variance review; success fee removes the credibility-for-money ask; keep F1 under 20% of Week 1. |
| Engine error produces a false claim and burns the first customer | Settlement methodology is settled by commission decisions, not by reading the order (red_team Q3) | Medium / high | No claim leaves without E's sign-off; the proof pack states assumptions and regime choice; start with the cleanest error class (additional surcharge on captive drawal). |
| Data-handling incident with customer bills | Exports carry RR numbers and consumption | Low / high | Signed data terms before any upload; folder-per-site; access log; delete on request. |

**Dissent note:** none on ranking or thresholds; the only addition is the overcharge vs avoidable-loss split in F2-A, which the Day-30 re-scope decision needs.
