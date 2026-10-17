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
