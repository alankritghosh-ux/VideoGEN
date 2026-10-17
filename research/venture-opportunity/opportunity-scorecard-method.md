# Opportunity scorecard: method note

Companion to `opportunity-scorecard.csv` (16 hypotheses, H1–H16). The binding frame is `research_notes/Venture scale opportunity search/decision_brief.md`; this note explains how the numbers were produced and how much to trust them.

## 1. The scoring system

Each hypothesis is scored 1–5 on ten criteria. Weighted score = Σ(weight × score) / 5, giving 0–100. Weights sum to 100.

| Criterion (weight) | 1 | 3 | 5 |
|---|---|---|---|
| Severity & frequency (10) | Occasional or cheap when it occurs | Recurring, loss in lakhs | Monthly or daily, loss in crores, regulatory deadline |
| Willingness to pay (15) | No buyer evidence; advisory given free | Proxies only (report prices, consultants exist, mandated spend) | Observed software purchases or a published fee for this job |
| Data accessibility & legality (10) | Privileged, tender-gated or licence-barred | Public with reuse restrictions, or routine customer exports | Public, machine-readable, explicit commercial reuse rights |
| Validation without privileged access (10) | Needs a design partner before anything can be shown | Partial backtest on public data | Full offline backtest on public records |
| Time & capital to test (5) | Months and lakhs | 6–10 weeks, under ₹1 lakh | Under two weeks at ~₹0 |
| Competitive intensity, 5 = low (10) | Many funded incumbents, or the regulator itself | A few incumbents touch the job; none has productised it | No vendor found after a real search |
| Ease of first three customers (10) | Government or L1 tender buyer | Reachable with introductions; 3–6 month cycle | Named, local, public prospect list; discretionary budget |
| Gross margin & scalability (10) | Services with software inside | Software plus expert delivery labour | Pure software at 90%+ contribution margin |
| Durability vs frontier models (10) | Core function reproducible from public documents by a general model | Models do the parse layer; customer data or accountability needed for the rest | Requires data rights, transaction position or regulatory standing |
| Accumulating advantage (10) | Nothing compounds; templates fixed by a third party | Rule libraries and benchmarks improve slowly | Each customer adds labelled outcomes nobody else holds |

Willingness to pay carries 15 because it was the least evidenced criterion across every track (no fee benchmark was found for any finalist) and because the moat test found that distribution and transaction access, not analytics, held in this market. A hypothesis that cannot show someone already paying for the job should not win on data or speed alone; the criterion with the most weight is the one the Validate First experiments measure.

## 2. Uncertainty convention

Scores are judgments made on the evidence cited in the research notes; they are not measurements. One primary document can move a cell by two points (CTUIL's copyright policy took F1's data score from 5 to 3; a downloaded SRPC zip took H13's data and validation scores from 2 to 4).

- Confidence tags: `confidence_lowest_criterion` names the least certain cell, tagged H/M/L. "H" on a low score means the weakness is well established, not that the hypothesis is strong.
- Raw vs red-teamed: `red_teamed` = Yes for F1–F3 (Phase D hostile pass) and H4–H6 (cluster-2 pass); Partial for H13 (the energy track examined commoditisation, incumbent financials and litigation, but no hostile pass targeted the product); No for the rest, shown raw.
- The ~10-point haircut: the cluster-2 hypotheses lost 14 (H4), 11 (H5) and 9 (H6) points when examined at finalist depth; the finalists lost 14, 5 and 12. `expected_score_after_haircut` therefore shows raw − 10 with a "~" prefix for every un-red-teamed row, and no un-red-teamed hypothesis ranks above a red-teamed finalist, which is why H16 (69 raw) sits fourth and H7 (62 raw) sixth.
- `final_rank` reproduces decision_brief.md section 9 exactly.

## 3. Sensitivity

Two re-weightings were computed from the post-red-team scores, rescaled to 0–100.

WTP weight 10 instead of 15: F2 71.6, F1 64.2, F3 60.0; finalist order and the Validate First choice are unchanged. H13 ties F3 at 60.0. In the tail, H5, H11 and H12 (53.7) move above H4 (52.6), and H10 falls to a tie with H6 (54.7). H16's raw score rises to 70.5, within 1.1 of F2, but the haircut convention keeps it fourth.

Durability weight 15 instead of 10: F2 70.5, F1 61.9, F3 61.0; order unchanged, but the F1–F3 gap narrows from 3 points to under 1 because F3 holds the strongest durability cell (4) among the finalists. H8 and H9 tie at 58.1; H5 falls to 51.4 behind H4. Nothing else moves.

The lead and the top-three order are robust to both re-weightings; only tie-breaks among rejected hypotheses shift.

## 4. Attractive but rejected

- H13 pure forecasting / QCA: commoditised at implied ₹4k–33k/MW/yr; pooling beats model accuracy; intraday needs live telemetry; data scores revised up, commercial verdict unchanged.
- H11 satellite construction monitoring: fee pool ~0.01–0.02% of capex; no Indian lender pilot; the signal is observation, not milestone certification.
- H12 transmission vegetation: no Indian buyer evidence; the budget line is drone LiDAR priced per km at survey stage.
- H4 CBAM engine: real spend, 69 competitors, the obligation sits with the EU importer who may lawfully use defaults; templates fixed by the Commission, so nothing accumulates.
- H6 CCTS engine: a window exists, but no CCC has traded, compensation is undefined, six provisional verifiers serve ~490 plants, and PAT's record argues forbearance.
- H5 development intelligence: records layer sold at ₹3,390/yr and given away free; the satellite stage field inherits H11's economics.
- H9 property-tax GIS: tender-driven, field-survey heavy, incumbents hold the contracts.
- H10 DISCOM analytics: right problem, wrong buyer (L1 tenders, confidential AMISP contracts).
- H7 Surya Ghar vendor operations: portal-feature risk; no moat beyond a benchmark dataset.
- H15 solar O&M analytics: consolidated by IBM, Reliance and Nextracker; the valuable signal is drone-only.

H8 (agri) and H14 (parametric) are rejected without the "attractive" label: both sit inside the satellite thesis the research established is not the entry wedge, and neither has an Indian buyer paying for third-party scores.

Margin cells score contribution margin after data, compute and support; for F2 the workbook's 97–99% excludes tariff-expert and CA labour, so true gross margin is estimated at 60–80% at 100 customers (Hypothesis).
