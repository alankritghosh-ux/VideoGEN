# Commercial model — summary (F2 / F1 / F3)

Companion to `commercial-model.xlsx` (same folder). Built 2026-10-17 from the research notes in `research_notes/Venture scale opportunity search/` only; no new web research. Every price point in the model is a **Hypothesis** inspired by a cited anchor, not a measured price: the notes found no published Indian fee for OA bill audit / advisory, connectivity advisory, or BESS optimisation.

## Workbook

| Sheet | What it holds |
|---|---|
| README | Purpose, how to use, colour convention (blue inputs, black formulas, green links, yellow key / must-validate cells), evidence classes, limitations |
| Assumptions | One block per finalist plus global cost drivers; Conservative / Base / Upside columns; scenario selector in C3 drives the Active column (INDEX); USD/INR in C4; each row carries evidence class, source ID (S1–S40) and a must-validate flag |
| Unit economics | ARPA, one-time vs recurring fees, variable cost, gross margin, CAC, onboarding cost, payback (two variants), lifetime, LTV, LTV/CAC, receivables — per scenario and Active |
| Scenarios | Steady-state P&L (revenue, COGS, GM, opex lines, EBITDA) at 10 / 100 / 1,000 customers for all three scenarios; feasibility flags vs reachable segment and segment × win rate; CTUIL gate for F1; MW-vs-pipeline check for F3 |
| Path to first revenue | 12-month F2 plan: pilot inputs, conversions, billing, cash with DSO and recovery lags, burn, cumulative burn, cash balance against a ₹10 lakh founder budget (input) and founder stipend (input) |
| Sensitivity | F2 base: one-way tornado tables (price, win rate, recoverable %, churn, CAC driver) on payback, LTV/CAC and EBITDA@100; two-way price × win rate grids; the calculation grid behind both (formulas, no Data Tables) |
| Operational constraints | Formula-driven hours/month, FTEs, staffing flags, sign-off / advice liability and segment checks at 10 / 100 / 1,000 customers per finalist, with qualitative "what breaks" notes |
| Sources | 40 anchors with value, evidence class, research note and URL |

Recalculation: the workbook was recalculated with LibreOffice via the spreadsheet skill's `recalc.py` — 1,904 formulas, 0 errors. Cached values are therefore present for any reader (Excel, LibreOffice, Google Sheets, pandas). No XLOOKUP, dynamic arrays or Data Tables are used.

## Base-case unit economics (selector = 2)

| | F2 OA settlement engine | F1 connectivity intelligence | F3 BESS dispatch & compliance |
|---|---|---|---|
| ARPA, steady state | ₹5.63 lakh (SaaS ₹4.5 lakh on 1.5 sites + ₹1.1 lakh recurring fees) | ₹6.0 lakh (₹5 lakh subscription + 1 report) | ₹1.05 Cr (₹3,000/MW/month × 250 MW + merchant revenue share) |
| Year-1 revenue per account | ₹11.25 lakh (adds ₹6.75 lakh one-time audit fee) | same as ARPA | same as ARPA |
| Gross margin per account | ₹5.49 lakh (97.7%) | ₹5.90 lakh (98.3%) | ₹1.05 Cr (99.6%) |
| Cost to acquire + onboard | ₹63,600 | ₹1.54 lakh | ₹3.32 lakh |
| Payback on steady-state GM | 1.4 months (0 net of the one-time fee) | 3.1 months | 0.4 months |
| LTV / cost to acquire | 68× | 19× | 210× |

Conservative payback: F2 18.4 months, F1 19.6 months (and revenue gated to zero by a refused CTUIL permission), F3 4.7 months. Gross margins are high because the only variable costs are support hours at an analyst rate, compute and (for F2) customer-supplied data; the real constraint is reach, not margin.

## Revenue at 10 / 100 / 1,000 customers (steady state, ₹)

