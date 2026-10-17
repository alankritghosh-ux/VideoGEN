# Executive decision memo — what a small, software-first company in Bengaluru should build

Prepared 2026-10-17 from the Phase B–D research notes in `research/research_notes/Venture scale opportunity search/` and the Phase D deliverables in this folder. Binding frame: `decision_brief.md` §9. This memo stands alone; the other artifacts hold the detail.

## 1. One-page executive summary

**The question.** What can a 21-year-old, software-only, limited-capital founder in Bengaluru build today that customers will pay for, that can be validated with accessible evidence, and that becomes more valuable or more defensible as the company operates?

**The answer.** **VALIDATE FIRST — F2, a C&I open-access settlement and procurement engine for industrial consumers, Karnataka first.** Not "Build": no finalist has verified willingness-to-pay, and F2's recurring value is unmeasured until the first experiment runs.

**Ranked top three (post-red-team, 0–100):** 1. F2 C&I open-access settlement & procurement engine — **71**. 2. F1 ISTS connectivity / grid-access intelligence — **63**. 3. F3 FDRE/BESS dispatch, availability-compliance and bid optimisation — **60**. Un-red-teamed hypotheses sit below after a ~10-point haircut.

**Three strongest reasons F2 could succeed.** (1) The buyer is numerous, local and publicly listed: Karnataka SLDC's wheeling-and-banking lists cover 556 generators / 4,924 MW and ≈922 consumer organisations, Infosys, Wipro, Shahi Exports and Biocon among them ([SLDC lists](https://kptclsldc.in/WBUpload.aspx), VF count / EST dedupe). (2) Settlement errors are documented: Karnataka runs two banking regimes at once, its additional surcharge swung ₹0.82 → ₹0.40/kWh in March 2026 with a captive exemption, and MERC ordered refunds of unlawful wheeling charges in Maharashtra ([MERC order](https://merc.gov.in/wp-content/uploads/2025/06/Final-Order-in-Case-Nos.-131-of-2024.pdf), VF). (3) The data arrives as routine customer exports, so there is no licence risk and validation is a 12-month backtest the customer can check.

