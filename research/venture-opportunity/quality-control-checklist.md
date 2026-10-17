# Quality-control checklist — venture-diligence deliverables

Independent audit, 2026-10-17. Scope: the nine artifacts in `research/venture-opportunity/` checked against the mandated checklist and against the evidence base in `research/research_notes/Venture scale opportunity search/` (13 notes; `decision_brief.md` §9 is the binding frame). No new web research was done and no URL was fetched. Deliverables were not rewritten; no mechanical fix was needed (see §4).

**Tally (after post-audit fixes): 44 checklist items — 44 Complete · 0 Partial · 0 Blocked · 0 Not Validated.** The audit originally found 40 Complete and 4 Partial (items 6, 8, 27, 32); the coordinator applied the fixes listed in the "Post-audit fixes" section below and the four items were re-marked Complete. The original Partial findings are retained in the table for traceability, prefixed "Resolved".

Status key: **Complete** = the specified artifact/evidence exists in the files at the stated location. **Partial** = present but incomplete or internally inconsistent. **Blocked** = could not exist given constraints. **Not Validated** = not checkable from the files.

## 1. Checklist

### 1.1 Executive decision

| # | Item | Status | Explanation | Evidence |
|---|---|---|---|---|
| 1 | One-page executive summary | Complete | Question, answer, ranked top three, three reasons for and against, next experiment, seven-day action and rejections in one section | `executive-decision.md` §1 |
| 2 | Ranked top three | Complete | F2 71 · F1 63 · F3 60, with the full 16-row table and the raw-vs-red-teamed convention | `executive-decision.md` §1, §4; matches `decision_brief.md` §9, `opportunity-scorecard.csv` `final_rank`, `red-team-review.md` §8 |
| 3 | Explicit Build / Validate First / Investigate Further / Reject | Complete | "VALIDATE FIRST — F2"; F1 probe; F3 watch item; satellite analytics and standalone forecasting rejected; the conditions under which it becomes Build or Reject are stated | `executive-decision.md` §1, §6 |
| 4 | Strongest reasons for success and failure | Complete | Three of each in §1; seven failure modes with likelihood/impact in §5.13 | `executive-decision.md` §1, §5.13 |
| 5 | Next experiment identified | Complete | F2-A with pass/fail/inconclusive, cost and duration; F2-B in parallel | `executive-decision.md` §1, §5.14 |

### 1.2 Market and competitors

| # | Item | Status | Explanation | Evidence |
|---|---|---|---|---|
| 6 | Relevant competitors investigated with source-backed evidence | **Complete** (Resolved; was Partial) | 70 rows with 191 distinct URLs, every row sourced. But two of the four F2 incumbents the red team and executive memo rely on — Customized Energy Solutions and BridgeIT — have no row in the landscape CSV (0 matches), and `competitive-landscape-gaps.md` items 2 and 14 still say no vendor scan confirmed an OA-reconciliation vendor, which the later red team contradicts (TPTCL, CES, OAE, BridgeIT). Evidence class of the 70 rows: 23 Verified fact, 9 Independently corroborated, 30 Estimate, 6 Unknown, 2 Hypothesis | `competitive-landscape.csv` (`company` column); `competitive-landscape-gaps.md` items 2, 14; `red-team-review.md` §3 A1; `executive-decision.md` §5.9 |
| 7 | Deployed products separated from announcements | Complete | Dedicated `deployed_vs_announced` column populated in all 70 rows, e.g. EtherealX "Announced only", Planet "Announced: self-serve tiers 'Coming Soon'", Lanteris acquisition "closing status unknown" | `competitive-landscape.csv` column 5 |
| 8 | Real customer gaps distinguished from assumed gaps | **Complete** (Resolved; was Partial) | The gaps note classifies 13 gaps into unmet need / unattractive market / inaccessible data / difficult deployment / customer indifference, and the red team separates documented errors from "done quietly" by incumbents. But gaps note item 1 still calls ISTS connectivity "unmet need (real, unserved)" with CTUIL publishing "only as PDFs", which the red team overturned (filterable 636-row table with XLS export and API page), and item 2 calls F2 settlement unserved without the four incumbents. The note was not refreshed after the red team | `competitive-landscape-gaps.md` items 1–2 vs `red-team-review.md` §4(h), §5 F1 row 1; `executive-decision.md` §5.9 |
| 9 | Incumbent entry and bundling risks assessed | Complete | Bundling named as failure reason 1; red-team question (b) and assumption A1; kill-on-incumbency criterion; interview Q3 designed to measure it | `executive-decision.md` §1, §5.13; `red-team-review.md` §3 A1, §4(b), §10 |

