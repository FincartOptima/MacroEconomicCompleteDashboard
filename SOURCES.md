# SOURCES.md — Indicator Trust Index

Each indicator is classified as **Tier 1** (exact per-month document/press release) or **Tier 2** (database/dashboard requiring drill-down).

| # | Indicator | Source | Tier | Notes |
|---|-----------|--------|------|-------|
| 1 | Monthly SIP Contribution | AMFI Monthly Note PDFs (`amfiindia.com/…/AMFIMonthlyNote_{Month}{Year}.pdf`) | 1 | SIP figure stated explicitly in SIP-trend section; pdfplumber text extraction |
| 2 | Monthly Lumpsum Inflow | AMFI repo XLS (`portal.amfiindia.com/spages/am{mon}{year}repo.xls`) | 1 | Derived: Sub Total II (Equity) col E + Sub Total III (Hybrid) col E − SIP |
| 2a | Monthly Repurchase/Redemption (Equity+Hybrid) | AMFI repo XLS (same as above) | 1 | Sub Total II col F + Sub Total III col F; gross outflows from equity and hybrid funds |
| 3 | RBI Repo Rate | RBI press releases / MPC resolutions | 1 | Each rate change has a dedicated press release; unchanged months cited to the last change PR |
| 4 | System Liquidity | RBI daily liquidity operations data | 2 | RBI publishes daily LAF data; monthly average requires aggregation |
| 5 | Bank Credit Growth (YoY) | RBI Sectoral Deployment of Credit / Statistical Tables | 2 | RBI DBIE database or fortnightly press release |
| 6 | Bank Deposit Growth (YoY) | RBI Statistical Tables / Scheduled Banks' Statement | 2 | Same RBI source as credit growth |
| 7 | Credit-to-Deposit (CD) Ratio | Derived from RBI credit & deposit data | 2 | Calculated from above two series |
| 8 | FII Net Flow | SEBI/NSDL monthly FPI data | 1 | NSDL publishes monthly FPI investment summary |
| 9 | DII Net Flow | SEBI / BSE/NSE monthly DII data | 2 | SEBI bulletin or exchange-published monthly data |
| 10 | Foreign Exchange Reserves | RBI Weekly Statistical Supplement | 1 | RBI WSS press release (end-of-month figure) |
| 11 | Manufacturing PMI | S&P Global India Manufacturing PMI press release | 1 | Monthly press release on S&P Global website |
| 12 | Services PMI | S&P Global India Services PMI press release | 1 | Monthly press release on S&P Global website |
| 13 | PV Vehicle Sales | SIAM monthly sales data | 1 | SIAM publishes monthly press release with exact figures |
| 14 | Vehicle Sales YoY | Derived from SIAM data | 1 | Calculated from consecutive SIAM monthly figures |
| 15 | Electricity Consumption | CEA / Ministry of Power monthly report | 1 | CEA monthly generation/consumption report PDF |
| 16 | Steel Production YoY | Joint Plant Committee / Ministry of Steel | 1 | JPC monthly bulletin |
| 17 | Fuel Consumption (Diesel/Petrol) | PPAC monthly consumption data | 1 | PPAC publishes monthly petroleum product consumption |
| 18 | CPI Inflation | MOSPI press release | 1 | Exact press release per month from mospi.gov.in |
| 19 | Core Inflation | Derived from MOSPI CPI components | 2 | No single official "core" figure; CPI ex-food & fuel calculated from MOSPI group-level data |
| 20 | WPI Inflation | DPIIT / Office of Economic Adviser press release | 1 | Exact press release per month |
| 21 | Food Inflation | MOSPI CPI press release (food sub-index) | 1 | Extracted from same CPI press release |
| 22 | GDP Growth (YoY) | MOSPI National Accounts press release | 1 | Quarterly; months within a quarter share the same figure |
| 23 | Unemployment Rate | CMIE Unemployment in India | 2 | CMIE publishes monthly unemployment; free preview limited |
| 24 | GST Collection | Ministry of Finance GST press release | 1 | MoF publishes exact monthly GST collection press release |
| 25 | GST YoY Change | Derived from above | 1 | Calculated from consecutive months |
| 26 | 10-Year G-Sec Par Yield | RBI Bulletin, Select Economic Indicators, row 4.14; dated FBIL month-end workbooks | 1 | Month-end, 10-year tenor, semi-annual quotation basis. Not the yield of a specific traded benchmark bond. |
| 27 | 91-Day T-Bill Yield | Dated RBI auction results / RBI Bulletin auction tables | 1 | Cut-off yield at the last successful auction of the calendar month. Exact auction date is stored with each value. |
| 28 | 364-Day T-Bill Yield | Dated RBI auction results / RBI Bulletin auction tables | 1 | Same convention as the 91-day series. Weighted-average auction yields are not substituted. |
| 29 | CapEx Outlay | Controller General of Accounts monthly fiscal data | 1 | CGA publishes monthly accounts with capital expenditure line |
| 30 | USD/INR | RBI Reference Rate | 1 | RBI publishes daily reference rate; end-of-month value used |
| 31 | GBP/INR | RBI Reference Rate | 1 | Same RBI reference rate page |
| 32 | Current Account Deficit (% GDP) | RBI Balance of Payments press release | 1 | Quarterly; RBI publishes exact BOP figures per quarter |
| 33 | NIFTY 50 P/E | [NSE Indices historical P/E data](https://www.niftyindices.com/reports/historical-data) | 2 | Calculated arithmetic mean of every published daily P/E observation in the calendar month. |

---
Market-series review completed **2026-10-05**, covering all 24 months from October 2024 through September 2026. Other indicators were not reviewed in this update.

### Measurement and verification rules

- **T-bills:** use the implicit yield at the cut-off price, preserving RBI's four-decimal precision in `data.json`. The dashboard displays two decimals. Select auctions by auction date, not settlement date. March 2026 uses 18 March because all bids on 25 March were rejected. September 2026 includes the 30 September auction even though settlement was 1 October. Each value links to its RBI release or a dated bulletin table containing the observation.
- **10-year G-Sec:** the previous row mixed approximate benchmark yields, averages and par yields. The entire history now uses the FBIL month-end **par yield on the semi-annual quotation basis**, labelled explicitly in the dashboard. For October 2024–June 2026, use row 4.14 of the linked RBI bulletin and the column for the observation month, not the bulletin publication month. For July–September 2026, the source links download FBIL's dated workbook: sheet `Par Yield`, tenor `10`, column `YTM% p.a.(Semi-Annual)`. Do not use the adjacent annualized column or a specific bond's yield in the `G-Sec` sheet.
- **NIFTY 50 P/E:** select `P/E, P/B & Div.Yield values`, index `NIFTY 50`, and the calendar month on NSE's historical-data page. The page publishes daily observations, not the dashboard's monthly average. All 496 daily inputs are retained in [data/nifty50-pe-daily.json](data/nifty50-pe-daily.json), with source and retrieval details. Calculate the arithmetic mean with decimal arithmetic and round half up to two places. Include special trading sessions when NSE publishes an observation. July, August and September 2026 were corrected from 20.70, 20.42 and 19.90 to **20.72, 20.61 and 19.77**. Earlier monthly averages were independently reproduced.
- A `fixed` source status means that the value and measurement were checked against the stated source. A working generic homepage alone is insufficient. Missing or unverified future observations must remain missing or explicitly unverified; never fill them with estimates under a verified status.

Run `python scripts/validate_market_data.py` to check coverage, dated sources and reproduce all P/E averages. Hover over a corrected value to read its observation notes, or click the indicator name for the latest details and calculation inputs.
