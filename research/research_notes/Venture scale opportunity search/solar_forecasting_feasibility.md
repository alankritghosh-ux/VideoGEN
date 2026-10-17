# Technical feasibility of solar/wind forecasting and plant-performance analytics in India from free/cheap data (software-only founder, Bengaluru, no plant access)

Research date: 2026-10-17 (all URLs accessed 2026-10-17 unless stated). Evidence classes used throughout: **Verified fact** (read on the primary page), **Independently corroborated** (two or more secondary sources agree), **Estimate** (my calculation from verified inputs), **Hypothesis** (recollection or inference not verified in this pass), **Unknown**.

Research-process caveats the report writer must know:
- The web-search budget for this session was exhausted after ~30 searches; the last third of the work relied on direct page fetches only.
- Grid-India (grid-india.in), POSOCO (posoco.in), WRLDC (wrldc.in) returned HTTP 503 on every attempt, and NREL hosts (nsrdb.nrel.gov, nrel.gov) failed DNS from this sandbox. Claims about those sources are therefore marked Hypothesis/Unknown even where I am fairly confident from prior knowledge.
- The Kaggle dataset page is JavaScript-rendered and returned only its title; its licence could not be read.
- The Mercom and SolarQuarter articles on the April-2026 CERC order were paywalled/rate-limited; the order's content is reconstructed from Energetica India and Power Line reports of the September-2025 proposal plus Mercom's headline/subtitle confirming notification.

---

## A. Weather inputs: NWP, satellite irradiance, AI weather models

### Takeaway
A software-only founder can get free, commercially-usable, 0.25° global NWP (ECMWF IFS and AIFS open data, CC-BY-4.0, including surface solar radiation `ssrd`, 4 runs/day, 15-day horizon) and a $29–99/month API (Open-Meteo) that bundles ECMWF/DWD/NOAA models plus an ERA5 archive back to 1940 and a satellite-radiation API. The weak link for India is *satellite-derived irradiance*: CAMS all-sky coverage of India is not confirmed, INSAT-3D access terms and a ready GHI product are unconfirmed, and Solcast publishes no India-specific validation. Open-weight AI weather models (WeatherNext 2, GraphCast/GenCast) are GPU-class (H100 for non-mini models) and effectively off the table for CPU-only inference, but their *outputs* (ECMWF AIFS open data) are free.

### Cited Findings