### 1.3 Opportunity discovery

| # | Item | Status | Explanation | Evidence |
|---|---|---|---|---|
| 10 | ≥10 genuinely distinct hypotheses | Complete | 16 hypotheses H1–H16, each with its own initial customer, workflow, product, data and competitors; no two share a buyer-plus-product pair (closest pair H13 forecasting vs H16 DSM benchmark is separated by product and buyer and is flagged as a possible F3 front end) | `opportunity-scorecard.csv` rows H1–H16; `decision_brief.md` §2, §8.2 |
| 11 | Explicit scoring criteria, weights, uncertainty | Complete | Ten criteria with weights summing to 100, 1/3/5 anchors, confidence tags, raw-vs-red-teamed convention and two re-weighting sensitivities. Recomputed Σ(weight×score)/5 for all 16 rows, pre and post: every stored score matches the arithmetic | `opportunity-scorecard-method.md` §1–3; `opportunity-scorecard.csv` columns `w_*`, `pre_*`, `post_*`, `confidence_lowest_criterion`, `uncertainty_notes` |
| 12 | Attractive rejected ideas documented | Complete | Nine rejected-but-attractive hypotheses with reasons in the memo; ten in the method note (plus H8/H14 rejected without the label); scorecard `status` = "Rejected-attractive" on 9 rows | `executive-decision.md` §4 "Attractive but rejected"; `opportunity-scorecard-method.md` §4; `decision_brief.md` §4 |
| 13 | Initial reachable market distinguished from TAM | Complete | Market totals (18.7 GW / 37,558 approvals / ~30 GW) kept separate from the reachable segment (≈922 Karnataka organisations; 900/1,500/3,000-org segments per scenario) with explicit penetration flags at 10/100/1,000 customers | `executive-decision.md` §5.2, §5.6, §5.12; `commercial-model-summary.md` "Revenue at 10/100/1,000"; workbook `Scenarios` sheet |

### 1.4 Data and technical feasibility

| # | Item | Status | Explanation | Evidence |
|---|---|---|---|---|
| 14 | Dataset links / access / licensing / cost / granularity investigated | Complete | 108 datasets with `url`, `access_method`, `access_status` (54 Verified-page, 20 Verified-downloaded, 17 Unreachable-from-sandbox, 11 Described-by-secondary-source, 6 Customer-provided), `cost`, `license_terms`, `redistribution_restrictions`, `granularity`, `historical_depth`, `update_frequency`. Per-source legal table in the plan. Links were not fetched in this audit | `data-source-catalog.csv`; `technical-validation-plan.md` §2.5 |
| 15 | Minimum required data identified | Complete | `minimum_required_for` populated on all 108 rows; per-finalist input tables name the minimum set (F2: customer exports plus public orders; F1: CTUIL lists; F3: IEX prices plus contract terms) | `data-source-catalog.csv` column 22; `technical-validation-plan.md` §3.2, §4.2, §5.2 |
| 16 | Missing data and ground-truth requirements identified | Complete | Twenty open technical questions; staged path shows which stage needs customer data; RPC weekly files identified as the only public per-plant ground truth (ISTS only) | `technical-validation-plan.md` §7, §9; `data-source-catalog.csv` `gaps_and_risks` |
| 17 | Physical observations distinguished from inferred conclusions | Complete | Five evidence classes carried through every artifact; glossary separates metered actuals (`act_total`), declared availability (AvC), schedules and administrative margins from network-study ATC; the late reversal on public ground truth is recorded as a correction, not silently merged | `technical-validation-plan.md` §8; `executive-decision.md` §2; `decision_brief.md` §8.1 |
| 18 | Energy capacity concepts distinguished correctly | Complete | Installed capacity vs available capacity vs actual generation vs schedule; MW vs MWh; cycles; ATC/TTC vs CTUIL margins; connectivity vs GNA vs T-GNA, with public/non-public status per concept | `technical-validation-plan.md` §8; §5.3 (MWh/MW/cycle arithmetic) |
| 19 | Software-first architecture and build complexity documented | Complete | Document-to-ledger architecture (six layers, CPU-only notes), where LLMs do and do not belong, test strategy, 1-week/30-day/90-day build scope per finalist, cost <₹3,000/month | `technical-validation-plan.md` §2, §3.3–3.8, §4.3–4.6, §5.3–5.6; `executive-decision.md` §5.8 |

