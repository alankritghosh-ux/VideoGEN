# Technical validation plan — finalists F2, F1, F3

Phase D technical-diligence deliverable, 2026-10-17. Evidence base: the Phase B–D research notes only (no new web research). Evidence classes follow the notes: **[VF]** verified fact (primary document read), **[IC]** independently corroborated, **[EST]** estimate, **[HYP]** hypothesis, **[UNK]** unknown. Where a fact is missing from the notes it is written as *not established in research; must be verified*. Finalist order follows the post-red-team ranking in `decision_brief.md` §7: **F2 (71) > F1 (63) > F3 (60)**.

## 1. Purpose and how to read this document

This document turns the three finalists into buildable, testable engineering plans and names the experiment that would most cheaply kill each one. It is written for a founder who builds with AI coding agents, on CPU-only infrastructure (a 2–4 vCPU VM class, no GPU), with limited capital (experiment budgets of ≈₹0–50k, not ₹ lakhs), and without privileged access to any grid operator, DISCOM or exchange. Every pipeline below is therefore designed so that the first experiment runs on public data or on exports a customer can hand over as files, needs no live integration, and produces a number against a stated threshold. Sections 2–5 describe the shared engine and each finalist's minimum product; §6 specifies the experiments; §7 the staged path from prototype to production; §8 fixes the energy-quantity vocabulary that the notes show is routinely confused; §9 lists what remains open. Numbers are labelled by evidence class; a number without a label is the writer's arithmetic from labelled inputs.

## 2. Shared core: regulatory-document and market-data ingestion engine

All three finalists consume the same families of documents: CERC/SERC regulations and tariff orders, CTUIL lists and margin sheets, SLDC statements and lists, and IEX price series. The core is a **document-to-ledger engine**, not an "AI product".

### 2.1 Architecture