**ECMWF open data (IFS + AIFS)**
- Licence: "Creative Commons CC-BY-4.0 licence" plus ECMWF Terms of Use; redistribution and commercial use allowed with attribution. Products at 0.25° in GRIB2 "unless stated otherwise"; higher resolution requires a paid Real-time Dissemination Service Agreement. — [ECMWF open data](https://www.ecmwf.int/en/forecasts/datasets/open-data) — Verified fact.
- Models: IFS high-res + ensemble (medium range), AIFS Single (deterministic) and AIFS ENS. Steps: IFS 00z/12z 0–144 h by 3 h then 150–360 h by 6 h (15 days); IFS 06z/18z 0–144 h by 3 h only; AIFS 0–360 h by 6 h for all four cycles. — [ECMWF open data](https://www.ecmwf.int/en/forecasts/datasets/open-data) — Verified fact.
- Solar variable: parameter ID 169 `ssrd` ("Surface short-wave (solar) radiation downwards") is listed for IFS control/ensemble and for AIFS Single and AIFS ENS. No DNI/DHI product is listed. Also 2 m temperature, 10 m and 100 m wind (wind-relevant), total precipitation, MSL pressure. — [ECMWF open data](https://www.ecmwf.int/en/forecasts/datasets/open-data) — Verified fact.
- Latency: page says IFS open data are "released at the end of the real-time dissemination schedule" and AIFS "as soon as the data are produced"; no hour figure is given. Rolling archive keeps only the last 12 runs (~2–3 days); full history needs a Service Agreement. Mirrored on AWS, Azure, GCP; portal capped at 500 simultaneous connections. — [ECMWF open data](https://www.ecmwf.int/en/forecasts/datasets/open-data) — Verified fact.
- IFS Cycle 50r1 (13 May 2026) changed stream names/file naming; the confluence guide was last updated 12 Oct 2026. — [ECMWF open data confluence](https://confluence.ecmwf.int/display/DAC/ECMWF+open+data%3A+real-time+forecasts+from+IFS+and+AIFS) — Verified fact.
- Hypothesis (not verified this pass): IFS 00z open data typically lands ~7–9 h after nominal run time (≈07:00–09:00 UTC ≈ 12:30–14:30 IST), i.e. the 00z run is *not* available for a 10:00 IST day-ahead submission; the previous day's 12z run (available ≈ 00:30–02:30 IST) is what a day-ahead pipeline would use. **Must be verified against the dissemination schedule before building.**
- Hypothesis (not verified; the AIFS documentation URL returned 404 and Hugging Face is blocked from this sandbox): ECMWF released AIFS Single v1 model weights openly in early 2025 under CC-BY-4.0. Not needed for the product since AIFS *outputs* are in open data.

**Open-Meteo**
- Free tier: non-commercial only; 600 calls/min, 5,000/h, 10,000/day, 300,000/month, no uptime guarantee. Paid: Standard 1M calls/month (commercial, no historical/ensemble/satellite-radiation APIs); Professional 5M calls/month (adds Historical, Climate, Ensemble and Satellite Radiation APIs, reserved servers); Enterprise 50M+. Weather data licence CC BY 4.0; server code AGPLv3. — [Open-Meteo pricing](https://open-meteo.com/en/pricing) — Verified fact (prices not rendered on the page).
- Prices: Standard $29/month (1M calls), Professional $99/month (5M calls), Enterprise on request. — [Open-Meteo blog, 12 Jun 2023](https://openmeteo.substack.com/p/api-subscriptions-for-commercial); corroborated by a German directory listing €29/€99 — [ki-syndikat](https://www.ki-syndikat.de/tools/open-meteo/) — Independently corroborated (currency ambiguity $ vs €; one aggregator lists an outdated €4.99 tier).
- Historical Weather API: ERA5 0.25° from 1940, ERA5-Land 0.1° from 1950, ECMWF IFS 9 km from 2017 (no delay), ERA5 updated daily with 5-day delay; hourly `shortwave_radiation` (GHI), `direct_radiation`, `diffuse_radiation`, `direct_normal_irradiance`, `global_tilted_irradiance`. — [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api) — Verified fact.
- Models: 30+ including ECMWF, DWD, NOAA, Météo-France, JMA, KMA, UK Met Office, CMA; "best_match" picks highest-resolution model; also "Previous Model Runs API" (forecast-as-issued history) and "Historical Forecast API". — [Open-Meteo pricing](https://open-meteo.com/en/pricing) — Verified fact.

**Other NWP**
- NCMRWF data portal (rds.ncmrwf.gov.in): IMDAA regional reanalysis (12 km, hourly, 1979–2018), NGFS global reanalysis (25 km, 6-hourly, 1999–2018), and "IMDAA-like" products from the operational 12 km NCUM beyond 2020 (some 3-hourly). Terms: free, worldwide, royalty-free but "for any non-commercial, educational/academic, and Research & Development purposes". — [NCMRWF RDS](https://rds.ncmrwf.gov.in) and search snippets — Independently corroborated (the privacy/terms page returned only a title on fetch). No evidence of a public real-time NCUM/IMD-GFS 12 km *forecast* feed was found. — Unknown.
- DWD open data: DWD Act obliges DWD to provide information "mostly free of charge"; model forecasts (ICON family) are on opendata.dwd.de; no SLA. Licence text and ICON grid specs were not on the fetched page. — [DWD open data](https://www.dwd.de/EN/ourservices/opendata/opendata.html) — Verified fact (partial); ICON-global ~13 km resolution and free-with-attribution terms are Hypothesis in this pass.
- NOAA GFS/HRRR: not fetched (search budget exhausted). HRRR is CONUS-only (Hypothesis, well-known). GFS 0.25° is public domain and is available via Open-Meteo. — Hypothesis.

**Satellite-derived irradiance**
- CAMS Solar Radiation Time-series (ADS): all-sky GHI/DHI/BHI/BNI and clear-sky equivalents, Wh m⁻², 1-min to monthly resolution; Meteosat from Feb 2004, Himawari from Jan 2016; all-sky coverage described only as "roughly Europe, Africa, part of South America, the Atlantic Ocean, the Middle East, part of Asia, and Australia"; licence CC-BY (DOI 10.24381/5cab0912). Latitude/longitude bounds, IODC coverage and latency are not stated. — [ADS CAMS solar radiation](https://ads.atmosphere.copernicus.eu/datasets/cams-solar-radiation-timeseries?tab=overview) — Verified fact.
- SoDa (CAMS distributor): free account, limited to 500 requests/day, historical from 2004 to present, 1-min to 1-month; India not explicitly named. — [SoDa CAMS Radiation Service](https://www.soda-pro.com/web-services/radiation/cams-radiation-service) — Verified fact.
- Whether CAMS all-sky covers India (68–97°E) with usable viewing angles via Meteosat IODC is **Unknown**; MSG-prime (0°) and Himawari (140°E) fields of view both reach India only at their edges. — Hypothesis/Unknown; this is a critical open item.
- MOSDAC (ISRO) access tiers: Registered General Users get "limited" datasets with 3-day latency; Registered Privileged Users get all data NRT; anonymous users get metadata/images/"Open Data" NRT. Cost, commercial-use and redistribution terms are in separate "Data Access Guidelines" PDFs not read. — [MOSDAC data access policy](https://www.mosdac.gov.in/data-access-policy) — Verified fact (partial).
- INSAT-3D Imager Asia-sector L1C data are 4 km, 30-minute. A peer-reviewed semi-empirical model (Kamath & Srinivasan, Solar Energy 2020) derived half-hourly GHI at 4 km from INSAT-3D visible channel, validated against 19 Indian ground stations for 2015–16. No MOSDAC page confirming an operational, ready-to-download GHI product was found. — [IISc eprints](https://eprints.iisc.ac.in/65109/) — Independently corroborated (existence of method); operational product: Unknown.
- Solcast: no public price list ("Request a quote" on every tier). Free: 15 historic site-months and 10 live/forecast requests at your own locations; unlimited at "unmetered" demo locations. Forecast tiers: Starter 30/60-min updated every 6 h (−7 to +14 days), Pro 15–60 min updated every 15 min, Max 5–60 min every 5 min. — [Solcast pricing](https://solcast.com/pricing) — Verified fact.
- Solcast historical GHI validation (DNV, 207 sites, published Feb 2024): mean bias +0.33%, nMAE 10.33%, nRMSE 15.99% (hourly, all sites); DNI nMAE 19.97%, nRMSE 31.51%. Solcast 2022 study (70 sites): GHI bias −0.1%, nRMSE 17.5%, MAPE 10.7%; ERA5 benchmark GHI bias +2.4%, MAPE 18.4%, DNI bias +23.3%. No India/South-Asia sites named; forecast accuracy on a separate page not fetched. — [Solcast validation](https://solcast.com/validation-and-accuracy) — Verified fact.
- NASA POWER: API documentation fetched gives API structure and 429 rate-limiting but not resolution, latency or terms. — [NASA POWER API docs](https://power.larc.nasa.gov/docs/services/api/) — Verified fact (partial). Hypothesis: POWER solar is CERES-based at 0.5°×0.625°/1° and is free/public domain with multi-week latency — unsuitable for operational forecasting, usable only for coarse long-term resource checks.
- NSRDB India (NREL/MNRE): host unreachable from sandbox. Hypothesis: 10 km, 30-min (or hourly), ~2000–2014, static historical. — Unknown (unverified).
- SolarAnywhere, Meteonorm, Global Solar Atlas: not researched in this pass (search budget). — Unknown.

**AI weather models**
- Google WeatherNext: WeatherNext 3 (v3.0) released 31 Aug 2026, 5 km multi-resolution, hourly updates to 360 h, live satellite input; WeatherNext 2 (June 2025) 64-member ensemble at 0.25°, 6-hourly; WeatherNext 2-mini code and weights open-sourced Aug 2026; GraphCast ("WeatherNext Graph") and GenCast ("WeatherNext Gen") deprecated 29 Jul 2026. Access: GCS Zarr (full ensemble), BigQuery and Earth Engine (surface statistics), Vertex AI Model Garden (WN2 soft-launched Oct 2025). Pricing and approval requirements not stated on the page. — [WeatherNext release notes](https://developers.google.com/weathernext/release-notes) — Verified fact.
- WeatherNext 3 is not open-weight; the full 64-member bucket is Requester-Pays; BigQuery access reportedly requires approval; pricing not disclosed. — search snippets citing secondary sources ([oflight](https://www.oflight.co.jp/en/columns/weathernext-3-google-weather-ai-api-2026), [winbuzzer](https://winbuzzer.com/2026/09/05/google-weathernext-3-hourly-runs-finer-local-forecasts-xcxwbn/)) — Independently corroborated (secondary).
- GraphCast repo README: code Apache 2.0, "all other materials" CC BY 4.0; includes WeatherNext 2 (2025 checkpoint, 0.25°, predicts 100 m wind), WeatherNext Cyclones, legacy GraphCast/GenCast; "TPU recommended"; non-Mini models "need an H100 for sufficient VRAM"; Mini models can run on a P100; CPU not mentioned. — [google-deepmind/graphcast README](https://raw.githubusercontent.com/google-deepmind/graphcast/main/README.md) — Verified fact.
- OCF reports using Google WeatherNext inside Quartz Wind for Indian state operators: "up to 8% accuracy improvement" vs their prior setup, and "13% average reduction in imbalance penalties" for Adani Green (29 Jan 2026). These are relative gains, not error metrics. — [OCF + DeepMind](https://www.openclimatefix.org/insights/open-climate-fix-and-google-deepmind-partner-to-boost-india-s-renewable-energy-with-ai) — Verified fact.

### Inferences
- For a CPU-only startup, the correct architecture is "consume AI/NWP *outputs*, don't run the models": ECMWF AIFS Single + IFS open data (free, CC-BY-4.0, `ssrd` + 100 m wind) as primary, Open-Meteo Professional ($99/mo) as a convenience/multi-model layer with ERA5 history and forecast-as-issued archive for leak-free backtests.
- The 6-hourly step of AIFS and 3-hourly step of IFS open data must be downscaled to 15-min blocks with a clear-sky model (pvlib) — i.e. the NWP supplies a cloud-modulation factor (ssrd/clear-sky), not block-level power. This is standard practice but caps intraday skill; satellite nowcasting is what fills 0–4 h, and that is exactly the input that is uncertain for India.
- Open-Meteo's free tier (10k calls/day) could technically serve 100 plants × 4 runs/day during *development*, but any commercial pilot needs the $29 Standard tier at minimum and the $99 Professional tier for history.

### Gaps
- ECMWF open-data latency in hours (not on the page); whether the 00z run is usable for a 10:00 IST day-ahead schedule.
- CAMS all-sky coverage of India (IODC inclusion, longitude bounds, data latency).
- MOSDAC commercial-use terms, cost, and existence of an operational INSAT-3D GHI product.
- NSRDB India specifics; NASA POWER resolution/latency; SolarAnywhere/Meteonorm pricing; Global Solar Atlas licence.
- ICON global specs and DWD licence text; NOAA GFS terms (public domain assumed).
- WeatherNext pricing and whether WN2 BigQuery data may be used commercially.

---

## B. Public ground truth for Indian plants and open datasets for method development

### Takeaway
No public, scrapeable source of per-plant 15-min/hourly actual generation for Indian utility-scale solar or wind plants was found; the National Power Portal daily generation report explicitly covers only thermal/hydro/nuclear ≥25 MW. The best public proxies are aggregate: all-India hourly solar and wind generation (Sep 2021–Jun 2025, CC BY 4.0, IIT Guwahati/NERLDC), state-level daily RE generation (India Data Portal, from Grid-India daily reports), and research dumps of SLDC 15-min data. For plant-level method development the only Indian plant dataset found is the 34-day, two-plant, 22-inverter, 15-min Kaggle/IEEE DataPort set (licence unverified).

### Cited Findings
- NPP Daily Generation Report: CEA collects data "from generating plants of 25 MW and above across thermal, hydro and nuclear sources" (≈534 stations, 1,750 units) and publishes it daily on NPP; the open-data mirror is titled "Daily Non-Renewable Power Generation" (sourced from npp.gov.in/dgrReports). — [CEA division page](https://cea.nic.in/divisionPage/530); [India Data Portal](https://ckandev.indiadataportal.com/dataset/daily-non-renewable-power-generation) — Independently corroborated. Solar/wind plants are not in the DGR.
- All-India hourly solar generation, wind generation and PMU demand, September 2021–June 2025 (v2, published 15 Sep 2025, DOI 10.17632/y58jknpgs8.2), source NERLDC/Grid-India, contributors IIT Guwahati and POWERGRID, licence CC BY 4.0. Description text says Sep 2021–Dec 2023 while the title says to Jun 2025 (unreconciled). — [Mendeley Data](https://data.mendeley.com/datasets/y58jknpgs8) — Verified fact.
- "State Control Renewable Energy Generation" dataset on India Data Portal gives daily state-level renewable generation (search snippet; page returned 403 on fetch). — [India Data Portal](https://ckandev.indiadataportal.com/dataset/power/resource/64942de9-2149-466c-82f7-49cc2d63aa93) — Hypothesis (snippet only).
- Karnataka SLDC research dataset on Hugging Face: 15-minute frequency, state demand, state generation and CGS exchange, 22 Apr–14 Aug 2024; gated access. Not RE-specific. — [HF Karnataka-SLDC](https://huggingface.co/datasets/happyman11/Karnataka-SLDC) — Independently corroborated (snippet; HF blocked from sandbox).
- Tamil Nadu: "fewer than 10 per cent" of wind/solar generators were sharing real-time operational data with the SLDC; 15-day compliance notice issued 30 May (year per article). — [DT Next](https://www.dtnext.in/news/tamilnadu/real-time-data-sharing-must-for-wind-solar-energy-generators-minister-nirmalkumar) — Verified fact (snippet).
- Regulators were asked as far back as 2015 to archive RE schedules, revisions and actuals at RLDCs "and easily made available through the web interface" (IIT Kanpur comment to CERC); no confirmation that plant-wise actuals are published today. — [IITK comment](https://cercind.gov.in/2015/draft_reg/Comments_RE/Anoop_Singh_IITKanpur.pdf) — Verified fact (that it was recommended); publication status Unknown.
- Grid-India daily PSP reports and RE reports: grid-india.in and posoco.in returned 503 on all fetches; WRLDC returned 503. Hypothesis: the daily PSP report lists state-wise daily solar and wind MU and all-India RE; WRLDC/SRLDC publish region-level RE curves and monthly RE forecasting-accuracy summaries but not plant-wise actuals. — Unknown (unverified).
- Kaggle "Solar Power Generation Data" (anikannal): two grid-connected PV plants in India, 34 days, ~15-min, inverter-level AC/DC power and yield, 22 inverters per plant, plant-level ambient temperature, module temperature and irradiation; four CSVs (~2 MB). IEEE DataPort mirror DOI 10.21227/r61r-rz14 (created 2 Nov 2025) requires login/subscription; neither page shows a licence. — [IEEE DataPort](https://ieee-dataport.org/documents/solar-power-generation-data); [Kaggle](https://www.kaggle.com/datasets/anikannal/solar-power-generation-data) — Independently corroborated (contents); licence Unknown; date range (commonly cited as 15 May–17 Jun 2020) Hypothesis.
- WRLDC (2018 POSOCO presentation on WR wind forecasting): "block-wise percentage error in intraday wind forecast is concentrated between −5% to +5% for more than 90% of time"; day-ahead error higher. — [ResearchGate, Pandey](https://www.researchgate.net/profile/Vivek_Pandey31/publication/328980195_Load_and_RE_Forecasting_Utilization_and_Impact_on_System_Operation/links/5bee6076299bf1124fd5ea4a/Load-and-RE-Forecasting-Utilization-and-Impact-on-System-Operation.pdf) — Verified fact (snippet; region-aggregate, not plant).
- Datasets not verified in this pass (search budget exhausted): PVOutput, Open Power System Data, NREL SOLETE, OCF PV datasets, DKASC (Alice Springs). Hypothesis: all exist and are commonly used for method development; DKASC and OCF datasets are non-Indian; none provide Indian utility-scale plant actuals.

### Inferences
- A *plant-level* public backtest in India is not possible from public data alone: the only plant-level Indian series found is 34 days long, which is too short to span even one monsoon transition and too short for degradation or seasonal error analysis.
- A *fleet/state-level* public backtest is possible: all-India hourly solar/wind (≈4 years) and state-level daily RE allow validating an NWP-to-power pipeline against aggregate actuals, with the strong caveats that aggregate smoothing makes errors look far smaller than plant-level errors, that curtailment and capacity growth over the period contaminate the target, and that installed-capacity denominators must be reconstructed month by month.
- The realistic path to plant-level ground truth is customer-supplied exports (QCA/SCADA CSVs, RLDC schedule-vs-actual statements sent to each generator), not scraping. Even the SLDCs themselves do not receive real-time data from most generators in Tamil Nadu.

### Gaps
- Grid-India/RLDC/SLDC page contents and whether any publishes plant-wise actuals (unreachable).
- Kaggle dataset licence and exact dates.
- Existence/terms of SECI/MNRE monthly solar-park generation reports (not researched).
- PVOutput/OPSD/SOLETE/OCF/DKASC licences and India relevance (not verified).

---

## C. Baselines and achievable accuracy; regulatory horizons; metrics and pitfalls

### Takeaway
Under India's DSM framework, deviation error is measured per 15-min block as (actual − schedule)/available capacity. The permitted band narrowed on 1 April 2026 from ±10% (solar/hybrid) and ±15% (wind) to ±5% and ±10%, with the denominator blending toward scheduled generation (X = 100% available-capacity weight in FY2026-27, declining to 0% by April 2031), subject to pending Delhi High Court writs. Grid-India's own 41-week, 16-plant simulation found plants would stay inside the tightened bands only 45–58% of blocks (solar), 32–73% (wind), 38–47% (hybrid) — the single best public indication of what incumbent QCAs actually achieve. Published plant-level day-ahead solar nMAE in India from NWP-only chains is ~5–6% of capacity (one study); tropical irradiance persistence rRMSE is ~55%; NWP-based day-ahead skill vs persistence is typically 35–40%. Wind is far harder (20–30% of capacity day-ahead in a dated 2012 Indian review).

### Cited Findings

**Regulatory framework and horizons**
- DSM Regulations 2024 bands: ±10% solar/hybrid, ±15% wind; CERC proposal (Sep 2025) to narrow to ±5% / ±10% from April 2026; Grid-India ran a 41-week simulation across 16 RE plants in NR/WR/SR to set X. — [Powerline, 15 Sep 2025](https://powerline.net.in/2025/09/15/cerc-proposes-revised-deviation-formula-and-tighter-tolerance-bands-for-wind-and-solar-sellers/); [Energetica India, 15 Sep 2025](https://www.energetica-india.net/news/cerc-proposes-phased-schedule-based-deviation-mechanism-for-wind-and-solar-from-april-2026) — Independently corroborated.
- Simulation outcomes: share of time within tightened bands — solar 45–58%, wind 32–73%, hybrid 38–47%; revenue losses solar 3.5–11.1%, hybrid 2.4–11.8%, wind up to 48.2% in extreme cases; QCA aggregation cut DSM charges by up to 67% in some regions. X schedule: 100% Apr 2026–Mar 2027, declining to 0% from April 2031 (WS at par with conventional). — [Energetica India](https://www.energetica-india.net/news/cerc-proposes-phased-schedule-based-deviation-mechanism-for-wind-and-solar-from-april-2026) — Verified fact (secondary report of the CERC staff paper).
- Final order: CERC "notifies phased move to schedule-based deviation", effective 1 April 2026, with X retained at 100% in year one and tolerance bands narrowed as proposed; implementation "subject to the outcome of writ petitions pending before the Delhi High Court" with "no coercive action" during interim relief. — [Mercom, 1 Apr 2026](https://www.mercomindia.com/cerc-notifies-phased-move-to-schedule-based-deviation-for-wind-solar-under-dsm) (headline/subtitle only; body paywalled); [SolarQuarter, 1 Apr 2026](https://solarquarter.com/2026/04/01/cerc-announces-phased-dsm-reform-for-wind-and-solar-tightens-deviation-norms-by-2031/) (rate-limited) — Independently corroborated (via search snippets).
- Error formula: error = (actual − schedule)/available capacity; older FoR model regulations set ±15% (existing) / ±10% (new) bands. — [FoR 50th meeting minutes](https://forumofregulators.gov.in/Data/Meetings/Minutes/50.pdf); [POSOCO solar forecasting slides, 2024](https://posoco.in/wp-content/uploads/2024/05/Solar_Power_Forecasting_Session_3_Day_2_compressed.pdf) (snippet; fetch 503) — Independently corroborated.
- Intraday revisions (IEGC 2023, Regulation 49(8)): "In case of requirement of revision of schedule due to forecasting error, a WS seller may revise its schedule only in case of bilateral transactions and not in case of collective transaction. Such revision of schedule shall become effective from the time block and in the manner as specified in sub-clause (c) of clause (4)" — i.e. from the 7th/8th time block counting the block in which the revision is made (≈1.5–2 h ahead). CERC order 14/SM/2023 dated 30.09.2023 extended this to WS sellers under GNA or deemed T-GNA. — [CERC order 14/SM/2023](https://www.cercind.gov.in/2023/orders/14-SM-2023.pdf) (text extracted locally) — Verified fact.
- No numerical cap on the number of daily WS schedule revisions appears in the extracted order text. A stakeholder comment states the pre-2023 practice was revisions effective from the 4th block, one per 1.5-hour window (consistent with the old "16 revisions/day" rule), and that moving to the 7th/8th block "raised revenue losses" because forecasters cannot predict local weather 2 h ahead. — [SPDA comment to CERC](https://cercind.gov.in/2024/draft_reg/comments-DSM%20Reg2024/Comments/54.%20SPDA.pdf) — Verified fact (stakeholder claim). "16 revisions/day" as a *current* rule: Hypothesis/outdated.
- OCF (Mar 2025) describes the operational reality: operators "can modify their generation schedule up to 2 hours before generating", penalties commonly for "deviations over 15%", "expected to reach 5% next year"; a partner estimated forecast errors can cost a single state ₹10 million (~$120k) in one day. — [OCF India insight](https://www.openclimatefix.org/insights/accurate-forecasting-tools-are-essential-to-support-indias-renewables-boom) — Verified fact.
- Day-ahead submission deadline ("by 10:00 for next day"): not verified in this pass. Order 14/SM/2023 references a 9:45 AM day-ahead-market surplus declaration for conventional generators only. — Hypothesis.
- Historical context: 2013 CERC fine for wind predictions off by >30% was suspended in 2014; IEGC 2010 required wind farms ≥10 MW to give 24-h forecasts in 15-min blocks with ±30% UI-free band from 1 Jan 2012. — [WRI](https://www.wri.org/insights/big-data-improves-renewable-power-forecasts-will-it-help-india); [Energetica India, 2012](https://teriin.org/opinion/overview-wind-power-forecasting-methods-india) — Independently corroborated.

**Published accuracy (not like-for-like; setups differ)**
- Indian PV plant, WRF-Solar + solaR plant model vs inverter data: normalised MAE 5.59% (first forecast day); Spanish plant 5.18%. (Abstract labels metric "Normalized Mean Annual Errors", likely a typo for mean absolute error.) — [EGU22-9393](https://meetingorganizer.copernicus.org/EGU22/EGU22-9393.html) — Verified fact (snippet).
- 250 MWp park, Southern India: operational day-ahead chain using ECMWF and NCMRWF GHI (Springer, Int. J. Energy Environ. Eng., 2023); error metrics behind login, not retrieved. — [Springer](https://link.springer.com/article/10.1007/s40095-023-00560-6) — Verified fact (existence only).
- Bhadla solar park hybrid model: "nMAE 2.3325 and RMSE 129.425" (units/normalisation unclear; treat as not comparable). — [Frontiers Energy Research 2022](https://public-pages-files-2025.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2022.1029449/text) — Verified fact (snippet), low comparability.
- Tropical irradiance day-ahead (Singapore): persistence, ETS and WRF rRMSE ~55–57%; WRF+ETS blend 49%. — [redi.cedia](https://redi.cedia.edu.ec/document/108009) — Verified fact (snippet).
- Day-ahead PV power with WRF inputs: skill vs persistence 35% (deterministic) and 39% (stochastic) (Pierro et al.). — [ENEA](https://ambiente.sostenibilita.enea.it/pubs/2341) — Verified fact (snippet).
- Reference-method debate: no consensus on skill-score reference; recommended reference is the optimal convex combination of climatology and persistence. — [Yang 2019 via HIT](https://scholar.hit.edu.cn/en/publications/standard-of-reference-in-operational-day-ahead-deterministic-sola/) — Verified fact (snippet).
- Day-ahead ECMWF HRES GHI across 60 Task-16 sites: RMSE correlates with site nominal variability (r = 0.72). — [ISES SWC2025 Lauret](https://proceedings.ises.org/conference/swc2025/papers/swc2025-0095-Lauret.pdf) — Verified fact (snippet).
- IEA PVPS Task 16 regional forecast report and Visser et al. day-ahead benchmark exist; numeric nRMSE tables were not retrieved. — [IEA PVPS T16 regional forecast](https://iea-pvps.org/wp-content/uploads/2020/07/IEA_PVPS_T16_regional_forecast.pdf); [Visser webinar 2020](https://live.ises.org/sites/default/files/webinars/Lennard%20Visser_27.08.2020.pdf) — Verified fact (existence).
- Satellite/irradiance-product skill ceiling: Solcast historical GHI hourly nMAE ≈10.3% (global, DNV) vs ERA5 GHI MAPE 18.4%. — [Solcast validation](https://solcast.com/validation-and-accuracy) — Verified fact. This is *estimation* of past irradiance, not forecasting; forecast errors are necessarily larger.
- Wind, India (2012 review): day-ahead error "between 20–30%" of farm capacity depending on terrain; SCADA actuals and real-time wind speed are required inputs; data gaps (zeros/−999) degrade forecasts. — [Energetica India 2012 via TERI link](https://teriin.org/opinion/overview-wind-power-forecasting-methods-india) — Verified fact (dated).
- Wind, Kutch Gujarat (2024, CEA data): ARIMA MAPE 5.87 on a multivariate time-series set (horizon not stated as day-ahead). — [TechRxiv](https://www.authorea.com/doi/full/10.36227/techrxiv.24516142.v1) — Verified fact (snippet), low comparability.
- WR intraday wind (region aggregate, 2018): >90% of blocks within ±5% of available capacity. — [POSOCO/Pandey 2018](https://www.researchgate.net/profile/Vivek_Pandey31/publication/328980195_Load_and_RE_Forecasting_Utilization_and_Impact_on_System_Operation/links/5bee6076299bf1124fd5ea4a/Load-and-RE-Forecasting-Utilization-and-Impact-on-System-Operation.pdf) — Verified fact (snippet).

### Inferences
- "What does a good day-ahead plant-level solar forecast achieve in India?" The only Indian plant-level NWP-chain number found is ≈5.6% nMAE of capacity (one plant, one year, WRF-Solar). Combined with Grid-India's finding that plants stay inside ±5% only 45–58% of blocks, a defensible claim is: day-ahead plant-level nMAE of 5–8% of capacity is achievable with NWP + plant model; staying inside ±5% block-by-block most of the time is *not* achievable day-ahead in monsoon/transition seasons, which is why the industry's economic lever is intraday revision (7th/8th block) plus QCA pooling, not day-ahead skill alone. — Estimate.
- Because error is normalised by *available capacity* (X=100% through March 2027), a plant that is partially curtailed or derated must report AvC correctly; a forecaster without plant telemetry cannot know AvC, so public-data forecasts are structurally handicapped on exactly the denominator that matters until X declines.
- The relevant horizons for a product are: (1) day-ahead block schedule (deadline unverified, assume morning IST, using previous-day 12z ECMWF run), (2) rolling intraday revisions effective ~1.5–2 h ahead (needs 0–4 h nowcasting: satellite + live plant telemetry — the OCF stack), (3) no real-time 15-min dispatch forecast is required of the generator beyond the schedule. Without satellite irradiance for India or live telemetry, a public-data product competes only on horizon (1), where NWP-blend skill is commoditised (Open-Meteo/Solcast/ECMWF).
- Pitfalls that must be designed into any backtest: use forecast-as-issued NWP (Open-Meteo Previous Model Runs API or an archive you build daily from ECMWF open data, since the open rolling archive is only 2–3 days) to avoid leakage; stratify by monsoon (Jun–Sep), post-monsoon and winter-fog regimes; reconstruct monthly installed capacity for any aggregate series; treat curtailment and outages as label noise (they are indistinguishable from weather in aggregate data); report nMAE/nRMSE vs installed capacity *and* block-within-band share, since the latter is what DSM charges depend on.

### Gaps
- IEGC 2023 text on day-ahead submission timing and any cap on number of WS revisions per day (PDF not read in full; search budget exhausted).
- CERC April-2026 order text (exact X glide path per year; charge rates).
- IEA PVPS Task 16 / Visser et al. numeric benchmark tables.
- Any published QCA/plant-level day-ahead error distribution for India (none found public).
- Solcast and Open-Meteo *forecast* accuracy pages (not fetched).

---

## D. Plant performance analysis from public/customer-export data

### Takeaway
With only weather + plant specs + monthly/daily energy, a founder can compute performance ratio and expected-vs-actual energy, detect gross outages and long-term degradation trends (RdTools year-on-year works on daily normalised yield), and see soiling "sawtooth" signatures if daily data exist; but RdTools itself states site irradiance is required for clear-sky filtering, and inverter/string-level fault localisation, availability decomposition (communication vs production outage), and IEC 61724-grade PR need SCADA/inverter data. The analytics toolchain is free and permissively licensed (pvlib BSD-3, RdTools MIT, PVAnalytics MIT). No Indian O&M-analytics vendor publishes per-MW pricing; the only public anchor is a European comparison showing €200–1,600 per MWp per year for monitoring software.

### Cited Findings
- RdTools: open-source Python for PV time series; degradation (preferred year-on-year method, Jordan 2018, bootstrapped rate distribution) and soiling (SRR, Deceglie 2018; CODS, Skomedal 2020) both computed on normalised yield "usually at the daily level"; system availability separates communication outages from production outages (Anderson & Blumenthal 2020); handles "hourly or better" and daily/weekly data, higher frequency gives best results; "site irradiance data is required to identify clear-sky conditions"; clear-sky and NSRDB-satellite workflows exist as sensor-drift checks; latest v3.2.1 (8 Jul 2026), Python 3.10+. — [RdTools docs](https://rdtools.readthedocs.io/en/stable/) — Verified fact.
- Licences: RdTools MIT (kWh Analytics, Alliance for Sustainable Energy, SunPower, DNV); pvlib-python BSD 3-Clause (pvlib contributors, Sandia); PVAnalytics MIT (Alliance for Sustainable Energy, Sandia NTESS). — [RdTools LICENSE](https://raw.githubusercontent.com/NREL/rdtools/master/LICENSE); [pvlib LICENSE](https://raw.githubusercontent.com/pvlib/pvlib-python/main/LICENSE); [PVAnalytics LICENSE](https://raw.githubusercontent.com/pvlib/pvanalytics/main/LICENSE) — Verified fact.
- Monitoring-software cost benchmark (Europe): yearly cost for 1 MWp from €200 to €1,600 for vendors that disclose; most "not public". — [Solytic comparison](https://solytic.com/comparisons/pv-monitoring-software-comparison/) — Verified fact (snippet).
- India SCADA hardware cost: EnerMAN (Bengaluru) claims solar SCADA cost fell from INR 3.5 lakh/MW (2015) to under INR 1 lakh/MW by building in-house. — [SolarQuarter, 30 Sep 2025](https://solarquarter.com/2025/09/30/enerman-redefines-solar-efficiency-with-ai-powered-monitoring-and-smart-insights-ashok-d-m-founder-ceo-md/amp/) — Verified fact (vendor claim).
- Proinso/Inspire Clean Energy: one free year of EIRA monitoring "can save up to $500 per project", then discounted subscription. — [pv magazine India](https://pv-magazine-india.com/press-releases/proinso-looks-to-increase-profitability-of-pv-assets-with-distinctive-monitoring-offer-in-india) — Verified fact (snippet).
- Raptor Maps: SaaS subscription + inspection services; drone-in-a-box ~\$50k system and ~\$2,500/yr service for a 100 MW plant (pv magazine estimate, unconfirmed by vendor); 373 GWdc analysed (2026). Prescinto, SmartHelio, Power Factors/Also Energy, Alectris: no published prices found. — [pv magazine USA, 2023](https://pv-magazine-usa.com/2023/03/28/drone-in-the-box-for-a-thousandths-of-a-cent-per-kilowatt-hour/) — Verified fact (estimate flagged by source); others Unknown.
- The Kaggle/IEEE two-plant dataset includes plant-level irradiation, ambient and module temperature plus 22 inverters per plant at 15-min for 34 days — enough to prototype inverter-level underperformance detection and PR, not degradation. — [IEEE DataPort](https://ieee-dataport.org/documents/solar-power-generation-data) — Verified fact.

### Inferences
- From monthly/daily energy + ERA5/satellite irradiance + specs, the defensible outputs are: monthly PR and weather-corrected expected energy (±several % uncertainty, dominated by irradiance-product error ~10% hourly nMAE, smaller when aggregated monthly), multi-year degradation trend (needs ≥2–3 years of daily data for RdTools YOY to be meaningful), gross outage days, and seasonal soiling signatures (only with daily data and a clean reference irradiance). Inverter/string fault localisation, availability attribution, curtailment separation and bankable PR require customer SCADA exports — which, once a customer shares them, are exactly the "plant-level data" the founder lacks; the product therefore starts as a BYO-data analytics layer.
- Price anchoring: at €200–1,600/MWp/yr in Europe and Indian SCADA hardware now <₹1 lakh/MW one-off, an Indian software-only analytics subscription would likely have to sit well under ₹50k/MW/yr to win against bundled monitoring — Estimate; no Indian price list found.

### Gaps
- IEC 61724 specifics (not fetched).
- Any published Indian O&M analytics price per MW (Prescinto, SmartHelio, Power Factors, Alectris) — none found.
- Solcast/CAMS monthly-aggregate irradiance uncertainty for India specifically.

---

## E. Grid-capacity / connectivity analysis from public information

### Takeaway
CTUIL does publish substation-wise and bay-wise ISTS connectivity margins (monthly "Summary Margin" PDFs through Aug 2025 and, since the GNA 3rd amendment, separate solar-hour and non-solar-hour margins; latest Annex-B/C/D uploads 13 Aug 2026 and 1 Oct 2026, page updated 16 Oct 2026), with the explicit caveat that margins "may vary depending on network topology, Load-Generation balance, etc." That supports a "connectivity opportunity screening" product (which substations have margin, in which hours, which bays, what is planned), but not an available-transfer-capability or load-flow product, which requires network models the public cannot access. Whether PSS/E-type studies are mandated for connectivity was not researched.

### Cited Findings
- CTUIL Bay Margin page: "Declaration of Solar & Non-solar hour access" for connectivity grantees, tentative bay-wise and substation-wise margins under CERC GNA Regulations; Annex-B (bay-wise solar/non-solar connectivity and margins), Annex-C (substation-wise margins), Annex-D (thermal RE connectivity), uploaded 01.10.2026 and approved versions 13.08.2026; archive section; page last updated 16 Oct 2026. — [CTUIL renewable energy](https://ctuil.in/renewable-energy) — Verified fact.
- Monthly summary margins by region and commissioning window (e.g. as on 31-07-2025, 31-08-2025) and bay-allocation sheets listing 220 kV/400 kV bays and transformer capacity per substation (e.g. Bhuj PS). — [CTUIL Summary Margin 31-08-2025](https://ctuil.in/uploads/assets/176415763298Summary%20Margin-31-08-2025_approved.pdf); [Allocation of bays Aug 2025](https://ctuil.in/uploads/assets/175931720504Allocation%20of%20bays%20Aug25_Approved.pdf) — Verified fact (existence; figures not read).
- After the GNA Regulations 3rd amendment, margins are split into solar and non-solar hours; CTUIL declared non-solar-hour margins on 10.09.2025; RoFR window ended 21.02.2026; CTUIL caveat: margins "may vary depending on network topology, Load-Generation balance, etc." — CTUIL page via search snippet — Verified fact (snippet).

### Inferences
- Realistic startup scope: a continuously-updated, geocoded index of ISTS substations × margin (solar/non-solar hours) × planned bays/lines (from CTUIL/CEA plans, Green Energy Corridor documents), with change alerts — a research/diligence tool for developers chasing connectivity, priced like data subscriptions. Anything branded "available transfer capability" or "curtailment risk by node" requires CTUIL/Grid-India network models, ratings and load-flow cases that are not public. — Estimate.

### Gaps
- Whether PSS/E/PowerWorld studies are mandated in the connectivity procedure (not researched).
- State (intra-state) transmission margin publication practices (not researched).
- Green Energy Corridor plan documents and CEA transmission plan URLs (not fetched).

---

## F. Compute and cost to run a 100-plant daily forecast on a small VM

### Takeaway
The compute problem is trivial on CPU: for 100 point locations, fetching only `ssrd`, 2 m temperature and 10/100 m wind from ECMWF open data (index-file subsetting) is on the order of hundreds of MB per run, and gradient-boosted or linear post-processing per plant runs in seconds. Expected cash cost: a 2–4 vCPU VM plus object storage (<$30/month, Estimate), optional Open-Meteo Professional $99/month, with Solcast on quote only. The real cost is the irradiance ground truth, not compute.

### Cited Findings
- ECMWF open data: 0.25° GRIB2, four runs/day, mirrored on AWS/Azure/GCP, index files per run allow per-parameter byte-range fetches (example `2t`). — [ECMWF open data](https://www.ecmwf.int/en/forecasts/datasets/open-data); [confluence guide](https://confluence.ecmwf.int/display/DAC/ECMWF+open+data%3A+real-time+forecasts+from+IFS+and+AIFS) — Verified fact.
- Open-Meteo Standard $29/mo (1M calls), Professional $99/mo (5M calls, historical/ensemble/satellite radiation). — [Open-Meteo blog](https://openmeteo.substack.com/p/api-subscriptions-for-commercial) — Verified fact.
- Hetzner shared-vCPU plans: CPX22 2 vCPU/4 GB/80 GB, CPX32 4 vCPU/8 GB/160 GB (EU, 20 TB traffic; Singapore 1–2 TB); prices not rendered. — [Hetzner Regular Performance](https://www.hetzner.com/cloud/regular-performance/) — Verified fact (specs); Hypothesis: CPX22 ≈ €5–8/month, CPX32 ≈ €10–15/month.
- Solcast: no public prices; free quota 15 historic site-months and 10 live/forecast requests at own sites. — [Solcast pricing](https://solcast.com/pricing) — Verified fact.

### Inferences (Estimates)
- Calls: 100 plants × 4 runs/day = 400 Open-Meteo calls/day ≈ 12k/month — inside the free tier's technical limits, but commercial use requires Standard/Professional. Training history for 100 plants × 3 years from the Historical/Previous-runs APIs ≈ a few thousand calls once.
- ECMWF direct: a global 0.25° single-level GRIB2 field is ~1–3 MB; `ssrd` + 2t + 10u/10v + 100u/100v for ~60 steps ≈ 0.5–1 GB per run uncompressed if whole fields are pulled, less with index subsetting; 4 runs/day ≈ 2–4 GB/day ≈ 1 TB/year if everything is kept — store only the 100 extracted point series (tens of MB/year) plus a thin NWP archive for retraining. Object storage at 1 TB ≈ $5–25/month depending on provider.
- Total infra: ≈ $15–40/month without paid APIs; ≈ $115–140/month with Open-Meteo Professional. Solcast at 100 sites: Unknown (quote).

### Gaps
- Exact ECMWF open-data per-run volumes and release times (not measured).
- Hetzner/AWS prices (not rendered).
- Solcast per-site commercial pricing.

---

## G. Synthesis tables and verdict

### Takeaway
Public data can validate a *fleet- or state-level* NWP-to-power forecasting pipeline for India and can prototype plant-level methods on a 34-day dataset; it cannot validate a plant-level forecasting or performance product against Indian ground truth, because no public per-plant actuals exist and the most valuable intraday input (satellite irradiance over India) is itself unverified for access.

### (1) Data-input table

| Source | Variables | Resolution | Latency | Licence | Cost | Verified? |
|---|---|---|---|---|---|---|
| ECMWF open data IFS | ssrd (ID 169), 2t, 10 m & 100 m wind, tp, msl, ensembles | 0.25°, 3-hourly to 144 h, 6-hourly to 360 h (00/12z) | "end of real-time dissemination schedule" (hours not stated; est. ~7–9 h after run, Hypothesis) | CC-BY-4.0 + ECMWF ToU; commercial OK with attribution | Free; 12-run rolling archive only | Yes (licence, vars, steps); latency No |
| ECMWF open data AIFS Single/ENS | ssrd, 2t, winds, etc. | 0.25°, 6-hourly to 360 h, 4 runs/day | "as soon as produced" | CC-BY-4.0 | Free | Yes |
| Open-Meteo Forecast API | GHI, DNI, DHI, GTI, temp, wind; 30+ models incl. ECMWF/DWD/NOAA | 1–11 km model-dependent, hourly (15-min for some) | Model-dependent; IFS 9 km "no delay" | Data CC BY 4.0; free tier non-commercial | Free (10k/day) / $29 / $99 per month | Yes (terms); prices via blog (2023) |
| Open-Meteo Historical | ERA5 GHI/DNI/DHI etc. | 0.25° (ERA5), 9 km IFS from 2017; hourly | ERA5 5-day delay | CC BY 4.0 | Professional $99/mo | Yes |
| NCMRWF RDS | IMDAA reanalysis 12 km hourly 1979–2018; NCUM-derived "IMDAA-like" post-2020 | 12 km | Not real-time forecast | Non-commercial/R&D only | Free | Partly (snippets) |
| DWD ICON open data | Model forecasts incl. radiation | ICON global ~13 km (Hyp.) | n/s | DWD "mostly free of charge"; terms not read | Free | Partly |
| NOAA GFS | GHI (DSWRF), winds | 0.25°, hourly to 120 h (Hyp.) | ~4–5 h (Hyp.) | Public domain (Hyp.) | Free | No (not fetched) |
| CAMS Solar Radiation (ADS/SoDa) | GHI, DHI, BHI, BNI, clear-sky | 1-min to monthly; MSG from 2004, Himawari from 2016 | Not stated | CC-BY | Free; 500 req/day on SoDa | Yes, except **India coverage Unknown** |
| MOSDAC INSAT-3D/3DR | L1C imagery 4 km/30-min; GHI product unconfirmed | 4 km, 30 min | General users 3-day; privileged NRT | Guidelines PDF not read | Unknown | Partly |
| Solcast | GHI/DNI/GTI, PV power, forecasts | 5–60 min; −7 to +14 d | 5 min–6 h updates by tier | Commercial | Quote only; small free quota | Yes (tiers); prices No |
| NASA POWER | ALLSKY_SFC_SW_DWN etc. | ~0.5° (Hyp.), hourly/daily | Weeks (Hyp.) | Free/public (Hyp.) | Free | No |
| NSRDB India (NREL/MNRE) | GHI/DNI/DHI | 10 km, 30-min, ~2000–2014 (Hyp.) | Static | Hyp. free | Free | No (host unreachable) |
| Google WeatherNext 2/3 | Ensemble surface vars | 0.25° (WN2), 5 km (WN3) | WN3 hourly | WN2-mini open; WN3 closed; BigQuery/GCS Requester-Pays | Not public | Yes (release notes) |
| All-India hourly solar/wind/demand (IITG/NERLDC, Mendeley) | Solar MW, wind MW, demand | Hourly, all-India, Sep 2021–Jun 2025 | Static | CC BY 4.0 | Free | Yes |
| India Data Portal state RE generation | Daily state-wise RE MU | Daily | ~daily | Not read | Free | Snippet only |
| Kaggle/IEEE two-plant dataset | Inverter AC/DC power, yield; plant irradiance, temps | 15-min, 34 days, 2 plants × 22 inverters | Static (2020, Hyp.) | **Unknown** | Free (Kaggle) / IEEE subscription | Contents yes; licence no |
| CTUIL margins | Substation-/bay-wise margin, solar/non-solar hours | Per substation/bay | Monthly-ish (latest 1 Oct 2026) | Public PDFs | Free | Yes |

### (2) Baseline / metric table (not like-for-like; see setup column)

| Baseline or result | Metric | Value | Setup | Source class |
|---|---|---|---|---|
| Persistence, day-ahead irradiance | rRMSE | ~55–57% | Singapore (tropical), GHI | Verified (snippet) |
| WRF + ETS blend, day-ahead irradiance | rRMSE | ~49% | Singapore | Verified (snippet) |
| NWP(WRF)-based day-ahead PV power | Skill vs persistence | 35% (deterministic), 39% (stochastic) | Pierro et al., Europe | Verified (snippet) |
| WRF-Solar + plant model, day 1 | nMAE (capacity) | 5.59% | One Indian PV plant vs inverter data | Verified (snippet) |
| Same chain, Spanish plant | nMAE | 5.18% | Comparison plant | Verified (snippet) |
| Satellite GHI *estimate* (not forecast) | nMAE / nRMSE | 10.33% / 15.99% hourly | Solcast vs 207 global sites (DNV 2024) | Verified |
| ERA5 GHI *estimate* | bias / MAPE | +2.4% / 18.4% | 70 sites, Solcast 2022 | Verified |
| Indian QCAs under tightened bands (simulation) | % blocks within ±5% (solar) / ±10% (wind) / hybrid | 45–58% / 32–73% / 38–47% | Grid-India, 41 weeks, 16 plants, NR/WR/SR | Verified (secondary) |
| WR intraday wind (region aggregate) | % blocks within ±5% of AvC | >90% | WRLDC 2018 | Verified (snippet) |
| Indian wind day-ahead (2012 review) | error % of capacity | 20–30% | Vendor tools, 2012 | Verified (dated) |
| DSM band, solar/hybrid | ± of AvC (X=100%) | ±10% → ±5% from 1 Apr 2026 | CERC DSM 2024 + Apr 2026 order (subject to Delhi HC) | Corroborated |
| DSM band, wind | ± of AvC | ±15% → ±10% from 1 Apr 2026 | same | Corroborated |
| Intraday revision lead | time blocks | effective from 7th/8th block (~1.5–2 h) | IEGC 2023 Reg 49(4)(c), 49(8) | Verified (order text) |

Recommended metric set for the product: nMAE and nRMSE normalised to installed capacity (daylight blocks only), block-within-band share at ±5%/±10% of AvC, skill score vs smart persistence (clear-sky index persistence) and vs the climatology–persistence convex blend, stratified by month/monsoon regime and by forecast lead (day-ahead vs 2-h revision).

### (3) Verdict: can a public-data backtest validate a plant-level forecasting product in India?

**No for plant level; yes for a fleet/state-level pipeline demonstration; yes for method prototyping.**

- Why not plant-level: no public per-plant 15-min/hourly actuals exist (NPP DGR excludes RE; RLDC/SLDC plant-wise publication unconfirmed and portals unreachable; even SLDCs lack real-time data from >90% of Tamil Nadu RE generators). The only Indian plant dataset (two plants, 34 days) cannot support seasonal, monsoon or degradation validation. The DSM denominator (available capacity) and curtailment are unobservable without telemetry.
- What *can* be validated publicly (exact dataset path):
  1. Target: all-India hourly solar and wind generation, Sep 2021–Jun 2025, CC BY 4.0 — https://data.mendeley.com/datasets/y58jknpgs8 (v2, DOI 10.17632/y58jknpgs8.2). Optional second target: state-wise daily RE from India Data Portal (https://ckandev.indiadataportal.com/dataset/power/resource/64942de9-2149-466c-82f7-49cc2d63aa93) — verify contents and licence.
  2. Capacity denominator: reconstruct monthly installed solar/wind capacity (MNRE monthly physical-progress reports — not fetched; Hypothesis) to normalise.
  3. Inputs, leak-free: Open-Meteo Professional ($99/mo) Historical Forecast / Previous Model Runs APIs for forecast-as-issued GHI/wind at a grid of ~50–100 proxy locations weighted by installed capacity (Rajasthan, Gujarat, Karnataka, Tamil Nadu, AP, MP, Maharashtra), or ERA5 (reanalysis — *not* a forecast; use only as an upper-bound "perfect-weather" test). Going forward, archive ECMWF IFS/AIFS open data daily (free) to build your own forecast-as-issued history.
  4. Plant model: pvlib (BSD-3) clear-sky + transposition + simple DC/AC model; wind via generic power curves.
  5. Baselines: smart persistence, climatology–persistence blend, NWP-direct.
  6. Metrics: nMAE/nRMSE vs capacity, monsoon-stratified, plus block-within-band share — stated clearly as *aggregate* results that will understate plant-level error by a large factor.
  7. Plant-level method demo: Kaggle/IEEE two-plant 15-min set (licence unverified — treat as demo only), to show inverter-level anomaly/PR analytics and 15-min downscaling.
- What still requires plant-level data: AvC and curtailment flags, inverter/string telemetry for performance attribution, live generation for intraday (7th/8th-block) revisions, and multi-year daily energy for degradation. Practically this means the venture must start with design partners (QCA, IPP or O&M firm) who supply SCADA/QCA exports under NDA; the public backtest is a credibility artefact for those conversations, not product validation.
- Decision informed: the venture is feasible as a software-only business only if (a) a design partner provides plant data within the first months, and (b) one of CAMS-over-India or MOSDAC INSAT-3D irradiance proves accessible on commercial terms; both are open items flagged above.

### Gaps (overall)
- Grid-India/RLDC/SLDC public RE pages (all 503 from sandbox).
- CAMS India coverage; MOSDAC commercial terms and GHI product.
- IEGC 2023 day-ahead deadline and revision count; CERC April-2026 order text.
- Kaggle licence; NSRDB India; NASA POWER specifics; GFS/ICON terms.
- Any India-specific Solcast or Open-Meteo forecast validation; IEA PVPS Task 16 numeric tables; Indian O&M analytics per-MW prices.