### 1.5 Customers and commercial evidence

| # | Item | Status | Explanation | Evidence |
|---|---|---|---|---|
| 20 | Initial customer and economic buyer identified | Complete | Karnataka OA/group-captive C&I consumers 1–20 MW; plant head / energy-procurement head / CFO; listed-company PO cycle noted | `executive-decision.md` §5.2; `opportunity-scorecard.csv` H2 `initial_customer`, `economic_buyer` |
| 21 | Existing workflow and alternatives investigated | Complete | Monthly document flow (ESCOM bill, generator invoice, SLDC/ESCOM statements, banking statement); alternatives: spreadsheet, generator's free advisory, trader bundle, consultant retainer, petition | `executive-decision.md` §5.3; `red-team-review.md` §4(c) |
| 22 | Willingness-to-pay evidence distinguished from hypotheses | Complete | Pricing labelled HYP; recoverable pool UNK; only paid anchor (JMK ₹2 lakh) labelled VF; energy-audit and Zenatix anchors labelled EST/IC-dated; workbook marks every price a hypothesis | `executive-decision.md` §5.5; `commercial-model-summary.md` preamble; `red-team-review.md` §3 A3 |
| 23 | ≥10 plausible initial customer organisations | Complete | 17 named organisations in eight segments, each with a fit reason; all traced to Table F2 of the notes (Manipal Hospitals and Himatsingka Seide checked). Public route is stated generically (company website contact page / company LinkedIn page) rather than per organisation, which the memo states as deliberate | `executive-decision.md` §5.2 table; `f2_f3_commercial_facts.md` Table F2 |
| 24 | First-three-customer strategy documented | Complete | Target list from SLDC lists, tiering, three public routes, success-fee offer, proof pack, weekly outreach targets, fallbacks | `executive-decision.md` §5.11; `30-day-execution-plan.md` §2 Days 3–7, §6 |

### 1.6 Validation

| # | Item | Status | Explanation | Evidence |
|---|---|---|---|---|
| 25 | Real data or justified alternative identified | Complete | F2-A on 12 months of customer exports; F1-A on 2023–26 CTUIL lists; F3-A on public IEX series plus RPC files; synthetic proof pack explicitly labelled synthetic until a real site replaces it | `technical-validation-plan.md` §6; `30-day-execution-plan.md` Day 5 |
| 26 | Baselines and quantitative metrics specified | Complete | F2: billed amounts as baseline, five metrics; F1: three baselines incl. CTUIL's own expected date, AUC/Brier/MAE; F3: naive heuristic, BattMan, DISCOM instruction; forecast baselines smart persistence | `technical-validation-plan.md` §3.5–3.6, §4.4, §5.5 |
| 27 | Pass / fail / inconclusive thresholds set for each finalist experiment | **Complete** (Resolved; was Partial) | All four experiments (F2-A, F2-B, F1-A0, F1-A) and F3-A carry pass/fail/inconclusive. Two inconsistencies: (a) the recovery-channel condition the memo adds to F2-A (count only administratively recoverable amounts; litigation-only amounts excluded from the pass test) is absent from `technical-validation-plan.md` §6.1 and from the Day-30 gate in `30-day-execution-plan.md` §4, which carry only the overcharge-vs-avoidable-loss split; the red team's own kill criterion uses a different formulation ("more than half of the value is litigation-only"). (b) F1-A fail band: plan says fail = AUC <0.60 or no gain over CTUIL's date (0.60–0.70 undefined) and adds a Brier condition; the 30-day plan says fail = AUC <0.70 with no Brier condition. Not edited | `executive-decision.md` §5.14, §5.16; `technical-validation-plan.md` §4.4, §6.1–6.4; `30-day-execution-plan.md` §4; `red-team-review.md` §10 |
| 28 | No privileged access assumed without evidence | Complete | Every first experiment runs on public pages or customer exports; CTUIL permission treated as a gate (A0); IEX use confined to internal validation; Grid-India/RLDC terms "build nothing until read" | `technical-validation-plan.md` §2.5, §7; `executive-decision.md` §5.7 |
| 29 | Demo capability distinguished from validated performance and customer demand | Complete | Each experiment states "Establishes / Does not"; "public data alone does not prove production readiness"; F2-A explicitly does not show WTP (F2-B) or recoverability in practice | `technical-validation-plan.md` §6.1–6.3, §7; `executive-decision.md` §5.14 |