**Three strongest reasons it could fail.** (1) Four incumbents touch the job — Tata Power Trading, Customized Energy Solutions, Open Access Exchange ("zero upfront"), BridgeIT (claims 1M+ bills) — and may bundle settlement at no visible fee. (2) Over-billing may be episodic and corrected in bulk by regulators (23 consumers' bills corrected in one order), leaving a small, lumpy per-consumer pool. (3) No Indian fee benchmark for OA bill audit or advisory exists; every price in the commercial model is a hypothesis.

**Next experiment.** F2-A (technical, ≤14 days, ≈₹0): recompute 12 months of bills and statements for 3–5 Karnataka OA/group-captive consumers under KERC rules. **Pass:** median recoverable ≥1.5% of annual OA bill and ≥₹5 lakh/yr at ≥3 of 5 sites. **Fail:** <0.5% at 4 of 5. In parallel F2-B: 10 interviews; **pass** = ≥4 of 10 already pay someone or lost money to a dispute/lapse in 24 months **and** ≥3 accept a success-fee audit.

**Seven-day action.** Encode the Karnataka rules from primary orders, build the ~900-row target list, contact 55 organisations through public routes, ship a synthetic proof pack, and email CTUIL for F1 permission.

**Rejected.** Satellite analytics as the wedge: the horizontal-analytics category has a near-100% failure or fire-sale record and Indian EO buyers are government or free-pilot corporates. Standalone solar forecasting / QCA: commoditised at an implied ₹4k–33k/MW/yr, pooling beats model accuracy, and a software-only entrant cannot pool without becoming the registered QCA.

## 2. How to read the evidence

**Five evidence classes** are used throughout, as in the notes: **VF** verified fact (primary document read directly); **IC** independently corroborated (two independent sources, or a primary quoted verbatim by a secondary); **EST** estimate (vendor blog, association claim, database output, or the researcher's arithmetic); **HYP** hypothesis / inference; **UNK** unknown after a real search. `opportunities_beyond_thesis.md` uses an older scheme (P-OFF/P-CO ≈ VF; S-AN/S-PRESS ≈ IC when two sources agree; V-BLOG/TRX-EST ≈ EST; INF ≈ HYP). Where a number matters, its class is stated beside it.

**Raw versus red-teamed scores.** A "raw" score is the coordinator's desk judgment on the ten weighted criteria (brief §2). A "red-teamed" score has survived a hostile counter-evidence pass (`red_team_counterevidence.md` for F1–F3; `red_team_cluster2.md` for H4/H5/H6). The three cluster-2 hypotheses lost 9–14 points each when examined, so every remaining raw score is shown with an expected haircut of about 10 points and no un-red-teamed hypothesis is ranked above a red-teamed finalist. Scores are judgments, not measurements; none of the 16 has a measured willingness-to-pay.

**The other eight artifacts.**
- `research_notes/.../decision_brief.md` — the binding frame: what the research established, weights, finalists, rejections, experiments, final ranking.
- `research-ledger.csv` — every load-bearing claim with class, source URL, date and the decision it informs.
- `competitive-landscape.csv` — 70 rows of incumbents, analogues and substitutes with evidence.
- `competitive-landscape-gaps.md` — where the gaps are real (unmet need) and where they are not (unattractive market, inaccessible data, difficult deployment, customer indifference).
- `commercial-model.xlsx` — assumptions, unit economics, 10/100/1,000-customer scenarios, path to first revenue, sensitivity, operational constraints, 40 sources.
- `commercial-model-summary.md` — the workbook's base-case numbers and caveats in prose.
- `technical-validation-plan.md` — shared ingestion engine, per-finalist pipelines, the experiments with thresholds, legal constraints per data source.
- `30-day-execution-plan.md` — days 1–7 in detail, weeks 2–4, gates at 30/60/90 days, budget, metrics, what not to do.

## 3. The thesis test — what survives if software is nearly free

The founder's original thesis was that satellite intelligence and solar forecasting could be defended by data, track record and calibration. `commoditization_and_failures.md` tested eight moat hypotheses against the 2019–2026 record.

| # | Moat hypothesis | Verdict | Decisive case |
|---|---|---|---|
| 1 | Proprietary data | Mixed; weak for software-only assembly | Kpler paid ~$241M for Spire's maritime data ([Spire](https://spire.com/press-release/spire-global-completes-sale-of-maritime-business-debt-eliminated/), VF) — but Gro, Orbital Insight and Descartes assembled third-party data and died or fire-sold |
| 2 | Validated prediction record | Weak | Zillow Offers: $540–569M write-downs when its record met transaction risk ([SEC 10-Q](https://www.sec.gov/Archives/edgar/data/1617640/000161764021000087/z-20210930.htm), VF) |
| 3 | Distribution | Supported as a moat; weak as something the founder has | Planet ≈82% government revenue; every acquirer of an analytics startup (DNV, Kpler, Uplight, Enverus) owned distribution ([Planet 10-K](https://www.sec.gov/Archives/edgar/data/1836833/000119312526119957/pl-20260131.htm), VF) |
| 4 | Workflow integration | Mixed | Core-workflow position holds; general agents with native connectors thin out integration moats (HYP) |
| 5 | Trust / accountability | Supported for incumbents; weak for a new entrant | DNV (a certifier) bought Solcast ([DNV](https://www.dnv.com/news/2023/dnv-expands-solar-forecasting-expertise-with-the-acquisition-of-solar-data-specialist-solcast-238386/), VF) |
| 6 | Transaction access | Mixed | The analytics vendor is acquired by the transaction owner, never the reverse |
| 7 | Customer-specific calibration | Mixed → weak | Calibration runs on the customer's SCADA; ERCOT deliberately runs multiple vendors ([ERCOT POB 1054](https://www.ercot.com/files/pobs/2022/08/31/Power_Operations_Bulletin_1054.doc), VF) |
| 8 | Network effects / switching costs / regulation | Weak / mixed | ClimateAi ($38M) wound down Aug 2026 despite climate-disclosure demand ([AgFunderNews](https://agfundernews.com/climate-resilience-platform-climateai-winds-down-operations), IC) |

The model layer is free: ECMWF's AI weather forecasts are open and operational, Open-Meteo data is CC-BY, zero-shot time-series models beat statistical baselines. What is not free is ground truth tied to a specific asset or customer, and the legal right to use it.

**Implications for product design, applied to F2.** (i) **Price per outcome** — success fee on verified recoveries first, subscription second; an outcome fee displaces no budget line. (ii) **Contractual rights to customer exhaust** — every pilot agreement lets anonymised bill/settlement pairs and dispute outcomes be retained; this corpus is the one asset a frontier model cannot reproduce. (iii) **Design for the position that owns the transaction** — traders and developers bundle settlement because they hold the transaction; F2 enters as the independent consumer-side auditor and aims, over time, at the settlement/scheduling-agent position, not a dashboard. (iv) **Compile a public-record time series nobody else has** — versioned KERC/TNERC/MERC rule libraries with effective dates, joined to refund orders, so a recomputation is reproducible under the rule in force on the billing date and the rule a commission later imposed.

## 4. Ranked opportunities

| Rank | # | Hypothesis | Score | Status | Expected after haircut | One-line status |
|---|---|---|---|---|---|---|
| 1 | H2 / F2 | C&I open-access settlement & procurement engine | 71 | red-teamed | 71 | Validate first; Karnataka |
| 2 | H1 / F1 | ISTS connectivity / GNA intelligence | 63 | red-teamed | 63 | 7-day probe + CTUIL permission request; no build |
| 3 | H3 / F3 | FDRE/BESS dispatch, compliance, bid optimisation | 60 | red-teamed | 60 | 2027–28 watch item |
| 4 | H16 | Public DSM-exposure benchmark / QCA scorecard from RPC files | 69 raw | added late, not red-teamed | ~59 | Optional one-week energy-side probe |
| 5 | H13 | Plant-level RE forecasting / QCA services | 60 | data scores revised; commercial verdict stands | ~50 | Rejected as a product; component only |
| 6 | H7 | PM Surya Ghar vendor operations | 62 raw | not red-teamed | ~52 | Rejected: portal-feature risk, no moat |
| 7 | H8 | Agri-lending / crop-insurance satellite verification | 59 raw | not red-teamed | ~49 | Rejected: SatSure holds the bank channel |
| 8 | H9 | Municipal property-tax change detection | 58 raw | not red-teamed | ~48 | Rejected: tender-driven, field-survey heavy |
| 9 | H10 | DISCOM smart-meter accounting / theft-lead scoring | 56 raw | not red-teamed | ~46 | Rejected: right problem, wrong buyer |
| 10 | H6 | CCTS compliance engine | 55 | red-teamed | 55 | Rejected for 2026; 2027+ option |
| 11 | H11 | Satellite construction-progress verification for lenders | 53 raw | not red-teamed | ~43 | Rejected: fee pool tiny |
| 12 | H12 | Transmission vegetation / encroachment analytics | 53 raw | not red-teamed | ~43 | Rejected: no Indian buyer evidence |
| 13 | H4 | CBAM embedded-emissions engine | 53 | red-teamed | 53 | Rejected: obligation sits with EU importer |
| 14 | H5 | Energy-project development intelligence (records + EO) | 53 | red-teamed | 53 | Rejected: sold at ₹3,390/yr already |
| 15 | H14 | Parametric weather-risk scoring | 51 raw | not red-teamed | ~41 | Rejected: philanthropy-funded premiums |
| 16 | H15 | Solar O&M performance analytics | 48 raw | not red-teamed | ~38 | Rejected: consolidated by IBM/Reliance/Nextracker |

**F2 (71).** The only finalist whose buyer is numerous, local and reachable from a public list, whose data arrives as routine exports, and whose value is a signed ₹ figure. C&I open access reached 18.7 GW by end-FY2024 with 37,558 GEOA approvals ([JMK/IEEFA](https://ieefa.org/sites/default/files/2024-12/Impact%20of%20Green%20Energy%20Open%20Acess_Dec2024.pdf), VF); Karnataka holds ≈23% of India's 32.9 GW of OA solar ([pv magazine citing Mercom](https://www.pv-magazine.com/2026/05/22/india-has-now-32-9-gw-of-operational-pv-capacity-under-private-ppas/), IC). The red team cut WTP 4→3 and competition 3→2; it still ranks first.

**F1 (63).** Hard rupee pain — bank-guarantee encashments of ₹3.1–11.5 Cr per developer and a compensation rate of ₹1,612/MW/day ([CTUIL](https://ctuil.in/uploads/assets/178645696705Compensation%20charges%20as%20per%20CERC%20order%20dtd%2003-08-2026%20to%20be%20uploaded%20on%20website.pdf), VF) — but CTUIL already publishes the queue as a filterable 636-row table, its margin PDFs are stamped RESTRICTED, its copyright policy forbids reproduction without permission ([policy](https://ctuil.in/copyright-policy), VF), and the backlog is demand-side: 40,420 MW of LoAs produced 2,338 MW of PPAs and CERC is releasing ~15.7 GW by order ([CERC 11/SM/2026](https://cercind.gov.in/2026/orders/11-SM-2026.pdf), VF). What survives is prediction and alerting under a CTUIL data arrangement.

**F3 (60).** The highest penalty density — FDRE shortfall at 1.5× tariff; 95% availability, 85% RTE and indigenous-EMS clauses in MSEDCL's 4 GWh award ([Energetica](https://www.energetica-india.net/news/oriana-bsl-engineering-armee-infotech-gk-energy-among-winners-in-msedcl-4-gwh-bess-auction), VF). But the ≈12.6 GWh operational fleet is ~80% merchant and owned by two conglomerates, Tier-2 awards are DISCOM-dispatched with 2027–28 SCODs, IEX data is "personal, non-commercial" ([IEX terms](https://www.iexindia.com/terms-of-uses), VF), and DSM escalation is stayed for petitioners and deferred to 2027 bids / 2029 COD ([CERC notification 208](https://cercind.gov.in/regulations/208-notification.pdf), VF). Pace Digitek (Bengaluru, 375 MW awarded) is the design partner when the time comes.

**H16 (69 raw → ~59).** Added late when Regional Power Committee weekly files were verified by download to carry 15-minute `available_capacity, sch_total, act_total` and charges per ISTS RE entity (SRPC zip: 122 entities × 672 blocks — [SRPC](https://srpc.gov.in/wp-content/uploads/2026/10/051026.zip), VF), reversing the earlier "no public ground truth" finding. A DSM-exposure benchmark is buildable in a week at ≈₹0, but plants already receive their own statements; it may work better as the lead-generation front end for F3 than as a paid product.

**Attractive but rejected.**
- *Plant-level forecasting / QCA (H13).* Implied fees ₹4k–33k/MW/yr; incumbents profitable on scale (REConnect FY26 revenue ₹72.1 Cr, PAT ₹4.28 Cr; Manikaran FY25 ₹35.9 Cr, PAT ₹7.38 Cr, 22 staff — EST); pooling cuts penalties 30–65% at X=100 — an organisational act beats model accuracy ([Prayas](https://energy.prayaspune.org/images/pdf/CERC_suo-motu_proposal_on_X_for_RE-DSM_Prayas_comments_17-10-25.pdf), VF).
- *Satellite construction monitoring for lenders (H11).* Fee pool 0.01–0.02% of capex (brief §2); no Indian lender pilot found; NHAI already mandates contractor drone video ([Governance Now](https://www.governancenow.com/news/gn-connect/drone-survey-mandatory-for-all-national-highways-projects), VF).
- *Transmission vegetation (H12).* Zero Indian satellite-vegetation contracts found; the budget line is ₹/km drone LiDAR ([RECPDCL RFP](https://www.recpdcl.in/assets/data/pdf/LiDAR_survey_RFP2.0_23062026.pdf), VF).
- *CBAM (H4).* Only the EU importer is obligated and may lawfully declare on default values; SAP now ingests supplier Excel on the importer side ([EUR-Lex 2025/2083](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32025R2083), VF; [SAP](https://news.sap.com/2026/06/sap-introduces-cbam-declarants-solution/), VF); 69 Indian carbon-accounting firms compete (EST).
- *CCTS (H6).* No CCC had traded as of 7 Oct 2026 and the compensation formula is keyed to an average price that does not exist; six provisional verifiers for ~490 plants ([BEE letter](https://www.beeindia.gov.in/WriteReadData/L45218/6065726594257663.pdf), VF); PAT's 56% non-compliance is the precedent.
- *Property-tax GIS (H9).* Tender-driven, field-survey heavy, incumbents and state remote-sensing centres; first meeting to revenue up to two years ([Outlook Business](https://www.outlookbusiness.com/magazine/why-indias-space-tech-start-ups-are-stuck-in-a-low-revenue-orbit), VF).
- *DISCOM analytics (H10).* ₹90,000 Cr+ annual loss and 41–57% booking rates are real ([ISGF](https://asiacleanenergyforum.adb.org/wp-content/uploads/2026/06/AI-Powered-ATC-Loss-Monitoring.pdf), IC), but the buyer is an L1-tendering DISCOM or a confidential AMISP contract — wrong buyer for this founder.
- *Surya Ghar vendor ops (H7).* MNRE already ships status dashboards and opened portal API access in June 2026; design-software incumbents (Arka360 at ₹46k/yr) can add the module (EST); no moat.
- *Solar O&M (H15).* Consolidated: Prescinto burned ~3× revenue before selling to IBM ([pv magazine](https://www.pv-magazine-india.com/2024/10/15/ibm-acquires-prescinto-for-renewables-asset-performance-management/), VF); large IPPs build forecasting in-house.

## 5. The final recommendation — F2 in seventeen parts

### 5.1 What to build
A monthly **settlement recomputation engine** for one consumer–generator pair in one state (Karnataka first): the bill recomputed line by line under the regime that binds the pair, a discrepancy list with ₹, confidence and clause citation, a 15-minute banking/lapse statement, and a signed-off "recoverable amount" memo. A **procurement optimiser** (group captive vs third-party vs rooftop vs DISCOM/DERS; banking share; term) is the second module, built only after F2-A passes.

### 5.2 Exact initial customer
Karnataka open-access and group-captive C&I consumers with 1–20 MW of contracted demand, in the BESCOM, CESC and MESCOM lists first (within ~40 km of Bengaluru), then the GESCOM/HESCOM steel-cement-textile belt. The SLDC spreadsheet shows 556 generators / 4,924 MW under wheeling-and-banking agreements (358 legacy WBA / 3,725 MW; 198 GEOA / 1,199 MW) and the consumer PDFs yield ≈922 distinct organisations ([SLDC](https://kptclsldc.in/WBUpload.aspx), VF count / EST dedupe). Segments and named organisations, all from those lists (`f2_f3_commercial_facts.md` Table F2) unless stated; public routes are the company website contact page and company LinkedIn page, never individual contacts:

| Segment | Organisations | Why |
|---|---|---|
| Multi-installation garments / textiles | Shahi Exports (≥6 HT installations across BESCOM/CESC); Himatsingka Seide (EHT, Hassan) | Multi-generator pairings = heaviest monthly reconciliation |
| Pharma / biotech | Biocon (Hosur Road and SEZ installations) | Continuous process load; banking-sensitive |
| IT services | Infosys (40 MW via Infosys Green Forum, BESCOM and CESC RR numbers); Wipro / Wipro GE Healthcare (≥6 RR numbers) | Large, multi-entity, legacy-regime exposure |
| Auto components | Toyota Tsusho India (Bidadi); Sansera Engineering (Bengaluru/Tumakuru) | Bidadi cluster; listed companies |
| Hospitals | Narayana Hrudayalaya (2+ RR numbers); Manipal Hospitals | 24×7 loads; standby and banking exposure |
| IT-park owners | Bagmane, RMZ (three entities), Manyata (BESCOM, CESC and MESCOM lists) | REIT-style multi-building loads |
| Airport | Bangalore International Airport Ltd | Large single-site EHT |
| GESCOM belt (Tier B) | Kirloskar Ferrous (Koppal), Kalyani Steels (Ginigera), Mukand (Hospet), Orient Cement | Heavy industrial loads; later wave |

Routes to statements, not customers: the largest generators in the lists (Clean Max, Atria, Greenergy, Radiance, AMP Solar) and the industry associations KASSIA, Peenya Industries Association and the FKCCI energy committee.

### 5.3 The painful problem and the current alternative
Every month the consumer receives an ESCOM bill, a generator invoice, SLDC/ESCOM energy-accounting statements and banking statements, and must reconcile them under rules that change every tariff order. Karnataka runs two banking regimes at once — annual 2% in-kind for 2018–2023 applicants, subject to a pending Supreme Court matter ([SolarQuarter 2023](https://solarquarter.com/2023/08/17/kerc-issues-vital-directive-on-wheeling-charges-and-banking-for-renewable-power-projects/), VF), and monthly banking with no carry-forward, 8% "or as decided", standby at 125% under the 2025 regulations ([Renewable Watch](https://renewablewatch.in/2025/04/25/karnataka-announces-open-access-regulations-2025/), IC). The additional surcharge fell from ₹0.82/kWh to ₹0.40 from March 2026 against BESCOM's request for ₹1.65 on a ₹1,028 Cr stranded-cost claim, and does not apply to captive drawal ([SolarQuarter](https://solarquarter.com/2025/10/14/bescom-seeks-kerc-approval-to-levy-%e2%82%b91-65-per-unit-additional-surcharge-on-open-access-consumers-in-karnataka/), VF). Today a plant engineer reconciles in a spreadsheet, the generator's "free" advisory audits its own invoices, or a trader bundles it with trading ([Tata Power](https://tatapower.com/what-we-do-nav/energy-services/power-trading-2), VF). Disputes are resolved by petition, slowly.

### 5.4 First product and boundaries
First product: a 12-month recomputation on exported files, delivered as a variance table and a two-page proof pack, with expert review before anything is claimed. It will **not** do: a dashboard or UI; live integration with any ESCOM or SLDC; forecasting, scheduling or QCA work; satellite imagery; Maharashtra or Tamil Nadu rules before three Karnataka sites are recomputed; dispute filing without a tariff expert's sign-off and a CA's signature on the memo; and it will not become free advisory for a generator's sales.

### 5.5 Why the customer would pay
A success fee of 20–25% of verified recoveries (the audit-firm structure, consistent with Zenatix's historical 8–12%-of-bill pricing — [Business Today](https://www.businesstoday.in/magazine/features/story/the-power-people-84654-2017-08-04), IC, dated) displaces no budget line and needs no credibility for money. Then ₹2–5 lakh/site/yr for monthly settlement and procurement optimisation, inside what plants already pay for a one-off energy audit (₹1.5–8 lakh, [Elion](https://elion.co.in/energy-audit-in-india-complete-guide-to-bee-compliance-process-cost-savings-2026/), EST). Status: the structure is HYP; the recoverable pool is UNK until F2-A; the only paid-for OA anchor is JMK's ₹2 lakh report ([JMK](https://jmkresearch.com/open-access-ci-re-market-in-india/), VF).

### 5.6 Evidence supporting the opportunity
- Market: 18.7 GW C&I OA by FY2024, 46% CAGR, 37,558 GEOA approvals — VF; "30 GW" by Dec 2025 — EST (vendor blog).
- Reachability: 556 generators / 4,924 MW; ≈922 consumer organisations with RR numbers and generator pairings in public SLDC lists — VF / EST.
- Error evidence: MERC-ordered MSEDCL wheeling refunds 2025 — VF; APTEL 366/2017, 23 consumers' bills corrected — single-source; Uttarakhand and Delhi CSS refund cases — single-source; Karnataka dual banking regime — VF.
- Recurring driver: annual surcharge determinations (₹0.82 → ₹0.40 vs ₹1.65 asked) — VF/IC; TN banking re-litigated at least four times — VF; banking moving to 15-minute / capacity-based settlement in Punjab, Maharashtra, Gujarat — VF/IC.
- Pool sizing: BESCOM-area OA energy ≈6,230 MU/yr back-solved from the petition; a ₹0.10/kWh error rate would be ₹62 Cr/yr across BESCOM alone — EST.
- Buyers pay for OA data: JMK ₹2 lakh report — VF; advisory "payback under 6 months" — EST (developer blog).

### 5.7 What can be built without privileged access
Everything in the first experiment: the Karnataka rule library from public KERC orders; the target list from public SLDC lists; the bill parser and 15-minute accounting engine tested on a synthetic site; the recomputation itself on customer exports. No ESCOM, SLDC, exchange or weather feed is needed. What public data cannot show is whether Karnataka ESCOMs/SLDC issue 15-minute accounting and banking statements as exports — the first design-partner conversation must settle it.

### 5.8 Technical architecture and key unknowns
A document-to-ledger engine, not an "AI product": Fetcher (hashed artefacts) → Extractor (deterministic PDF/XLSX parsing; LLM fallback only on rejected pages, flagged for human check) → Normaliser (entities, units, 96-block dates; no LLM at runtime) → Rule library (one effective-dated module per regulation version) → append-only Ledger (entity, attribute, value, valid_from/to, artefact, verifier) → Explain layer. LLMs draft rule code and explanations; they are never the source of a number that reaches a bill. Pipeline: bill → line items; 15-minute injection and drawal → block table; **regime identification** (legacy WBA vs 2025 vs GEOA; captive vs third-party; voltage; term) before any arithmetic; banking state machine; charge engine; discrepancy list. The procurement optimiser is a small MILP on an open-source solver. Tests: golden files per document type, rule tests to ≤₹1 per line, energy-conservation property tests. CPU-only; <₹3,000/month for several pilots (EST). Key unknowns: statement availability as exports; FY26–28 wheeling and SLDC ₹/kWh charges in unparsed tariff-order annexures (UNK); population error frequency (UNK); which claims an ESCOM will entertain (expert).

### 5.9 Competitors and market entry
Tata Power Trading (energy accounting, DSM and OA reconciliation, group-captive consultancy; no pricing — VF); Customized Energy Solutions (bill-settlement verification is a staffed line — VF); Open Access Exchange ("end-to-end OA compliance", "zero upfront", developer-subsidised — VF); BridgeIT (bill-validation ERP claiming 1M+ bills, 100+ DISCOMs — EST); developers' free pre-signing advisory. None publishes a fee; none was found to productise consumer-side monthly reconciliation; no OA settlement software vendor appears among 205 Indian companies in the relevant database feeds (EST). **Entry:** as the independent, outcome-priced auditor on the consumer's side, tied to no generator or trader — the trader audits trades it arranged and the generator audits its own invoice; the independent position is open (HYP). Interview question 3 asks what the incumbent bundle actually covers.

### 5.10 Why it could survive improving frontier models — and where it would not
Survives: the parse layer is reproducible by any model, but the binding interpretation of a tariff order is a commission decision (the MERC 2021 billing-methodology proceeding and the APTEL 2018 case settled the netting order), so the curated rule library with outcome history, the corpus of bill/settlement pairs and dispute outcomes per ESCOM under contractual data rights, and accountability (a CA-signed memo the customer takes to the DISCOM) are not obtainable from public data. Would not survive: if the value is only arithmetic on the order text — a plant engineer with a general model and the KERC order could recompute a bill; if an ESCOM or SLDC ships a self-service reconciliation portal; or if the business never moves from audit practice to the settlement-agent position, in which case it is an hourly services firm — profitable but slow, as the forecasting incumbents show.

### 5.11 Obtaining the first three customers from Bengaluru with no reputation
Per `30-day-execution-plan.md`: (1) build the ~900-row target list from the SLDC lists and tier it (Tier A = multi-installation consumers within 40 km); (2) reach them through public routes only — website contact pages, company LinkedIn pages, a free member briefing offered to KASSIA, Peenya Industries Association and the FKCCI energy committee on "checking open-access bills under the 2025 regulations", and the five largest generators as a route to statements; (3) offer a success-fee audit: free recomputation of 12 months of bills, nothing owed unless money is found, NDA and deletion on request; (4) lead with the proof pack — synthetic first, then the first real site anonymised — and the expert's name on the variance review, not a pitch. Targets: 55 organisations contacted in week 1, 125 by day 30; ≥3 interviews and ≥1 real site recomputed by day 14; 5 statement sets by day 30. Fallbacks: read bills on-site; ask for 3 months first; accept redacted sets.

### 5.12 Proposed pricing and economics
From `commercial-model.xlsx` (base scenario; every price is a hypothesis inspired by a cited anchor): ARPA ₹5.63 lakh/yr (SaaS ₹4.5 lakh on 1.5 sites + ₹1.1 lakh recurring fees); year-1 revenue per account ₹11.25 lakh including a ₹6.75 lakh one-time audit fee; cost to acquire and onboard ₹63,600; payback 1.4 months on steady-state margin (18.4 months in the conservative case); LTV/CAC 68×.

| Scenario | 10 customers | 100 | 1,000 | Reach flag |
|---|---|---|---|---|
| Conservative | ₹16.3 lakh | ₹1.63 Cr | ₹16.3 Cr | 1,000 exceeds the 900-org Karnataka segment; 100 needs 11% penetration |
| Base | ₹66.4 lakh | ₹6.64 Cr | ₹66.4 Cr | 1,000 needs 67% of a 1,500-org segment |
| Upside | ₹2.84 Cr | ₹28.4 Cr | ₹284 Cr | 1,000 needs 33% of a 3,000-org segment |

Base EBITDA at 100 customers ₹6.1 Cr. Path to first revenue on a ₹10 lakh budget: first invoice month 5, first cash month 7, 4.5 paying customers at month 12, cumulative burn ₹11.9 lakh, lowest cash ₹1.87 lakh in month 10. Sensitivity: payback stays under 4 months across 0.5–1.5× price and 5–15% win rate — economics are not the risk; reach, incumbent bundling and the unmeasured recoverable % are. **Margin caveat:** the workbook's 97.7% "gross margin" is a contribution margin after data, compute and support hours only; delivery labour (tariff expert, CA sign-off) sits in opex, so true gross margin will be lower — estimate 60–80% at 100 customers (HYP). Operations: 100 customers need ≈3.5 delivery FTE (225 statement sets/month, three state libraries); 1,000 need ≈32 FTE and carry ≈₹4.5 Cr/yr of sign-off liability on ₹225 Cr of claimed recoveries at a 2% misstatement rate.

### 5.13 Strongest reasons it could fail
1. Incumbents bundle settlement at no visible fee once a consumer asks (TPTCL, CES, OAE, BridgeIT) — medium likelihood, high impact.
2. Statements not obtainable as exports — the likeliest gate failure; high likelihood, fatal if unmitigated.
3. Over-billing episodic and corrected in bulk by regulators; per-consumer pool below 0.5% of bill — medium.
4. Rule changes mid-pilot (KERC FY27 surcharge; legacy banking before the Supreme Court; MERC capacity-based banking) — high likelihood, medium impact; also the recurring demand.
5. An engine error produces a false claim and burns the first customer — medium/high; no claim leaves without expert sign-off.
6. Founder bandwidth and credibility at listed-company vendor onboarding (4–8 weeks, HYP).
7. It stays a Karnataka audit practice and never becomes an engine or a settlement agent.

### 5.14 Cheapest experiment that could invalidate the thesis
**F2-A** (≤14 days after data receipt; ≈₹0 compute; ≈₹25–50k expert review if paid): obtain 12 months of bills, generator invoices, SLDC/ESCOM accounting and banking statements and 15-minute meter data from 3–5 Karnataka consumers; identify the regime; recompute; blind expert review; agreed recoverable ₹, split "overcharge recoverable from ESCOM/generator" vs "avoidable lapse/standby/DERS loss". **Pass:** median ≥1.5% of annual OA bill **and** ≥₹5 lakh/yr at ≥3 of 5 sites. **Fail:** <0.5% at ≥4 of 5 — the recurring value is bookkeeping; re-scope to procurement optimisation or stop. **Inconclusive:** <3 complete sites, or discrepancies the expert cannot adjudicate — extend 14 days on travel-only spend; <3 sites by day 44 = fail on access. It shows money exists and the engine finds it; it does not show willingness to pay (F2-B) or recoverability in practice.

**Recovery-channel condition (adopted from the red-team dissent in `red-team-review.md`).** Count toward the pass threshold only amounts recoverable through an administrative channel inside the founder's runway: ESCOM bill correction, generator credit note, or an existing commission order that already covers the error class. Amounts recoverable only through fresh litigation (the APTEL 366/2017 route took roughly 18 months) are reported separately and do not carry a success fee. If the administrative-channel share alone fails the 1.5% / ₹5 lakh threshold, treat F2-A as a fail even when the gross figure passes. The same split applies to the Day-30 gate in 5.16.

### 5.15 The next seven days (from `30-day-execution-plan.md`; ≈₹6,000 cash, ~60 founder hours)
- **Day 1 (Mon 19 Oct):** create `rules/karnataka/` with one effective-dated, source-cited file per charge; download KERC OA Regulations 2025, the 17 Aug 2023 directive, the 31 Mar 2026 DERS order and the 27 Mar 2025 tariff order; build the PDF-to-text pipeline; encode the first six rules (two banking regimes, surcharge with captive exemption, standby 125%, wheeling at 25% of transmission charges, CSS as EST); register a domain and email.
- **Day 2:** send the CTUIL permission email; scrape the 636-row effective-connectivity table and 2023–2026 grant PDFs as a private research copy; start the F2 target list from the SLDC lists (~900 rows tagged by ESCOM, RR count, pairings, captive flag, WBA end date).
- **Day 3:** write the 15-question interview script (no pitching before Q13); draft the one-page outreach note; tier the list (40 Tier-A names); list public routes.
- **Day 4:** outreach wave 1 to 25 Tier-A organisations; write to the three associations; parse the CTUIL grant lists into a panel.
- **Day 5:** settlement engine v0 with unit tests per rule; synthetic proof pack for a 5 MW BESCOM HT consumer showing the three plausible errors (surcharge on captive drawal, wrong banking regime, standby above 125%).
- **Day 6:** F1-A model (AUC for effective-within-12-months, pass ≥0.70); draft mutual NDA and data-handling terms; week-1 metrics.
- **Day 7:** review replies, book interviews for days 8–14; outreach wave 2 (30 sent, including the five largest generators); week-1 note; decide on the expert retainer from week 3.

### 5.16 Milestones and go/no-go gates
**Day 30 (17 Nov 2026).** F2-A as in 5.14. F2-B: ≥4/10 pay someone or report a dispute/lapse loss in 24 months **and** ≥3 accept a success-fee audit = pass; <2 and none accept = fail; otherwise 10 more interviews via associations by day 44. F1-A0: written permission (even conditional) = keep F1 as a later module, no build before day 90; refusal or silence after two follow-ups = F1 dead as a product. F1-A: AUC ≥0.70 = skill; below = aggregation only, kill. **Stop if:** both F2 tests fail; or F2-B fails regardless of F2-A (money found, nobody will pay to find it); or <2 sites' statements after 110+ messages and three association requests (unreachable without a channel partner). Budget to day 30 ≈₹1.43 lakh.

**Day 60 (17 Dec 2026).** ≥2 signed success-fee letters and ≥1 claim filed = pass (file claims; start the Maharashtra library on the MERC refund precedent); 0 signed = stop. Any invoice triggers the incorporation decision; incorporate only if ≥2 letters are signed and a counterparty needs an entity. Karnataka rule coverage complete. **Stop if:** no signed letter, or the first claim is rejected on a ground the rule library got wrong and the expert confirms it was foreseeable.

**Day 90 (16 Jan 2027).** ≥₹3 lakh invoiced or ≥₹10 lakh verified recoverable under signed letters = pass; <₹1 lakh invoiced and <₹5 lakh verified = stop or re-scope. Rules usable in 2–3 states; ≥1 site on the monthly settlement run — none means it is an audit practice, decide if acceptable. Raise only with 5+ paying sites, a channel producing statements without cold outreach, and a credible path to ₹1 Cr ARR; otherwise stay bootstrapped. No F1 build and no F3 work before day 90 under any outcome. Budget to day 90 ≈₹4.7–4.85 lakh of the assumed ₹10 lakh.

### 5.17 The five most important unanswered questions
1. Do Karnataka ESCOMs / SLDC issue 15-minute accounting and banking statements to consumers as exports, in what format? (Gates F2-A; UNK.)
2. What is the recoverable pool — overcharge versus avoidable loss — as a share of the OA bill across a population of sites, not litigated cases? (F2-A; UNK.)
3. Will consumers accept a success-fee audit and then ₹2–5 lakh/site/yr, when no Indian OA audit fee is published and "zero upfront" advisory is the norm? (F2-B; UNK.)
4. What do the incumbent bundles cover — does Tata Power Trading sell settlement without trading, does BridgeIT handle OA banking logic, what does Open Access Exchange do after signing? (Interview Q3; UNK.)
5. Which claims will an ESCOM entertain in practice, and how will KERC's FY27 surcharge determination, the Supreme Court matter on legacy banking and MERC's capacity-based banking change the rule library mid-pilot? (Expert review; UNK.)

## 6. Decision

**VALIDATE FIRST — F2, C&I open-access settlement and procurement engine, Karnataka first; F1 limited to a zero-cost probe plus the CTUIL permission request; F3 a 2027–28 watch item; satellite analytics and standalone forecasting rejected as entry wedges.** It becomes **Build** when F2-A and F2-B both pass at day 30 and at least two success-fee letters are signed by day 60 with one claim filed. It becomes **Reject** if F2-B fails (fewer than two of ten pay anyone today and none accepts a success-fee audit) regardless of the money F2-A finds, or if fewer than two sites' statements can be obtained after 110+ messages and three association requests.

## 7. Ledger of key numbers

| # | Number | Value | Class | Source |
|---|---|---|---|---|
| 1 | Karnataka W&B generators under agreement (09.07.2024) | 556 / 4,924 MW | VF | [KPTCL SLDC](https://kptclsldc.in/WBUpload.aspx) |
| 2 | Distinct Karnataka approved OA/W&B consumer organisations | ≈922 | EST (dedupe of VF lists) | [KPTCL SLDC](https://kptclsldc.in/WBUpload.aspx) |
| 3 | Karnataka additional surcharge FY26 → from Mar 2026 (not on captive drawal) | ₹0.82 → ₹0.40/kWh | IC | [Mercom](https://mercomindia.com/karnataka-halves-additional-surcharge-for-open-access-power) |
| 4 | BESCOM stranded-cost claim behind the ₹1.65/kWh request | ₹1,028.29 Cr/yr | VF | [SolarQuarter](https://solarquarter.com/2025/10/14/bescom-seeks-kerc-approval-to-levy-%e2%82%b91-65-per-unit-additional-surcharge-on-open-access-consumers-in-karnataka/) |
| 5 | Karnataka legacy banking vs 2025 regime | 2% annual in-kind vs monthly, no carry-forward, 8% "or as decided", standby 125% | VF / IC | [SolarQuarter 2023](https://solarquarter.com/2023/08/17/kerc-issues-vital-directive-on-wheeling-charges-and-banking-for-renewable-power-projects/); [Renewable Watch](https://renewablewatch.in/2025/04/25/karnataka-announces-open-access-regulations-2025/) |
| 6 | C&I OA capacity end-FY2024; GEOA approvals | 18.7 GW; 37,558 | VF | [JMK/IEEFA](https://ieefa.org/sites/default/files/2024-12/Impact%20of%20Green%20Energy%20Open%20Acess_Dec2024.pdf) |
| 7 | MERC-ordered MSEDCL refund of unlawful wheeling charges | 2025 orders exist | VF (exists; not parsed) | [MERC](https://merc.gov.in/wp-content/uploads/2025/06/Final-Order-in-Case-Nos.-131-of-2024.pdf) |
| 8 | Only paid OA-data anchor | JMK report ₹2 lakh + GST | VF | [JMK](https://jmkresearch.com/open-access-ci-re-market-in-india/) |
| 9 | F2-A pass threshold | median ≥1.5% of OA bill and ≥₹5 lakh/yr at ≥3 of 5 sites | HYP (threshold) | `decision_brief.md` §7 |
| 10 | F2 base ARPA / year-1 revenue / payback | ₹5.63 lakh / ₹11.25 lakh / 1.4 months (18.4 conservative) | HYP (workbook) | `commercial-model-summary.md` |
| 11 | F2 base revenue at 10 / 100 / 1,000 customers | ₹66.4 lakh / ₹6.64 Cr / ₹66.4 Cr | HYP (workbook) | `commercial-model-summary.md` |
| 12 | Budget to day 30 / day 90 | ≈₹1.43 lakh / ≈₹4.7–4.85 lakh | EST | `30-day-execution-plan.md` |
| 13 | F1 cost-of-problem: BG encashments; compensation rate | ₹3.1–11.5 Cr per developer; ₹1,612.15/MW/day | IC / VF | [CTUIL](https://ctuil.in/uploads/assets/178645696705Compensation%20charges%20as%20per%20CERC%20order%20dtd%2003-08-2026%20to%20be%20uploaded%20on%20website.pdf) |
| 14 | Forecasting incumbents' scale | REConnect FY26 ₹72.1 Cr / PAT ₹4.28 Cr; Manikaran FY25 ₹35.9 Cr / PAT ₹7.38 Cr, 22 staff | EST (filings via database) | `energy_software_india_forecasting.md` Q5 |
| 15 | Public per-plant 15-minute ground truth (ISTS) | SRPC weekly zip: 122 entities × 672 blocks | VF | [SRPC](https://srpc.gov.in/wp-content/uploads/2026/10/051026.zip) |

Dissent note: none on ranking, weights or thresholds. The one addition carried from the execution plan is the overcharge-versus-avoidable-loss split inside F2-A, which the day-30 re-scope decision needs.