| Finalist | Scenario | 10 | 100 | 1,000 | Feasibility |
|---|---|---|---|---|---|
| F2 | Conservative | ₹16.3 lakh | ₹1.63 Cr | ₹16.3 Cr | 1,000 exceeds the 900-org Karnataka-only segment; 100 needs 11% penetration (> 5% win rate) |
| F2 | Base | ₹66.4 lakh | ₹6.64 Cr | ₹66.4 Cr | 1,000 needs 67% of a 1,500-org segment (> 10% win rate) |
| F2 | Upside | ₹2.84 Cr | ₹28.4 Cr | ₹284 Cr | 1,000 needs 33% of a 3,000-org segment |
| F1 | Conservative | ₹30 lakh (bankable: ₹0) | ₹3.0 Cr (₹0) | ₹30 Cr (₹0) | BLOCKED (CTUIL permission refused); 100 and 1,000 exceed the 70-org segment |
| F1 | Base | ₹60 lakh | ₹6.0 Cr | ₹60 Cr | 1,000 exceeds the 200-org segment; 100 needs 50% penetration |
| F1 | Upside | ₹1.4 Cr | ₹14 Cr | ₹140 Cr | 1,000 exceeds the 400-org segment |
| F3 | Conservative | ₹2.4 Cr | ₹24 Cr | ₹240 Cr | 100 and 1,000 exceed the 15-org segment; 10 needs 67% penetration |
| F3 | Base | ₹10.5 Cr | ₹105 Cr | ₹1,050 Cr | 100 and 1,000 exceed the 30-org segment; 10 needs 33% penetration; 10 customers = 2,500 MW = 64% of the identified Tier-2 pipeline |
| F3 | Upside | ₹37.8 Cr | ₹378 Cr | ₹3,782 Cr | 100 and 1,000 exceed the 60-org segment |

Base EBITDA at 100 customers: F2 ₹6.1 Cr, F1 ₹5.3 Cr, F3 ₹103.5 Cr (F3 at 100 customers is not reachable). The 1,000-customer columns for F1 and F3 are shown only to make the feasibility flags visible: F1's buyer universe is a few hundred developers and F3's is roughly 19 named Tier-2 awardees today.

## Path to first revenue (F2, base scenario, ₹10 lakh budget, ₹50k/month stipend)

Pilot plan of 1 then 2 success-fee audits per month, 30% pilot-to-paid conversion after a 4-month cycle: first revenue billed in month 5, first cash in month 7 (SaaS, 45-day DSO), 4.5 paying customers at month 12, ₹13.3 lakh billed but only ₹4.05 lakh collected in the year because audit-fee cash arrives after a 6-month recovery lag plus DSO (month 13 onward). Cumulative burn ₹11.9 lakh; lowest cash balance ₹1.87 lakh in month 10; no runway breach. Reducing the recovery lag or billing SaaS quarterly in advance are the two inputs that most change the cash shape.

## Sensitivity (F2 base, ±30%)

- Payback: SaaS price (swing 0.73 months) and win rate (0.63) dominate; recoverable % matters less for payback (0.17) because recoveries are largely one-time; churn does not affect payback by construction.
- LTV/CAC: churn (swing 38×), win rate (29×) and price (28×) dominate.
- EBITDA at 100 customers: price (₹2.7 Cr swing) and recoverable % (₹1.3 Cr) dominate; CAC and win rate are second-order once the base is installed.
- Two-way grid: payback stays under 4 months across 0.5×–1.5× price and 5%–15% win rate, i.e. F2's economics are not the risk; segment reach, incumbent bundling and the unmeasured recoverable % are.

## Operational constraints (base, active scenario)

- F2: founder can run 10 customers (≈70 delivery hours/month); 100 customers need ≈3.5 delivery FTE, driven by manual statement collection (225 statement sets/month) and three state rule libraries; 1,000 customers need ≈32 FTE and six state libraries and carry ≈₹4.5 Cr/yr of sign-off liability on ₹225 Cr of claimed recoveries at a 2% misstatement rate.
- F1: founder can run 10; 100 needs ≈1.8 FTE; bespoke reports do not scale; advice liability references ₹5 Cr of bank guarantee per customer; CTUIL data-reuse permission is the gate.
- F3: a 24×7 dispatch desk (730 hours/month) is required as soon as any merchant MW is live, so even 10 customers need ≈5 FTE; capacity charge at risk under availability tests is ≈₹36 Cr/yr for 10 base customers.

## Evidence gaps carried as yellow "must validate" cells

Recoverable % of bill (F2-A experiment), success-fee % and SaaS price (no Indian OA fee published), win rates and churn (no interviews yet), CTUIL permission and licence fee (policy requires permission; no fee schedule), IEX data licence fee (terms non-commercial; fee on request), F3 merchant headroom and optimiser uplift (no Indian track record), labour / engineer / G&A / travel costs (no data in the notes; user inputs).

`f2_f3_commercial_facts.md` was present and used (Karnataka SLDC counts, TN / MH regimes, pricing anchors, F3 awardee list, capacity charges, IEX terms).