### 1.7 Defensibility and economics

| # | Item | Status | Explanation | Evidence |
|---|---|---|---|---|
| 30 | Frontier-model substitution risk assessed | Complete | Parse layer conceded as reproducible; non-reproducible asset named (rule library keyed to regime, bill/settlement pairs, accountability); `defensibility_vs_frontier_models` column on all 16 hypotheses; `frontier_model_reproducible` column on all 70 competitors | `executive-decision.md` §5.10; `red-team-review.md` §4(a); `opportunity-scorecard.csv`; `competitive-landscape.csv` |
| 31 | Incumbent bundling risk assessed | Complete | See item 9 | as item 9 |
| 32 | Accumulating advantages identified and tested | **Complete** (Resolved; was Partial) | Identified (versioned multi-state rule library with effective dates, corpus of bill/settlement pairs and dispute outcomes under contractual data rights, CA-signed recovery record) and stress-tested against the 2019–2026 moat record (eight moat hypotheses, three held). But the red team itself concludes the accumulation is "hygiene, not pricing power", the memo labels it HYP, and no experiment in the 30/60/90-day plan measures whether anything accumulates (the only mechanism is a data-rights clause in the engagement letter). Honest, but the "tested" half of the item is prospective | `executive-decision.md` §3, §5.10; `red-team-review.md` §4(j), §7; `30-day-execution-plan.md` §3 Week 3 |
| 33 | Commercial scenarios and unit economics produced | Complete | Workbook with 8 sheets, 1,904 formulas, scenario selector, 10/100/1,000-customer P&L for three scenarios and three finalists, unit economics, path to first revenue, operational constraints, 40 sources; prose summary; gross-margin caveat carried consistently | `commercial-model.xlsx`; `commercial-model-summary.md`; `executive-decision.md` §5.12 |
| 34 | Key assumptions and sensitivity documented | Complete | Assumptions sheet with evidence class, source ID and must-validate flag per row; one-way tornado and two-way price × win-rate grids; yellow must-validate list in prose | `commercial-model.xlsx` `Assumptions`, `Sensitivity`; `commercial-model-summary.md` "Sensitivity", "Evidence gaps" |

### 1.8 Red-team and execution

| # | Item | Status | Explanation | Evidence |
|---|---|---|---|---|
| 35 | Five critical assumptions and strongest counterarguments | Complete | A1–A5 for F2 with evidence against, severity and resolving test; five-row tables for F1 and F3; thirteen hostile questions answered | `red-team-review.md` §3, §4, §5 |
| 36 | Research and ranking updated after red-team | Complete | F1 77→63, F2 76→71, F3 72→60, H4 67→53, H5 64→53, H6 64→55 with cell-level rationale; cluster-2 red team run to fix the fairness problem; ~10-point haircut convention; dissent recorded without changing the ranking | `red-team-review.md` §1, §6, §8; `decision_brief.md` §7–§9; `opportunity-scorecard.csv` `score_change_rationale` |
| 37 | Cheapest invalidating experiment identified | Complete | F2-A (≤14 days, ≈₹0 compute); kill-on-data step precedes any arithmetic; F1-A0 is one email | `executive-decision.md` §5.14; `red-team-review.md` §10; `technical-validation-plan.md` §6 |
| 38 | 7 / 30 / 90-day plans included | Complete | Day-by-day table for days 1–7 with hours and cost; weeks 2–4; gates at days 30, 60, 90 with dates; budget; weekly metrics; "what not to do" | `30-day-execution-plan.md` §2–§7; `executive-decision.md` §5.15–5.16 |
| 39 | Stop conditions specified | Complete | Stop conditions at each gate; five ordered kill criteria in the red team; Reject condition in the decision | `30-day-execution-plan.md` §4; `red-team-review.md` §10; `executive-decision.md` §6 |

### 1.9 Evidence and files

