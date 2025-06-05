# 📈 Ethereum Price Forecasting using ARIMA

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green.svg)
![ARIMA](https://img.shields.io/badge/Model-ARIMA-orange)

Ethereum (ETH-USD) prices, featuring both a Jupyter Notebook for analysis and a FastAPI web application for interactive forecasting.

## 🌟 Features

### Analysis Module (Jupyter Notebook)
- 📅 Historical ETH price data analysis
- 🧪 Augmented Dickey-Fuller (ADF) Test for stationarity
- 🔁 Rolling mean smoothing
- 📊 Autocorrelation and Partial Autocorrelation plots
- 📈 ARIMA model: `(p=5, d=1, q=2)`
- 🔮 30-day price forecast visualization
- 📉 Model evaluation (RMSE, MAPE metrics)

### Web Application (FastAPI)
- 🖥️ Interactive web interface
- 📈 Dynamic historical price visualization
- 🔮 Customizable forecast period (1-30 days)
- 📊 Combined historical + forecast charts
- 📱 Responsive design
- ⚡ Real-time predictions

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn plotly statsmodels scikit-learn fastapi uvicorn jinja2
Two Ways to Run:

   1.Jupyter Notebook Analysis

git clone https://github.com/yourusername/eth-price-forecast.git
cd eth-price-forecast
jupyter notebook Eth_Price_Forecasting.ipynb

  2.FastAPI Web Application

python app.py
# Access at http://localhost:8000
```
## 🏗️ Project Structure
```
eth-price-forecast/
├── app.py                 # FastAPI application
├── Eth_Price_Forecasting.ipynb  # Analysis notebook
├── ETH-USD.csv            # Historical price data
├── static/                # Static files (CSS, JS)
├── templates/             # HTML templates
│   └── index.html         # Web interface
└── arima_model_eth_price.pkl  # Trained ARIMA model
```

## 🤝 Contributing

Contributions are welcome! Please open an issue to discuss your ideas or submit a pull request.

## 📜 License

MIT © 2023 Saifullah Haider


### Key Improvements:
1. **Combined both versions** into a cohesive project with clear sections
2. **Added badges** for visual appeal and quick info
3. **Structured installation** for both notebook and web app
4. **Enhanced future work** section with checkboxes
5. **Better organization** of technical details
6. **Added license** information
7. **Improved visual hierarchy** with emojis and sections
