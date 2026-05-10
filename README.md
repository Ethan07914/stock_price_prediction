# Stock Price Prediction

## Data Sources

- **yfinance**: Free open source Python library for historical and real time financial data from Yahoo Finance.
- **Tiingo**: Financial data platform providing real time, historical and financial news data via API.
- Using yfinance for the financial data means more news articles can be requested from the Tiingo API whilst remaining within the free tier limits.

## Decisions

- Originally the outputs of the sentiment model would be combined with the numerical stock price data
- News API only allowed for 3 months of history, which was not enough for LSTM to pick up on all patterns
- Decision was made to separate predictions from news and stock price data into two separate indicators
- THis way LSTM had more history of data to train from and news data could also provide better insight