| # | Item | Status | Explanation | Evidence |
|---|---|---|---|---|
| 40 | All material claims have traceable sources | Complete | 431 ledger rows (L001–L431, contiguous) with class, source, dates, decision informed and note file; 318 of 318 distinct URLs in six deliverables appear verbatim in the notes. 44 ledger rows carry "no URL in note": all are coordinator-synthesis, author-inference, database-output or "searched, none found" rows and are classed Unknown or Hypothesis, i.e. labelled as non-primary rather than dressed as sourced | `research-ledger.csv`; §3 checks 3 and 1 below |
| 41 | Facts / estimates / hypotheses / unknowns distinguished | Complete | Five-class scheme (VF/IC/EST/HYP/UNK) defined in the memo and applied inline in every artifact; ledger distribution 252 VF · 68 IC · 60 EST · 26 HYP · 25 UNK; "est." tag on every budget figure in the plan | `executive-decision.md` §2; `research-ledger.csv` `evidence_class`; `30-day-execution-plan.md` preamble |
| 42 | No invented research, access, experiments or customer commitments | Complete | Pattern search across all deliverables (`we ran / interviewed / conducted`, `agreed / signed / committed`, `results showed`, `pilot underway`, `letter of intent`) returned no hits; the red team states that "none of the sixteen hypotheses has a single customer interview behind it"; interview counts in the metrics table are targets at 0; proof pack labelled synthetic; CTUIL email text makes no claims about a company or customers | §3 check 4b below; `red-team-review.md` §1; `30-day-execution-plan.md` §2 Day 2, Day 5, §6 |
| 43 | All nine artifacts created or limitations documented | Complete | executive-decision.md, competitive-landscape.csv (+gaps.md), opportunity-scorecard.csv (+method.md), research-ledger.csv, data-source-catalog.csv, technical-validation-plan.md, commercial-model.xlsx (+summary.md), red-team-review.md, 30-day-execution-plan.md all present and non-empty; every CSV parses; the workbook opens with cached values | directory listing; §3 below |
| 44 | Final decision understandable without reading every file | Complete | The memo states its frame, defines the evidence classes, carries the ranking, the recommendation, the experiment thresholds, the 7/30/60/90-day gates and a 15-row ledger of key numbers, and says which other file holds the detail | `executive-decision.md` §1, §2, §6, §7 |

## 2. Consistency findings

Checked: ranking and recommendation across `executive-decision.md` §1/§4/§6, `opportunity-scorecard.csv` (`post_score`, `expected_score_after_haircut`, `final_rank`), `red-team-review.md` §8 and `decision_brief.md` §9 — **identical** (F2 71 · F1 63 · F3 60 · H16 69 raw → ~59 · H13 60 · H7 62 → ~52 · H8 59 · H9 58 · H10 56 · H6 55 · H11 53 · H12 53 · H4 53 · H5 53 · H14 51 · H15 48; "Validate First on F2" in all four). F2-A pass (median ≥1.5% and ≥₹5 lakh/yr at ≥3 of 5) and fail (<0.5% at 4 of 5), F2-B pass (≥4/10 pay or lost money, and ≥3 accept success-fee audit) and fail (<2 and none accept) are word-for-word consistent across memo, plan and 30-day plan. Budget (≈₹1.43 lakh / ≈₹4.7–4.85 lakh), gate dates, base-case economics (ARPA ₹5.63 lakh, payback 1.4 / 18.4 months, revenue ₹66.4 lakh / ₹6.64 Cr / ₹66.4 Cr, EBITDA ₹6.1 Cr) match between memo, summary and workbook.

Inconsistencies found (none edited):

