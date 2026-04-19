import yfinance as yf

# Initialize the ticker
ticker = yf.Ticker("GOOG")

# Fetch recent news
news = ticker.news

print(news)