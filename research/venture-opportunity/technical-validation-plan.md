# Technical validation plan — finalists F2, F1, F3

Phase D technical-diligence deliverable, 2026-10-17. Evidence base: the Phase B–D research notes only (no new web research). Evidence classes follow the notes: **[VF]** verified fact (primary document read), **[IC]** independently corroborated, **[EST]** estimate, **[HYP]** hypothesis, **[UNK]** unknown, **[INF]** inference. Where the notes lack a fact it is written as *not established in research; must be verified*. Finalist order follows the post-red-team ranking in `decision_brief.md` §7, confirmed in §8: **F2 (71) > F1 (63) > F3 (60)**. The brief's §8 late-evidence changes — Regional Power Committee (RPC) weekly DSM files as public per-plant ground truth for ISTS plants, the ≈12.6 GWh operational BESS fleet, and the Karnataka SLDC consumer lists — are incorporated below.

## 1. Purpose and how to read this document

This document turns the three finalists into buildable, testable engineering plans and names the experiment that would most cheaply kill each one. It is written for a founder who builds with AI coding agents, on CPU-only infrastructure (a 2–4 vCPU VM, no GPU), with limited capital (experiment budgets of ≈₹0–50k), and without privileged access to any grid operator, DISCOM or exchange. Every pipeline is therefore designed so that the first experiment runs on public data or on files a customer can export, needs no live integration, and yields a number against a stated threshold. §2 is the shared engine; §3–5 each finalist; §6 the experiments; §7 the staged path to production; §8 the energy-quantity vocabulary; §9 open questions. A number without a class label is the writer's arithmetic from labelled inputs.

## 2. Shared core: regulatory-document and market-data ingestion engine

All three finalists consume the same document families — CERC/SERC regulations and tariff orders, CTUIL lists and margin sheets, SLDC statements and lists, RPC weekly DSM files, IEX price series. The core is a **document-to-ledger engine**, not an "AI product".

### 2.1 Architecture

