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
| 26 | 10-Year G-Sec Yield | RBI / CCIL / FBIL reference rate | 2 | CCIL/FBIL publish daily; end-of-month or monthly average needed |
| 27 | 91-Day T-Bill Yield | RBI T-Bill auction results | 1 | RBI publishes per-auction cut-off yields |
| 28 | 364-Day T-Bill Yield | RBI T-Bill auction results | 1 | Same RBI auction results page |
| 29 | CapEx Outlay | Controller General of Accounts monthly fiscal data | 1 | CGA publishes monthly accounts with capital expenditure line |
| 30 | USD/INR | RBI Reference Rate | 1 | RBI publishes daily reference rate; end-of-month value used |
| 31 | GBP/INR | RBI Reference Rate | 1 | Same RBI reference rate page |
| 32 | Current Account Deficit (% GDP) | RBI Balance of Payments press release | 1 | Quarterly; RBI publishes exact BOP figures per quarter |

---
*Last updated: 2026-06-18*
