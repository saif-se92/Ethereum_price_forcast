from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import pickle
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import io
import base64

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="F:/Cv/eth_forecast/static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="F:/Cv/eth_forecast/templates")

# Load your dataset (modify path as needed)
df = pd.read_csv('F:/Cv/eth_forecast/ETH-USD.csv', parse_dates=["Date"], index_col=["Date"])

# Load or train your ARIMA model
try:
    with open('arima_model_eth_price.pkl', 'rb') as f:
        model_fit = pickle.load(f) 
except FileNotFoundError:
    # Train the model if not found (you should pre-train this)
    # This is just a placeholder - you should train with your actual data
    model = ARIMA(df['Close'], order=(5,1,0))
    model_fit = model.fit()
    with open('arima_model_eth_price.pkl', 'wb') as f:
        pickle.dump(model_fit, f)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Generate plot for the homepage
    plot_url = generate_plot(df['Close'])
    return templates.TemplateResponse("index.html", {
        "request": request,
        "plot_url": plot_url,
        "current_price": df['Close'][-1],
        "last_update": df.index[-1].strftime('%Y-%m-%d')
    })

@app.post("/forecast", response_class=HTMLResponse)
async def make_forecast(request: Request, days: int = Form(...)):
    # Make forecast
    forecast = model_fit.forecast(steps=days)
    
    # Generate dates for forecast
    last_date = df.index[-1]
    forecast_dates = [last_date + timedelta(days=i) for i in range(1, days+1)]
    
    # Generate plot
    plot_url = generate_forecast_plot(df['Close'], forecast, forecast_dates)
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "plot_url": plot_url,
        "forecast": list(zip(
            [d.strftime('%Y-%m-%d') for d in forecast_dates],
            [round(p, 2) for p in forecast]
        )),
        "days": days,
        "current_price": df['Close'][-1],
        "last_update": df.index[-1].strftime('%Y-%m-%d')
    })

def generate_plot(series):
    plt.figure(figsize=(10, 5))
    plt.plot(series.index, series.values)
    plt.title('Historical Ethereum Price')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    
    # Save plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    
    # Encode plot to base64 for HTML
    plot_url = base64.b64encode(buf.read()).decode('utf-8')
    return f"data:image/png;base64,{plot_url}"

def generate_forecast_plot(history, forecast, forecast_dates):
    plt.figure(figsize=(12, 6))
    
    # Plot historical data
    plt.plot(history.index, history.values, label='Historical Price')
    
    # Plot forecast
    plt.plot(forecast_dates, forecast, 'r--', label='Forecast')
    
    plt.title('Ethereum Price Forecast')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    
    # Save plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    
    # Encode plot to base64 for HTML
    plot_url = base64.b64encode(buf.read()).decode('utf-8')
    return f"data:image/png;base64,{plot_url}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)