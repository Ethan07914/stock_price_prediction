import yfinance as yf
import pandas as pd

# Initialize the ticker
ticker = yf.Ticker("GOOG")

# Fetch recent news
news = ticker.news

news_df = pd.read_csv("pipeline/extracted_news_data.csv")
print(news_df[news_df['description'].isnull()])