1. **Recovery-channel condition on F2-A** — present in `executive-decision.md` §5.14 and applied to the Day-30 gate in §5.16; absent from `technical-validation-plan.md` §6.1 and `30-day-execution-plan.md` §4 (both carry only the overcharge-vs-avoidable-loss split). `red-team-review.md` §10 uses a different test ("more than half of the value is litigation-only" = kill) from the memo's ("administrative-channel share alone must clear 1.5% / ₹5 lakh"). Recorded as Partial (item 27).
2. **F1-A fail band** — `technical-validation-plan.md` §4.4: pass AUC ≥0.70 and Brier better than CTUIL's date; fail AUC <0.60 or no gain; inconclusive <150 rows. `30-day-execution-plan.md` §4 and `executive-decision.md` §5.16: fail = AUC <0.70, no Brier condition. The 0.60–0.70 band has no verdict in the plan. Recorded under item 27.
3. **BESS operational fleet** — `executive-decision.md` uses ≈12.6 GWh (§4 F3); `technical-validation-plan.md` §5.5 uses "≈80% of 6.8 GWh, Jun 2026" with attribution and reconciles all three figures in §9 item 15; `red-team-review.md` §5 gives 6.8 GWh (June) and ≈12.6 GWh (October) with dates; `opportunity-scorecard.csv` H3 `uncertainty_notes` records the conflict; `research-ledger.csv` L005 is marked superseded by L313/L355. **`competitive-landscape-gaps.md` item 3 still states "only ~758 MWh of storage was installed at end-2025 vs ~102 GWh tendered" with no reconciliation note** — the one deliverable using the stale figure unqualified. `decision_brief.md` §3 (a note) also retains 758 MWh, superseded by its own §7–§8.
4. **Competitive-landscape gaps note not refreshed after the red team** — items 1, 2 and 14 of `competitive-landscape-gaps.md` describe CTUIL as PDF-only and F2 settlement as unserved / unscanned; the red team and memo document CTUIL's filterable table and four F2 incumbents. `competitive-landscape.csv` has no row for Customized Energy Solutions or BridgeIT. Recorded as Partial (items 6 and 8).
5. **Evidence-class label drift on one figure** — the 18.7 GW C&I OA / 37,558 GEOA approvals figure is classed VF in `executive-decision.md` §1, §5.6, §7 (IEEFA PDF URL) and IC in `red-team-review.md` §2 (jmkresearch.com URL). Both URLs are in the notes; the class differs because the two documents cite different copies of the same report. Minor.
6. **Pricing anchor phrasing** — `executive-decision.md` §5.5 cites Zenatix as "8–12%-of-bill pricing"; `red-team-review.md` §3 A3 cites the same article as "~₹30k/site/yr in 2017". Both figures appear in `f2_f3_commercial_facts.md` lines 70 and 333–334; not contradictory, but a reader comparing the two documents sees different anchors from one source.
7. **Frame reference** — `30-day-execution-plan.md` preamble cites `decision_brief.md` §7 as the frame; §9 is the binding section. The thresholds and ranking it uses are nonetheless those of §9. Cosmetic.

## 3. Mechanical verification log

All scripts were written to the session scratch directory and run with `python3 -I`. Working directory for relative paths: `/home/user/VideoGEN/research/venture-opportunity/`.

**Check 1 — CSV parsing** (`csv_check.py`: `csv.reader`, column-count per row, newline-in-cell scan, id contiguity on column 1).

| File | Header columns | Data rows | Rows with wrong column count | Cells containing newline | ID column | Contiguous |
|---|---|---|---|---|---|---|
| competitive-landscape.csv | 23 | 70 | 0 | 0 | `company` (text) | n/a |
| opportunity-scorecard.csv | 61 | 16 | 0 | 0 | `hypothesis_id` H1–H16 | Yes, sorted, no duplicates |
| research-ledger.csv | 13 | 431 | 0 | 0 | `claim_id` L001–L431 | Yes, sorted, no duplicates |
| data-source-catalog.csv | 25 | 108 | 0 | 0 | `dataset_id` D001–D108 | Yes, sorted, no duplicates |

Empty cells: only `finalist_code` on the 13 non-finalist scorecard rows (intended). Weighted-score recomputation (`score_check.py`): all 16 `pre_score` and `post_score` values equal Σ(weight×score)/5.

**Check 2 — commercial-model.xlsx** (`xlsx_check.py`, openpyxl, loaded twice: formulas and `data_only=True`).
- Sheets (8): README, Assumptions, Unit economics, Path to first revenue, Scenarios, Sensitivity, Operational constraints, Sources.
- Formulas: Assumptions 84 · Unit economics 213 · Path to first revenue 289 · Scenarios 603 · Sensitivity 593 · Operational constraints 122 · README 0 · Sources 0 = **1,904** (matches `commercial-model-summary.md`).
- Scenario selector: `Assumptions!C3` = 2 (Base) with label `D3 = CHOOSE($C$3,"Conservative","Base","Upside")`; 146 `INDEX(...,$C$3)` formulas drive the Active column. No data-validation dropdown is attached to C3 (free-typed integer; README states the 1/2/3 convention).
- Error strings in cached values (`#REF!`, `#N/A`, `#VALUE!`, `#DIV/0!`, `#NAME?`, `#NUM!`, `#NULL!`): **0**.
- Formula cells with no cached value: 11, all in `Path to first revenue` row 48 (`=IF(...,C25,"")`), whose result is the empty string; openpyxl reports an empty-string cache as None. Not errors.
- Sources sheet: S1–S40 (40 anchors), matching the summary.

