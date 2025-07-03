# ml_trading_algo.py (Fixed and Cleaned)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import yfinance as yf
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from xgboost import XGBClassifier
import streamlit as st
import datetime

def init_db(db_name="trading_data.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS trades (
                        date TEXT,
                        symbol TEXT,
                        prediction INTEGER,
                        actual INTEGER,
                        profit_loss REAL
                     )''')
    conn.commit()
    return conn

def fetch_data(symbol="AAPL", start="2020-01-01", end="2024-12-31"):
    df = yf.download(symbol, start=start, end=end, auto_adjust=True)
    df.dropna(inplace=True)
    df["Close"] = df["Close"] if "Close" in df.columns else df.iloc[:, -1]
    df["Return"] = df["Close"].pct_change()
    df["Target"] = (df["Return"].shift(-1) > 0).astype(int)
    return df

def compute_rsi(series, period=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def add_features(df):
    df["MA10"] = df["Close"].rolling(10).mean()
    df["MA50"] = df["Close"].rolling(50).mean()
    df["Volatility"] = df["Return"].rolling(10).std()
    df["RSI"] = compute_rsi(df["Close"], 14)
    ema_12 = df['Close'].ewm(span=12, adjust=False).mean()
    ema_26 = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = ema_12 - ema_26
    df['MACD_Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
    df['MACD_Hist'] = df['MACD'] - df['MACD_Signal']
    df['Volume_MA20'] = df['Volume'].rolling(window=20).mean()
    df['SMA_Cross'] = 0
    df.loc[df['MA10'] > df['MA50'], 'SMA_Cross'] = 1
    df.loc[df['MA10'] < df['MA50'], 'SMA_Cross'] = -1
    df['Cross_Signal'] = df['SMA_Cross'].diff()
    df.dropna(inplace=True)
    return df

def train_model(df):
    features = ["MA10", "MA50", "Volatility", "RSI", "MACD_Hist", "Volume", "Volume_MA20"]
    X = df[features]
    y = df["Target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    return model

def simulate_trading(df, model, symbol, conn):
    features = ["MA10", "MA50", "Volatility", "RSI", "MACD_Hist", "Volume", "Volume_MA20"]
    df["Prediction"] = model.predict(df[features])
    df["Strategy Return"] = df["Return"] * df["Prediction"].shift(1)
    df["Cumulative Return"] = (1 + df["Return"]).cumprod()
    df["Cumulative Strategy"] = (1 + df["Strategy Return"]).cumprod()

    volume, volume_ma = df['Volume'].align(df['Volume_MA20'], join='inner')
    df = df.loc[volume.index]

    buy_condition = (
        (df['Cross_Signal'] == 2) &
        (df['RSI'] < 50) &
        (df['MACD_Hist'] > 0) &
        (volume > volume_ma) &
        (df['Volatility'] < 0.03)
    )
    sell_condition = (
        (df['Cross_Signal'] == -2) &
        (df['RSI'] > 50) &
        (df['MACD_Hist'] < 0)
    )
    df['Buy_Signal'] = np.where(buy_condition, df['Close'], np.nan)
    df['Sell_Signal'] = np.where(sell_condition, df['Close'], np.nan)
    cursor = conn.cursor()
    for i, row in df.iterrows():
        if pd.notna(row["Prediction"]):
            profit = row["Return"] if row["Prediction"] == row["Target"] else -abs(row["Return"])
            cursor.execute("INSERT INTO trades VALUES (?, ?, ?, ?, ?)",
                           (str(i), symbol, int(row["Prediction"]), int(row["Target"]), profit))
    conn.commit()
    return df

def plot_performance(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df["Cumulative Return"], name="Market"))
    fig.add_trace(go.Scatter(x=df.index, y=df["Cumulative Strategy"], name="Strategy"))
    fig.add_trace(go.Scatter(x=df.index, y=df['Buy_Signal'], mode='markers', marker_symbol='triangle-up',
                             marker_color='green', marker_size=10, name='Buy'))
    fig.add_trace(go.Scatter(x=df.index, y=df['Sell_Signal'], mode='markers', marker_symbol='triangle-down',
                             marker_color='red', marker_size=10, name='Sell'))
    fig.update_layout(title="Cumulative Performance with Buy/Sell Signals",
                      xaxis_title="Date", yaxis_title="Cumulative Return")
    return fig

def streamlit_ui():
    st.title("ML-Based Trading Dashboard")
    symbol = st.text_input("Enter Ticker Symbol", value="AAPL")
    start_date = st.date_input("Start Date", datetime.date(2020, 1, 1))
    end_date = st.date_input("End Date", datetime.date.today())
    if st.button("Run Strategy"):
        conn = init_db()
        df = fetch_data(symbol, str(start_date), str(end_date))
        df = add_features(df)
        model = train_model(df)
        df = simulate_trading(df, model, symbol, conn)
        fig = plot_performance(df)
        st.plotly_chart(fig)
        conn.close()

def run_pipeline(symbol="AAPL"):
    conn = init_db()
    df = fetch_data(symbol)
    df = add_features(df)
    model = train_model(df)
    df = simulate_trading(df, model, symbol, conn)
    fig = plot_performance(df)
    fig.show()
    conn.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "web":
        streamlit_ui()
    else:
        run_pipeline("MSFT")