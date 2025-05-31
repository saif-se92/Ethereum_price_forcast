# 📈 Ethereum Price Forecasting using ARIMA

This project applies classical time series modeling with ARIMA to forecast the price of Ethereum (ETH-USD). It walks through the full pipeline from data preparation and EDA to model development and evaluation.

---

## 🧠 Methodology

The project follows a traditional time series workflow:

1. **Data Collection & Cleaning**
2. **Exploratory Data Analysis (EDA)**
3. **Stationarity Testing (ADF Test)**
4. **ACF/PACF Analysis for Parameter Selection**
5. **ARIMA Modeling**
6. **Model Evaluation (RMSE, MAPE)**
7. **Forecasting Future Prices**

---

## 🔍 Features

- 📅 Historical ETH price data
- 🧪 Augmented Dickey-Fuller (ADF) Test for stationarity
- 🔁 Rolling mean smoothing
- 📊 Autocorrelation and Partial Autocorrelation plots
- 📈 ARIMA model: `(p=5, d=1, q=2)`
- 🔮 30-day price forecast with visualization


---
pip install pandas numpy matplotlib seaborn plotly statsmodels scikit-learn

## 🚀 Running the Project

- 1.Clone the repository:
git clone https://github.com/saif-se92/eth-arima-forecasting.git
cd eth-arima-forecasting
- 2.Launch the notebook:
jupyter notebook Eth_Price_Forecasting.ipynb

---
## 📊 Model Evaluation

   - RMSE (Root Mean Squared Error) and MAPE (Mean Absolute Percentage Error) are used for performance.

   - Visual comparison of actual vs predicted values.

---

## 🖼️ Visualizations

   - ETH closing prices over time

   - Volume trends

   - ACF & PACF plots

   - Actual vs forecast comparison

## 🔮 Future Work

   - Compare with advanced ML models (e.g., LSTM, Prophet)

   - Incorporate technical indicators and macroeconomic variables

   - Build a dashboard using Streamlit

## 🤝 Contributions

Feel free to fork, open issues, or suggest improvements!
## 🔗 Connect with Me

- 📧 Email: saifullah44356@gmail.com
- 🔗 LinkedIn: www.linkedin.com/in/saifullah-haider-944a38278


---

Would you like me to:
- Fill in your GitHub and LinkedIn links?
- Generate a Streamlit version of this forecasting tool?
- Compare ARIMA with LSTM in the same notebook?

Let me know how you'd like to expand or share this! ​:contentReference[oaicite:0]{index=0}​


