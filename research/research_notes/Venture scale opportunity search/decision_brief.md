# Decision brief (coordinator synthesis, Phase C) — 2026-10-17

This brief fixes the frame every deliverable must follow. Writers must not change the ranking, weights or finalist definitions; they may add evidence and flag disagreements in a "Dissent" note.

## 1. What the eight research tracks established (reconciled)

1. **Analytics on third-party satellite data is a graveyard** (Orbital Insight, Descartes, Gro, ClimateAi, Farmers Edge, Blue Sky Analytics); survivors own sensors and sell ~80% to governments (Planet, BlackSky, ICEYE). Indian EO buyers are government (YES-TECH needs ₹5 Cr turnover; property-tax GIS is tender/field-survey driven). The only proven Indian commercial EO buyer is banks' agri-credit (SatSure: ₹31.5 Cr revenue, ₹42.6 Cr loss). → Satellite analytics is **not** the entry wedge. It may re-enter later as a feature (project-stage verification) inside a records-based product.
2. **Plant-level RE forecasting in India is a commoditised, thin-fee service** (implied ₹4k–33k/MW/yr; REConnect FY26 revenue ₹72.1 Cr, PAT ₹4.3 Cr; Manikaran ₹35.9 Cr, PAT ₹7.4 Cr with 22 staff). The model layer is free (ECMWF AIFS open data, Open-Meteo CC-BY). No public per-plant actuals exist, so a plant-level product cannot be validated without a design partner. Pooling (an organisational act) beats model accuracy. → Forecasting is a **component**, not a product.
3. **The money in Indian power is moving to three places that no Indian vendor visibly serves with software**: (a) ISTS connectivity/GNA — 128 GW application backlog, CTUIL now publishes bay-/substation-wise margins, grant lists and cluster declarations as PDFs; (b) FDRE/RTC and BESS contracts — 1.5× tariff shortfall penalties, 95–97% availability LDs, merchant surplus on IEX (RTM 54.85 BU, +41%); ReNew's 20-F admits an intraday price-forecasting gap; (c) C&I green open access — 30 GW, 37,558 approvals, state-specific banking/CSS/DSM rules, the only free tool (CEEW) frozen at FY22 tariffs, JMK sells OA data at ₹2 lakh.
4. **Regulatory tailwind with litigation risk**: DSM bands halved on 1 Apr 2026 (solar ±5%, wind ±10%); CERC X-factor glide path raises individual-plant deviation exposure from ~₹1.9 lakh/MW/yr to ~₹4.8 lakh (solar) and ₹12.6–18.9 lakh (wind) by FY32 — subject to Delhi HC writs.
5. **Moat test verdict**: distribution, accountability and transaction access are the moats that held, and incumbents hold them. A software-only entrant must (i) compile a dataset nobody else has (time series of public records), (ii) obtain contractual rights to customer exhaust data, (iii) price per outcome, (iv) design for the position that owns the transaction (scheduling/trading agent), not for a seat-based dashboard.

## 2. Hypothesis set (15, distinct) and scoring

Weights (sum 100): Severity & frequency 10 · Willingness-to-pay/budget evidence 15 · Data accessibility & legality 10 · Validation without privileged access 10 · Time & capital to test 5 · Competitive intensity (5 = low) 10 · Ease of first three customers 10 · Gross margin & scalability 10 · Durability vs frontier models 10 · Accumulating advantage 10. Scores 1–5. Weighted score = Σ(weight × score)/5 → 0–100. Confidence tag per score (H/M/L). Scores are judgments on the evidence in the notes; they are not measurements.

