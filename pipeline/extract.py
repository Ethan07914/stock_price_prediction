import yfinance as yf
import tiingo
import pandas as pd

ticker = "GOOG"

df = yf.download(ticker, period="1mo")

print(df.tail())

