[![View Repositories](https://img.shields.io/badge/View-My_Repositories-blue?logo=GitHub)](https://github.com/Yulia-Momotyuk?tab=repositories)
[![View My Profile](https://img.shields.io/badge/View-My_Profile-green?logo=GitHub)](https://github.com/Yulia-Momotyuk)
# CryptoInvest Insight — Investment Strategies & Risk Analysis

## 1. Project Overview
This project analyzes **5 major cryptocurrencies (BTC, ETH, ADA, SOL, XRP)** using historical data extracted via **CoinGecko API**.  
The main objective is to explore market dynamics, risks, and the effectiveness of investment strategies to answer key questions:
- Which coins deliver the highest returns and which are more stable?  
- Do trading volumes significantly impact profitability?  
- Which strategy is more effective: Buy & Hold, Dollar Cost Averaging (DCA), or Buy on Dip?  
- Can prices be forecasted using basic ML models?  
- Which assets provide the best **risk–return tradeoff (Sharpe ratio)**?  

---

## 2. Technologies Used
- **Data extraction**: Python (`requests`, CoinGecko API)  
- **Data processing**: `pandas`, `numpy`  
- **Visualization**: `matplotlib`, `seaborn`  
- **Statistics & ML**: `scipy` (t-tests, A/B-tests), `sklearn` (Linear Regression)  
- **BI Dashboard**: Power BI (KPI-cards, Risk–Return Map, Waterfall)  
- **Environment**: Jupyter Lab  

---

## 3. Key Features
1. **Market Overview**
   - Price dynamics, volatility, and drawdowns.  
   - Seasonality analysis (weekdays, months).  
   - Correlation heatmap between coins.  
2. **Investment Strategies**
   - Simulations of Buy & Hold, DCA, and Buy on Dip.  
   - Risk–Return Map (ROI vs Drawdown).  
   - Comparison in both % ROI and final $ values.  
3. **Statistical Experiments**
   - A/B-test: High vs Low volume days.  
   - Hypothesis testing: Do higher volumes drive stronger price moves?  
4. **ML Forecast**
   - Linear Regression (time series) for BTC (7-day forecast).  
   - R² ≈ 0.77 → model captures the trend but struggles on sharp spikes.  
5. **Risk Metrics**
   - ROI, Volatility, Max Drawdown.  
   - Sharpe and Sortino ratios.  
   - Coefficient of Variation (CV).  

---

## 4. Data Overview
- **Source**: CoinGecko API (historical data 2024–2025).  
- **Main dataset**: `market_daily.csv`  
  - `date` — trading day  
  - `symbol` — coin (BTC, ETH, ADA, SOL, XRP)  
  - `price_usd`, `volume_usd`, `market_cap_usd`  
  - Calculated metrics: `return_pct`, `drawdown_pct`, `rolling_vol_14d`, `roi_pct`, `is_dip_3d`  
- **Additional dataset**: `sim_results.csv` with strategy simulation results.  

---

## 5. Methodology
1. **Data Extraction**: API request (CoinGecko) → JSON → CSV.  
2. **Data Processing**: cleaning, calculation of ROI, volatility, drawdowns.  
3. **Exploratory Data Analysis (EDA)**: trends, boxplots, correlation analysis.  
4. **Simulation**: investment strategy modeling.  
5. **Statistical Testing**: t-tests & A/B-tests for volume-based effects.  
6. **Machine Learning**: BTC forecasting with Linear Regression.  
7. **Visualization & Dashboard**: Python (matplotlib/seaborn) + Power BI.  

---

## 6. Key Insights
- **XRP and ADA**: top performers, but with high drawdowns.  
- **BTC and ETH**: stable "anchors" of the portfolio.  
- **SOL**: weakest asset in the sample.  
- **DCA**: reduces risk but often underperforms vs. Buy & Hold.  
- **High-volume days**: significantly impact BTC and XRP returns.  
- **ML model**: captures general trends but weak on short-term timing.  
- **Sharpe ratio** ranking: XRP > BTC > ETH > ADA > SOL.  

---
## 7. Installation  
To run this project locally:  
```bash
git clone https://github.com/Yulia-Momotyuk/crypto-insight.git
cd crypto_invest_insight
```
### Open Notebook

Open **[`ccrypto_invest_insight.ipynb`](crypto_invest_insight.ipynb)** in Jupyter Lab.

---

### Business & Technical Goals  

- **Business Goal:** Assess cryptocurrency performance and strategy efficiency to support investment decision-making and risk management.
- **Technical Goal:** Extract raw data via API, process it in Python, simulate strategies, apply statistics & ML, and deliver insights through visualization and a Power BI dashboard.

---
## 📬 Contact

[LinkedIn](https://www.linkedin.com/in/yuliia-kononchuk-78913633b/) | [Email](mailto:kononchuk.yuliia@gmail.com)

---
> **Author**: _Yuliia Kononchuk_  
> _This repository is part of my personal learning journey and professional portfolio._ 