| # | Hypothesis | Sev | WTP | Data | Valid | Time | Comp | First3 | Margin | Durable | Accum | Score | Lowest-confidence score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| H1 | ISTS connectivity / GNA headroom intelligence for RE & BESS developers | 4 | 2 | 5 | 5 | 5 | 5 | 3 | 4 | 3 | 4 | **77** | WTP (L) — only proxies |
| H2 | C&I open-access procurement optimiser + monthly settlement/bill-audit engine | 4 | 4 | 4 | 5 | 4 | 3 | 4 | 4 | 3 | 3 | **76** | Comp (L) — no vendor scan completed |
| H3 | FDRE/BESS dispatch, scheduling, availability-compliance and IEX bid optimiser (forecasting embedded) | 5 | 3 | 4 | 3 | 3 | 4 | 2 | 4 | 4 | 4 | **72** | First3 (M) — assets not yet operating |
| H4 | CBAM embedded-emissions engine for steel/aluminium/cement exporters | 4 | 5 | 4 | 4 | 4 | 1 | 3 | 3 | 2 | 3 | 67 | Comp (H) — 69 firms |
| H5 | Energy-project development intelligence (records + EO stage verification) | 2 | 3 | 5 | 4 | 5 | 3 | 4 | 3 | 2 | 2 | 64 | Durable (M) |
| H6 | CCTS compliance engine for ~490 obligated entities | 3 | 4 | 4 | 4 | 4 | 2 | 3 | 3 | 2 | 3 | 64 | Sev (L) — enforcement unproven |
| H7 | PM Surya Ghar rooftop-vendor operations (approval tracking, delay prediction) | 3 | 3 | 5 | 4 | 5 | 2 | 4 | 3 | 1 | 2 | 62 | Durable (H) |
| H8 | Agri-lending / crop-insurance satellite verification | 3 | 4 | 5 | 3 | 3 | 1 | 2 | 3 | 2 | 3 | 59 | Comp (H) |
| H9 | Municipal property-tax change detection | 3 | 5 | 4 | 3 | 3 | 2 | 1 | 2 | 3 | 2 | 58 | First3 (H) |
| H10 | DISCOM smart-meter energy accounting / theft-lead scoring | 5 | 4 | 2 | 2 | 2 | 2 | 1 | 3 | 3 | 3 | 56 | First3 (H) |
| H11 | Satellite construction-progress verification for lenders/LIEs | 2 | 2 | 4 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 53 | WTP (M) — fee pool 0.01–0.02% of capex |
| H12 | Transmission corridor vegetation/encroachment/exposure analytics | 3 | 2 | 3 | 3 | 3 | 2 | 1 | 4 | 3 | 3 | 53 | WTP (M) — zero Indian contracts found |
| H13 | Plant-level RE forecasting / QCA services (founder's original idea) | 4 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 52 | Data (H) — no public ground truth |
| H14 | Parametric weather-risk scoring for insurers/lenders | 3 | 2 | 4 | 3 | 3 | 3 | 1 | 3 | 2 | 2 | 51 | WTP (M) |
| H15 | Solar O&M performance analytics / underperformance detection | 3 | 3 | 2 | 2 | 3 | 1 | 2 | 3 | 2 | 3 | 48 | Comp (H) — IBM/Reliance/Nextracker |

## 3. Finalists (pre-red-team)

- **F1 = H1. India grid-access intelligence ("where can I connect, when, and what will it cost")** for RE/BESS developers, lenders and advisors. Public-data wedge: parse every CTUIL/CERC/RLDC publication (bay/substation margins by solar/non-solar hour, grant lists, effective/not-effective status, cluster declarations, reallocation notices, SCOD extensions) into a geocoded, versioned substation database; estimate time-to-effective connectivity and reallocation options; alert on changes. Validation: backtest on 2023–2026 grant lists. Honest ceiling alone: ₹20–50 Cr/yr (few hundred developers). Venture scale only via F3.
- **F2 = H2. C&I open-access settlement and procurement engine** for industrial consumers (1–20 MW) in Karnataka/Maharashtra/Tamil Nadu/Gujarat: recompute what the consumer should have paid under the applicable tariff order from exported bills, SLDC statements and banking statements; recover overcharges (success fee), then annual sourcing optimisation. Validation: backtest on 12–24 months of a customer's bills.
- **F3 = H3. FDRE/BESS dispatch, availability-compliance and bid optimisation** (with RE forecasting embedded) for Tier-2 developers winning SECI/NTPC/GUVNL/state tenders. Validation: public IEX 15-min price backtests + contract terms; needs customer telemetry for compliance module. Entry timing risk: cumulative installed storage was ~758 MWh at end-2025 vs ~102 GWh tendered in 2025.

Shared core across F1–F3: a regulatory-document and market-data parsing engine for CERC/SERC/CTUIL/SLDC/IEX publications, and a developer customer base. Satellite imagery enters only as an optional "stage-verified" field in F1 (is the plant actually under construction at the substation it holds connectivity for).

## 4. Rejected-but-attractive (must appear in deliverables with reasons)
Pure forecasting/QCA (commoditised, unverifiable without plant data, pooling beats models); satellite construction monitoring for lenders (fee pool tiny, no Indian lender pilot, signal is observation not milestone); transmission vegetation (no Indian buyer evidence, drone LiDAR Rs/km is the budget line); CBAM (real spend, 69 competitors, no accumulating advantage); CCTS (window exists but enforcement history weak, no CCC traded); property-tax GIS (tender-driven, field-survey heavy, incumbents); DISCOM analytics (right problem, wrong buyer); Surya Ghar vendor ops (portal-feature risk, no moat); solar O&M (consolidated by IBM/Reliance/Nextracker).

## 5. Preliminary recommendation
**Validate First** on F1, with F2 as a parallel five-interview customer-discovery test and F3 as the designed expansion. Do not commit capital or incorporate until the two cheapest invalidating experiments below return "pass".
- Experiment A (technical, ≤7 days, ≈₹0): parse all CTUIL grant/effectiveness/margin PDFs since 2023; measure whether a simple model predicts "effective" date and firm-vs-in-principle outcome better than naive baselines (MAE in months; AUC for effective-within-12-months). Fail = no skill over naive → product is aggregation only, price accordingly or stop.
- Experiment B (commercial, ≤14 days, ≈₹10k): 10 structured interviews with BD/regulatory heads at Tier-2 developers + 3 lenders/advisors. Pass = ≥4 of 10 currently pay an external party for connectivity work or lost ≥₹1 Cr to connectivity delay in the last 24 months AND ≥3 agree to a paid pilot (₹1–3 lakh). Fail = <2 pay anyone today and nobody agrees to pay.

## 6. Open questions Phase D must answer
1. Does CTUIL's own Connectivity Monitoring Portal / NSWS already deliver what F1 proposes? (incumbent-bundling risk)
2. What do developers pay regulatory consultants for connectivity applications today? Who are those consultants?
3. Evidence of losses from connectivity delay (SCOD extensions, bank guarantee encashment, CERC petitions).
4. US analogues' economics (Nira Energy, Pearl Street, Enverus deal) as the only WTP comparables.
5. For F3: are merchant/co-optimised operations allowed under current SECI/state BESS contracts; which developers have trading desks; which OEM EMS bundles bidding; any Indian startup already doing it.
6. For F2: does any Indian SaaS/consultant already reconcile OA bills; evidence of over-billing; what consumers pay energy consultants.
7. 10+ named initial customer organisations for F1 with source-backed reasons and public contact routes.

---

## 7. Post-red-team update (coordinator, after reading red_team_counterevidence.md and f1_customers_and_buying.md)

**Accepted score changes** (weights unchanged). Rationale in red_team_counterevidence.md; coordinator agrees with every move except where noted.

| Finalist | Pre | Post | Cells moved | Why |
|---|---|---|---|---|
| F1 connectivity intelligence | 77 | **63** | Sev 4→3, Data 5→3, Comp 5→3, Durable 3→2, Accum 4→3 | CTUIL already publishes the queue as a filterable/exportable table and an API-backed status page; margin PDFs are stamped RESTRICTED and CTUIL's copyright policy forbids reproduction without permission; backlog is demand-side (22,054 MW blocked by unsigned PPAs, CERC 11/SM/2026 clearing ~15.7 GW); Tier-2 developers (Cleanmax, Gentari, Mahindra Susten, Serentica, ACME) file their own CERC comments, i.e., have in-house regulatory capacity. What survives: prediction/alerting layer, and the hard cost evidence (BG encashments ₹3.1–11.5 Cr per developer; CTUIL compensation rate ₹1,612/MW/day). |
| F2 OA settlement & procurement | 76 | **71** | WTP 4→3, Comp 3→2 | ≥4 incumbents touch the job (Tata Power Trading settlement services; Customized Energy Solutions advisory; Open Access Exchange "zero upfront"; BridgeIT bill-validation SaaS claiming 1M+ bills/100+ DISCOMs). Over-billing is real but episodic/litigated (APTEL 366/2017, MERC 2021, DERC CSS petitions). No fee benchmark found. Still: the only finalist whose buyer is numerous, local to Bengaluru, and whose data arrives as routine customer exports. |
| F3 BESS/FDRE dispatch | 72 | **60** | Sev 5→4, Data 4→2, Valid 3→2, Comp 4→3, First3 2→1 | Merchant storage (~80% of ~6.8 GWh operational per JMK Jun 2026 — supersedes the 758 MWh figure in opportunities_beyond_thesis.md, which counted standalone tendered projects only) is Adani and ACME, in-house capable; Tier-2 pipeline is availability-paid and SLDC-dispatched; draft ISTS rules bar grid charging; IEX terms of use are non-commercial, so backtests/feeds need a licence; DSM escalation for WS sellers deferred to bids ≥1 Jan 2027 / COD ≥1 Jan 2029; market-coupling rules not notified. |

**Fairness caveat**: non-finalists were not red-teamed at the same depth. A bounded red-team of the next cluster (H4 CBAM, H5 dev-intel, H6 CCTS) is being run so the final ranking compares like with like. Until then, treat the post-red-team table as: F2 71 · [H4 67 / H5 64 / H6 64 — un-red-teamed] · F1 63 · H7 62 · F3 60.

**Revised recommendation (provisional, to be confirmed in executive-decision.md): Validate First on F2**, with F1 reduced to (a) a 7-day technical probe plus a written data-reuse permission request to CTUIL and (b) an optional later module on the generator side; F3 becomes a 2027+ watch item tied to merchant-storage rules. Satellite imagery and plant-level forecasting remain rejected as entry wedges.

**Cheapest invalidating experiments (revised)**
- F2-A (technical, ≤14 days, ≈₹0): obtain 12 months of bills + SLDC/DISCOM energy-accounting statements from 3–5 Karnataka OA/group-captive consumers (via personal network, industry associations such as KASSIA/Peenya Industries Association/FKCCI energy committee, or a consultant partner); recompute charges under KERC tariff orders; measure recoverable overcharges + avoidable banking-lapse/DSM losses as % of annual OA bill. Pass: median ≥1.5% and ≥₹5 lakh/yr for ≥3 of 5 sites. Fail: <0.5% for 4 of 5 → the recurring value is bookkeeping, not money; re-scope to procurement optimisation or stop.
- F2-B (commercial, ≤14 days): 10 interviews with plant heads/energy managers/CFOs at Karnataka/TN/MH OA consumers (1–20 MW). Pass: ≥4 of 10 currently pay someone (trader/consultant/in-house FTE) for OA settlement or report a dispute/lapse loss in 24 months AND ≥3 accept a success-fee audit. Fail: <2 and none accept.
- F1-A0/A (≤7 days, ≈₹0): email CTUIL for written permission to reuse published data commercially; in parallel scrape the queue table/XLS and 2023–2026 PDFs and test whether a simple model predicts effective-within-12-months better than base rate (AUC ≥0.70 = skill). If permission refused or no skill → F1 is dead as a product; keep as internal research tool.

## 8. Late evidence changes (coordinator, after india_electricity_data_sources.md and f2_f3_commercial_facts.md)

1. **Reversal on public ground truth.** solar_forecasting_feasibility.md concluded no public per-plant actuals exist. india_electricity_data_sources.md verified by download that the Regional Power Committees publish weekly DSM files with 15-minute `available_capacity, sch_total, act_total, dev, dev_perc, rate, ppa_rate` and charges per ISTS-connected RE entity/QCA (SRPC weekly zip: 122 RE/QCA entities; NRPC weekly xlsx from 2021; NERPC deviation reports; WRPC per secondary). Prayas built FY24–FY25 datasets from them. Limits: ISTS plants only, weekly lag with revisions, no stated licence, retention depth unverified. Consequence: plant-level forecasting backtests ARE possible for ISTS plants; H13 (forecasting) scores move Data 2→4, Valid 2→4 (52→60). The commercial verdict on H13 is unchanged (fees ₹4k–33k/MW/yr; pooling beats models; intraday revisions need live telemetry).
2. **New hypothesis H16 — Public DSM-exposure benchmark and QCA/plant performance scorecard** (weekly, per ISTS plant and pooling station, from RPC files): deviation cost, within-band share, peer comparison, attribution (forecast error vs AvC declaration vs curtailment), projected exposure under the X-factor glide path. Buyers: IPP asset managers, lenders, QCAs' customers. Honest concerns: plants already receive their own statements; value is benchmarking and vendor accountability; may work better as the lead-generation front end for F3 than as a paid product. Provisional score (not red-teamed): Sev 4, WTP 2, Data 4, Valid 5, Time 5, Comp 3, First3 3, Margin 4, Durable 3, Accum 3 → **69**. Flag it in the scorecard as "added late; not red-teamed; expect a 5–10 point haircut".
3. **F2 strengthened on reachability**: Karnataka SLDC publishes approved wheeling-and-banking consumer lists (556 generators / 4,924 MW; ~922 distinct consumer organisations incl. Infosys 40 MW, Wipro, Shahi Exports, Biocon, Toyota Tsusho, Sansera, Kirloskar Ferrous, BIAL, IT parks). First3 for F2 stays 4 (already high) and Data stays 4; this is the reason F2 remains the lead despite the incumbent haircut. Two coexisting banking regimes in Karnataka (2% annual in-kind for 2018–2023 applicants vs monthly no-carry-forward under 2025 regs) and MERC-ordered MSEDCL refunds of unlawful wheeling charges (2025) are direct evidence that settlement errors are real.
4. **F3 fleet correction**: operational grid BESS ≈12.6 GWh by Oct 2026 (AGEL Khavda 6.63 GWh; ACME ~2 GWh); ~80% merchant but concentrated in two conglomerates; state BESPAs (e.g., MSEDCL 2,000 MW/4,000 MWh, Sep 2026) are availability contracts that require indigenous EMS software — a tailwind for an Indian EMS/compliance vendor in 2027–28 but not a 2026 wedge. Pace Digitek (Bengaluru, 375 MW awarded) is the natural first design partner when F3 is revisited.

Final order for the deliverables (pending red_team_cluster2.md): F2 71 · H16 69* · H4 67* · H5 64* · H6 64* · F1 63 · H7 62 · F3 60 · H13 60 (* = not red-teamed at finalist depth). Recommendation remains **Validate First on F2**; H16 is the designated energy-side probe if the founder wants to keep the forecasting/grid thread alive at near-zero cost (one week of RPC-file parsing).
