# Energy software landscape: India RE forecasting, scheduling, DSM, QCA, asset performance, grid analytics, trading (+ global comparables)

Access date for every URL: 2026-10-17. Evidence classes used: **Verified fact** (primary regulation/filing/company page read directly), **Independently corroborated** (two or more independent secondary sources), **Estimate** (my calculation from cited inputs), **Hypothesis** (inference, not yet evidenced), **Unknown** (searched, not found). "Informs" = the diligence decision the item feeds.

Research-process note: the shared web-search budget was exhausted mid-task; after that point I worked only from direct fetches of known URLs, locally extracted PDFs (CERC notification, Prayas, Forum of Regulators, REConnect deck, IEEFA, Adani FY26 AR, ReNew FY26 20-F) and Tracxn. Items that needed further searching are listed as Gaps.

---

## Q1. What is the Indian regulatory demand driver (CERC DSM 2024, X-factor order, state F&S regs) and who bears deviation cost?

### Takeaway
Forecasting is a legal obligation for essentially every utility-scale wind/solar plant in India, and from 1 April 2026 the penalty-free bands halved (solar/hybrid ±5%, wind ±10%) with under-injection beyond band costing up to 200% of PPA tariff at ISTS level. The generator (or its pooled QCA group) bears the cost; DISCOMs do not. Intra-state regimes (e.g., Karnataka 2026) use small fixed paise/unit slabs with an annual cap of 3 paise/unit, which makes the intra-state penalty pool structurally small compared with ISTS.

