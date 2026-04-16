from tiingo import TiingoClient
from dotenv import load_dotenv
from datetime import timedelta
import yfinance as yf
import datetime as dt
import os


load_dotenv()

class Extract:
    def __init__(self, ticker, client):
        self.ticker = ticker
        self.end_date = dt.date.today()
        self.start_date = self.end_date - timedelta(days=1000)
        self.client = client

    def extract_stock_data(self):
        return yf.download(self.ticker,
                           start=self.start_date,
                           end=self.end_date)

    def extract_news_data(self):
        try:
            news_data = self.client.get_news(tickers=[self.ticker],
                                             startDate=self.start_date,
                                             endDate=self.end_date)
        except Exception as e:
            raise RuntimeError(f"Data request failed for {self.ticker}") from e

        return news_data


def establish_tiingo_connection(api_token= \
                                        os.getenv("tiingo_api_token")):
    '''
    This function configures a connection to the Tiingo API using
    the tiingo Python package.

    source: (Cameron Yick, https://pypi.org/project/tiingo/)
    '''

    # Setup authorization dictionary
    config = {}
    config["session"] = True
    config["api_key"] = api_token

    # Initialise client
    client = TiingoClient(config)

    return client

extract = Extract("GOOG", establish_tiingo_connection())
# extract.extract_news_data().to_csv("data/news_data.csv")
extract.extract_stock_data().to_csv("extracted_stock_data.csv")