| Layer | Function | CPU-only implementation note |
|---|---|---|
| Fetcher | Polls sources on a schedule; stores every artefact byte-for-byte with URL, time, headers, SHA-256 | CTUIL's effectiveness table is JS-paginated (10 rows rendered server-side on fetch) [VF, f1_customers_and_buying.md], so a headless-browser path or the page's underlying request is needed |
| Extractor | PDF/XLSX/HTML → typed rows per document schema | `pdftotext -layout` reproduced the CTUIL margins table in one pass but hit 28 corrupt flate streams [VF, [CTUIL PDF](https://ctuil.in/uploads/assets/176011721061Website%20sheet_solar%20non%20solar%20margins_all.pdf)]; a vision/LLM fallback runs only on pages the deterministic parser rejects, and every such row is flagged for human verification |
| Normaliser | Entity resolution (SPVs, substations, ESCOMs), units (MW/MWh, ₹ lakh/MW/month vs ₹/kWh), dates, 96 × 15-min blocks | Versioned alias tables; no LLM at runtime |
| Rule library | Charge formulas, bands, slabs, banking regimes, penalty clauses as code with effective-date ranges | One module per regulation version (e.g., `KERC_OA_2025`, `CERC_DSM_2024_R8_4`, `CERC_DSM_3A_2026_R8_4A`) |
| Ledger | Append-only facts: (entity, attribute, value, valid_from, valid_to, artefact, extraction_method, verified_by) | A snapshot is a point-in-time query; the diff between snapshots is the alert feed |
| Explain layer | Human-readable explanation of a computed charge or queue change, citing the clause | LLM text always rendered beside the deterministic number and its citation |

### 2.2 Where LLMs belong

LLMs do (a) first-pass schema discovery on a new document type, (b) extraction fallback on malformed pages, (c) drafting rule-module code from a tariff order for human review, and (d) explanations. They are **never the source of a number** that reaches a bill, a bid or a prediction. The red team's point that the parse layer is reproducible by any frontier model [HYP, red_team_counterevidence.md Q3] means the only defensible asset is the verified ledger and rule library.

### 2.3 Versioning and provenance

Every regulation, order and CTUIL sheet is an immutable artefact; rule modules carry the artefact hash they were written from; every output carries rule-module version and input hashes. Reversals are routine — TN wind banking re-litigated at least four times [VF/IC, f2_f3_commercial_facts.md F2-Q2]; MERC-ordered wheeling refunds in 2025 [VF, [MERC](https://merc.gov.in/wp-content/uploads/2025/06/Final-Order-in-Case-Nos.-131-of-2024.pdf)]; CERC restoring 2,300 MW and 400 MW of revoked connectivity [VF-sec, [SolarQuarter](https://solarquarter.com/2025/12/06/cerc-directs-restoration-of-2300-mw-renewable-connectivity-condones-delay-under-gna-regulations/)] — so a recomputation must be reproducible under both the rule version in force on the billing date and the version a regulator later imposed.

### 2.4 Test strategy

**Golden files**: three hand-verified extractions per document type (clean, layout-drifted, corrupt-stream) in CI. **Rule tests**: each formula against worked examples from the order text and, once available, a real bill, tolerance ≤₹1 per line. **Snapshot tests**: replay the diff between consecutive CTUIL releases against the alert feed produced at the time. **Property tests**: 15-minute accounting must conserve energy (injection = drawal + banked + lapsed + losses) per block and month.

### 2.5 Legal constraints per source

| Source | Terms found | Design consequence |
|---|---|---|
| CTUIL site and PDFs | "Contents of this website may not be reproduced partially or fully, without due permission from CTUIL" [VF, [policy](https://ctuil.in/copyright-policy)]; margins PDF stamped "RESTRICTED" on every page [VF]; all liability on the user [VF, [disclaimer](https://ctuil.in/disclaimer)] | Re-publishing parsed tables in a paid product needs written permission (gate A0, §6.4); derived alerts are a grey area; private use for a customer's own applications is the fallback. Enforcement practice unknown — aggregators re-publish today [UNK] |
| IEX prices | "personal, non-commercial purpose"; no download/copy/extract/distribute without authorisation [VF, [ToU](https://www.iexindia.com/terms-of-uses)]; 15-min DAM data from 1 Apr 2022 downloadable without login under "all rights reserved, quotation with attribution" [VF, [snapshot](https://www.iexindia.com/market-data/day-ahead-market/market-snapshot)] | Internal backtests feasible; any product use needs a licence (cost *not established; must be verified*) |
| CERC/SERC | No terms of use; Hindi disclaimer only [VF, [CERC](https://cercind.gov.in/)] | Lowest risk; clauses can be quoted |
| Karnataka SLDC lists | Public XLSX/PDF downloads [VF, [kptclsldc.in](https://kptclsldc.in/WBUpload.aspx)]; terms not examined | Usable for prospecting; redistribution terms *not established* |
| RPC weekly DSM files (SRPC/NRPC/NERPC; WRPC secondary) | No licence or terms text on any RPC site [VF absence, [SRPC](https://srpc.gov.in/commercial/), [NRPC](https://www.nrpc.gov.in/comm/dsa.html)]; published under CERC DSM transparency obligations [EST, india_electricity_data_sources.md Q9] | Least-restricted route to ISTS plant-level 15-minute ground truth; retention depth and revision handling must be verified |
| CEA | Prior permission by email, attribution, no modification [VF, [CEA](https://cea.nic.in/api/websitepolicy/pdf/view/en/2)] | Send the permission email early |
| Maharashtra SLDC | Prior permission even to hyperlink; "All Rights Reserved" [VF, [MSLDC](https://mahasldc.in/website-policies)] | No scraping for a product without permission |
| Customer bills, statements, telemetry | Customer-supplied; no third-party privacy issue identified [VF, red team Q5] | Pilot agreements need a data-rights clause so anonymised bill/settlement pairs can be retained |
| Grid-India/RLDC/SLDC terms | HTTP 503 on all attempts [UNK] | Build nothing on them until read |

## 3. Finalist F2 — C&I open-access settlement and procurement engine (lead)

### 3.1 Minimum product

A monthly **settlement recomputation** for one consumer–generator pair in one state (Karnataka first): (i) recomputed bill line by line under the applicable regime, (ii) discrepancy list with ₹, confidence and clause, (iii) 15-minute banking/lapse statement, (iv) signed-off "recoverable amount" memo. The procurement optimiser is the second module.

### 3.2 Data inputs and sources

| Input | Source and form | Status |
|---|---|---|
| DISCOM OA bill (monthly) | Customer export; an MSEDCL sample itemises drawal, injection, banked and over-injected units [VF, [MSEDCL](https://mahadiscom.in/consumer/wp-content/uploads/2024/12/155-519_170019002163_202411-oa-print1.pdf)]; consumers "receive two separate bills" [VF, [OAE](https://www.openaccessexchange.com/)] | ESCOM bill templates *not established; obtain from design partner* |
| Generator invoice | Customer export | Format [UNK] |
| SLDC/DISCOM energy-accounting and banking statements | Customer export; Karnataka SLDC states it does "Energy Accounting" but publishes no monthly statements [VF, [kptclsldc.in](https://kptclsldc.in/)]; Delhi SLDC publishes monthly short-term OA invoices [VF, [delhisldc.org](https://delhisldc.org/)]; Kerala had no 15-minute accounting for short-term OA consumers [VF-snippet, [KSEB](https://kseb.in/uploads/Downloadtemsuppy/b-17149864122140522808.pdf)]; Maharashtra SLDC lists REMC weekly deviation statements per QCA (16 QCAs) but the list is JS-loaded and contents unverified [VF existence, [MSLDC](https://mahasldc.in/reports/remc-weekly-deviation-statements)]; Karnataka SLDC has no DSM/QCA statement pages [VF, india_electricity_data_sources.md Q4] | Intra-state statements are unpublished (Karnataka) or QCA-gated (Maharashtra), so customer exports are the only route; whether 15-minute statements reach Karnataka consumers as exports is F2's largest unknown |
| 15-minute meter data | Customer export (ABT/AMR) | Availability per ESCOM *not established* |
| Rules and tariff orders | KERC OA Regulations 2025: 100 kW threshold, SLDC nodal, monthly banking without carry-forward, banking 8% "or as decided", standby 125%, relinquishment = 3 months of charges, under-utilisation penalties [VF-sec/IC, [SolarQuarter](https://solarquarter.com/2025/04/02/karnataka-introduces-new-open-access-regulations-2025-to-boost-power-accessibility-and-renewable-energy/), [Renewable Watch](https://renewablewatch.in/2025/04/25/karnataka-announces-open-access-regulations-2025/)]; legacy annual 2% in-kind banking for 2018–2023 applicants [VF, [SolarQuarter 2023](https://solarquarter.com/2023/08/17/kerc-issues-vital-directive-on-wheeling-charges-and-banking-for-renewable-power-projects/)]; additional surcharge ₹0.82/kWh (FY26) → ₹0.40 from Mar 2026, not on captive drawal [IC, [Mercom](https://mercomindia.com/karnataka-halves-additional-surcharge-for-open-access-power)]; TNERC GEOA 2025: 8% in-kind banking within billing cycle, 14%/12-month legacy wind, 75% buy-back, standby 125% [VF-sec, [SolarQuarter](https://solarquarter.com/2025/09/26/tnerc-issues-new-regulations-2025-for-green-energy-open-access-2025-in-tamil-nadu)]; Maharashtra wheeling by voltage, CSS ₹1.50–2.20 indicative [EST, [Bridgeway](https://bridgewaypower.in/blog/solar-wheeling-charges-maharashtra-merc-2026)]; GEOA Rules 2022: banking ≥ monthly, ≥30% of monthly consumption, 8% in kind [VF, [IEEFA/JMK](https://ieefa.org/sites/default/files/2024-12/Impact%20of%20Green%20Energy%20Open%20Acess_Dec2024.pdf)] | FY26–28 Karnataka ₹/kWh wheeling and SLDC charges sit in unparsed tariff-order annexures [UNK] |
| Consumer–generator pairings (prospecting) | Karnataka SLDC: 556 IPPs / 4,924 MW; ≈922 distinct consumer organisations [VF count / EST dedupe, [kptclsldc.in](https://kptclsldc.in/WBUpload.aspx)] | GESCOM/HESCOM lists failed to download [UNK] |

### 3.3 Pipeline

1. Bill PDF → typed line items (deterministic parser per ESCOM template; flagged LLM fallback).
2. 15-minute injection and drawal → block table with regime-specific loss factors.
3. **Regime identification** — which banking/charge regime binds the pair (legacy WBA vs 2025 regulation vs GEOA; captive vs third-party; voltage; term), from WBA date and the SLDC spreadsheet's captive flag [VF]. Each target state runs two or more concurrent regimes [INF, f2_f3 F2-Q2], so this precedes all arithmetic.
4. Energy accounting per block; residual to banking; monthly (or legacy annual) settlement; lapse and buy-back.
5. Charge engine: wheeling, transmission, CSS, additional surcharge with captive exemption, banking in kind, standby, SLDC charges, under-utilisation and relinquishment events.
6. Compare with billed amounts → discrepancy list with ₹ and clause → monthly report and cumulative recoverable ledger.

### 3.4 Analytical methods and where each discipline belongs

| Component | Method | Discipline |
|---|---|---|
| Charge recomputation | Effective-dated deterministic rule engine | Rules |
| 15-minute energy accounting | Conservation-checked block arithmetic; banking state machine | Rules + metering physics |
| Banking/lapse simulation | Monte-Carlo over the customer's historical load and generation under each regime | Statistics |
| Procurement optimiser | LP/MILP: contracted MW by source (group captive, third-party, rooftop, DISCOM/DERS), banking share, term; constraints: 15-minute load, ≥26% equity / ≥51% consumption for captive status [V-BLOG, [SurgePV](https://www.surgepv.com/solar-compliance/india/guides/open-access)], OA participants barred from the 20% DERS headroom [VF, [SolarQuarter](https://solarquarter.com/2026/04/02/kerc-extends-discounted-energy-rate-scheme-till-fy28-eases-open-access-rules-for-consumers-in-karnataka/)]; objective: expected landed cost across tariff scenarios; open-source MILP solver, seconds per site | Operations research |
| Bill anomaly detection | Control charts per line item vs the customer's history and peer sites, run before the rule engine | Statistics |
| Explanation and dispute drafting | LLM over the discrepancy list with clause citations | LLM, human-verified |

### 3.5 Baseline

**What the customer paid, as billed**, and what they would have paid under the regime they believe applies; the product's value is the signed difference after expert review. CEEW's free calculator is frozen at FY2021-22 charges and does no scheduling, DSM or reconciliation [S-AN, [CEEW](https://www.ceew.in/cef/shared/CEEW-CEF-Open-access-landed-cost-calculator-methodology.pdf)] — useful only as a staleness reference.

### 3.6 Metrics and limitations

| Metric | Definition | First-experiment target |
|---|---|---|
| Recoverable ₹/yr | Verified discrepancies in the customer's favour over 12 months | ≥₹5 lakh/yr per site (brief §7) |
| % of annual OA bill | Recoverable ÷ OA-related charges | median ≥1.5% |
| Flag false-positive rate | Expert-rejected flags ÷ flags raised | ≤20% after two months [EST target] |
| Reconciliation closure rate | Discrepancies credited or written off with reason within 90 days ÷ raised | reported; no target until pilots |
| Time to monthly settlement | Receipt of exports → signed memo | ≤2 working days |

Limitations: over-billing is documented but episodic and often fixed for many consumers at once by commission order (23 OA consumers in one case [single-source, [APTEL 366/2017](https://www.aptel.gov.in/judgements/Judg2018/A.No.%20366%20of%202017%20&%20IA%20No.%20933%20of%202017_28.11.18_J.pdf)]), so the per-consumer pool may be lumpy [HYP, red team Q2]; error frequency is *not established*. Incumbents bundle settlement: Tata Power Trading (DSM and OA reconciliation) [VF, [Tata Power](https://tatapower.com/what-we-do-nav/energy-services/power-trading-2)], CES (bill-settlement verification) [VF-snippet], BridgeIT (1M+ bills, 100+ DISCOMs) [EST, [BeBee](https://bebee.com/in/companies/bridgeit)].

### 3.7 Costs, skills, agents vs specialists

Data and compute cost is near zero: customer files, free PDFs, a 35,040-row block table and a single-site MILP run on a laptop; <₹3,000/month for several pilots [EST]. Coding agents implement parsers, the accounting state machine, the MILP, reports and tests. They cannot decide which regime binds a legacy WBA with a pending Supreme Court matter [VF, SolarQuarter 2023], how an ESCOM applies the captive exemption, or whether a refund is enforceable — a regulatory/tariff expert does that, and a CA signs the memo the customer takes to the DISCOM. The founder needs working knowledge of OA charges, 15-minute accounting and LP formulation.

### 3.8 Build scope

- **1 week**: one Karnataka regime (2025 regulation, third-party, HT), one ESCOM bill parser, accounting engine with conservation tests, synthetic 12-month run.
- **30 days**: legacy WBA, 2025 and GEOA/captive regimes; standby, under-utilisation and surcharge exemption; TN GEOA 2025; anomaly charts; first real backtest (F2-A).
- **90 days**: Maharashtra module with MERC refund logic, procurement MILP with DERS-vs-OA scenarios, multi-site consumers, dispute drafting, five-customer pilot reporting.

### 3.9 What would make F2 infeasible

Statements not obtainable as exports (*not established either way; the first design-partner conversation must resolve it*); rule changes outpacing the library (four TN re-litigations; annual Karnataka surcharge swings) despite effective-dated modules; incumbent bundling at zero visible fee ("zero upfront" advisory [VF, OAE]), tested by the brief's F2-B interviews; a recoverable pool <0.5% of bill for most sites.

## 4. Finalist F1 — ISTS connectivity / grid-access intelligence

### 4.1 Minimum product

A versioned, geocoded substation ledger joined across CTUIL publications, with (i) change alerts and (ii) a calibrated probability that an application becomes effective within 12 months. **Legal gate**: nothing is sold before CTUIL gives written permission (A0, §6.4).

### 4.2 Data inputs

| Input | Form | Note |
|---|---|---|
| "Connectivity to be Made Effective" list | HTML table, 636 rows, technology/region/state filters, PDF/XLS export icons (JS; output unconfirmed) [VF, [CTUIL](https://ctuil.in/connectivity-effective-list)] | **Already filterable/exportable — an input, not a product.** Includes CTUIL's own *expected effective date*, which becomes a baseline |
| Grant lists | Structured PDF, 200+ rows: application ID, applicant, submission date, region, type, MW, substation, in-principle/firm dates, status [VF, [CTUIL Jul 2025](https://www.ctuil.in/uploads/assets/175747971577July%2025_Main-Connectivity%20under%20GNA.pdf)] | Grants page lists monthly PDFs Jan–Aug 2026 plus an archive [VF, [CTUIL](https://ctuil.in/gna2022updates)]; completeness back to 2023 not enumerated |
| Bay/substation margins (solar/non-solar hours) | PDF only, three files per release, archive at `/renewable-energy-ol` [VF, [CTUIL](https://ctuil.in/renewable-energy)]; RESTRICTED | The genuine parsing gap, but CTUIL keeps the archive [VF, red team Q1] |
| Application status | API-backed page `/nswsapi/gna` [VF] | |
| Cluster declaration (16 Jul 2026), Reg 11(C) reallocation notices, BESS MWh advisory (14 Sep 2026) | PDFs [VF, [ctuil.in](https://www.ctuil.in/)] | |
| 11/SM/2026 eligible-entities list (17 Sep 2026) | PDF with LoA, PPA status, application ID, substation, dates [VF, [CTUIL](https://ctuil.in/uploads/assets/178963420036Final%20List%20of%20eligible%20entities%20as%20per%2011SM2026_rev%2001.pdf)] | ~70 developers; the prospect list |
| CERC orders | Restorations, compensation, 11/SM/2026 [VF, [CERC](https://cercind.gov.in/2026/orders/11-SM-2026.pdf)] | Label-noise source |
| Compensation rate | ₹1,612.15/MW/day, 15-month cap then revocation [VF, [CTUIL](https://ctuil.in/uploads/assets/178645696705Compensation%20charges%20as%20per%20CERC%20order%20dtd%2003-08-2026%20to%20be%20uploaded%20on%20website.pdf)] | Cost-of-delay input |
| Substation coordinates | "Tentative Coordinates of RE PS" [VF] | Geocoding |
| Inter-regional TTC/ATC | Nine "indicative only" declarations Oct 2019–Apr 2025 naming the binding element per corridor [VF, [CTUIL](https://ctuil.in/ttc-atc-declaration)] | Context feature only; no nodal ATC exists publicly |

### 4.3 Pipeline and methods

Fetch → extract → normalise applicant/substation names → one row per application-month (panel) → features as known at each month → labels from later snapshots → train/evaluate → alerts and probabilities to the ledger.

- **Rules**: queue position, cluster membership, bay availability, 15-month compensation clock, 60-day election windows.
- **Statistics/ML**: binary classifier (logistic regression, gradient-boosted trees on CPU; isotonic calibration) for "effective within 12 months"; features knowable at grant: substation, region, state, technology, MW, cluster, application and in-principle dates, voltage, PPA status, substation margin at grant, applications ahead at the same substation. Prediction is the only layer the red team accepted as defensible [HYP, red team Q1].
- **Physics**: none — load flow and ATC need network models the public cannot access [EST, solar_forecasting_feasibility.md §E].
- **LLM**: explanation of orders and alerts; draft "which 11/SM/2026 option" memo for human review.

### 4.4 Backtest design (Experiment F1-A)

| Element | Specification |
|---|---|
| Universe | All applications in grant and effectiveness lists, Jan 2023–Oct 2026 (several hundred; the effectiveness list alone has 636 [VF]) |
| Target | Effective within 12 months of the firm (or in-principle) start date recorded at grant; secondary: months to effective |
| Features | As above; strictly knowable at the grant month |
| Baselines | (1) base rate; (2) same-substation last-known outcome; (3) CTUIL's published expected date, converted to yes/no at 12 months |
| Leakage controls | Time split: train ≤ Dec 2024, validate 2025 H1, test 2025 H2 (windows close by Oct 2026); no features from later snapshots; restorations and 11/SM/2026 surrenders treated as censoring and reported separately |
| Metrics | AUC, Brier, 10-bin reliability diagram, MAE in months |
| Pass / fail | AUC ≥0.70 **and** Brier better than baseline (3); fail: AUC <0.60 or no gain over CTUIL's own date; inconclusive: <150 usable test rows |

With ≈300 test rows and a positive rate near 40%, the standard error of an AUC near 0.70 is ≈0.03 — enough to separate 0.70 from 0.60 [EST].

### 4.5 Baseline, limitations, costs, skills

Stranded connectivity is demand-side — 40,420 MW of LoAs → 2,338 MW PPAs; 22,054 MW without PPAs; ≈15.7 GW released by order [VF, CERC 11/SM/2026] — and outcomes turn on petitions, which CTUIL lists cannot see; expect modest skill. Costs ≈₹0 (free PDFs, <10⁵ rows, seconds to train). Agents build the scraper, parsers, panel and models; a specialist interprets procedure ("firm", "effective", "deemed GNA" are not defined in the notes), labels edge cases (partial surrender, reallocation, restoration) and runs the CTUIL conversation. Law firms, not software, are today's advisor [VF, red team Q4].

### 4.6 Build scope

- **1 week**: send A0; scrape effectiveness list and all grant PDFs since 2023; panel; baselines; first classifier; AUC/Brier table.
- **30 days** (only if A0 not refused and F1-A shows skill): margins parser with corrupt-page fallback, cluster and 11/SM/2026 joins, geocoding, alert feed, calibration report, one-page substation sample for interviews.
- **90 days**: private-use alerting for 3–5 developers' own applications; reallocation-option analysis; BESS MWh-enhancement screen.

### 4.7 What remains if prediction shows no skill; infeasibility

Aggregation alone is "already free" — CTUIL's table plus Excel replicates 70–80% of the value [HYP, red team Q4]. What survives: a monitoring/interpretation service priced like a newsletter, internal use for F2/F3 customers' own applications, and the ledger as an F3 siting input. Per the brief: refusal or no skill → F1 is dead as a product; keep as an internal research tool. Further killers: CTUIL ships a margins CSV/dashboard; the GNA 4th amendment (draft, not notified by 16 Oct 2026 [VF, [CERC](https://cercind.gov.in/Draft_reg.html)]) lets CTUIL close applications and clears the backlog.

## 5. Finalist F3 — FDRE/BESS dispatch, availability-compliance and bid optimisation

### 5.1 Minimum product

Not a bidder. A **contract-compliance and dispatch-planning engine** for an availability-paid standalone BESS or FDRE project: daily dispatch plan honouring cycle budget, RTE and availability tests; monthly availability/DFR certificate with LD exposure; optional bid file for any merchant tranche. The red team's substitution of a compliance pilot for the bid-optimiser wedge is adopted [HYP, red team Q9].

### 5.2 Data inputs

| Input | Source | Constraint |
|---|---|---|
| IEX DAM/RTM 15-min prices | Public from 1 Apr 2022, no login [VF, [IEX](https://www.iexindia.com/market-data/day-ahead-market/market-snapshot)] | Non-commercial ToU — licence for product use [VF]; market coupling pending (Supreme Court admitted IEX's appeal; CERC rules "shortly"; not notified by 16 Oct 2026 [VF-sec, red team Q6]) weakens the 2022–26 series as a guide to future prices |
| Contract terms | MSEDCL BESPA: 15 years, ≥6,300 cycles, 95% annual availability, 85% monthly AC-AC RTE, indigenous EMS software [VF, [Energetica](https://www.energetica-india.net/news/oriana-bsl-engineering-armee-infotech-gk-energy-among-winners-in-msedcl-4-gwh-bess-auction)]; NVVN-Kerala 420 cycles/yr; KPTCL two cycles/day [VF]; FDRE-X: 4,000 kWh/MW/day in four buyer-designated peak hours, shortfall at 1.5× PPA tariff capped at 400 MWh per 100 MW, ≤5% market sourcing [VF, [Energetica](https://www.energetica-india.net/news/seci-floats-tender-for-1200-mw4800-mwh-fdre-supply)]; DFR 90% peak / 80% off-peak / 90% annual [IC] | Merchant rights in state BESPAs *not established* |
| DSM for storage | Standalone ESS = general seller; co-located ESS under WS rules while RE injects [VF, [CERC DSM 2024](https://www.cercind.gov.in/regulations/192-Noti.pdf)]; infirm power before trial run ≤₹2.00/kWh [VF, [notification 208](https://cercind.gov.in/regulations/208-notification.pdf)] | |
| Charging rules | CMETS-WR draft: 2-h minimum, RE-only charging, no ISTS drawal; RVPN draft: solar 10:00–15:00 / wind 00:00–04:00 windows, SLDC may curtail [VF, [JMK](https://jmkresearch.com/indias-emerging-merchant-bess-market-faces-its-first-regulatory-test/)] | Drafts; status *must be verified* |
| Weather | ECMWF IFS/AIFS open data, 0.25°, `ssrd`, 2 m temperature, 10/100 m wind, CC-BY-4.0, 12-run rolling archive [VF, [ECMWF](https://www.ecmwf.int/en/forecasts/datasets/open-data)]; Open-Meteo $29/$99 per month with forecast-as-issued history [VF/IC, [Open-Meteo](https://open-meteo.com/en/pricing)] | Open-data latency in hours *not established*; satellite irradiance over India unverified [UNK] |
| Plant-level 15-minute ground truth (ISTS plants) | RPC weekly DSM files: SRPC zip with one CSV per ISTS RE entity (122 entities; 672 blocks of `available_capacity, sch_total, act_total, dev, dev_perc, rate, ppa_rate` plus charges) [VF, [SRPC](https://srpc.gov.in/wp-content/uploads/2026/10/051026.zip)]; NRPC weekly `Supporting_files.xlsx` with block-wise `DC_Stations`, `Solar_availability`, `Act_Inj_Gen_Stations`, weeks listed from 29 Mar 2021 [VF, [NRPC](https://www.nrpc.gov.in/comm/dsa.html)]; WRPC block-wise data per weekly statement [secondary]; Prayas built FY24–FY25 sets for 24–40 plants per region from WR/SR files [VF, [Prayas](https://energy.prayaspune.org/images/pdf/CERC_suo-motu_proposal_on_X_for_RE-DSM_Prayas_comments_17-10-25.pdf)]. Block-wise DSM normal rate and DAM ACP also sit in these files (SRPC `commercial_actual_marketrate2022.csv`, `commercial_dam_acprate.csv`; NRPC `Normal_Rate`) — an unlicensed route to part of the price history, not to full RTM series [VF] | ISTS plants only; weekly lag with R1/R2 revisions; no stated licence; historical retention unverified [UNK] |
| Asset telemetry | Customer EMS/SCADA exports: SoC, MW per block, availability flags, temperatures, auxiliaries | Required for the SoC/availability side of compliance; no public substitute |
| Benchmarks | Ember: merchant revenue INR 2.4 m/MWh (2025), LCOS INR 4.5/kWh, break-even ₹7.56/kWh charging at ₹2.6 [S-AN, [Ember](https://ember-energy.org/latest-insights/the-age-of-storage-batteries-primed-for-indias-power-markets/chapter-3-the-economics-of-merchant-bess/)]; FY26 IEX arbitrage spread ₹4.81/kWh [IC, [Mercom](https://mercomindia.com/iex-revenue-rises-11-in-q1-fy-2027-as-power-trading-volume-grows)]; open Indian model BattMan [VF, [Ember](https://ember-energy.org/latest-insights/the-age-of-storage-batteries-primed-for-indias-power-markets/supporting-materials)] | |

### 5.3 MILP formulation sketch

Index t over 15-minute blocks (96/day); daily horizon with a rolling monthly cycle budget.

- Variables: charge c_t ≥ 0, discharge d_t ≥ 0, state of charge s_t, binary mode m_t (no simultaneous charge/discharge), delivery shortfall e_t ≥ 0 in designated hours, monthly availability shortfall a ≥ 0.
- Dynamics: s_{t+1} = s_t + η_c·c_t·Δt − d_t·Δt/η_d with η_c·η_d ≥ 0.85 monthly (MSEDCL test); s_min ≤ s_t ≤ s_max (degradation-adjusted).
- Power: c_t ≤ P_max·(1−m_t); d_t ≤ P_max·m_t.
- Cycle budget: Σ_t d_t·Δt per month ≤ cycles_month × E_rated (6,300/15 yr ≈ 420/yr ≈ 35/month).
- Charging source (draft rules): c_t ≤ RE_t (forecast RE) and c_t = 0 outside permitted windows.
- FDRE delivery: Σ_{t∈peak} d_t·Δt + e_day ≥ 4,000 kWh/MW × P_contract; monthly penalty = 1.5 × tariff × Σ e, capped at 400 MWh per 100 MW; per-block DFR ≥90% in peak hours.
- Availability: unavailable blocks ≤ 5% annually; LD as a convex cost on a.
- DSM: deviation from committed schedule priced per CERC bands (general seller for standalone; WS rule for co-located).
- Objective: maximise Σ_t price_t·(d_t − c_t)·Δt (merchant tranche or FDRE's ≤5% allowance) − penalties − degradation cost; for pure availability contracts this reduces to minimising expected LDs and cycle-budget breaches.

Solvable with an open-source MILP solver on CPU in seconds per day; a year's backtest in minutes.

### 5.4 Forecasting component

Consume NWP outputs; do not run weather models (open-weight AI weather models need H100-class GPUs [VF, solar_forecasting_feasibility.md §A]). ECMWF `ssrd` → clear-sky index (pvlib) → 15-minute downscaling → plant model (pvlib, BSD-3) → power; wind via generic power curves on 100 m wind. Baselines: smart persistence (clear-sky-index persistence) and the climatology–persistence blend [VF-snippet, [Yang 2019](https://scholar.hit.edu.cn/en/publications/standard-of-reference-in-operational-day-ahead-deterministic-sola/)]. Metrics: nMAE/nRMSE vs installed capacity (daylight blocks), block-within-band share at ±5% solar / ±10% wind of AvC, skill vs smart persistence, stratified by monsoon regime and lead (day-ahead vs the 7th/8th-block revision ≈1.5–2 h [VF, [CERC 14/SM/2023](https://www.cercind.gov.in/2023/orders/14-SM-2023.pdf)]). Reference points: one Indian plant-level NWP chain reached 5.59% day-ahead nMAE [VF-snippet, [EGU22](https://meetingorganizer.copernicus.org/EGU22/EGU22-9393.html)]; Grid-India's 16-plant simulation found plants inside tightened bands only 45–58% (solar) and 32–73% (wind) of blocks [VF-sec, [Energetica](https://www.energetica-india.net/news/cerc-proposes-phased-schedule-based-deviation-mechanism-for-wind-and-solar-from-april-2026)]. Ground truth: for ISTS-connected plants the RPC weekly files supply 15-minute AvC, schedule and actual per entity (§5.2), so plant-level forecast and DSM-exposure backtests are possible without customer data — reversing the earlier feasibility note's conclusion [VF, india_electricity_data_sources.md Q1; brief §8]. State-embedded plants have only aggregates (all-India hourly solar/wind, Sep 2021–Jun 2025, CC BY 4.0 [VF, [Mendeley](https://data.mendeley.com/datasets/y58jknpgs8)]). Live telemetry remains necessary for intraday (7th/8th-block) revisions and for SoC/availability.

### 5.5 Disciplines, baselines, metrics, limitations

Rules: contract clauses, cycle counting, DSM pricing. Physics: SoC dynamics, RTE, pvlib. Statistics: price-scenario bootstrap by hour and season; forecast error distributions. ML: light NWP post-processing per plant. OR: the MILP. LLM: certificate and clause explanations for review. Baselines: (a) naive "charge three cheapest / discharge three dearest blocks"; (b) BattMan; (c) the DISCOM's dispatch instruction. Metrics: ₹/MWh/yr captured vs Ember; LD exposure avoided; cycle adherence; forecast metrics above. Limitations: Tier-2 awards are DISCOM/SECI-dispatched [VF/IC]; the merchant fleet (≈80% of 6.8 GWh, Jun 2026) is Adani and ACME [VF, JMK]; DSM escalation is stayed for NSEFI petitioners [VF-sec, [PowerPeak](https://powerpeakdigest.com/karnataka-hc-stays-cerc-dsm-2024/)] and deferred for new WS sellers to bids on/after 1 Jan 2027 or COD on/after 1 Jan 2029 [VF, notification 208].

### 5.6 Costs, skills, scope, infeasibility

Costs: ₹0 for the price backtest plus an IEX licence of unknown cost; ≈$15–40/month infrastructure and $99/month for Open-Meteo history [EST, §F]; telemetry customer-supplied. Agents implement the MILP, scenario generator, pvlib pipeline, backtests and certificates; a specialist reads BESPA/PPA clauses authoritatively (availability tests, LD computation), validates SoC/degradation against OEM warranty, and handles SLDC/RLDC procedure. No IEX membership is needed — bids go through the customer's proprietary membership or a trader member [VF, [IEX](https://www.iexindia.com/membership)].

- **1 week**: IEX 2022–26 ingested; MILP with cycle budget and RTE; perfect-foresight and price-persistence backtests vs naive heuristic and Ember.
- **30 days**: FDRE penalty/DFR and charging-window constraints; scenario bootstrap; RPC-file ingestion with revision de-duplication; ECMWF→pvlib day-ahead forecast vs smart persistence on 10–20 ISTS solar plants from SRPC/NRPC files; one public BESPA clause extraction for expert review.
- **90 days**: compliance module on one design partner's 6–12 months of telemetry; monthly availability/RTE/cycle certificate vs the customer's own; LD report.

Infeasible if: IEX licence refused or unaffordable; draft charging rules adopted (headroom collapses to RE-charged, SLDC-overridable schedules); Tier-2 SCODs (2027–28 for most state awards [EST, f2_f3 F3-Q1]) outlast the runway; OEM EMS bundles dispatch (Envision at Juniper; Fluence–ReNew JV [VF/IC]).

## 6. Validation experiments

Priority: F1-A0 (one email), F2-A (kills or confirms the lead), F1-A, F3-A — all ≈₹0. The brief's commercial interviews (F2-B, F1-B) run in parallel and gate the same decisions.

### 6.1 F2-A — Settlement recomputation on real bills (lead)

- **Hypothesis**: for Karnataka OA/group-captive consumers of 1–20 MW, recomputing 12 months of bills and statements under the applicable KERC regime finds recoverable overcharges plus avoidable banking-lapse/DSM losses ≥1.5% of the annual OA bill and ≥₹5 lakh/yr for most sites.
- **Supporting**: median ≥1.5% **and** ≥₹5 lakh/yr for ≥3 of 5 sites (brief §7). **Falsifying**: <0.5% for ≥4 of 5. **Inconclusive**: <3 sites with complete 12-month exports, or discrepancies the expert cannot adjudicate.
- **Evidence and how obtained**: 12 months of DISCOM bills, generator invoices, SLDC/DISCOM accounting and banking statements and 15-minute meter data from 3–5 consumers, via personal network, KASSIA / Peenya Industries Association / FKCCI energy committee or a consultant partner (brief §7); prospects from the SLDC lists, preferring multi-installation consumers (Shahi Exports, Wipro, Infosys, Manyata, RMZ) [VF, [kptclsldc.in](https://kptclsldc.in/WBUpload.aspx)].
- **Procedure and baseline**: regime identification → accounting → charge engine → discrepancy list → blind review by a tariff expert → agreed recoverable ₹; baseline = billed amounts (and the customer's own reconciliation if any).
- **Sample/period**: 12 months per site covers a full tariff year and the FY26→FY27 surcharge switch (₹0.82 → ₹0.40 [IC]); 5 sites so the median is not one outlier; 24 months where available to catch retroactive true-ups.
- **Metrics**: recoverable ₹/yr, % of bill, expert-rejected flag rate, time to settlement.
- **Time/cost**: ≤14 days after data receipt; ≈₹0 compute; expert review ≈₹25–50k if paid [EST].
- **Establishes**: money exists and the engine finds it. **Does not**: willingness to pay, recoverability from the DISCOM in practice, population error frequency.
- **Next**: pass → 90-day build and success-fee pilots; fail → re-scope to procurement optimisation or stop; inconclusive → five more sites via an association.

### 6.2 F1-A — Backtest of effective-within-12-months on 2023–2026 CTUIL lists

- **Hypothesis**: features knowable at grant predict "effective within 12 months" with AUC ≥0.70 and a better Brier score than CTUIL's own expected date.
- **Supporting / falsifying / inconclusive**: as in §4.4.
- **Evidence**: effectiveness list (JS pagination), monthly grant PDFs since 2023, 11/SM/2026 lists, CERC restoration orders [VF]; no customer needed.
- **Procedure, baselines, metrics**: §4.4; all 2023–2026 applications, time-split so every test window has closed.
- **Time/cost**: ≤7 days, ≈₹0.
- **Establishes**: whether prediction from public records is possible. **Does not**: willingness to pay or legality of sale (A0).
- **Next**: skill + A0 positive → 30-day build; skill + A0 refused → private-use alerting only; no skill → internal research tool.

### 6.3 F3-A — Public-price dispatch backtest and compliance simulation

- **Hypothesis**: on 2022–2026 IEX 15-minute DAM/RTM prices, a cycle- and RTE-constrained MILP with day-ahead price persistence captures ≥70% of perfect-foresight arbitrage value and beats the naive heuristic by ≥15%; and an FDRE-style delivery constraint (4,000 kWh/MW/day in a 4-hour evening window) is met on ≥90% of days with RE-only charging from a forecast RE profile.
- **Supporting**: both hold across seasons including the near-zero solar-hour price days of 2025–26 [S-AN/IC]. **Falsifying**: <50% of perfect foresight, or RE-only charging fails on >20% of days (the binding constraint is then asset/contract design, not dispatch). **Inconclusive**: IEX series gaps.
- **Evidence**: public IEX DAM (from 1 Apr 2022) and RTM series [VF]; FDRE-X and MSEDCL terms [VF]; ECMWF/Open-Meteo forecast-as-issued irradiance for a Rajasthan/Gujarat site; all-India aggregate for sanity checks. **Commercial use of IEX data needs a licence**; this is internal validation.
- **Procedure**: §5.3 MILP under (a) perfect foresight, (b) previous-day price persistence, (c) bootstrap scenarios; compare with the naive heuristic and BattMan; report ₹/MWh/yr vs INR 2.4 m/MWh and LCOS INR 4.5/kWh.
- **Sample/period**: ≈1,500 days (2022–26) so monsoon, summer-peak and solar-glut regimes all appear; results by year because coupling may change price formation.
- **Metrics**: ₹/MWh/yr; % of perfect foresight; delivery-constraint satisfaction; cycles used; aggregate forecast nMAE/nRMSE.
- **Time/cost**: ≤7 days; ≈₹0 (+$99/month if Open-Meteo history is used).
- **Establishes**: the optimisation has value and is tractable. **Does not**: availability-contract value (needs telemetry), legality of product use of IEX data, or that Tier-2 developers own the decision.
- **Plant-level add-on (from brief §8)**: on 12 months of SRPC/NRPC 15-minute files for ≥10 ISTS solar plants, (i) reproduce each plant's published weekly DSM charges from `available_capacity`, `sch_total`, `act_total` and the published rates within ±10% (validates the rule engine), and (ii) test whether the ECMWF→pvlib day-ahead forecast beats smart persistence by ≥20% on nMAE vs capacity and raises the ±5% within-band share. Supporting: both hold; falsifying: no skill over smart persistence (the forecasting component is then bought, not built). Cost ≈₹0; +5 days.
- **Next**: pass → seek one design partner's telemetry while watching charging-rule drafts and coupling; fail → 2027+ watch item.

### 6.4 F1-A0 — Written permission from CTUIL

- **Hypothesis**: CTUIL will permit reuse of published connectivity/margin data in a commercial product with attribution.
- **Supporting**: written permission or a licensing route. **Falsifying**: refusal, or confirmation that RESTRICTED bars redistribution. **Inconclusive**: no reply in 30 days (treat as refusal for planning; tolerated aggregator practice [UNK] is not a licence).
- **Procedure/cost**: one email citing the policy [VF, [ctuil.in/copyright-policy](https://ctuil.in/copyright-policy)], describing derived use (analytics, alerts), requesting terms; ≈₹0; ≤30 days.
- **Establishes**: whether F1 can be sold at all. **Next**: as in §6.2.

## 7. Staged path to industrial access

No live integration is needed for any first experiment: F2-A, F1-A, F3-A and A0 run on files and public pages. Conversely, **public data alone does not prove production readiness** — it cannot show recoverability from a DISCOM, plant-level forecast accuracy, or compliance under real telemetry.

| Stage | F2 | F1 | F3 |
|---|---|---|---|
| 1. Public-data prototype | Rule library from KERC/TNERC/MERC orders; synthetic site; SLDC lists for prospecting | Scrape, panel, baselines | IEX backtest MILP; RPC-file ingestion; forecast pipeline |
| 2. Historical backtest | — (needs customer bills) | F1-A on 2023–26 grants | F3-A on 2022–26 prices |
| 3. Ground-truth validation | Expert-adjudicated discrepancies | Outcomes from later CTUIL snapshots and CERC orders | Per-plant DSM-charge reproduction and forecast skill on RPC files (ISTS plants); SoC/availability still needs stage 4 |
| 4. Customer historical export | F2-A: 12–24 months of bills/statements, 3–5 sites | A developer's own application history and deficiency letters (private use) | 6–12 months of EMS/SCADA exports from one awardee (Pace Digitek, Oriana or similar [INF, f2_f3 F3-Q5]) |
| 5. Read-only / shadow pilot | Monthly recomputation alongside the customer's process; no DISCOM filings until agreed | Alerts and probabilities delivered and compared with what the team saw | Shadow dispatch plan and monthly certificate vs DISCOM instruction and the customer's own certificate |
| 6. Production | Success-fee audit, then subscription; dispute letters with CA sign-off | Only under CTUIL permission; else private-use tool | Bid files via the customer's membership or a trader; contractually relied-upon compliance reports |

## 8. Energy-quantity glossary

| Term | Meaning as used here | Public? |
|---|---|---|
| Installed capacity | Nameplate MW (AC or DC stated); normaliser for forecast error | Yes — CTUIL lists, awards [VF] |
| Available capacity (AvC) | Cumulative inverter/turbine capability net of outages/derating; DSM denominator while X=100% [VF, [CERC DSM 2024](https://www.cercind.gov.in/regulations/192-Noti.pdf)] | Yes for ISTS entities — SRPC `available_capacity` per block, NRPC `DC_Stations`/`Solar_availability` [VF, india_electricity_data_sources.md Q1]; not for state-embedded plants |
| Actual generation | Metered injection per 15-minute block | ISTS plants: 15-minute `act_total` per entity in RPC weekly files (weekly lag, revisions) [VF]; state-embedded: state daily totals; all-India hourly aggregate (CC BY 4.0) [VF, Mendeley] |
| Schedule vs actual | Schedule = declared block-wise injection, revisable from the 7th/8th block; deviation = (actual − schedule)/AvC to 31 Mar 2026, then /(X%·AvC + (100−X)%·schedule) [VF] | ISTS entities: `sch_total` block-wise in RPC files [VF]; intra-state: unpublished (Karnataka) or QCA-gated (Maharashtra) |
| DSM bands | Solar/hybrid ≤5%, 5–10%; wind ≤10%, 10–15% from 1 Apr 2026; under-injection beyond band at 200% of contract rate [VF]; Karnataka intra-state slabs ₹0.25/0.50/0.75 per unit, capped at 3 paise/unit annually [VF-sec] | Rules public; per-plant weekly charges public for ISTS entities (RPC files) [VF], not for intra-state plants |
| ATC/TTC vs CTUIL "tentative margins" | ATC/TTC come from network studies needing non-public load-flow models; CTUIL's bay/substation margins are administrative headroom that "may vary depending on network topology, Load-Generation balance" [VF-snippet, [CTUIL](https://ctuil.in/renewable-energy)] — not a curtailment or ATC figure | Margins public (PDF, RESTRICTED); inter-regional TTC/ATC: nine indicative CTUIL declarations Oct 2019–Apr 2025 (e.g., WR–NR TTC 23,000 / ATC 21,750 MW) [VF, [CTUIL](https://ctuil.in/ttc-atc-declaration)]; RLDC monthly and nodal ATC not public [UNK] |
| Connectivity vs GNA vs T-GNA | Connectivity = right to connect at an ISTS substation (in-principle → firm → effective); GNA = general network access with one-time charge ₹1 lakh/MW and access BG ₹5 lakh/MW [VF, [CTUIL advisory](https://www.ctuil.in/uploads/assets/169780473570Advisory%20regd%20Procedure%20for%20payment%20of%20one-time%20GNA%20charges.pdf)]; T-GNA = temporary GNA for short-term access, referenced for WS sellers in CERC 14/SM/2023 [VF]; "deemed GNA" is a column in the effectiveness list [VF]. Precise definitions are not reproduced in the notes; verify against the GNA Regulations 2022 | Grant/effectiveness lists public [VF] |
| Solar-hour vs non-solar-hour access | Post-3rd-amendment split of access with separate margins [VF] | Public (PDF) |

## 9. Known limitations and open technical questions

1. Whether Karnataka SLDC/ESCOMs issue 15-minute accounting and banking statements to consumers as exports — gates F2; *not established*.
2. Frequency of OA billing errors across the population — only litigated cases known [UNK].
3. FY26–28 Karnataka wheeling, SLDC and operating ₹/kWh charges (tariff-order annexures unparsed) [UNK].
4. CTUIL's stance on commercial reuse and the meaning of the RESTRICTED stamp — A0.
5. Whether CTUIL's XLS export works and the full 636-row table is retrievable without a headless browser [UNK].
6. Operational definitions of "firm", "effective", "deemed GNA" and T-GNA for labelling — regulation text not in the notes.
7. Completeness of the CTUIL grant-list archive back to 2023 (Jan–Aug 2026 listed; earlier months not enumerated).
8. IEX licence terms and cost for product use; member API rules [UNK].
9. Merchant rights in state BESPAs; SECI-ESS-IV clauses (RfS unparsed) [UNK].
10. Final status of CMETS-WR/RVPN charging rules and the Power Market (Second Amendment) coupling regulations [UNK as of 16 Oct 2026].
11. ECMWF open-data latency in hours and the day-ahead submission deadline (assumed morning IST) [HYP].
12. Satellite irradiance over India (CAMS coverage, INSAT-3D GHI product, commercial terms) for intraday revisions [UNK].
13. Outcome of the Karnataka HC stay after 10 Jun 2026 and the Delhi HC writ on the merits [UNK].
14. SCODs for KPTCL/MSEDCL/TN/Kerala BESS awards [UNK].
15. Operational BESS totals are unreconciled across sources — 758 MWh (end-2025, Tenderkosh), 6.8 GWh (JMK, Jun 2026), ≈12.6 GWh (Energetica, Oct 2026); the brief's §8 adopts ≈12.6 GWh and supersedes §3 [EST].
16. KERC DSM 2026 wind/hybrid slab rates unconfirmed [UNK].
17. No LLM-extraction accuracy test has been run on CTUIL PDFs or tariff orders; §2.4 golden files are the remedy.
18. RPC file retention depth (one SRPC week verified by download; NRPC weeks listed from Mar 2021), WRPC zip URLs (JS site), R1/R2 revision handling, and whether `act_total` is SEM-metered energy [HYP] — all needed before the plant-level backtest is relied on.
19. No licence text on any RPC site; whether the files fall under GODL-India [UNK].
20. The brief's §8 hypothesis H16 (public DSM-exposure scorecard from RPC files, score 69, not red-teamed) is not a finalist and is not planned here; it would reuse the RPC ingestion built for F3-A.