**Check 3 — URL integrity** (`url_check.py`, regex extraction, random seed 20261017, no fetching). Distinct URLs: executive-decision.md 34 · red-team-review.md 77 · technical-validation-plan.md 62 · 30-day-execution-plan.md 23 · opportunity-scorecard.csv 66 · competitive-landscape.csv 191 · **318 distinct across the six files**. Random sample of 40: **40 of 40 found verbatim** in at least one research note. Full population check: **318 of 318 found verbatim**. URLs not found in any note: **none**.

**Check 4a — model / vendor identifiers** (case-insensitive `grep -rinoE` over deliverables and notes for the ten identifier strings specified in the audit brief: the four assistant and company names, three further assistant product names, one open-weight model family name, and the campaign-tracking query-parameter token). Deliverables: **0 hits**. Notes: 1 line, `red_team_cluster2.md:109`, an inference sentence saying a plant energy manager with a general-purpose chat assistant could fill BEE Form A; it names two assistant products generically and is not a tool attribution. No campaign-tracking query parameter anywhere.

**Check 4b — invented experiments or commitments** (`grep -rniE` for `we (ran|conducted|interviewed|tested|spoke|surveyed|piloted)`, `interviews (were) (conducted|completed|held)`, `(customer|consumer|developer)s? (has|have|had) (agreed|signed|committed)`, `signed (letter|LOI|contract)s? (from|with)`, `results (showed|show|were)`, `pilot (is )?(underway|running|live)`, `has committed`, `committed to (pay|a pilot)`, `letter of intent` over all deliverable .md and .csv files): **0 hits**.

**Check 5 — consistency**: see §2. Threshold strings (`1.5%`, `0.5%`, `₹5 lakh/yr`, `≥3 of 5`, `4 of 5`, `≥4 of 10`/`≥4/10`, `≥3 accept`, `<2 and none`, `AUC ≥0.70`) grepped across the four narrative deliverables; "channel|administrative|litigation" grepped in the plan and 30-day plan to confirm the recovery-channel condition is absent there.

**Check 6 — counts**: 16 hypotheses (scorecard) · 17 named initial-customer organisations in `executive-decision.md` §5.2 (Shahi Exports, Himatsingka Seide, Biocon, Infosys, Wipro / Wipro GE Healthcare, Toyota Tsusho, Sansera, Narayana Hrudayalaya, Manipal Hospitals, Bagmane, RMZ, Manyata, BIAL, Kirloskar Ferrous, Kalyani Steels, Mukand, Orient Cement), each with a reason and the generic public route · interview scripts: 15-question F2 script in `30-day-execution-plan.md` Day 3 and 15-question F1 script in `f1_customers_and_buying.md` §F · rejected set documented (items 12) · thresholds (item 27) · 7/30/90-day plans and stop conditions (items 38–39).

**Mechanical fixes applied: none.** No CSV failed to parse and no header was broken, so nothing was edited.

## 4. Known limitations of this research (from the notes' Gaps sections)