### Cited Findings
- CERC (Deviation Settlement Mechanism and Related Matters) Regulations, 2024, No. L-1/260/2021/CERC, dated 05 Aug 2024. WS-seller deviation formula to 31.03.2026: Deviation% = 100 × (Actual − Scheduled)/Available Capacity; from 01.04.2026: denominator = X% of Available Capacity + (100−X)% of Scheduled Generation, X to be fixed by separate order. — [CERC 192-Noti.pdf](https://www.cercind.gov.in/regulations/192-Noti.pdf) [Verified fact; pub 2024-08-05; informs: size of penalty exposure]
- Same regulation, Reg. 8(4), charges for WS sellers (incl. QCA-pooled stations) with no frequency linkage: over-injection receivable @ contract rate within VLwS(1), @ 90% of contract rate in VLwS(2), zero beyond; under-injection payable @ contract rate in VLwS(1), @ 110% in VLwS(2), @ 200% of contract rate beyond VLwS(2). Volume limits to 31.03.2026: solar/hybrid VLwS(1) ≤10%, VLwS(2) 10–15%; wind ≤15%, 15–20%. From 01.04.2026: solar/hybrid ≤5%, 5–10%; wind ≤10%, 10–15%. — [CERC 192-Noti.pdf](https://www.cercind.gov.in/regulations/192-Noti.pdf) [Verified fact; informs: penalty model]
- Same regulation, Note-2: in QCA aggregation the contract rate is the weighted average of pooled sellers' rates; Available Capacity is cumulative inverter/turbine capability; de-pooling of deviation charges among sellers is "as per the methodology mutually agreed upon between the QCA and such individual WS seller(s)". Standalone ESS is treated as a general seller; co-located ESS follows the WS rule when RE is injecting. — [CERC 192-Noti.pdf](https://www.cercind.gov.in/regulations/192-Noti.pdf) [Verified fact; informs: QCA tooling gap (de-pooling is unregulated and contractual)]
- Normal Rate (NR) of deviation charges = highest of (A) weighted-avg I-DAM ACP, (B) weighted-avg RTM ACP, (C) 1/3 I-DAM + 1/3 RTM + 1/3 ancillary service charge. — [CERC 192-Noti.pdf](https://www.cercind.gov.in/regulations/192-Noti.pdf) [Verified fact]
- CERC suo-motu order dated 31 Mar 2026 fixed the X glide path: solar/hybrid 100% (FY27), 90, 75, 55, 30, 0% (from FY32); wind 100, 95, 85, 65, 35, 0%. Bands tightened to ±5%/±10% from 1 Apr 2026. Implementation is subject to Delhi High Court writ petitions against the DSM Regulations 2024; the Court directed no coercive action pending hearing. — [Energetica India, 1 Apr 2026](https://www.energetica-india.net/news/cerc-notifies-phased-x-factor-reduction-for-wind-and-solar-tightens-deviation-bands-from-april-2026); corroborated by [Mondaq](https://www.mondaq.com/india/renewables/1779874/central-electricity-regulatory-commission-sets-trajectory-for-deviation-computation-in-renewable-energy-sector) and [PSU Watch, 3 Apr 2026](https://psuwatch.com/newsupdates/cerc-tightens-dsm-for-wind-and-solar-generators-writ-petitions-challenge-order-in-delhi-hc) [Independently corroborated; informs: timing risk — the whole tightening could be stayed]
- ReNew's FY2026 Form 20-F confirms: "a Suo-Motu order was issued by CERC on March 31, 2026 regarding determination of value of 'X'", and describes the X-factor as "a scaling parameter that increases penalties based on the schedule rather than the available capacity, thereby incentivizing better forecasting and scheduling". — [ReNew 20-F FY2026](https://www.sec.gov/Archives/edgar/data/0001848763/000119312526325073/rnw-20260331.htm) [Verified fact]
- Grid-India study cited in the consultation: under the new bands, time-within-band falls to 45–58% (solar), 32–73% (wind), 38–47% (hybrid); developers criticised it as covering 16 projects over 41 weeks. NSEFI estimated IRR hits up to 5.5 pp (solar-hybrid) and up to 24 pp (wind) under high-deviation scenarios. — [Mercom](https://www.mercomindia.com/cerc-proposes-tightening-grid-deviations-by-renewable-energy-projects) (search snippet; page later returned 404) and [PSU Watch](https://psuwatch.com/newsupdates/cerc-tightens-dsm-for-wind-and-solar-generators-writ-petitions-challenge-order-in-delhi-hc) [Independently corroborated for the 16-project/41-week point; IRR numbers are a single secondary-source snippet → treat as Estimate]
- Prayas (Energy Group), 17 Oct 2025 comments, based on 15-min DSM data for FY24–FY25 covering >70% of ISTS-connected W/S capacity in WR and SR: tightening bands cuts time-blocks-within-limits by 20–30% without pooling; pooling at the pooling-station reduces penalties 30–65% at X=100; benefits of pooling vanish once X falls below ~60%. — [Prayas comments PDF](https://energy.prayaspune.org/images/pdf/CERC_suo-motu_proposal_on_X_for_RE-DSM_Prayas_comments_17-10-25.pdf) [Verified fact (read PDF text); informs: value of pooling/QCA software]
- Prayas: since 16 Sep 2024 penalties beyond the outermost band were doubled, and aggregation via QCA at pooling stations was allowed at ISTS level for the first time. — same PDF [Verified fact]
- Who bears: the FOR model regulations define the QCA as an agency that "Undertake[s] commercial settlement of all charges on behalf of the generators, including payments to the State UI pool accounts" and "de-pooling of payments… settling them with the individual generators"; the generator remains the economic payer. — [Forum of Regulators, Model F&S Regulations 2015](https://forumofregulators.gov.in/Data/study/MR.pdf) [Verified fact; informs: who the customer is (generator, not DISCOM)]
- FOR model (intra-state) charge slabs for sale within the state: absolute error ≤10% nil; >10–20% ₹0.50/unit on the excess; >20–30% +₹1.00/unit; >30% +₹1.50/unit (older plants: 15/25/35% thresholds). For sale outside the state: under-injection at the fixed rate up to 15%, 110% of fixed rate for 15–25%, 120% beyond. — [FOR MR.pdf](https://forumofregulators.gov.in/Data/study/MR.pdf) [Verified fact]
- Karnataka: KERC F&S/DSM Regulations 2026 gazetted 22 Jun 2026 (replacing 2015 regs): solar band ±5% (from ±10%); charges on scheduled generation; annual deviation charges capped at 3 paise per unit of annual generation at the pooling station/QCA; revision point moves to 7th/8th block (IEGC 2023 alignment); ESS zero tolerance; buyers excluded. — [SolarQuarter, 24 Jun 2026](https://solarquarter.com/2026/06/24/kerc-notifies-dsm-regulations-2026-tightens-forecasting-norms-for-solar-wind-and-hybrid-projects-in-karnataka/) [Verified fact (secondary report of a primary gazette; primary PDF not fetched)]
- Karnataka 2026 solar slab (per Power Peak Digest / EQ): ≤5% nil; >5–15% ₹0.25/unit; >15–25% +₹0.50/unit; >25% +₹0.75/unit; applicability wind ≥10 MW, solar/hybrid ≥5 MW (contracted capacity at pooling point); one QCA per pooling substation; SLDC becomes default F&S agency if no QCA appointed, with "applicable service charges"; late payment 0.04%/day; SLDC to publish QCA registration procedure incl. "qualifying criteria and fees" within 60 days. — [Power Peak Digest](https://powerpeakdigest.com/karnataka-renewable-dsm-regulations/); [EQ Mag](https://www.eqmagpro.com/kerc-forecasting-scheduling-deviation-settlement-mechanism-and-related-matters-for-sellers-of-wind-solar-and-ws-hybrid-generation-sources-regulations-2026-eq/) [Independently corroborated]
- Karnataka history: 2022 amendment cut the band from ±15% to ±10% after QCAs/SLDC/generators filed comments on implementation difficulties. — [SolarQuarter, Jan 2023](https://solarquarter.com/2023/01/17/kerc-reduces-permitted-deviations-to-10-for-solar-wind-projects/) (search snippet; page 403 on fetch) [Independently corroborated via KERC regs index](https://kerc.karnataka.gov.in/27/regulations/en)
- Maharashtra (MERC 2018 F&S regs): QCAs for ISTS-connected projects must deposit a corpus of ₹25,000/MW (solar) and ₹50,000/MW (wind); the ₹2,250/day scheduling and revision charges were later exempted. — [Mercom, 3 Jan 2019](https://www.mercomindia.com/qca-maharashtra-pay-25000-mw-solar) and [Mercom](https://www.mercomindia.com/maharashtra-scheduling-forecasting-solar-wind) (snippet) [Independently corroborated; informs: QCA working-capital burden]
- REConnect (2019) called the MERC ₹50,000/MW wind and ₹25,000/MW solar payment security "irrational", and flagged that TN & Maharashtra require QCAs to run a 24-hour control centre with voice recording and "complete control" over injection feeders. — [REConnect deck to CERC Expert Group, 29 Jul 2019](http://www.cercind.gov.in/2019/expert-group/Stakeholders%20Presentation/REConnect.pdf) [Verified fact (read PDF)]
- Tamil Nadu: QCA charges "are mutually agreed upon and paid directly by the generators" — no regulated per-MW fee. — [Mercom TN](https://www.mercomindia.com/tamil-nadu-regulator-wind-and-solar-integration) (search snippet; 404 on fetch) [single secondary source]
- Odisha draft: generators bear QCA cost where they fail to appoint one. — [Mercom Odisha](https://www.mercomindia.com/odisha-forecasting-scheduling-wind-solar) (snippet; 404 on fetch) [single secondary source]
- Telangana: ReNew subsidiaries have challenged the levy of deviation/periphery charges under TSERC F&S Regulations 2018 and obtained a stay subject to deposit. — [ReNew 20-F FY2026](https://www.sec.gov/Archives/edgar/data/0001848763/000119312526325073/rnw-20260331.htm) [Verified fact; informs: litigation reduces intra-state cash flows]
- Prayas 2016 (grid integration report): under the then FOR framework, a generator's revenue did not change for −15%…+15% error and even at −27%/+33% error "the loss to the generator is only 2%". — [Prayas, Sep 2016](https://energy.prayaspune.org/images/pdf/gridzintegrationzreport.pdf) [Verified fact; informs: historical penalty levels were tiny, which explains commoditised QCA pricing]

### Inferences
- The ISTS regime (CERC) is where the money is: 200% of PPA tariff beyond band vs. Karnataka's ₹0.25–0.75/unit slabs capped at 3 paise/unit annually. Any software value proposition must be sized separately for ISTS vs. intra-state plants.
- The X-factor glide path makes penalties scale with scheduled generation rather than capacity from FY28 onward, which (per Prayas) is where losses jump (solar 4%→10%, wind 2–4%→16–24% of PPA revenue). The "pain" grows roughly 2–6× over 2027–2031 if the Delhi HC does not stay it.
- De-pooling methodology is contractual (CERC Note-2(c)), and REConnect reported "very little consensus" and disputes — a plausible software gap (QCA settlement/de-pooling tooling).

### Gaps
- Full text of KERC 2026 regs, GERC 2019, RERC 2017, TNERC 2023 and MERC 2018 not read directly (fetches 403/404 or not attempted after search budget exhausted). Wind/hybrid slab rates in Karnataka 2026 not confirmed.
- Outcome of the Delhi HC writ petitions (petitioners, hearing dates) — Unknown.

---

## Q2. QCA regime: what a QCA does, how it is appointed/paid, how many exist, typical commercial terms and prices

### Takeaway
QCAs are generator-appointed (majority authorisation), SLDC-registered aggregators that forecast, schedule, settle and de-pool DSM at a pooling station. No regulator sets a QCA fee; prices are bilateral and no public tender award discloses a ₹/MW/month figure. Revenue and portfolio data from the two largest independent QCAs imply low single-digit thousands of rupees per MW per year for pure F&S — a commoditised service — yet both are profitable (Manikaran ~20% net margin), so the margin sits in scale, not price.

### Cited Findings
- FOR model definition: QCA "may be one of the generators or any other mutually agreed agency" to provide schedules with revisions, handle metering/data/communication, undertake commercial settlement incl. State UI pool payments, de-pool receipts, and "shall be treated as a State Entity". — [FOR MR.pdf](https://forumofregulators.gov.in/Data/study/MR.pdf) [Verified fact]
- Karnataka 2026: registration with SLDC "based on authorisation from a majority of generators"; only one QCA per pooling substation; SLDC is default F&S provider for non-appointing generators; SLDC to set qualifying criteria and fees. — [Power Peak Digest](https://powerpeakdigest.com/karnataka-renewable-dsm-regulations/) [Verified fact (secondary of primary)]
- NTPC Green Energy tenders for QCA services: 250 MW Anantapur (Jul 2025; 12 months + 6; security deposit = 5% of "monthly billed service charges", i.e., monthly billing; scope = SCADA/meter integration, day-ahead/week-ahead 96-block schedules, intra-day revisions, web app, 24/7 support, weekly DSM de-pooling logs); 296 MW Fatehgarh (Aug 2025); 325 MW Shajapur (2025); 850 MW SKB-1&2 + Nokhra (Sep 2026; 730-day contract; no EMD, no reverse auction). None publish a rate. — [Energetica, 18 Jul 2025](https://www.energetica-india.net/news/ntpc-green-energy-invites-bids-for-qca-services-at-its-250-mw-anantapur-solar-plant); [SolarQuarter, 29 Sep 2026](https://solarquarter.com/2026/09/29/ntpc-green-energy-invites-bids-for-qca-services-for-850-mw-solar-projects/); [Mercom Fatehgarh](https://www.mercomindia.com/ntpc-green-invites-bids-to-select-qca-for-296-mw-solar-project) [Verified fact for scope/tenure; price: Unknown/not published]
- NLC India tender (May 2023) for QCA/F&S for 1.4 GW in Tamil Nadu (140 MW Neyveli, 550 MW Tirunelveli, 51 MW wind, 659 MW Aruppukottai), 24-month tenure; no price published. — [Energetica, 24 May 2023](https://www.energetica-india.net/news/nlc-looking-for-qca-services-for-14-gw-of-solar-and-wind-plants) [Verified fact]
- REConnect Energy (Bengaluru) self-reported QCA portfolio (2019): Karnataka ~5,200 MW (132 pooling sub-stations, 350+ generators), Rajasthan ~3,600 MW, MP ~1,700 MW, AP ~750 MW, Gujarat ~1,800 MW and Maharashtra ~900 MW (registration in progress), ~1,500 MW other states; "55% market share wind/solar forecasting in IPP category, ~14 GW, 910 active clients"; "awarded all 11 REMCs". — [REConnect deck, 29 Jul 2019](http://www.cercind.gov.in/2019/expert-group/Stakeholders%20Presentation/REConnect.pdf) [Verified fact that it was claimed; company claim]
- REConnect 2022 filing: forecasts >14,000 MW wind and 8,000 MW solar across 10 states; "largest QCA" in Karnataka, Rajasthan, AP, MP, UP, Punjab. — [REConnect comments to CERC 2022](https://cercind.gov.in/2022/draft_reg/IEGC-Comments-2022/REConnect%20Energy.pdf) (search snippet) [company claim]
- REConnect financials (Tracxn, from filings): FY26 (31 Mar 2026) revenue ₹72.1 crore (+39% YoY), net profit ₹4.28 crore; employees 225 (Sep 2026); total equity funding only US$0.57M (seed, Sep 2014; Infuse Ventures, SINE, angels, Caspian Debt). Inc42 gives FY25 revenue ₹45.8–52.0 crore (internally inconsistent) and PAT ₹3.8 crore. — [Tracxn via MCP, accessed 2026-10-17]; [Inc42](https://inc42.com/company/reconnect-energy/financials/) [Verified fact (filing-derived); informs: scale of incumbent and bootstrapped economics]
- Manikaran Analytics (Delhi/Kolkata, Manikaran Power group): claims "largest RE F&S and QCA portfolios in India, aggregate capacity exceeding 90 GW", "3,500+ clients", "5,000+ daily schedules", logos incl. Adani, Tata, EDF, Greenko, JSW, Ayana, Engie, Brookfield, Serentica, Torrent, CLP, Enel; BESS/hybrid F&S; no pricing. — [manikarananalytics.in](https://www.manikarananalytics.in/) [company claim]
- Manikaran Analytics financials (Tracxn): FY25 revenue ₹35.9 crore (+47%), net profit ₹7.38 crore (~20.5% net margin), 22 employees (labour filing, Aug 2025), unfunded. — [Tracxn via MCP] [Verified fact (filing-derived); informs: QCA is profitable at scale with tiny headcount]
- Tata Power Trading states it is registered as QCA in Karnataka, AP, Rajasthan and Gujarat. — [tatapowertrading.com](https://tatapowertrading.com/?p=552) (search snippet; DNS failed on fetch) [company claim]
- energy & meteo systems (Germany) sells power forecasts in India to "more than a dozen large electricity providers" and "several QCAs" for "several gigawatts" of parks since 2016; no names, no price. — [emsys](https://www.emsys-renewables.com/customers/customer_projects/power-forecasts_india.php) [Verified fact (company page); informs: QCAs buy forecasts from European vendors — the forecast layer and the QCA service layer are separable]
- Reuters (3 Dec 2025): Adani Green said it "works with overseas technology firms in Switzerland and France" and deep-learning models yet still struggles with hyper-local weather; IndiGrid Solar said IMD data updates only every 6 hours making short-term forecasting "next to impossible"; no radars in RE-rich areas. — [MarketScreener/Reuters](https://www.marketscreener.com/news/india-s-clean-energy-firms-seek-better-weather-data-as-rules-tighten-ce7d51dedc8af327) [Verified fact; informs: weather-data layer is an acknowledged gap even for the largest IPP]
- REConnect (2019) on QCA pain points: scope creep (MP LVRT data, TN curtailment responsibility, MP "any other charges"), no AMR so meter reading needs physical presence, weekly meter data in TN/MAH, poor site data availability, no consensus on de-pooling methodology causing disputes, every state has a different portal/file format and "No state as API/FTP based submission". — [REConnect deck 2019](http://www.cercind.gov.in/2019/expert-group/Stakeholders%20Presentation/REConnect.pdf) [Verified fact; informs: QCA-ops tooling gap, albeit 2019-dated]

### Inferences
- Implied price per MW (Estimate, crude): Manikaran FY25 revenue ₹35.9 crore ÷ claimed 90 GW = ₹3,990/MW/yr ≈ ₹330/MW/month. Even if only one-third of the 90 GW is paid F&S/QCA work, that is ≈₹1,000/MW/month. REConnect FY26 ₹72.1 crore ÷ ~22 GW (2022 portfolio; revenue also includes REC/ESCert trading and REMC/utility contracts) ≈ ₹32,800/MW/yr ≈ ₹2,700/MW/month upper bound. Working hypothesis: pure F&S/QCA pricing is on the order of ₹500–3,000/MW/month (₹6k–36k/MW/yr), i.e., 0.1–0.7% of a 1 MW solar plant's ~₹48 lakh annual PPA revenue. **This is an estimate, not a quoted price.**
- Both incumbents are profitable and bootstrapped/unfunded, with 22–225 staff, so the business is a services business with software inside, not a VC-style SaaS. A new entrant competing on QCA price would be fighting a ₹/MW race against players that already cover 20–90 GW.
- The buyers who tender publicly (NTPC Green, NLC) use 12–24 month contracts with monthly billing — low switching cost, which cuts both ways for a new entrant.

### Gaps
- No quoted ₹/MW/month QCA rate from any tender award, SLDC circular or company disclosure — **not published**. Would need NGEL/NLC award documents or a QCA's rate card.
- Count of registered QCAs per state: no SLDC-published lists found for Karnataka (KPTCL SLDC), Gujarat, Rajasthan, TN or AP.
- Statkraft India as QCA: **Unknown** — no evidence found. Arbutus Consultants, Energy Exemplar India, Jakson, Sterlite analytics: not researched before the search budget ran out.
- Penalty-sharing terms in QCA contracts (does the QCA bear deviation beyond Y%?): not published anywhere found.

---

## Q3. Size of the pool: installed wind+solar, capacity under forecasting obligations, estimated annual DSM penalties for RE

### Takeaway
India had 171 GW solar and 59 GW wind at 30 Sep 2026; roughly 130–190 GW of that (ground-mount utility solar + hybrid + wind) falls under F&S obligations. No official aggregate of DSM paid by RE generators exists; Prayas's plant-level FY25 analysis (≈4% of PPA revenue for an individual solar plant, 2–4% for wind at X=100, 3.1%/0.9% pooled) and REConnect's 1–7.5 paise/unit range let me bound the national RE deviation pool at roughly ₹1,500–8,000 crore/yr at X=100 (ISTS-heavy), rising sharply as X falls.

### Cited Findings
- MNRE physical progress as of 30 Sep 2026: solar 171,051.46 MW (ground-mounted 125.65 GW, rooftop 33.41 GW, hybrid solar component 5.36 GW, off-grid 6.63 GW); wind 59,201.07 MW; total RE incl. large hydro 299.25 GW; Sept-2026 additions 3,011 MW solar, 681 MW wind. — [MNRE](https://mnre.gov.in/en/physical-progress/); [Saur Energy](https://www.saurenergy.com/solar-energy-news/india-adds-2456-gw-renewable-energy-capacity-in-h1-fy-2026-27-12637483) [Verified fact (search-snippet of MNRE table); informs: TAM]
- JMK: 35.2 GW solar and 4.69 GW wind added Jan–Sep 2026. — [JMK Research](https://jmkresearch.com/india-added-35-2-gw-of-solar-and-4-69-gwo-f-wind-capacity-in-the-first-nine-months-of-2026/) [Independently corroborated]
- Applicability thresholds (Karnataka 2026): wind ≥10 MW, solar/hybrid ≥5 MW at pooling point; CERC regime applies to all ISTS-connected WS sellers. — [Power Peak Digest](https://powerpeakdigest.com/karnataka-renewable-dsm-regulations/); [CERC 192-Noti.pdf](https://www.cercind.gov.in/regulations/192-Noti.pdf) [Verified fact]
- Prayas FY25 plant-level DSM losses relative to PPA rate: individual solar plants ~4% at X=100 to 10% at X=0; individual wind 2–4% at X=100 to 16–24% at X=0; pooled solar station PSS_S_11: 3.1%→6.6%; pooled wind PSS_W_4: 0.9%→13.2%. Penalty for PSS_S_11 before pooling ₹69.3 crore (X=100) → ₹123.5 crore (X=0); after pooling ₹45.8 → ₹96.4 crore. PSS_W_4: ₹43.2 → ₹285.8 crore before pooling; ₹14.8 → ₹213.4 crore after pooling. Both stations are ≥1,000 MW (text: "RE-rich pooling stations with capacities of 1000 MW or more (i.e. PSS_S_11 and PSS_W_4)"). — [Prayas 17 Oct 2025](https://energy.prayaspune.org/images/pdf/CERC_suo-motu_proposal_on_X_for_RE-DSM_Prayas_comments_17-10-25.pdf) [Verified fact (read PDF)]
- REConnect (2019) "Expected DSM" with its model: ~2.5–7.5 paise/unit with preliminary model, ~1.0–2.5 p/u with real-time data, ~0.8–1.0 p/u with AvC updates, <0.1 p/u with aggregation (>1,000 MW). Gujarat: state-aggregate wind DSM <0.1 p/u vs standalone wind 3.9 p/u and solar 1.8 p/u; Karnataka: <0.5 p/u aggregated vs 6 p/u for a small wind project. — [REConnect deck 2019](http://www.cercind.gov.in/2019/expert-group/Stakeholders%20Presentation/REConnect.pdf) [Verified fact (vendor's own 2019 data, pre-2024 rules)]
- Karnataka 2026 caps annual deviation charges at 3 paise/unit of annual generation. — [SolarQuarter](https://solarquarter.com/2026/06/24/kerc-notifies-dsm-regulations-2026-tightens-forecasting-norms-for-solar-wind-and-hybrid-projects-in-karnataka/) [Verified fact]
- Prayas: ≥50.05 Hz occurred ~9.5% of time in FY25 but affected <1% of generation (so the "no payment for over-injection at high frequency" rule has negligible revenue impact). — [Prayas 2025 PDF](https://energy.prayaspune.org/images/pdf/CERC_suo-motu_proposal_on_X_for_RE-DSM_Prayas_comments_17-10-25.pdf) [Verified fact]
- DISCOM side comparison: Uttar Pradesh paid ~₹374 crore in DSM charges in H1 FY23. — [CEEW blog](https://www.ceew.in/blogs/what-is-deviation-settlement-mechanism-power-grid-system-security-india) (search snippet; 403 on fetch) [single secondary]
- Adani Green FY26 AR related-party table shows "Reimbursement received for Deviation Settlement Mechanism Charges paid on behalf of" SPVs at ₹1 crore / ₹0 — DSM is handled centrally but the disclosed amounts are immaterial at SPV level. — [AGEL FY26 AR](https://www.adanigreenenergy.com/-/media/project/greenenergy/investor-downloads/annual-reports/fy26.pdf) [Verified fact (read PDF)]

### Inferences
- Capacity under F&S obligation (Estimate): ground-mount solar 125.65 GW + hybrid 5.36 GW + wind 59.2 GW ≈ 190 GW; excluding sub-5 MW solar and legacy sub-10 MW wind, ~160–180 GW is a defensible "obligated" base. Rooftop (33 GW) and off-grid (6.6 GW) are out of scope.
- National RE DSM pool (Estimate; see Q11 calculation): at 1–2.5 p/u (good QCA, real-time data) on ~300 BU of obligated W/S generation ≈ ₹300–750 crore/yr; at 2.5–7.5 p/u ≈ ₹750–2,250 crore/yr; using Prayas's 2–4% of PPA revenue on ISTS plants ≈ ₹1,500–3,500 crore/yr. Range ₹500–3,500 crore/yr at X=100; 2–6× higher by FY31 at X=0 if the order survives. This is an Estimate; no regulator publishes the number.

### Gaps
- No CERC/Grid-India/FOR/CEEW/IEEFA/Ember publication quantifying total DSM paid by RE generators — Unknown. Grid-India's RE DSM pool accounts (RLDC pool statements) would be the primary source but were not fetched.
- Exact MW of PSS_S_11 and PSS_W_4 not stated in the Prayas text (only "≥1,000 MW").

---

## Q4. Upcoming changes (VPP/aggregation, GNA, Green Open Access, FDRE, BESS tenders, RTM/GDAM/intraday): do they create new software needs?

### Takeaway
Three structural shifts create new optimisation problems that did not exist under plain-vanilla PPAs: (1) FDRE/RTC contracts with demand-fulfilment ratios and 1.5× tariff shortfall penalties plus permitted merchant sale of surplus storage; (2) RTM volume growing 41% YoY to 54.85 BU with DSM Normal Rate explicitly tied to I-DAM/RTM prices; (3) CERC's solar-hour/non-solar-hour GNA framework. Each requires joint forecast + storage-dispatch + bid optimisation, which incumbents market only generically.

### Cited Findings
- IEX FY26: record 141 BU traded (+17%); RTM 54.85 BU (+41% from 38.90 BU); DAM incl. HP-DAM 62.78 BU (+2.4%); Green Market (G-DAM + G-TAM) 10.78 BU (+23% from 8.75 BU); G-DAM weighted-avg price ₹3.59/unit (−10.6%). — [SolarQuarter, 6 Apr 2026](https://solarquarter.com/2026/04/06/indian-energy-exchange-reports-record-141-bu-trade-volume-in-fy26-prices-decline-on-higher-supply); [Outlook Business](https://www.outlookbusiness.com/corporate/iex-sees-highest-ever-electricity-traded-volume-of-141-bu-in-fy26) [Independently corroborated; informs: bid-optimisation TAM]
- SECI 1 GW FDRE-RTC tender (Aug 2026): tariff ₹5.25/kWh (Kengeri Prime 180 MW, Resolven 150, Hexa Climate 150, Hero Solar 120, EMIF II 100, Purvah 70; Juniper Green ₹5.26); DFR 90% peak, 80% off-peak (70% for two months Jul–Sep), 90% annual; 25-yr PPA; ESS-backed. — [pv magazine India, 7 Aug 2026](https://www.pv-magazine-india.com/2026/08/07/secis-1-gw-fdre-rtc-power-tender-discovers-inr-5-25-kwh-tariff/) [Verified fact]
- SECI FDRE-IX: 1,200 MW / 4,800 MWh ISTS peak power; 4-hour buyer-nominated peak window, 4,000 kWh/MW/day; monthly under-delivery >10% penalised at 1.5× PPA tariff on shortfall; batteries must charge from RE; surplus storage usable for spot trading on IEX in the other 20 hours. — [pv-tech](https://www.pv-tech.org/seci-launches-4800mwh-fdre-tender-backed-by-co-located-energy-storage/); [PCEnersys](https://www.pcenersys.com/industry-news/seci-India-largest-bess-tender-2026.html) (search snippets) [Independently corroborated for size/penalty; merchant-surplus clause single-source]
- SECI 50 MW/100 MWh short-term BESS tender: charging/discharging under SECI control, DSM penalties "levied separately on the ESSD for the charging and discharging activities". — [Saur Energy](https://www.saurenergy.com/solar-energy-news/seci-floats-short-term-tender-for-50-mw100-mwh-bess-with-2-hour-storage-12457149) (snippet) [single secondary]
- CERC DSM 2024 treats standalone ESS as a general seller (frequency-linked bands, ±10% or 100 MW), and co-located ESS under WS rules while RE injects — storage scheduling has its own penalty regime. — [CERC 192-Noti.pdf](https://www.cercind.gov.in/regulations/192-Noti.pdf) [Verified fact]
- ReNew 20-F FY26: a GNA amendment introduced a "solar-hours based framework" distinguishing solar and non-solar hours, which "determines transmission access and curtailment priority, basis technology (solar/wind/BESS/hybrid)"; projects may seek GNA or T-GNA accordingly. ReNew also flags "limited ability to accurately forecast or hedge against intraday pricing fluctuations" for merchant sales and that BESS integration "introduces complex operational dependencies, including … forecasting accuracy". — [ReNew 20-F FY2026](https://www.sec.gov/Archives/edgar/data/0001848763/000119312526325073/rnw-20260331.htm) [Verified fact; informs: largest listed IPP admits an intraday price-forecasting/hedging gap]
- KERC issued Demand Flexibility/Demand Side Management Regulations on 10 Mar 2026 mandating DISCOM DF/DSM cells, load research and demand-flexibility targets with incentives/penalties. — [ReNew 20-F FY2026](https://www.sec.gov/Archives/edgar/data/0001848763/000119312526325073/rnw-20260331.htm) [Verified fact; informs: DISCOM-side aggregation/VPP demand in Karnataka]
- Green Energy Open Access Rules 2022: eligibility cut from 1 MW to 100 kW; banking at least monthly, ≥30% of monthly consumption, no carry-forward; GEOA banking charge in kind 8% of banked energy; cumulative C&I open-access RE 18.7 GW by end-FY2024 (46% CAGR FY22–24, +90.4% in FY24); Gujarat+Rajasthan >70% of recent installs; 37,558 GEOA applications approved by 10 Dec 2024; Karnataka facilitation fee ₹25,000/MW; state banking charges vary (Karnataka 2% in-kind to Chhattisgarh 30%). — [IEEFA/JMK, Dec 2024](https://ieefa.org/sites/default/files/2024-12/Impact%20of%20Green%20Energy%20Open%20Acess_Dec2024.pdf) (read PDF text); [JMK](https://jmkresearch.com/renewable-sector-published-reports/impact-of-green-energy-open-access-rules-2022/); [ETPI state-wise analysis](https://etpi.in/sites/default/files/publications/ETPI_Green%20Energy%20Open%20Access%20Regulations%20in%20India.pdf) (snippet) [Verified fact / Independently corroborated]
- 2025 C&I open-access solar additions reported as 7.8 GW (Mercom via a vendor blog) — unverified. — [Qbits Energy blog](https://qbitsenergy.com/blog/open-access-solar-india-explained/) [Hypothesis-grade]
- India Energy Stack: the Task Force chair (R.S. Sharma) proposes open-source DPI principles for the power sector, citing data silos from proprietary DISCOM software. — [OpenSourceForU, Sep 2025](https://www.opensourceforu.com/2025/09/ram-sewak-sharma-pushes-open-source-digital-infrastructure-for-indias-power-sector/) [Verified fact (secondary)]

### Inferences
- FDRE/RTC contracts convert a forecasting problem into a daily co-optimisation (RE forecast × storage state-of-charge × DFR compliance × IEX price forecast × DSM). The 1.5× tariff shortfall penalty on ₹5.25/kWh power is ₹7.9/kWh — an order of magnitude above intra-state DSM slabs. This is the highest-value, least-served software problem identified.
- RTM at 54.85 BU with 15-min gate closure, plus DSM NR tied to RTM/I-DAM prices, means a plant's deviation cost is now a market price, not a fixed slab — which favours software that forecasts both generation and price.
- C&I open access (18.7 GW+, tens of thousands of consumers, state-specific banking rules) is a plausible mid-market software wedge (banking/settlement reconciliation), but no incumbent's product or pricing was found, so it remains a Hypothesis.

### Gaps
- No evidence found of a CERC/FOR Virtual Power Plant or aggregator regulation as of Oct 2026 (search not completed) — Unknown.
- What software C&I open-access buyers use for scheduling/banking: not found; no vendor identified.
- GDAM standalone FY26 volume not disclosed (only combined Green Market 10.78 BU).

---

## Q5. India-focused companies: layer, product, customers, pricing, funding, HQ (esp. Bengaluru)

### Takeaway
The Indian forecasting/QCA layer is dominated by two profitable, essentially unfunded service firms (REConnect, Bengaluru; Manikaran Analytics, Delhi/Kolkata), with a long tail of trading houses (Tata Power Trading) and European forecast vendors (emsys, Meteologica, Swiss/French firms used by Adani) upstream. The asset-performance layer has already been consolidated by global buyers (Prescinto→IBM 2024, SenseHawk→Reliance 2022/Nextracker 2024). ReNew has exited Climate Connect (UK entity sold Jun 2024; Indian entity sold Apr 2025), so the "ReNew-owned" premise is outdated.

### Cited Findings
- **REConnect Energy Solutions** (Bengaluru, founded 2010; co-founders Vibhav Nuwal, Vishal Pandya): F&S/QCA, REC/ESCert trading (claimed 45% share, 440 clients, 2019), demand-forecast trials with grid operators, REMC forecasting award (claimed all 11, 2019); FY26 revenue ₹72.1 crore, PAT ₹4.28 crore; 225 staff; US$0.57M lifetime equity (2014 seed, Infuse Ventures/SINE). — [Tracxn via MCP]; [Inc42](https://inc42.com/company/reconnect-energy/financials/); [REConnect deck 2019](http://www.cercind.gov.in/2019/expert-group/Stakeholders%20Presentation/REConnect.pdf) [Verified fact / company claims as labelled]
- **Manikaran Analytics Ltd** (Manikaran Group; Delhi office, Tracxn lists Kolkata; founded 2011): F&S/QCA for wind, solar, hybrid+BESS; claims >90 GW, 3,500+ clients; FY25 revenue ₹35.9 crore, PAT ₹7.38 crore, 22 employees; unfunded. — [manikarananalytics.in](https://www.manikarananalytics.in/); [Tracxn via MCP] [Verified fact (filings) / company claims]
- **Climate Connect** (founded 2010, New Delhi/Pune; founders Nitin Tanwar, Sanand Sule): AI/ML forecasting and optimisation for DISCOMs (25 GW load portfolio) and RE generators (6 GW at acquisition); acquired by ReNew 4–5 Jun 2020 (terms undisclosed; prior funding $1.2M). ReNew then sold Climate Connect Digital Ltd (UK) on 21 Jun 2024 for INR 4 million against net liabilities, and sold Regent Climate Connect Knowledge Solutions Pvt Ltd (India) on 22 Apr 2025 for INR 86 million vs net assets INR 84 million; "Digital Solutions" headcount 53 (FY24) → 28 (FY25) → 0 (FY26). Current website lists Enterprise Net-Zero, Carbon Projects, Clean Energy Trading; "12+ GW generation managed", "50+ GW peak grid balancing daily"; London + Gurugram offices. — [EQ Mag, 4 Jun 2020](https://www.eqmagpro.com/renew-power-acquires-climate-connect/); [CB Insights](https://www.cbinsights.com/company/climate-connect-technologies); [ReNew 20-F FY2026](https://www.sec.gov/Archives/edgar/data/0001848763/000119312526325073/rnw-20260331.htm); [climateconnect.digital](https://climateconnect.digital/) [Verified fact; informs: a strategic acquirer exited the Indian forecasting-software asset at roughly book value — a negative signal on standalone value]
- **Prescinto** (Bengaluru, founded 2016, CEO Puneet Singh Jaggi): renewable APM SaaS, 16 GW in 14 countries, clients incl. SoftBank Energy and Macquarie; acquired by IBM 15 Oct 2024 (undisclosed) into Maximo Application Suite; total equity raised US$15.7M (Series A $3.0M, Feb 2024; investors Venture Catalysts, Mumbai Angels, IPV, BlackSoil, Pegasus…); FY23 revenue ₹8.15 crore, net loss ₹25.9 crore; 31 employees (Aug 2026, −11 YoY). — [pv magazine India, 15 Oct 2024](https://www.pv-magazine-india.com/2024/10/15/ibm-acquires-prescinto-for-renewables-asset-performance-management/); [ESG Today](https://www.esgtoday.com/ibm-acquires-ai-powered-renewables-asset-performance-management-software-provider-prescinto/); [Tracxn via MCP] [Verified fact; informs: Bengaluru APM startup burned ~3× revenue and sold; APM is a buyer's market]
- **SenseHawk** (California/Bengaluru-origin): Reliance Industries agreed 6 Sep 2022 to buy a majority (79.4%) stake for US$32M incl. growth funding; 140+ customers, 15 countries, >100 GW; later reported acquired by Nextracker/Nextpower (Aug 2024) — sources do not reconcile the two transactions. — [Saur Energy](https://www.saurenergy.com/solar-energy-news/reliance-industries-to-acquire-majority-stake-in-californias-solar-digital-platform-sensehawk); [Crunchbase](https://www.crunchbase.com/organization/sensehawk); [Wikipedia Nextpower](https://en.wikipedia.org/wiki/Nextpower) [Independently corroborated for Reliance deal; 2024 sale unreconciled]
- **SmartHelio** (Ecublens, Switzerland; founded 2019; YC): GAIA AI agent, Autopilot, AI Audit, BESS analytics, CRA; 8 GW AUM, 20,000+ plants onboarded; US$6.0M raised (Series A $5M Dec 2022; Collab Fund, Serpentine, Pegasus, Y Combinator); 31 employees. India presence not stated on site. — [smarthelio.com](https://www.smarthelio.com/); [Tracxn via MCP] [Verified fact]
- **Skymet Weather Services**: runs its own meso/micro-scale NWP and provides wind/solar forecasts to RE companies and power generators. — [Wikipedia](https://en.wikipedia.org/wiki/Skymet_Weather_Services); [Digital Knowledge Centre](https://digitalknowledgecentre.in/?p=2944) (snippets) [single secondary each]
- **Tata Power Trading**: registered QCA in Karnataka, AP, Rajasthan, Gujarat. — [tatapowertrading.com](https://tatapowertrading.com/?p=552) (snippet) [company claim]
- **energy & meteo systems** (Oldenburg): forecasts for "more than a dozen" Indian electricity providers and several QCAs; several GW. — [emsys](https://www.emsys-renewables.com/customers/customer_projects/power-forecasts_india.php) [Verified fact]
- **Meteologica** (Spain): 600 GW wind / 260 GW solar forecast globally, 80+ countries, xTraders tool; has an india@meteologica.com contact. — [meteologica.com](https://www.meteologica.com/) [Verified fact (company page)]
- **REMCs**: 11 centres (7 SLDCs: TN, KA, AP, MH, MP, GJ, RJ; 3 RLDCs; NLDC) inaugurated 28 Feb 2020, ~55 GW monitored, POWERGRID implementing agency, Grid-India (POSOCO) operates regional/national. Business Standard reported REConnect won F&S for all 11, Siemens the western region and OSI the southern region (article returned 403; single source). — [pv magazine India, 28 Feb 2020](https://www.pv-magazine-india.com/2020/02/28/power-minister-inaugurates-11-renewable-energy-management-centers/); [PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1604689); [Business Standard](https://www.business-standard.com/article/economy-policy/centre-launches-project-to-integrate-renewable-power-with-national-grid-119100800786_1.html) [Verified fact for structure; vendor split single-source]
- **Adani Green (FY26 AR)**: "AI-based generation forecasting improves accuracy, enabling smarter scheduling and despatch decisions… lower volatility losses"; "AI-based weather and generation forecasting models… reduces generation losses from forecast deviations, lowers grid imbalance penalties"; in-house AI/ML forecasting tools; R&D list includes "Short Term Weather and Power Forecasting" and "AI based Weather Forecasting"; ENOC cloud platform; made representation on "Introduction of X factor in DSM Regulation" at stakeholder consultation. — [AGEL FY26 AR](https://www.adanigreenenergy.com/-/media/project/greenenergy/investor-downloads/annual-reports/fy26.pdf) [Verified fact (read PDF); informs: top-3 IPPs build in-house and buy weather data abroad]
- **ReNew (20-F FY26)**: lists DSM as a regulatory risk factor; states it is "incorporating… forecast and scheduling and e-surveillance" into O&M; divested its digital subsidiary (above). — [ReNew 20-F FY2026](https://www.sec.gov/Archives/edgar/data/0001848763/000119312526325073/rnw-20260331.htm) [Verified fact]

### Inferences
- Bengaluru has produced both an APM exit (Prescinto→IBM) and the largest independent QCA (REConnect); talent and customer proximity exist, but the two paths diverge: services (profitable, slow) vs. SaaS (loss-making, acquired).
- The strategic buyers of Indian energy software to date (IBM, Reliance, Nextracker, ReNew) bought for capability, and ReNew later exited at ~book, which suggests limited standalone pricing power in forecasting software.
- Logo overlap (Adani, Tata, JSW, Greenko, Ayana appear on Manikaran's site while Adani says it builds in-house) implies large IPPs multi-source: in-house models + QCA service + foreign weather data.

### Gaps
- Not researched (search budget): Arbutus Consultants, Energy Exemplar India, Jakson, Sterlite Power analytics, Ampin, Mitra, Vibrant Energy, Greenko's internal platform, Enlog, PowerAgent. Tracxn free-text screening failed (field not queryable); only the five named vendors were pulled.
- Tata Power Renewables, JSW Energy, Greenko, Avaada, Sprng, Hero Future, Ayana, O2, ACME, Juniper, Azure annual-report language on forecasting: not retrieved (searches not run).
- Pricing for every Indian vendor: not published.

---

## Q6. Global comparables: what they sell, who pays, public price, adoption evidence

### Takeaway
Only Grid Status publishes an entry price (Pro ≈ US$500/month per a third-party profile; free API tier 500k rows/month); Solcast, Raptor Maps, Clir, Yes Energy, Nira, Pearl Street, Kevala, Camus, Paces, Meteologica, REsurety and Sitetracker are all quote-only. Adoption evidence is mostly vendor-stated GW figures; the one independently funded, control-room-adopted forecaster (Open Climate Fix/NESO) is a non-profit paid through regulator innovation funds, which is itself a signal about forecasting's monetisation.

### Cited Findings
- **Solcast** (DNV): plans Starter/Pro/Max/Custom for Historical, TMY, Live, Forecast; Forecast Starter = 6-hourly updates, 30/60-min; Pro = 15-min updates; Max = 5-min. No prices; "Request a quote". Free: 10 live/forecast requests at own sites, 15 site-months historical. — [solcast.com/pricing](https://solcast.com/pricing) [Verified fact; price: not published]
- **Grid Status**: open-source `gridstatus` library (BSD-3) free; hosted API free tier 500,000 rows/month; Pro reported at US$500/month and Enterprise custom (Preqin profile); raised $8M led by Energize Capital (Aug 2024); third-party revenue estimate $1.7M (2025, GetLatka), 15 employees. — [apis.io profile, 11 Jul 2026](https://apis.io/plans/gridstatus/gridstatus-plans-pricing/); [Preqin](https://www.preqin.com/data/profile/asset/grid-status-inc-/700360) (snippet); [NA Clean Energy](https://nacleanenergy.com/alternative-energies/grid-status-raises-8m-to-democratize-access-to-real-time-grid-data-to-meet-demands-of-rapidly-changing-energy-grid) (snippet); [GetLatka](https://getlatka.com/companies/gridstatus.io) [Price: single secondary; revenue: Estimate (third-party)]
- **Amperon**: AI demand/supply forecasting for traders, IPPs, utilities, retailers, C&I; $20M Series B (4 Oct 2023, Energize; D.E. Shaw, Veriten, HSBC AM; Ørsted a customer-investor); $30M total. No pricing. — [ESG Today](https://www.esgtoday.com/energy-analytics-startup-amperon-raises-20-million/) [Verified fact]
- **Raptor Maps**: "100+ GW of solar PV analyzed", 8,100 assets digitised, customers prevented >$82M annualised revenue loss (2022); ENGIE across 90 sites/6.5 GW; Series C $35M (Dec 2024, Maverix) per a weak dataset; no public pricing. — [raptormaps.com/about/impact](https://raptormaps.com/about/impact); [ENGIE](https://innovation.engie.com/en/news/interview/viva-technology/ai-with-impact-how-raptor-maps-is-redefining-solar-asset-management/30545) (snippet) [Verified fact for site claims; funding weak]
- **Clir Renewables**: AI platform "built on 350+ GW"; products Clir Portfolio/Enhance/Associate; buyers = investment managers, asset owners, corporate offtakers (logos: CIP, CPP Investments, Nuveen/Glennmont, HASI, Octopus Energy Generation…); quote-only. — [clir.eco](https://www.clir.eco/) [Verified fact (company page)]
- **Yes Energy**: market data (PowerSignals, Live Power, Demand Forecasts), modelling (EnCompass), bid-to-bill (PowerCore); traders/IPPs/utilities/developers; 1,400+ data sources; Accel-KKR PE-backed; quote-only. — [yesenergy.com](https://www.yesenergy.com/); [Crunchbase](https://www.crunchbase.com/organization/yes-energy) (snippet) [Verified fact]
- **Pearl Street Technologies** (now part of Enverus): SUGAR for transmission providers ("500+ GW contracted by ISOs"), Interconnect® for developers/offtakers with "pricing options for any project development budget" (no figures). — [pearlstreettechnologies.com](https://www.pearlstreettechnologies.com/) [Verified fact]
- **Nira Energy**: substation-level capacity/upgrade-cost prospecting, in-queue and local-study tools; subscription; customers Ørsted, AES, BW Solar, Doral; "700+ GW modeled, 100+ developers, 97% accuracy replicating ISO studies". Funding figures conflict ($500K vs $65.5M vs ~$3.1M) — unreliable. — [niraenergy.com](https://www.niraenergy.com/); [Tracxn](https://tracxn.com/d/companies/nira-energy/__tqVzBJRkWxDta7tKdlWxXtvR0wW_IwT-Uic-3GQbL5M/funding-and-investors) [Verified fact for product; funding Unknown]
- **Kevala**: integrated grid planning, electrification impact, siting, production-cost modelling; customers Exelon, National Grid, CPUC, US DOE; quote-only. — [kevala.com](https://www.kevala.com/) [Verified fact]
- **Camus Energy**: FlexConnect for flexible grid connections (utilities + data centres), Google case study, PPL/AES/co-ops logos; quote-only. — [camus.energy](https://www.camus.energy/) [Verified fact]
- **Paces**: AI agent + reports + expert services for power/data-centre developers; customers Qcells, Demeter, onCORE; quote-only. — [paces.com](https://www.paces.com/) [Verified fact]
- **REsurety**: CleanSight (market/PPA analytics), CleanTrade (CFTC-registered as-generated energy platform), $1.5B transactions, 25 GW+ contracts; quote-only. — [resurety.com](https://www.resurety.com/) [Verified fact]
- **Meteologica**: 600 GW wind/260 GW solar forecast, 100,000+ assets, 80+ countries; quote-only. — [meteologica.com](https://www.meteologica.com/) [Verified fact]
- **Sitetracker**: asset-lifecycle PM platform (telecom + energy transition; RWE, EVgo logos); quote-only. — [sitetracker.com](https://www.sitetracker.com/) [Verified fact]
- **Open Climate Fix** (UK non-profit): Quartz Solar fully integrated into NESO control room (announced 6 Nov 2025), 2.8× more accurate within-day, halves large errors, ≥£30M/yr imbalance-cost saving (up to £150M/yr by 2035); national + ~300 GSP regional forecasts to 36h; funded via NIA/NIC/Ofgem SIF; open-source "Open Quartz" library (FOSDEM 2026); Netherlands national forecast also listed. — [OCF](https://www.openclimatefix.org/insights/neso-adopts-ai-solar-forecasting-control-room); [pv magazine, 7 Nov 2025](https://www.pv-magazine.com/2025/11/07/ai-powered-solar-forecasting-helps-uk-grid-operator-reduce-balancing-costs/) [Independently corroborated; savings are OCF/NESO claims]
- **energy & meteo systems / enercast / DNV Forecaster / Tomorrow.io / Enverus PRISM / Vaisala-3TIER**: pages not retrievable (404/image-only) or not fetched; no prices found. [Unknown]

### Inferences
- The global pattern: forecasting-as-data is quote-priced and increasingly open-sourced (OCF, gridstatus library); money is made either in services/aggregation (QCAs, Amperon's customer-investor model) or in adjacent decision layers (interconnection analytics, bid-to-bill, PPA settlement) where a wrong answer costs the customer far more than the subscription.
- The India analogue of Pearl Street/Nira (interconnection/GNA capacity analytics) does not appear to exist; CTUIL publishes GNA/connectivity lists as PDFs, which is raw material for such a product (Hypothesis).

### Gaps
- Verified prices for Solcast paid tiers, Raptor Maps, Clir, Yes Energy, Enverus, Nira: not published.
- Grid Status $500/month figure is from a Preqin profile snippet, not the vendor page (JS-rendered, 403 on fetch).

---

## Q7. Is RE forecasting in India commoditised/price-competitive, or is there margin?

### Takeaway
Commoditised on price, but not margin-less: the two scaled QCAs are profitable (Manikaran ~20% net, REConnect ~6% net) on revenue that implies low thousands of rupees per MW per year. Margin comes from operating leverage (22 staff serving a claimed 90 GW), not from pricing power. Forecast accuracy is bounded by public weather data (IMD 6-hourly, no RE-area radars), which caps differentiation at the model layer.

### Cited Findings
- Manikaran Analytics FY25: revenue ₹35.9 crore, PAT ₹7.38 crore, 22 employees. REConnect FY26: revenue ₹72.1 crore, PAT ₹4.28 crore, 225 employees. — [Tracxn via MCP] [Verified fact (filings)]
- Manikaran claims >90 GW and 3,500+ clients; REConnect claimed ~22 GW (2022) and 910 clients (2019). — [manikarananalytics.in](https://www.manikarananalytics.in/); [REConnect CERC 2022](https://cercind.gov.in/2022/draft_reg/IEGC-Comments-2022/REConnect%20Energy.pdf) [company claims]
- TN regulator leaves QCA charges to bilateral agreement. — [Mercom TN](https://www.mercomindia.com/tamil-nadu-regulator-wind-and-solar-integration) (snippet) [single secondary]
- NGEL re-tenders QCA services on 12–24 month cycles with no EMD, no reverse auction (Sep 2026). — [SolarQuarter](https://solarquarter.com/2026/09/29/ntpc-green-energy-invites-bids-for-qca-services-for-850-mw-solar-projects/) [Verified fact]
- Weather-data ceiling: IMD updates every 6 hours; no radars in RE-rich areas; Adani buys from Swiss/French vendors. — [Reuters via MarketScreener, 3 Dec 2025](https://www.marketscreener.com/news/india-s-clean-energy-firms-seek-better-weather-data-as-rules-tighten-ce7d51dedc8af327) [Verified fact]
- Prayas: pooling alone cuts penalties 30–65% at X=100 — aggregation, not model quality, is the biggest lever today. — [Prayas 2025](https://energy.prayaspune.org/images/pdf/CERC_suo-motu_proposal_on_X_for_RE-DSM_Prayas_comments_17-10-25.pdf) [Verified fact]
- REConnect 2019: aggregation drives DSM from 3.9 p/u (standalone wind) to <0.1 p/u (state aggregate). — [REConnect deck](http://www.cercind.gov.in/2019/expert-group/Stakeholders%20Presentation/REConnect.pdf) [Verified fact (vendor data)]

### Inferences
- Implied revenue per MW (Estimate): Manikaran ≈ ₹4,000/MW/yr on claimed GW; REConnect ≤ ₹33,000/MW/yr (upper bound, mixed revenue). A 1 MW solar plant earns ≈ ₹48 lakh/yr at ₹2.5/kWh, so F&S fees are ≈0.1–0.7% of revenue, vs. DSM exposure of 2–4% (Prayas). Customers rationally under-spend on forecasting relative to penalty exposure — but only until X falls.
- Because pooling (a regulatory/organisational act) beats model accuracy, the winning QCA is the one that already controls the pooling station; a software-only entrant cannot pool without becoming the registered QCA (one per PSS in Karnataka).

### Gaps
- No rate card, tender award price, or contract with penalty-sharing terms found. Share of Manikaran/REConnect revenue that is pure F&S vs trading/REMC: not disclosed.

---

## Q8. Who bears deviation penalties and how large per MW per year for a typical solar or wind plant?

### Takeaway
The generator bears them (via the QCA as settlement agent). Using Prayas's FY25 ISTS data, a typical individual solar plant loses ~4% of PPA revenue ≈ ₹1.9 lakh/MW/yr at X=100 (≈₹4.8 lakh at X=0); wind 2–4% ≈ ₹1.6–3.2 lakh/MW/yr (₹12.6–18.9 lakh at X=0). Pooled stations and intra-state (Karnataka, capped at 3 p/u ≈ ₹58k/MW/yr) are far lower. Full calculation in Q11.

### Cited Findings
- Prayas FY25 loss ratios (above). — [Prayas 2025](https://energy.prayaspune.org/images/pdf/CERC_suo-motu_proposal_on_X_for_RE-DSM_Prayas_comments_17-10-25.pdf) [Verified fact]
- Karnataka 3 paise/unit cap; slabs ₹0.25/0.50/0.75. — [SolarQuarter](https://solarquarter.com/2026/06/24/kerc-notifies-dsm-regulations-2026-tightens-forecasting-norms-for-solar-wind-and-hybrid-projects-in-karnataka/); [EQ Mag](https://www.eqmagpro.com/kerc-forecasting-scheduling-deviation-settlement-mechanism-and-related-matters-for-sellers-of-wind-solar-and-ws-hybrid-generation-sources-regulations-2026-eq/) [Verified fact]
- CERC WS-seller charges (100%/110%/200% under-injection; 100%/90%/0% over-injection). — [CERC 192-Noti.pdf](https://www.cercind.gov.in/regulations/192-Noti.pdf) [Verified fact]
- REConnect 1.0–7.5 p/u expected DSM. — [REConnect deck 2019](http://www.cercind.gov.in/2019/expert-group/Stakeholders%20Presentation/REConnect.pdf) [Verified fact (vendor)]
- FDRE-IX shortfall penalty 1.5× PPA tariff on monthly under-delivery >10%. — [pv-tech](https://www.pv-tech.org/seci-launches-4800mwh-fdre-tender-backed-by-co-located-energy-storage/) (snippet) [Independently corroborated]

### Inferences
- See Q11 numeric summary.

### Gaps
- CUF and PPA tariff assumptions are mine (sourced from general market levels, not from a specific cited plant); the Prayas percentages are the load-bearing input.

---

## Q9. Software gaps by segment: what players use today

### Takeaway
Evidence supports gaps in (a) QCA de-pooling/settlement tooling, (b) BESS/FDRE co-optimisation and IEX bid optimisation, (c) intraday price forecasting (ReNew admits it), and (d) a GNA/interconnection-capacity analytics analogue to Nira/Pearl Street. Forecasting-model quality per se is constrained by public weather data, and APM is consolidated by IBM/Reliance/Nextracker.

### Cited Findings
- De-pooling is "mutually agreed" (CERC Note-2(c)); REConnect reports "very little consensus" and disputes; weekly de-pooling logs are an NGEL tender deliverable. — [CERC 192-Noti.pdf](https://www.cercind.gov.in/regulations/192-Noti.pdf); [REConnect 2019](http://www.cercind.gov.in/2019/expert-group/Stakeholders%20Presentation/REConnect.pdf); [Energetica NGEL](https://www.energetica-india.net/news/ntpc-green-energy-invites-bids-for-qca-services-at-its-250-mw-anantapur-solar-plant) [Verified fact]
- "No state has API/FTP based submission; every state has a different portal/format" (2019). — [REConnect 2019](http://www.cercind.gov.in/2019/expert-group/Stakeholders%20Presentation/REConnect.pdf) [Verified fact, dated]
- ReNew: "limited ability to accurately forecast or hedge against intraday pricing fluctuations"; BESS integration depends on "forecasting accuracy". — [ReNew 20-F FY2026](https://www.sec.gov/Archives/edgar/data/0001848763/000119312526325073/rnw-20260331.htm) [Verified fact]
- Manikaran markets hybrid+BESS F&S and "energy arbitrage" as a use case but shows no dedicated optimisation product. — [manikarananalytics.in](https://www.manikarananalytics.in/) [Verified fact]
- Adani Green builds forecasting in-house (ENOC, AI/ML tools) and buys foreign weather data. — [AGEL FY26 AR](https://www.adanigreenenergy.com/-/media/project/greenenergy/investor-downloads/annual-reports/fy26.pdf); [Reuters](https://www.marketscreener.com/news/india-s-clean-energy-firms-seek-better-weather-data-as-rules-tighten-ce7d51dedc8af327) [Verified fact]
- CTUIL publishes GNA/connectivity application lists as PDFs (e.g., "Connectivity under GNA 30062024", "List of connectivity to be made effective 31012025"). — [CTUIL](https://www.ctuil.in/uploads/assets/172191857826pdf_Connectivity%20under%20GNA_30062024.pdf); [CTUIL](https://ctuil.in/uploads/assets/174403072822List%20of%20connectiivty%20to%20be%20made%20effective_31012025_date%20wise.pdf) [Verified fact (exist); informs: raw data for a GNA-analytics product]
- Grid-India/NLDC was directed to frame a procedure with RPCs for deviation computation where scheduled generation is minimal (post-2031). — [Mondaq](https://www.mondaq.com/india/renewables/1779874/central-electricity-regulatory-commission-sets-trajectory-for-deviation-computation-in-renewable-energy-sector) [Verified fact]
- KERC DF/DSM regs (10 Mar 2026) mandate DISCOM demand-flexibility programmes with targets, incentives and penalties. — [ReNew 20-F FY2026](https://www.sec.gov/Archives/edgar/data/0001848763/000119312526325073/rnw-20260331.htm) [Verified fact]

### Inferences
- Segment-by-segment (Hypothesis unless noted): intra-state DSM optimisation — low value (3 p/u cap), served by QCAs; QCA operations tooling — real but the buyer set is ~5–10 QCAs plus SLDCs (small); RTM/GDAM bid optimisation — unserved domestically, buyers are trading desks of IPPs/traders (IEX 141 BU); BESS/FDRE scheduling — highest penalty density (1.5× tariff), new, unserved; C&I open-access banking/settlement — large fragmented buyer base (37k+ GEOA approvals), no identified vendor; DISCOM RE scheduling — REMC/SLDC systems built by POWERGRID vendors, procurement-driven; transmission congestion/GNA analytics — no Indian Nira/Pearl Street found; plant underperformance — consolidated (IBM/Prescinto, Reliance/SenseHawk, Raptor, SmartHelio).

### Gaps
- No direct evidence of what tools IPP trading desks or C&I open-access consumers use today; vendor landscape for those segments not established.

---

## Q10. Competitor table

### Takeaway
Twenty-plus players across six layers; verified prices exist for essentially none except Grid Status's reported $500/month Pro tier and MERC's ₹25k/₹50k per MW QCA security deposits.

### Cited Findings
| Company | Layer | What it sells | Who pays | Verified price | Adoption evidence | Startup compete / adjacent? |
|---|---|---|---|---|---|---|
| REConnect Energy (Bengaluru) | QCA / F&S / REC trading / REMC | F&S, QCA settlement, REC/ESCert trading, utility demand forecasts | RE generators, utilities, Grid-India/SLDCs | not published | FY26 rev ₹72.1 Cr, PAT ₹4.3 Cr; ~22 GW (2022); 225 staff ([Tracxn]; [deck](http://www.cercind.gov.in/2019/expert-group/Stakeholders%20Presentation/REConnect.pdf)) | Compete (QCA); adjacent (settlement tooling) |
| Manikaran Analytics (Delhi/Kolkata) | QCA / F&S | F&S incl. hybrid+BESS, QCA, settlement, de-pooling | RE generators | not published | FY25 rev ₹35.9 Cr, PAT ₹7.4 Cr, 22 staff; claims 90 GW, 3,500 clients ([site](https://www.manikarananalytics.in/); [Tracxn]) | Compete |
| Tata Power Trading | QCA / trading | QCA in KA, AP, RJ, GJ; power trading | RE generators | not published | company claim ([site](https://tatapowertrading.com/?p=552)) | Compete |
| Climate Connect (ex-ReNew) | DISCOM/IPP forecasting, net-zero, trading | Forecasting, decarbonisation, clean-energy trading | DISCOMs, generators, enterprises | not published | 12+ GW, 50+ GW grid balancing (claim); sold by ReNew 2024/2025 at ~book ([site](https://climateconnect.digital/); [20-F](https://www.sec.gov/Archives/edgar/data/0001848763/000119312526325073/rnw-20260331.htm)) | Adjacent |
| energy & meteo systems (DE) | Forecast data | Wind/solar power forecasts | Indian utilities, QCAs | not published | "dozen" providers, several QCAs, several GW ([site](https://www.emsys-renewables.com/customers/customer_projects/power-forecasts_india.php)) | Adjacent (supplier) |
| Meteologica (ES) | Forecast data | Wind/solar/price/load forecasts, xTraders | Operators, traders, TSOs | not published | 600 GW wind/260 GW solar, 80 countries ([site](https://www.meteologica.com/)) | Adjacent |
| Skymet (IN) | Weather/forecast data | NWP-based wind/solar forecasts | RE companies | not published | qualitative ([wiki](https://en.wikipedia.org/wiki/Skymet_Weather_Services)) | Adjacent |
| Prescinto / IBM Maximo (Bengaluru) | APM | Renewable APM SaaS | Asset owners (SoftBank Energy, Macquarie) | not published | 16 GW, 14 countries; FY23 rev ₹8.2 Cr, loss ₹25.9 Cr; acquired Oct 2024 ([pv mag](https://www.pv-magazine-india.com/2024/10/15/ibm-acquires-prescinto-for-renewables-asset-performance-management/); [Tracxn]) | Compete (APM) — consolidated |
| SenseHawk (Reliance→Nextracker) | Solar lifecycle/APM | Construction + O&M digital platform | Developers/EPCs | not published | 140+ customers, 15 countries, >100 GW; $32M deal ([Saur](https://www.saurenergy.com/solar-energy-news/reliance-industries-to-acquire-majority-stake-in-californias-solar-digital-platform-sensehawk)) | Compete (APM) — consolidated |
| SmartHelio (CH) | APM/AI diagnostics | GAIA agent, Autopilot, BESS analytics | Asset owners | not published | 8 GW AUM; $6M raised ([site](https://www.smarthelio.com/); [Tracxn]) | Compete (APM) |
| Raptor Maps (US) | APM / inspection | Solar insights platform | Asset owners/operators (ENGIE, Cypress Creek) | not published | 100+ GW analysed ([site](https://raptormaps.com/about/impact)) | Adjacent |
| Clir Renewables (CA) | Portfolio analytics | Investor-grade reporting, yield reforecast | Investors/asset managers | not published | 350+ GW ([site](https://www.clir.eco/)) | Adjacent |
| Grid Status (US) | Grid market data | Open-source lib, hosted API, dashboards | Traders, analysts, developers | Free 500k rows/mo; Pro ~$500/mo (Preqin snippet); Enterprise custom | $8M raised; ~$1.7M rev est. ([apis.io](https://apis.io/plans/gridstatus/gridstatus-plans-pricing/); [GetLatka](https://getlatka.com/companies/gridstatus.io)) | Adjacent (India analogue possible) |
| Amperon (US) | Demand/supply forecasting | AI forecasts for markets | Traders, IPPs, utilities (Ørsted) | not published | $30M raised ([ESG Today](https://www.esgtoday.com/energy-analytics-startup-amperon-raises-20-million/)) | Adjacent |
| Yes Energy (US) | Market data / bid-to-bill | PowerSignals, EnCompass, PowerCore | Traders, IPPs, utilities | not published | 1,400+ sources; Accel-KKR ([site](https://www.yesenergy.com/)) | Adjacent |
| REsurety (US) | PPA analytics / trading | CleanSight, CleanTrade (CFTC-registered) | Corporate buyers, developers | not published | $1.5B transactions, 25 GW+ ([site](https://www.resurety.com/)) | Adjacent |
| Pearl Street (Enverus) (US) | Interconnection analytics | SUGAR (ISOs), Interconnect (developers) | ISOs, developers | not published ("options for any budget") | 500+ GW contracted by ISOs ([site](https://www.pearlstreettechnologies.com/)) | Adjacent (India GNA analogue) |
| Nira Energy (US) | Interconnection analytics | Prospecting/in-queue/local-study tools | Developers (Ørsted, AES, BW Solar, Doral) | subscription, not published | 700+ GW modelled, 100+ developers ([site](https://www.niraenergy.com/)) | Adjacent |
| Kevala (US) | Grid analytics | Integrated grid planning, siting | Utilities, regulators (Exelon, National Grid, CPUC, DOE) | not published | logos ([site](https://www.kevala.com/)) | Adjacent |
| Camus Energy (US) | Flexible interconnection | FlexConnect | Utilities, data centres (Google case) | not published | logos ([site](https://www.camus.energy/)) | Adjacent |
| Paces (US) | Site/permitting intel | AI agent + reports | Developers (Qcells) | not published | testimonials ([site](https://www.paces.com/)) | Adjacent |
| Open Climate Fix (UK, non-profit) | Solar forecasting | Quartz Solar, Open Quartz (OSS) | NESO via NIA/NIC/SIF funds | n/a (grant-funded) | live in NESO control room, ≥£30M/yr claimed ([OCF](https://www.openclimatefix.org/insights/neso-adopts-ai-solar-forecasting-control-room)) | Model/OSS reference for an Indian build |
| Solcast (DNV) | Irradiance/forecast API | Historical/TMY/Live/Forecast tiers | Developers, operators, forecasters | quote-only; free 10 forecast requests ([pricing](https://solcast.com/pricing)) | widely used (no count) | Adjacent (supplier) |
| Sitetracker (US) | Project/asset lifecycle | PM platform | Owners/EPCs (RWE, EVgo) | not published | logos ([site](https://www.sitetracker.com/)) | Not relevant |

### Inferences
- The only Indian players a software-only founder would directly compete with on day one are REConnect, Manikaran and the trading-house QCAs; all others are either upstream data suppliers or consolidated APM assets.

### Gaps
- Energy Exemplar, Arbutus, Jakson, Sterlite, Ampin, Mitra, Vibrant, Enverus PRISM, Tomorrow.io, DNV Forecaster, Vaisala/3TIER, enercast: not verified.

---

## Q11. Numeric summary of DSM/QCA economics (calculation shown)

### Takeaway
For an ISTS-connected plant at X=100 (FY27), deviation cost ≈ ₹1.9 lakh/MW/yr (solar) and ₹1.6–3.2 lakh/MW/yr (wind); forecasting/QCA fees are an order of magnitude smaller (~₹6k–36k/MW/yr, estimate). By FY31 (X=0) exposure rises to ~₹4.8 lakh (solar) and ₹12.6–18.9 lakh (wind) per MW. Intra-state Karnataka exposure is capped at ~₹58k/MW/yr.

### Cited Findings
Inputs (all cited above): Prayas FY25 loss ratios (solar 4%→10%; wind 2–4%→16–24%; pooled solar 3.1%→6.6%; pooled wind 0.9%→13.2%) — [Prayas 2025](https://energy.prayaspune.org/images/pdf/CERC_suo-motu_proposal_on_X_for_RE-DSM_Prayas_comments_17-10-25.pdf); REConnect 1.0–7.5 paise/unit — [REConnect 2019](http://www.cercind.gov.in/2019/expert-group/Stakeholders%20Presentation/REConnect.pdf); Karnataka cap 3 paise/unit — [SolarQuarter](https://solarquarter.com/2026/06/24/kerc-notifies-dsm-regulations-2026-tightens-forecasting-norms-for-solar-wind-and-hybrid-projects-in-karnataka/); Manikaran/REConnect revenue — [Tracxn via MCP]; installed capacity — [MNRE](https://mnre.gov.in/en/physical-progress/).

Assumptions (mine, Estimate): solar CUF 22%, PPA ₹2.50/kWh; wind CUF 30%, PPA ₹3.00/kWh. 1 MW × 8,760 h × CUF = annual units.

**Per-MW economics (Estimate)**

| Item | Solar (1 MW) | Wind (1 MW) |
|---|---|---|
| Annual generation | 0.22 × 8,760 = 1,927 MWh = 19.27 lakh units | 0.30 × 8,760 = 2,628 MWh = 26.28 lakh units |
| PPA revenue | 19.27 lakh × ₹2.50 = ₹48.2 lakh | 26.28 lakh × ₹3.00 = ₹78.8 lakh |
| DSM loss, individual plant, X=100 (Prayas 4% / 2–4%) | ₹1.93 lakh | ₹1.58–3.15 lakh |
| DSM loss, individual plant, X=0 (10% / 16–24%) | ₹4.82 lakh | ₹12.6–18.9 lakh |
| DSM loss, pooled station, X=100 (3.1% / 0.9%) | ₹1.49 lakh | ₹0.71 lakh |
| DSM loss, pooled station, X=0 (6.6% / 13.2%) | ₹3.18 lakh | ₹10.4 lakh |
| DSM at REConnect "good QCA" 1.0–2.5 p/u | ₹19k–48k | ₹26k–66k |
| DSM at REConnect "preliminary model" 2.5–7.5 p/u | ₹48k–145k | ₹66k–197k |
| Karnataka intra-state cap 3 p/u | ≤₹57.8k | ≤₹78.8k |
| Implied F&S/QCA fee (Manikaran ₹35.9 Cr ÷ 90 GW) | ≈₹4.0k/MW/yr | ≈₹4.0k/MW/yr |
| Implied upper bound (REConnect ₹72.1 Cr ÷ ~22 GW, mixed revenue) | ≈₹33k/MW/yr | ≈₹33k/MW/yr |
| MERC QCA security deposit (one-time, refundable corpus) | ₹25,000/MW | ₹50,000/MW |

**Pool sizing (Estimate)**: obligated W/S base ≈ 160–180 GW (ground-mount solar 125.65 + hybrid 5.36 + wind 59.2 GW, less sub-threshold plants). Annual generation ≈ 130 GW × 1,927 MWh + 55 GW × 2,628 MWh ≈ 250 + 145 = ~395 BU; assume ~75% is ISTS/large-pool and ~25% intra-state/small.
- At REConnect 1–2.5 p/u across all: ₹395–990 crore/yr.
- At Prayas individual-plant ratios on the ISTS share (≈300 BU × avg ₹2.7/kWh × 3%): ≈ ₹2,400 crore/yr; pooled ratios (≈2%): ≈ ₹1,600 crore/yr.
- Working range for the national RE DSM pool at X=100: **₹500–3,500 crore/yr**; at X=0 (FY32): **2–6×** that, i.e., potentially ₹3,000–15,000 crore/yr — *conditional on the Delhi HC not staying the order*.
- Software/QCA fee pool: 170 GW × ₹4k–33k/MW/yr ≈ **₹70–560 crore/yr** (Estimate) — consistent with the two leaders' combined ₹108 crore of revenue being a large share of a ₹100–300 crore market.

### Inferences
- Ratio of penalty exposure to fee spend is ~5–50× today and rises as X falls; the rational buyer will pay more for anything that demonstrably reduces deviation (pooling, real-time AvC/meter data, storage dispatch) — but the existing fee pool (~₹100–300 crore) is small for a venture-scale outcome unless a product captures a share of the avoided penalty or the FDRE/RTM upside.
- For a solo founder: the cheapest verified data path is the open regulatory record (CERC/SLDC statements, CTUIL lists, IEX prices) rather than proprietary weather; the OCF/Open Quartz open-source stack demonstrates a non-proprietary forecasting baseline that could be re-trained on Indian data.

### Gaps
- All ₹/MW fee numbers are implied, not quoted. CUF/tariff assumptions are generic. The national pool estimate lacks a primary Grid-India/SLDC pool-account figure.