| Layer | What it does | Implementation notes (CPU-only) |
|---|---|---|
| Fetcher | Polls source pages on a schedule, stores every retrieved artefact byte-for-byte with URL, retrieval time, HTTP headers and SHA-256 | Plain HTTP client + object store; CTUIL pages are JS-paginated (the effective-connectivity table rendered only 10 rows server-side when fetched) [VF, [f1_customers_and_buying.md]], so the fetcher needs a headless-browser path or the page's underlying request |
| Extractor | Converts PDFs/XLSX/HTML to typed rows against a per-document schema | `pdftotext -layout` reproduced the CTUIL margins table in one pass but hit 28 corrupt flate streams [VF, [CTUIL PDF](https://ctuil.in/uploads/assets/176011721061Website%20sheet_solar%20non%20solar%20margins_all.pdf)]; a vision/LLM fallback is used **only for pages the deterministic parser rejects**, and every LLM-extracted row is flagged for human verification |
| Normaliser | Resolves entity names (applicant SPVs, substations, ESCOMs), units (MW vs MWh, ₹ lakh/MW/month vs ₹/kWh), dates and time blocks (96 × 15-min) | Deterministic lookup tables with versioned alias lists; never an LLM at runtime |
| Rule library | Encodes charge formulas, bands, slabs, banking regimes, penalty clauses as code with effective-date ranges | One module per regulation version (e.g., `KERC_OA_2025`, `CERC_DSM_2024_R8_4`, `CERC_DSM_3rd_Amd_2026_R8_4A`) |
| Ledger | Append-only, versioned facts: (entity, attribute, value, valid_from, valid_to, source_artefact, extraction_method, verified_by) | A "snapshot" is a query at a point in time; a "diff" between snapshots is the alert feed |
| Explain layer | Produces human-readable explanations of a computed charge or a queue change, citing the source clause | LLM-generated text, always rendered with the clause citation and the deterministic number it explains |

### 2.2 Where LLMs belong

LLMs are used for (a) first-pass schema discovery on a new document type, (b) extraction fallback on malformed pages, (c) drafting rule-library code from a tariff order for a human to review, and (d) explaining results to a customer. They are **never the source of a number** that reaches a bill, a bid or a prediction. The red team's finding that the parse layer is reproducible by any frontier model [HYP, [red_team_counterevidence.md] Q3] means the moat, if any, is in the verified ledger and rule library, not in extraction.

### 2.3 Versioning and provenance

Every regulation, tariff order and CTUIL sheet is stored as an immutable artefact; rule modules carry the artefact hash they were written from; every output row carries the rule-module version and the input artefact hashes. This matters because the notes record repeated retroactive reversals (TN wind banking re-litigated at least four times with APTEL set-asides in 2021 and 2025 [VF/IC, [f2_f3_commercial_facts.md] F2-Q2]; MERC-ordered refunds of wheeling charges in 2025 [VF, [MERC order](https://merc.gov.in/wp-content/uploads/2025/06/Final-Order-in-Case-Nos.-131-of-2024.pdf)]; CERC restoring 2,300 MW and 400 MW of revoked connectivity [VF-sec, [SolarQuarter](https://solarquarter.com/2025/12/06/cerc-directs-restoration-of-2300-mw-renewable-connectivity-condones-delay-under-gna-regulations/)]). A recomputation must be reproducible under the rule version that was in force on the billing date and under the rule version a regulator later imposed.

### 2.4 Test strategy

- **Golden files**: for each document type, a hand-verified extraction of at least three real artefacts (one clean, one with layout drift, one with corrupt streams) checked into the repo; CI fails if extraction output changes.
- **Rule tests**: each charge formula is tested against worked examples taken from the regulation or order text and against at least one real customer bill once obtained (F2), with tolerance ≤ ₹1 per line item.
- **Snapshot tests**: the ledger diff between two consecutive CTUIL releases is replayed and compared with the alert feed produced at the time.
- **Property tests**: 15-minute energy accounting must conserve energy (injection = drawal + banked + lapsed + losses) per block and per month.

### 2.5 Legal constraints per source (from the red team)

| Source | Terms found | Consequence for design |
|---|---|---|
| CTUIL website and PDFs | "Contents of this website may not be reproduced partially or fully, without due permission from CTUIL" [VF, [copyright policy](https://ctuil.in/copyright-policy)]; margins PDF stamped "RESTRICTED" on every page [VF]; disclaimer places all liability on the user [VF, [disclaimer](https://ctuil.in/disclaimer)] | Re-publishing parsed CTUIL tables in a paid product needs written permission (gate A0, §6.4). Derived predictions/alerts are a grey area; internal use for a customer's own applications is the fallback. Enforcement practice is unknown — aggregators re-publish lists today [UNK] |
| IEX price data | "You may use the Content only for personal, non-commercial purpose"; no download/copy/extract/distribute without authorisation [VF, [IEX ToU](https://www.iexindia.com/terms-of-uses)]; 15-min DAM data from 1 Apr 2022 downloadable without login under "all rights reserved, quotation with attribution" [VF, [market snapshot](https://www.iexindia.com/market-data/day-ahead-market/market-snapshot)] | Backtests for internal validation are feasible; any commercial product using IEX series or feeds needs a licence (cost **not established in research; must be verified**) |
| CERC/SERC orders and regulations | No terms of use on CERC's site; Hindi disclaimer only [VF, [CERC](https://cercind.gov.in/)] | Lowest risk; rule library can quote clauses |
| Karnataka SLDC lists (W&B generators/consumers) | Public XLSX/PDF downloads; no terms examined [VF, [kptclsldc.in](https://kptclsldc.in/WBUpload.aspx)] | Usable for prospecting; redistribution terms **not established; must be verified** |
| Customer bills, SLDC/DISCOM statements (F2), asset telemetry (F3) | Supplied by the customer; no third-party privacy issue identified [VF, red team Q5] | Requires a data-rights clause in the pilot agreement so that anonymised bill/settlement pairs can be retained for the rule library |
| Grid-India/RLDC/SLDC terms | Sites returned HTTP 503 on all attempts [UNK] | Treat as unknown; do not build a product feature on them until read |

## 3. Finalist F2 — C&I open-access settlement and procurement engine (lead)

### 3.1 Minimum product

A monthly **settlement recomputation** for one consumer–generator pair in one state (Karnataka first), producing: (i) a line-by-line recomputed bill under the applicable regime, (ii) a list of discrepancies with ₹ value, confidence and the clause relied on, (iii) a banking/lapse statement at 15-minute granularity, and (iv) a signed-off "recoverable amount" memo. Procurement optimisation (annual sourcing plan) is the second module, not the first.

### 3.2 Data inputs and sources

| Input | Source and form | Evidence |
|---|---|---|
| DISCOM OA bill (monthly) | Customer export; MSEDCL sample itemises drawal, injection, banked and over-injected units [VF, [MSEDCL sample](https://mahadiscom.in/consumer/wp-content/uploads/2024/12/155-519_170019002163_202411-oa-print1.pdf)]; consumers "receive two separate bills" (generator + DISCOM) [VF, [OAE](https://www.openaccessexchange.com/)] | Formats for BESCOM/GESCOM/HESCOM bills **not established in research; must be obtained from a design partner** |
| Generator invoice | Customer export | Format unknown [UNK] |
| SLDC/DISCOM energy-accounting and banking statements | Customer export; Karnataka SLDC states it does "Energy Accounting" but publishes no monthly statements [VF, [kptclsldc.in](https://kptclsldc.in/)]; Delhi SLDC publishes monthly operating/transmission invoices for short-term OA [VF, [delhisldc.org](https://delhisldc.org/)]; Kerala had no 15-minute accounting for short-term OA consumers [VF-snippet, [KSEB](https://kseb.in/uploads/Downloadtemsuppy/b-17149864122140522808.pdf)] | Whether 15-minute statements are issued to Karnataka consumers as exports is the single biggest unknown for F2 |
| 15-minute meter data (ABT/AMR) | Customer export from DISCOM portal or meter reads | Availability per ESCOM **not established** |
| Tariff orders and OA regulations | KERC OA Regulations 2025 (100 kW threshold, SLDC nodal, monthly banking, no carry-forward, standby 125%, relinquishment = 3 months of charges, under-utilisation rules) [VF-sec/IC, [SolarQuarter](https://solarquarter.com/2025/04/02/karnataka-introduces-new-open-access-regulations-2025-to-boost-power-accessibility-and-renewable-energy/), [Renewable Watch](https://renewablewatch.in/2025/04/25/karnataka-announces-open-access-regulations-2025/)]; legacy annual 2% in-kind banking for 2018–2023 applicants [VF, [SolarQuarter 2023](https://solarquarter.com/2023/08/17/kerc-issues-vital-directive-on-wheeling-charges-and-banking-for-renewable-power-projects/)]; additional surcharge ₹0.82/kWh FY26 → ₹0.40/kWh from Mar 2026, not on captive drawal [IC, [Mercom](https://mercomindia.com/karnataka-halves-additional-surcharge-for-open-access-power)]; TNERC GEOA 2025 (8% in-kind banking in billing cycle, 14%/12-month legacy wind, 75% buy-back, standby 125%) [VF-sec, [SolarQuarter](https://solarquarter.com/2025/09/26/tnerc-issues-new-regulations-2025-for-green-energy-open-access-2025-in-tamil-nadu)]; MERC: wheeling by voltage, CSS ₹1.50–2.20 indicative [EST, [Bridgeway](https://bridgewaypower.in/blog/solar-wheeling-charges-maharashtra-merc-2026)], refund orders [VF]; GEOA Rules 2022: banking ≥ monthly, ≥30% of monthly consumption, 8% in-kind charge [VF, [IEEFA/JMK](https://ieefa.org/sites/default/files/2024-12/Impact%20of%20Green%20Energy%20Open%20Acess_Dec2024.pdf)] | Current FY26–28 Karnataka ₹/kWh wheeling and SLDC charges sit in the KPTCL tariff order annexures, not yet extracted [UNK] |
| Consumer–generator pairings (prospecting) | Karnataka SLDC: 556 IPPs / 4,924 MW; ≈922 distinct consumer organisations in the BESCOM/CESC/MESCOM lists [VF count / EST dedupe, [kptclsldc.in](https://kptclsldc.in/WBUpload.aspx)] | GESCOM/HESCOM lists failed to download [UNK] |

### 3.3 Pipeline and transformations

1. Ingest bill PDF → typed line items (deterministic parser per ESCOM template; LLM fallback flagged).
2. Ingest 15-minute injection and drawal → block table (96/day), with meter-loss factors applied as per regime.
3. **Regime identification**: determine which banking/charge regime binds this pair (legacy WBA vs 2025 regulation vs GEOA; captive vs third-party; voltage level; term), from the WBA date and the IPP spreadsheet's captive/non-captive flag [VF]. The notes find two or more concurrent regimes in each target state [INF, f2_f3 F2-Q2], so this step precedes any arithmetic.
4. Energy accounting: per block, match injection to drawal; residual to banking account; apply monthly (or annual, legacy) settlement; compute lapse and buy-back (TN 75%).
5. Charge engine: wheeling, transmission, CSS, additional surcharge (with captive exemption), banking charge in kind, standby at 125%, SLDC/operating charges, under-utilisation and relinquishment events.
6. Compare with billed amounts → discrepancy list with ₹ and clause.
7. Monthly report; cumulative recoverable ledger.

### 3.4 Analytical methods and where each discipline belongs

| Component | Method | Discipline |
|---|---|---|
| Charge recomputation | Deterministic rule engine with effective-dated modules | Rules (no ML) |
| 15-minute energy accounting | Conservation-checked block arithmetic; banking state machine | Rules + physics (metering losses) |
| Banking/lapse simulation | Monte-Carlo over the customer's historical load and generation profiles to size the expected lapse under each regime | Statistics |
| Procurement optimiser | LP/MILP: decision variables = contracted MW by source (group captive, third-party, rooftop, DISCOM/DERS), banking share, term; constraints = 15-minute load, ≥26% equity / ≥51% consumption for captive status [V-BLOG, [SurgePV](https://www.surgepv.com/solar-compliance/india/guides/open-access)], contract-demand headroom (OA participants cannot claim the 20% DERS headroom [VF, [SolarQuarter](https://solarquarter.com/2026/04/02/kerc-extends-discounted-energy-rate-scheme-till-fy28-eases-open-access-rules-for-consumers-in-karnataka/)]); objective = expected annual landed cost under tariff scenarios; solved with an open-source MILP solver on CPU in seconds for a single site | Operations research |
| Anomaly detection on bills | Simple statistical control charts per line item (z-score vs the customer's own history and vs peer sites) to catch mis-keyed rates before the rule engine runs | Statistics (no deep learning needed) |
| Explanation and dispute drafting | LLM over the discrepancy list, citing clauses | LLM with human verification |

### 3.5 Baseline

The baseline is **what the customer paid**, as billed, and what they would have paid under the regime they believe applies. The product's value is the signed difference after a tariff expert's review. A second baseline is the CEEW landed-cost calculator, which is frozen at FY2021-22 charges and does no scheduling, DSM or reconciliation [S-AN, [CEEW methodology](https://www.ceew.in/cef/shared/CEEW-CEF-Open-access-landed-cost-calculator-methodology.pdf)] — useful only to show how stale a static tool becomes.

### 3.6 Metrics and limitations

| Metric | Definition | Target in the first experiment |
|---|---|---|
| Recoverable ₹/yr | Sum of verified discrepancies in the customer's favour over 12 months | ≥₹5 lakh/yr per site (brief §7) |
| % of annual OA bill | Recoverable ÷ total OA-related charges | median ≥1.5% across sites |
| False-positive rate of flags | Flags rejected by the tariff expert ÷ flags raised | ≤20% after the first two months [EST target] |
| Reconciliation closure rate | Discrepancies resolved (credited, written off with reason) ÷ raised, within 90 days | reported, no target until pilots |
| Time to monthly settlement | Wall-clock from receipt of exports to signed memo | ≤2 working days |

Limitations: over-billing evidence in the notes is real but episodic and often resolved by commission orders covering many consumers at once (23 OA consumers' bills corrected in one MERC-related case [single-source, [APTEL 366/2017](https://www.aptel.gov.in/judgements/Judg2018/A.No.%20366%20of%202017%20&%20IA%20No.%20933%20of%202017_28.11.18_J.pdf)]), so the recoverable pool per consumer may be lumpy [HYP, red team Q2]; the frequency of billing errors is **not established**. Transaction-holding incumbents bundle settlement (Tata Power Trading lists DSM reconciliation and OA reconciliation [VF, [Tata Power](https://tatapower.com/what-we-do-nav/energy-services/power-trading-2)]; CES staffs bill-settlement verification [VF-snippet]; BridgeIT claims 1M+ bills validated across 100+ DISCOMs [EST, [BeBee](https://bebee.com/in/companies/bridgeit)]).

### 3.7 Data and compute costs

Near zero: bills and statements are customer files; regulations are free PDFs; a single-site MILP and 12 months of 15-minute data (35,040 rows) run on a laptop. Estimated infrastructure <₹3,000/month for a handful of pilots [EST]. The real cost is expert time: a tariff/regulatory specialist to sign off the rule library per state and a chartered accountant for recovery memos.

### 3.8 Minimum engineering skills; agent vs specialist

AI coding agents can implement the parsers, the energy-accounting state machine, the MILP, the reports and the tests. They cannot decide which regime binds a legacy WBA with a pending Supreme Court matter [VF, SolarQuarter 2023], how a DISCOM applies the captive exemption to the additional surcharge, or whether a claimed refund is enforceable — those need a regulatory/tariff expert (ex-SLDC/ESCOM or consultant) and, for the memo the customer takes to the DISCOM, a CA's sign-off. The founder needs working knowledge of Indian OA charges, 15-minute energy accounting and basic LP formulation.

### 3.9 Build scope

- **1 week**: Karnataka rule module for one regime (2025 regulation, third-party, HT); parser for one ESCOM bill template; energy-accounting engine with conservation tests; synthetic 12-month example end to end.
- **30 days**: three regimes (legacy WBA, 2025 regulation, GEOA/captive), standby and under-utilisation events, additional-surcharge captive exemption, TN GEOA 2025 banking, bill anomaly control charts, first real customer backtest (Experiment F2-A).
- **90 days**: Maharashtra module with MERC refund logic, procurement MILP with DERS-vs-OA scenario, multi-site consumer support, dispute-letter drafting, five-customer pilot reporting.

### 3.10 What would make F2 infeasible

- Monthly SLDC/DISCOM statements are not obtainable as exports (only paper or portal screenshots), making 15-minute reconciliation impossible — **not established either way; the first design-partner conversation must resolve it**.
- Rule changes outpacing the library: four re-litigations of TN banking and annual Karnataka surcharge swings show the rate of change; mitigated by effective-dated modules but a two-state library needs continuous expert review.
- Incumbent bundling at zero visible fee (traders, OA developers, "zero upfront" advisory [VF, OAE]) collapses willingness to pay — the brief's F2-B interview test exists for this.
- Recoverable pool below ~0.5% of bill for most sites (brief's fail threshold), leaving only bookkeeping value.

## 4. Finalist F1 — ISTS connectivity / grid-access intelligence

### 4.1 Minimum product

A versioned, geocoded substation ledger joined across CTUIL publications (grant lists, effectiveness list, bay/substation margins by solar/non-solar hour, cluster declarations, 11/SM/2026 eligible lists, compensation determinations) with (i) change alerts and (ii) a calibrated probability that a given application becomes effective within 12 months. **Legal gate**: nothing is sold until CTUIL gives written permission to reuse published data commercially (A0, §6.4).

### 4.2 Data inputs and sources

| Input | Form | Notes |
|---|---|---|
| "Connectivity to be Made Effective" list | HTML table, 636 rows, filters by technology/region/state, PDF/XLS export buttons (JS; output unconfirmed), JS-paginated [VF, [CTUIL](https://ctuil.in/connectivity-effective-list)] | Already filterable/exportable — this layer is not a product; it is an input. Columns include CTUIL's own **expected effective date**, which becomes a baseline predictor |
| Grant lists ("Details of Connectivity granted under GNA") | Structured PDF, 200+ rows: application ID, applicant, submission date, region, project type, MW, substation, in-principle/firm start dates, effective status [VF, [CTUIL Jul 2025](https://www.ctuil.in/uploads/assets/175747971577July%2025_Main-Connectivity%20under%20GNA.pdf)] | Monthly series since 2023 must be collected from the archive; Aug/Sep 2026 issues were not located on the updates page [UNK] |
| Bay/substation margins, solar and non-solar hours | PDF only; three files per release (latest 01.10.2026 and 13.08.2026); archive at `/renewable-energy-ol` [VF, [CTUIL](https://ctuil.in/renewable-energy)]; RESTRICTED stamp | Genuine parsing gap, but CTUIL keeps the archive, so the "time series nobody else has" claim is weak [VF, red team Q1] |
| Application status | API-backed page `/nswsapi/gna` [VF] | Public status lookup exists |
| Cluster declaration (16 Jul 2026), reallocation notices (Reg 11(C)), BESS MWh enhancement advisory (14 Sep 2026) | PDFs on CTUIL homepage [VF, [ctuil.in](https://www.ctuil.in/)] | |
| 11/SM/2026 final eligible-entities list (17 Sep 2026) | PDF with LoA, PPA status, application ID, substation, in-principle/firm/expected dates [VF, [CTUIL](https://ctuil.in/uploads/assets/178963420036Final%20List%20of%20eligible%20entities%20as%20per%2011SM2026_rev%2001.pdf)] | ~70 developers; the prospect list |
| CERC orders (restorations, compensation, 11/SM/2026) | PDFs [VF, [CERC 11/SM/2026](https://cercind.gov.in/2026/orders/11-SM-2026.pdf)] | Label-noise source: outcomes decided by petition |
| Compensation rate | ₹1,612.15/MW/day (RATE6), 15-month cap then revocation [VF, [CTUIL 11-08-2026](https://ctuil.in/uploads/assets/178645696705Compensation%20charges%20as%20per%20CERC%20order%20dtd%2003-08-2026%20to%20be%20uploaded%20on%20website.pdf)] | Cost-of-delay input |
| Substation coordinates | CTUIL "Tentative Coordinates of RE PS" [VF, CTUIL homepage] | Geocoding |

### 4.3 Pipeline

Fetch → extract → normalise applicant/substation names → build one row per application-month (the panel) → compute features as known at each month → label outcomes from later snapshots → train/evaluate → publish alerts and probabilities to the ledger.

### 4.4 Analytical methods

- **Rules**: queue position, cluster membership, bay availability, 15-month compensation clock, 60-day election windows — all deterministic from documents.
- **Statistics/ML**: a survival or binary classifier for "effective within 12 months of in-principle grant". Features (all available at application/grant date): substation, region, state, technology (solar/wind/hybrid/ESS/standalone ESS), MW, cluster, application date, in-principle date, voltage level, whether the LoA has a PPA (from eligible lists), margin at the substation at grant time, count of applications ahead in the same substation. Models: logistic regression and gradient-boosted trees on CPU; calibration by isotonic regression. Prediction is the only part the red team accepted as defensible [HYP, red team Q1 inferences].
- **Physics**: none (load flow and ATC need network models the public cannot access [EST, [solar_forecasting_feasibility.md] §E]).
- **LLM**: explanation of CERC orders and alerts; drafting of the "which 11/SM/2026 option" memo for a human reviewer.

### 4.5 Backtest design (Experiment F1-A)

| Element | Specification |
|---|---|
| Universe | All applications appearing in CTUIL grant lists and the effectiveness list from Jan 2023 to Oct 2026 (expected several hundred to ~900 rows; the effectiveness list alone has 636 [VF]) |
| Target | Binary: connectivity made effective within 12 months of the firm (or in-principle) start date recorded at grant time; secondary: months from grant to effective (regression) |
| Features | As in §4.4; strictly those knowable at the grant month |
| Baselines | (1) base rate; (2) "same-substation last-known" — the most recent outcome at the same substation; (3) CTUIL's own published expected date, converted to a yes/no at 12 months |
| Leakage controls | Time-based split: train on grants to Dec 2024, validate on 2025 H1, test on 2025 H2 (whose 12-month windows close by Oct 2026); no features from later snapshots; CERC restorations and 11/SM/2026 surrenders treated as censoring events, reported separately |
| Metrics | AUC, Brier score, reliability diagram (10 bins), MAE in months for the regression |
| Pass | AUC ≥0.70 on the time-split test set **and** Brier better than baseline (3); fail: AUC <0.60 or no improvement over CTUIL's own expected date |

Statistical justification: with ≈300 test-set applications and a positive rate near 40%, the standard error of an AUC near 0.70 is ≈0.03, enough to distinguish 0.70 from 0.60 at conventional confidence [EST]. If fewer than 150 test rows are available after censoring, the result is "inconclusive" by construction.

### 4.6 Baseline, metrics and limitations

The red team shows the dominant cause of stranded connectivity is demand-side — 40,420 MW of LoAs → 2,338 MW PPAs; 22,054 MW of connectivity without PPAs; ≈15.7 GW being released by order [VF, CERC 11/SM/2026] — and that outcomes turn on petitions and condonations. A model trained on CTUIL lists cannot see PPA negotiations; expect modest skill. The RESTRICTED stamp and copyright policy make the ledger itself unsellable without permission.

### 4.7 Data and compute costs

≈₹0: all inputs are free PDFs; the panel is <10⁵ rows; models train in seconds on CPU.

### 4.8 Skills; agent vs specialist

Agents implement the scraper (headless browser for the JS table), parsers, panel builder, models and calibration. A specialist is needed to (a) interpret CERC/CTUIL procedure (what "firm", "effective", "deemed GNA" mean operationally — the notes do not define them precisely), (b) label edge cases (partial surrender, reallocation, restoration), and (c) handle the CTUIL permission conversation. Law-firm counsel, not software, is the incumbent advisor [VF, red team Q4].

### 4.9 Build scope

- **1 week**: send the A0 permission request; scrape the effectiveness list and all grant-list PDFs since 2023; build the panel; run baselines and a first classifier; produce the AUC/Brier table.
- **30 days** (only if A0 is answered positively or neutrally and F1-A shows skill): margins parser with corrupt-page fallback, cluster and 11/SM/2026 joins, geocoding, alert feed, calibration report; one-page substation sample for interviews.
- **90 days**: private-use alerting for 3–5 developers' own applications; reallocation-option analysis; BESS MWh-enhancement screen under the 14 Sep 2026 advisory.

### 4.10 What remains if prediction shows no skill

Aggregation without prediction is "already free" (CTUIL's table plus Excel replicates 70–80% of the value at zero cost [HYP, red team Q4]). What survives: a monitoring/alerting and interpretation service priced like a newsletter, usable internally for F2/F3 customers' own applications, and the compiled ledger as an input to F3's siting decisions. The brief's instruction stands: refusal or no skill → F1 is dead as a product; keep as an internal research tool.

### 4.11 What would make F1 infeasible

CTUIL refuses permission or enforces the RESTRICTED classification; CTUIL ships a dashboard/CSV export of the margins (its effectiveness page already has export icons [VF]); the GNA 4th amendment (still draft; hearing 23 Jun 2026, not notified as of 16 Oct 2026 [VF, [CERC draft regs](https://cercind.gov.in/Draft_reg.html)]) lets CTUIL close applications and clears the backlog; prediction shows no skill.

## 5. Finalist F3 — FDRE/BESS dispatch, availability-compliance and bid optimisation

### 5.1 Minimum product

Not a bidder. A **contract-compliance and dispatch-planning engine** for an availability-paid standalone BESS or an FDRE project: daily dispatch plan honouring cycle budget, RTE and availability tests; monthly availability/DFR certificate with LD exposure; and an optional bid file for any merchant tranche. The red team's recommendation to replace the bid-optimiser wedge with a compliance pilot for one VGF winner is adopted [HYP, red team Q9].

### 5.2 Data inputs and sources

| Input | Source | Constraint |
|---|---|---|
| IEX DAM/RTM 15-minute prices | Public download from 1 Apr 2022 without login [VF, [IEX](https://www.iexindia.com/market-data/day-ahead-market/market-snapshot)] | Non-commercial ToU; licence needed for any product use [VF]; market coupling pending (Supreme Court admitted IEX's appeal; CERC says rules "shortly"; not notified as of 16 Oct 2026 [VF-sec, red team Q6]) reduces representativeness of the 2022–26 series |
| Contract terms | Public RfS/BESPA: MSEDCL 15-year BESPA, ≥6,300 cycles over term, 95% annual availability, 85% monthly AC-AC RTE, indigenous EMS software, ≥20% local content [VF, [Energetica](https://www.energetica-india.net/news/oriana-bsl-engineering-armee-infotech-gk-energy-among-winners-in-msedcl-4-gwh-bess-auction)]; NVVN-Kerala 420 cycles/yr [VF]; KPTCL two cycles/day [VF]; FDRE-X: 4,000 kWh/MW/day in four buyer-designated peak hours, shortfall penalty 1.5× PPA tariff capped at 400 MWh per 100 MW, ≤5% market sourcing [VF, [Energetica](https://www.energetica-india.net/news/seci-floats-tender-for-1200-mw4800-mwh-fdre-supply)]; DFR 90% peak / 80% off-peak / 90% annual [IC]; SECI standard BESSA public but not parsed [VF exists] | Merchant rights in state BESPAs **not established** |
| DSM rules for storage | Standalone ESS = general seller (frequency-linked bands, ±10% or 100 MW); co-located ESS under WS rules while RE injects [VF, [CERC DSM 2024](https://www.cercind.gov.in/regulations/192-Noti.pdf)]; infirm power before trial run at Normal Rate ≤ ₹2.00/kWh [VF, [CERC notification 208](https://cercind.gov.in/regulations/208-notification.pdf)] | |
| Charging rules | CMETS-WR draft: 2-hour minimum, charge only from dedicated RE, no ISTS drawal; RVPN draft: solar 10:00–15:00 / wind 00:00–04:00 charging windows, SLDC may curtail/reschedule [VF, [JMK](https://jmkresearch.com/indias-emerging-merchant-bess-market-faces-its-first-regulatory-test/)] | Drafts; status **must be verified** |
| Weather inputs for RE forecast | ECMWF IFS/AIFS open data, 0.25°, `ssrd`, 2 m temperature, 10/100 m wind, CC-BY-4.0, 12-run rolling archive [VF, [ECMWF](https://www.ecmwf.int/en/forecasts/datasets/open-data)]; Open-Meteo $29/$99 per month with forecast-as-issued history [VF/IC, [Open-Meteo](https://open-meteo.com/en/pricing)] | Open-data latency in hours **not established**; satellite irradiance over India (CAMS coverage, INSAT-3D GHI product) unverified [UNK] |
| Asset telemetry | Customer EMS/SCADA exports: SoC, charge/discharge MW per block, availability flags, temperature, auxiliary load | Required for the compliance module; no public substitute |
| Benchmarks | Ember: merchant revenue INR 2.4 m/MWh (2025), LCOS INR 4.5/kWh, break-even ₹7.56/kWh when charging at ₹2.6/kWh; DAM arbitrage 80–85% of earnings [S-AN, [Ember](https://ember-energy.org/latest-insights/the-age-of-storage-batteries-primed-for-indias-power-markets/chapter-3-the-economics-of-merchant-bess/)]; FY26 average IEX arbitrage spread ₹4.81/kWh [IC, [Mercom](https://mercomindia.com/iex-revenue-rises-11-in-q1-fy-2027-as-power-trading-volume-grows)]; open Indian dispatch/sizing model BattMan [VF, [Ember materials](https://ember-energy.org/latest-insights/the-age-of-storage-batteries-primed-for-indias-power-markets/supporting-materials)] | |

### 5.3 MILP formulation sketch

Index t over 15-minute blocks (96/day), horizon one day with a rolling monthly cycle budget.

- Variables: charge power c_t ≥ 0, discharge power d_t ≥ 0, state of charge s_t, binary mode m_t (no simultaneous charge/discharge), shortfall e_t ≥ 0 in designated hours, availability-shortfall a ≥ 0 per month.
- Dynamics: s_{t+1} = s_t + η_c·c_t·Δt − d_t·Δt/η_d, with η_c·η_d ≥ 0.85 monthly AC-AC (MSEDCL test) [VF]; s_min ≤ s_t ≤ s_max (degradation-adjusted).
- Power limits: c_t ≤ P_max·(1−m_t), d_t ≤ P_max·m_t.
- Cycle budget: Σ_t d_t·Δt over the month ≤ cycles_month × E_rated (e.g., 6,300/15 years ≈ 420/yr ≈ 35/month [VF-derived]).
- Charging-source constraint (co-located/merchant under draft rules): c_t ≤ RE_t (forecast RE generation) and c_t = 0 outside permitted windows [VF, JMK].
- FDRE delivery: Σ_{t∈peak} d_t·Δt + e_day ≥ 4,000 kWh/MW·P_contract; monthly penalty = 1.5 × tariff × Σ e, capped at 400 MWh per 100 MW [VF]; DFR constraints per time block in peak hours (≥90%) [VF-snippet].
- Availability: Σ months of unavailable blocks ≤ 5% annual, with LD as a convex cost term on a [VF].
- DSM: deviation of delivered schedule from committed schedule priced per CERC bands (general seller for standalone; WS rule for co-located) [VF].
- Objective: maximise Σ_t (price_t·d_t − price_t·c_t)·Δt (for merchant tranche or FDRE's ≤5% market allowance) − penalties − degradation cost; for pure availability contracts the objective reduces to minimising expected LDs and cycle-budget violation.

Solvable with an open-source MILP solver on CPU in seconds per day; a year's backtest is minutes.

### 5.4 Forecasting component

Architecture: consume NWP outputs, do not run weather models (open-weight AI weather models need H100-class GPUs [VF, [solar_forecasting_feasibility.md] §A]). ECMWF `ssrd` → clear-sky index via pvlib → 15-minute downscaling → plant model (pvlib, BSD-3) → power; wind via generic power curves on 100 m wind. Baselines: smart persistence (clear-sky-index persistence) and the climatology–persistence convex blend [VF-snippet, [Yang 2019](https://scholar.hit.edu.cn/en/publications/standard-of-reference-in-operational-day-ahead-deterministic-sola/)]. Metrics: nMAE and nRMSE normalised to installed capacity (daylight blocks), block-within-band share at ±5% (solar) / ±10% (wind) of AvC, skill vs smart persistence, stratified by monsoon regime and by lead (day-ahead vs the 7th/8th-block intraday revision ≈1.5–2 h [VF, [CERC 14/SM/2023](https://www.cercind.gov.in/2023/orders/14-SM-2023.pdf)]). Reference points: one Indian plant-level NWP chain achieved 5.59% nMAE day-ahead [VF-snippet, [EGU22](https://meetingorganizer.copernicus.org/EGU22/EGU22-9393.html)]; Grid-India's 16-plant simulation found plants inside the tightened bands only 45–58% (solar), 32–73% (wind) of blocks [VF-sec, [Energetica](https://www.energetica-india.net/news/cerc-proposes-phased-schedule-based-deviation-mechanism-for-wind-and-solar-from-april-2026)]. Public ground truth is aggregate only (all-India hourly solar/wind, Sep 2021–Jun 2025, CC BY 4.0 [VF, [Mendeley](https://data.mendeley.com/datasets/y58jknpgs8)]); no public per-plant actuals exist [VF, §B], so plant-level accuracy claims need customer telemetry.

### 5.5 Where disciplines belong

Rules: contract clauses, cycle counting, DSM pricing. Physics: SoC dynamics, RTE, pvlib plant model. Statistics: price-scenario generation (bootstrap by hour-of-day and season from the IEX series), forecast error distributions. ML: light post-processing of NWP (gradient boosting per plant once telemetry exists). Operations research: the MILP. LLM: explaining monthly certificates and contract clauses; drafting RfS clause extractions for human review.

### 5.6 Baseline, metrics, limitations

Baselines: (a) naive "charge at the three cheapest blocks, discharge at the three dearest" heuristic; (b) Ember's BattMan; (c) the DISCOM's dispatch instruction as issued (for availability contracts). Metrics: ₹/MWh/yr captured vs Ember's INR 2.4 m/MWh benchmark; LD exposure avoided; cycle-budget adherence; forecast metrics above. Limitations: Tier-2 awards are DISCOM/SECI-dispatched, so optimisation headroom is small [VF/IC]; the merchant fleet (≈80% of 6.8 GWh in June 2026) is owned by Adani and ACME [VF, JMK]; DSM escalation is stayed for NSEFI petitioners in Karnataka HC [VF-sec, [PowerPeak](https://powerpeakdigest.com/karnataka-hc-stays-cerc-dsm-2024/)] and deferred for new WS sellers to bids on/after 1 Jan 2027 or COD on/after 1 Jan 2029 [VF, CERC notification 208].

### 5.7 Data and compute costs

Public price backtest: ₹0 plus the IEX licence for any commercial use (**unknown**). Forecasting: ≈$15–40/month infrastructure, $99/month Open-Meteo Professional for history [EST, §F]. Telemetry: customer-supplied.

### 5.8 Skills; agent vs specialist

Agents implement the MILP, scenario generator, pvlib pipeline, backtest harness and certificate reports. A specialist is needed to read the BESPA/BESSA and FDRE PPA clauses authoritatively (availability test definitions, LD computation), to validate SoC/degradation models against the OEM warranty, and to handle SLDC/RLDC scheduling procedure. An IEX membership is not needed: bids can be executed through the customer's proprietary membership or a trader member [VF, [IEX membership](https://www.iexindia.com/membership)].

### 5.9 Build scope

- **1 week**: IEX 15-min series 2022–2026 ingested; MILP with cycle budget and RTE; perfect-foresight and day-ahead-price-persistence backtests; comparison with the naive heuristic and Ember benchmarks.
- **30 days**: FDRE penalty and DFR constraints; charging-window constraints; price-scenario bootstrap; ECMWF→pvlib forecast with smart-persistence baseline on the all-India aggregate; first contract-clause extraction from one public BESPA for expert review.
- **90 days**: compliance module on one design partner's historical telemetry (6–12 months): monthly availability/RTE/cycle certificate vs the customer's own; LD exposure report.

### 5.10 What would make F3 infeasible

IEX refuses or prices a licence beyond reach; draft charging rules are adopted and collapse merchant headroom to RE-charged, SLDC-overridable schedules; Tier-2 winners' SCODs (2027–28 for most state awards [EST, f2_f3 F3-Q1]) push revenue beyond a bootstrapped runway; OEM EMS bundles dispatch (Envision at Juniper; Fluence–ReNew JV [VF/IC]).

## 6. Validation experiments

Priority order: F1-A0 (free, 1 email), F2-A (free, kills or confirms the lead), F1-A (free, 7 days), F3-A (free, 7 days). F2-B and F1-B (commercial interviews, brief §5/§7) run in parallel and are not restated here except where they gate a decision.

### 6.1 F2-A — Settlement recomputation on real bills (lead)

- **Hypothesis**: for Karnataka OA/group-captive consumers of 1–20 MW, deterministic recomputation of 12 months of bills and statements under the applicable KERC regime finds recoverable overcharges plus avoidable banking-lapse/DSM losses ≥1.5% of the annual OA bill and ≥₹5 lakh/yr for most sites.
- **Supporting result**: median across sites ≥1.5% **and** ≥₹5 lakh/yr for ≥3 of 5 sites (brief §7). **Falsifying**: <0.5% for ≥4 of 5 sites. **Inconclusive**: fewer than 3 sites deliver complete 12-month exports, or discrepancies cannot be adjudicated by the expert.
- **Evidence needed**: 12 months of DISCOM bills, generator invoices, SLDC/DISCOM energy-accounting and banking statements, and 15-minute meter data from 3–5 consumers; obtained via personal network, KASSIA / Peenya Industries Association / FKCCI energy committee, or a consultant partner (brief §7); prospect names come from the SLDC consumer lists (e.g., multi-installation consumers such as Shahi Exports, Wipro, Infosys, Manyata, RMZ [VF, [kptclsldc.in](https://kptclsldc.in/WBUpload.aspx)]).
- **Procedure**: regime identification → energy accounting → charge engine → discrepancy list → independent review by a tariff expert (blind to the engine's ₹ total) → agreed recoverable ₹. Baseline: billed amounts; secondary: customer's own in-house reconciliation if any.
- **Sample size/period**: 12 months per site covers one full tariff year and the FY26→FY27 additional-surcharge switch (₹0.82 → ₹0.40/kWh [IC]); 5 sites is the minimum to report a median that is not a single outlier; 24 months where available to catch retroactive true-ups.
- **Metrics**: recoverable ₹/yr, % of OA bill, expert-rejected flag rate, time to settlement.
- **Time and cost**: ≤14 days after data receipt; ≈₹0 compute; expert review ≈₹25–50k if paid [EST].
- **Establishes**: that money exists and the engine can find it. **Does not establish**: willingness to pay, recoverability from the DISCOM in practice, or error frequency across the population.
- **Next decision**: pass → 90-day build and success-fee pilots; fail → re-scope to procurement optimisation only or stop; inconclusive → extend to 5 more sites via an association partner.

### 6.2 F1-A — Backtest of effective-within-12-months on 2023–2026 CTUIL lists

- **Hypothesis**: features knowable at grant time predict "effective within 12 months" with AUC ≥0.70 and a better Brier score than CTUIL's own published expected date.
- **Supporting**: AUC ≥0.70 and Brier better than all three baselines on the time-split test set. **Falsifying**: AUC <0.60 or no improvement over baseline (3). **Inconclusive**: <150 usable test rows.
- **Evidence**: CTUIL effectiveness list (scrape with JS pagination), monthly grant-list PDFs since 2023 (archive), 11/SM/2026 lists, CERC restoration orders [all VF]. No customer needed.
- **Procedure and baselines**: §4.5.
- **Sample**: all applications 2023–2026 (several hundred); time split so that every test row's 12-month window has closed by Oct 2026.
- **Metrics**: AUC, Brier, calibration, MAE months.
- **Time/cost**: ≤7 days, ≈₹0.
- **Establishes**: whether prediction is possible from public records. **Does not establish**: that anyone will pay, or that the product is lawful to sell (A0).
- **Next decision**: skill + A0 positive → 30-day build; skill + A0 refused → private-use alerting only, no standalone product; no skill → F1 is an internal research tool.

### 6.3 F3-A — Public-price dispatch backtest and compliance simulation

- **Hypothesis**: on 2022–2026 IEX 15-minute DAM/RTM prices, a cycle- and RTE-constrained MILP with day-ahead price persistence captures ≥70% of perfect-foresight arbitrage value and exceeds the naive heuristic by ≥15%, while an FDRE-style delivery constraint (4,000 kWh/MW/day in a 4-hour evening window) can be met on ≥90% of days with RE-only charging from a forecast RE profile.
- **Supporting**: both conditions hold across seasons, including the near-zero solar-hour price days of 2025–26 [S-AN/IC]. **Falsifying**: captured value <50% of perfect foresight, or RE-only charging fails the delivery constraint on >20% of days (meaning the optimiser cannot help; the binding constraint is the asset/contract design). **Inconclusive**: IEX data gaps or inability to reconstruct RTM series for the full period.
- **Evidence**: IEX public 15-min DAM (from 1 Apr 2022) and RTM series [VF]; FDRE-X and MSEDCL contract terms [VF]; ECMWF/Open-Meteo forecast-as-issued irradiance for a representative Rajasthan/Gujarat site; all-India aggregate for forecast sanity checks. **Commercial use of IEX data needs a licence**; this experiment is internal validation.
- **Procedure**: implement MILP (§5.3); run (a) perfect foresight, (b) persistence of previous-day prices, (c) bootstrap scenarios; compare with the naive heuristic and BattMan; report ₹/MWh/yr vs Ember's INR 2.4 m/MWh and LCOS INR 4.5/kWh.
- **Sample/period**: full 2022–2026 series (≈1,500 days) so monsoon, summer-peak and solar-glut regimes are all present; results stratified by year because market coupling may change price formation.
- **Metrics**: ₹/MWh/yr captured; % of perfect foresight; delivery-constraint satisfaction rate; cycles used; forecast nMAE/nRMSE on the aggregate.
- **Time/cost**: ≤7 days; ≈₹0 (plus $99/month if Open-Meteo history is used).
- **Establishes**: that the optimisation problem has value and is tractable. **Does not establish**: availability-contract value (needs telemetry), legality of product use of IEX data, or that Tier-2 developers own the decision.
- **Next decision**: pass → seek one design partner's telemetry for the compliance module (90-day scope) while watching the charging-rule drafts and coupling; fail → F3 remains a 2027+ watch item.

### 6.4 F1-A0 — Written permission from CTUIL

- **Hypothesis**: CTUIL will grant written permission to reuse published connectivity/margin data in a commercial product, with attribution.
- **Supporting**: written permission or a stated licensing route. **Falsifying**: written refusal, or confirmation that the RESTRICTED classification bars redistribution. **Inconclusive**: no reply within 30 days (treat as refusal for planning; the aggregator practice tolerated today [UNK] is not a licence).
- **Evidence/procedure**: one email citing the copyright policy [VF, [ctuil.in/copyright-policy](https://ctuil.in/copyright-policy)], describing derived use (analytics and alerts), requesting terms. Cost ≈₹0; ≤30 days.
- **Establishes**: whether F1 can be sold at all. **Next decision**: as in §6.2.

## 7. Staged path to industrial access

No live integration is needed for any first experiment: F2-A, F1-A, F3-A and A0 all run on files and public pages. Conversely, **public data alone does not prove production readiness** — it cannot show recoverability from a DISCOM, plant-level forecast accuracy, or contract-compliance under real telemetry.

| Stage | F2 | F1 | F3 |
|---|---|---|---|
| 1. Public-data prototype | Rule library from KERC/TNERC/MERC orders; synthetic 12-month site; SLDC lists for prospecting | Scrape + panel + baselines | IEX backtest MILP; aggregate forecast sanity check |
| 2. Historical backtest | — (needs customer bills) | F1-A on 2023–26 grants | F3-A on 2022–26 prices |
| 3. Ground-truth validation | Expert-adjudicated discrepancies | Outcomes from later CTUIL snapshots and CERC orders | Telemetry-free: none; requires stage 4 |
| 4. Customer historical export | F2-A: 12–24 months of bills/statements from 3–5 sites | A developer's own application history and deficiency letters (private-use) | 6–12 months of EMS/SCADA exports from one awardee (Pace Digitek, Oriana or similar [INF, f2_f3 F3-Q5]) |
| 5. Read-only / shadow pilot | Monthly recomputation in parallel with the customer's process; no DISCOM filings until agreed | Alerts and probabilities delivered to the customer; compared with what their team saw | Daily dispatch plan and monthly certificate computed in shadow, compared with the DISCOM instruction and the customer's own certificate |
| 6. Production | Success-fee audit then subscription; dispute letters with CA sign-off | Only under CTUIL permission; otherwise private-use tool | Bid files via the customer's membership or a trader; compliance reports contractually relied upon |

## 8. Energy-quantity glossary (applied correctly)

| Term | Meaning as used in the notes | Public? |
|---|---|---|
| Installed capacity | Nameplate MW (AC or DC must be stated); used to normalise forecast errors (nMAE vs capacity) | Yes, per project in CTUIL lists and tender awards [VF] |
| Available capacity (AvC) | Cumulative inverter/turbine capability at the time, net of outages/derating; the DSM denominator while X=100% [VF, [CERC DSM 2024](https://www.cercind.gov.in/regulations/192-Noti.pdf)] | No — plant telemetry only; a public-data forecaster cannot know it [EST, solar note §C] |
| Actual generation | Metered injection per 15-minute block | No per-plant public series; aggregate all-India hourly exists (CC BY 4.0) [VF, Mendeley] |
| Schedule vs actual | Schedule = declared block-wise injection (day-ahead, revisable from the 7th/8th block); deviation = actual − schedule, divided by AvC (to 31 Mar 2026) then by X%·AvC + (100−X)%·schedule [VF] | Schedules not public per plant [UNK] |
| DSM bands | Volume limits within which deviation is settled at contract rate: solar/hybrid ≤5%, 5–10%; wind ≤10%, 10–15% from 1 Apr 2026; under-injection beyond band at 200% of contract rate [VF]; Karnataka intra-state slabs ₹0.25/0.50/0.75 per unit, capped at 3 paise/unit annually [VF-sec] | Rules public; charges per plant not |
| ATC/TTC vs CTUIL "tentative margins" | ATC/TTC are transfer capabilities from network studies (require load-flow models not available publicly); CTUIL's bay- and substation-wise "tentative margins" are administrative connectivity headroom that "may vary depending on network topology, Load-Generation balance" [VF-snippet, [CTUIL](https://ctuil.in/renewable-energy)] — not a curtailment or ATC figure | Margins public (PDF, RESTRICTED stamp); ATC/TTC publication by Grid-India not established (site 503) [UNK] |
| Connectivity vs GNA vs T-GNA | Connectivity = right to connect at an ISTS substation (in-principle → firm → effective); GNA = general network access for drawal/injection with one-time charge ₹1 lakh/MW and access BG ₹5 lakh/MW [VF, [CTUIL advisory](https://www.ctuil.in/uploads/assets/169780473570Advisory%20regd%20Procedure%20for%20payment%20of%20one-time%20GNA%20charges.pdf)]; T-GNA = temporary GNA for short-term access, referenced for WS sellers in CERC 14/SM/2023 [VF]; "deemed GNA" appears as a column in the effectiveness list [VF]. Precise regulatory definitions are not reproduced in the notes; verify against the GNA Regulations 2022 | Grant/effectiveness lists public [VF] |
| Solar-hour vs non-solar-hour access | Post-3rd-amendment split of connectivity/GNA by hours, with separate margins [VF] | Public (PDF) |

## 9. Known limitations and open technical questions

1. Whether Karnataka SLDC/ESCOMs issue 15-minute energy-accounting and banking statements to consumers as exports (vs paper/portal) — gates F2 entirely; **not established**.
2. Frequency of OA billing errors across the consumer population — only litigated cases are known [UNK].
3. Current FY26–28 Karnataka wheeling, SLDC and operating charges (KPTCL tariff-order annexures not parsed) [UNK].
4. CTUIL's stance on commercial reuse and the meaning of the RESTRICTED stamp — A0.
5. Whether CTUIL's XLS export works and whether the full 636-row table can be retrieved without a headless browser [UNK].
6. Operational definitions of "firm", "effective", "deemed GNA" and T-GNA for labelling — regulation text not in the notes.
7. Availability of monthly grant-list PDFs for every month 2023–2026 (Aug/Sep 2026 not located) — affects panel completeness.
8. IEX data-licence terms and cost for product use; API access rules for members [UNK].
9. Whether state BESPAs permit idle-capacity merchant use; SECI-ESS-IV merchant clauses (RfS not parsed) [UNK].
10. Final status of CMETS-WR/RVPN charging rules and the Power Market (Second Amendment) coupling regulations [UNK as of 16 Oct 2026].
11. ECMWF open-data release latency in hours and the day-ahead schedule submission deadline (assumed morning IST) — both unverified [HYP].
12. Satellite irradiance over India (CAMS coverage, MOSDAC INSAT-3D GHI product, commercial terms) — needed for intraday revisions [UNK].
13. Outcome of the Karnataka HC stay after 10 Jun 2026 and the Delhi HC writ on the merits — determines DSM penalty exposure [UNK].
14. SCOD dates for KPTCL/MSEDCL/TN/Kerala BESS awards — determines when F3 customers have assets to operate [UNK].
15. Reconciliation of operational BESS totals: 758 MWh (end-2025, Tenderkosh), 6.8 GWh (JMK, Jun 2026) and ≈12.6 GWh (Energetica, Oct 2026) are not reconciled by the sources; the brief's §3 figure is stale [EST].
16. Whether the KERC DSM 2026 wind/hybrid slab rates match the solar slabs reported [UNK].
17. No LLM-extraction accuracy test on CTUIL PDFs or tariff orders has been run; the golden-file strategy in §2.4 is the proposed remedy.