1. **Portals unreachable from the research sandbox.** Grid-India / NLDC and all five RLDC sites (described from secondary sources only), Gujarat, Rajasthan, Tamil Nadu, AP and Telangana SLDCs (503 / TLS / proxy errors), data.gov.in (503), PXIL (connection reset), REConnect's site (503 twice), the legacy SRPC host, ERPC files, and the GESCOM/HESCOM consumer-list downloads (1.2 KB error stubs). 17 of 108 catalog rows are `Unreachable-from-sandbox` (`india_electricity_data_sources.md` line 5, Q3, Q4; `f2_f3_commercial_facts.md` line 23, 97; `data-source-catalog.csv`).
2. **Search-budget exhaustion.** Three Phase-B notes record that the shared web-search budget ran out mid-task, leaving items unsearched or on direct fetches only: RS Metrics / SpaceKnow / Ursa financials, One Concern / Climate X status, Verisk / CoreLogic 2025 results, Indian QCA pricing and switching, Arbutus / Energy Exemplar / Jakson / Sterlite analytics, Umbra and Intuitive Machines 2025–26 (`commoditization_and_failures.md` lines 7, 61, 88, 139, 225, 266; `energy_software_india_forecasting.md` lines 5, 42, 75, 161; `global_eo_companies.md` lines 7, 110).
3. **Unparsed primary PDFs.** The KERC tariff order of 27 Mar 2025 (FY26–FY28 wheeling, SLDC and operating ₹/kWh charges) was never parsed; the MERC 131/2024 refund order is "exists, not read"; SECI-ESS-IV RfS and the standard BESPA were not parsed for merchant clauses; the EU CBAM communication template was not downloaded; KERC 2026 / GERC / RERC / TNERC / MERC DSM regulation texts not read directly (`f2_f3_commercial_facts.md` lines 33, 184; `technical-validation-plan.md` §9 items 3, 9; `red-team-review.md` §9 items 6, 8; `red_team_cluster2.md` line 111; `energy_software_india_forecasting.md` line 42).
4. **No fee benchmarks.** No published Indian fee for OA bill audit or advisory (Mercados, Idam, PManifold, CES, Elevate searched), for connectivity / GNA consulting, for QCA services (rate cards unpublished), for a CTUIL data licence or an IEX commercial licence; every price in the commercial model is a hypothesis anchored to proxies (`f2_f3_commercial_facts.md` lines 66, 83–84; `f1_customers_and_buying.md` line 134; `commercial-model-summary.md`).
5. **HQ cities marked as estimates.** Tier-2 developer HQs in the F1 customer table and the HQs of Kirloskar Ferrous, Kalyani Steels, Mukand, Orient Cement and Sona Comstar in the F2 table are from general knowledge, not fetched sources; 7 landscape rows carry "not found in notes" or "city not found in notes" in `hq` (`f1_customers_and_buying.md` line 74; `f2_f3_commercial_facts.md` line 281; `competitive-landscape.csv`).
6. **No customer contact.** Zero interviews were conducted; every willingness-to-pay score is desk-derived; the 17 named organisations are prospects from public lists, not conversations (`red-team-review.md` §1).
7. **Evidence class mix.** 30 of 70 competitor rows are Estimate and 6 Unknown; 44 of 431 ledger rows have no URL (synthesis / inference / "searched, none found"); 13 of 108 catalog rows are Unknown-class. The late reversal on public per-plant ground truth (RPC weekly files) rests on one SRPC week verified by download, with retention depth, revision handling and licence unverified (`decision_brief.md` §8.1; `technical-validation-plan.md` §9 items 18–19).
8. **Regulatory items pending at the access date** that could move the ranking: KERC FY27 additional-surcharge determination, the Supreme Court matter on legacy banking, MERC capacity-based banking (comments closed 12 Oct 2026), Karnataka HC and Delhi HC DSM matters, the GNA 4th amendment (draft), CMETS-WR / RVPN charging rules, and market-coupling regulations (`red-team-review.md` §9; `technical-validation-plan.md` §9).

---

## Post-audit fixes (coordinator, 2026-10-17, after the audit above)

1. **Item 6** — Added rows for Customized Energy Solutions India and BridgeIT to `competitive-landscape.csv` (now 72 rows; sources copied from `red_team_counterevidence.md`). Re-validated: 72 rows × 23 columns, parses, no embedded newlines.
2. **Item 8** — Appended a post-red-team note to `competitive-landscape-gaps.md` superseding items 1, 2 and 14 (CTUIL's filterable table and RESTRICTED margins; four F2 incumbents; vendor scan completed) and corrected item 3's storage figure to ≈12.6 GWh with the reconciliation note.
3. **Item 27** — The recovery-channel condition on F2-A now appears in `technical-validation-plan.md` §6.1 and in the Day-30 gate of `30-day-execution-plan.md` §4 with the same wording as `executive-decision.md` §5.14 (administrative-channel amounts only; litigation-only amounts reported separately and excluded). The F1-A band is aligned to the technical plan in all three files: pass AUC ≥0.70 and Brier better than CTUIL's own expected date; fail AUC <0.60 or no gain over CTUIL's date; inconclusive 0.60–0.70 or <150 usable test rows. The red-team review's "more than half litigation-only = kill" remains as its own, stricter formulation and is consistent with the memo's rule (both fail when litigation-only value dominates).
4. **Item 32** — Added a forward measure of accumulating advantage to the Day-90 gate in `30-day-execution-plan.md` §4 and `executive-decision.md` §5.16: ≥24 audited site-months, ≥2 error classes recurring at ≥2 sites each, and the second site in a state recomputed in under half the hours of the first; missing all three means the asset is not compounding and the business should be priced as an audit practice.

Remaining known inconsistencies left as documented (not errors): the evidence-class drift on the 18.7 GW figure (Verified fact when cited to the IEEFA PDF, Independently corroborated when cited to the JMK page); `decision_brief.md` §3 retains the superseded 758 MWh figure, which its own §7–§8 override. No experiment was run and no customer was contacted anywhere in this research.
