[![View Repositories](https://img.shields.io/badge/View-My_Repositories-blue?logo=GitHub)](https://github.com/Yulia-Momotyuk?tab=repositories)
[![View My Profile](https://img.shields.io/badge/View-My_Profile-green?logo=GitHub)](https://github.com/Yulia-Momotyuk)
# CryptoInvest Insight — Investment Strategies & Risk Analysis

## Project Overview
This project analyzes the cryptocurrency market (BTC, ETH, ADA, SOL, XRP) using **historical data extracted directly via CoinGecko API**. 
The dataset was engineered into daily time series with returns, volatility, and drawdowns, forming the basis for an end-to-end analytical pipeline.  

The goal was to evaluate investment strategies, risk–return tradeoffs, and test whether even basic ML models can forecast short-term market dynamics.  

---

## Technologies Used
- **Data Engineering**: Python (requests, pandas, numpy), CoinGecko API (automated data extraction).  
- **Data Analysis**: matplotlib, seaborn (EDA & visualization), scipy (t-tests), sklearn (Linear Regression).  
- **BI & Visualization**: Power BI with **custom DAX measures** (ROI %, Volatility, Sharpe, Sortino, Max Drawdown).  
- **Workflow**: Jupyter Lab for integration of analysis, modeling, and storytelling.  

---

## Methodology
1. - **Source**: CoinGecko API (historical data 2024–2025).  
   - **Main dataset**: `crypto_market.csv`  
   - `date` — trading day  
   - `symbol` — coin (BTC, ETH, ADA, SOL, XRP)  
   - `price_usd`, `volume_usd`, `market_cap_usd`  
   - Calculated metrics: `return_pct`, `drawdown_pct`, `rolling_vol_14d`, `roi_pct`, `is_dip_3d`  
   - **Additional dataset**: `sim_results.csv` with strategy simulation results.  

2. **Exploratory Data Analysis**  
   - Trends, seasonality (weekday/month), volatility & drawdown analysis.  
   - Correlation heatmap between assets.  

3. **Investment Strategy Simulations**  
   - Modeled **Buy & Hold, Dollar Cost Averaging (DCA), Buy-on-Dip**.  
   - Compared ROI (%) and final values ($).  
   - Risk–Return Map to visualize performance.  

4. **Statistical Testing**  
   - **t-tests**: examined whether high-volume days significantly impact returns.  
   - Results: strong effect for BTC & XRP; not significant for ETH, SOL, ADA.  

5. **Machine Learning Forecast**  
   - Applied **Linear Regression** with TimeSeriesSplit for BTC (7-day horizon).  
   - R² ≈ 0.77 → model captures general trend but underperforms on sharp spikes.  

6. **BI Dashboard**  
   - Power BI dashboard with KPI cards, Risk–Return Map, Sharpe ratio comparison, drawdown analysis.  
   - Interactive **strategy simulator** (Buy & Hold, DCA, Buy-on-Dip).  

---

## Key Insights
- **XRP & ADA**: highest ROI, but also highest drawdowns (high-risk/high-reward).  
- **BTC & ETH**: portfolio stabilizers with moderate, reliable returns.  
- **SOL**: weakest performer in the sample.  
- **Strategies**: Buy & Hold was the most consistent; DCA lowered risks but reduced returns; Buy-on-Dip only worked in selective cases.  
- **Volume Analysis**: BTC & XRP are highly sensitive to trading volumes.  
- **ML Model**: captured BTC’s overall trend, but failed during extreme volatility.  

---

### Business & Technical Goals  
- **Business Impact**: clear framework to evaluate crypto assets and strategies by profitability vs risk.  
- **Technical Impact**: demonstrates **full-stack analytics** — API → Python → statistics → ML → Power BI storytelling.  

---

## 📬 Contact

[LinkedIn](https://www.linkedin.com/in/yuliia-kononchuk-78913633b/) | [Email](mailto:kononchuk.yuliia@gmail.com)

---

> **Author**: _Yuliia Kononchuk_  
> _This repository is part of my personal learning journey and professional portfolio._ 

