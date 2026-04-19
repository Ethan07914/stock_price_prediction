from tiingo import TiingoClient
from dotenv import load_dotenv
from datetime import timedelta
import pandas as pd
import datetime as dt
import os


load_dotenv()

class Extract:
    def __init__(self, ticker, client, articles_per_day):
        self.ticker = ticker
        self.articles_per_day = articles_per_day
        self.end_date = dt.date.today()
        self.start_date = self.end_date - timedelta(days=10)
        self.client = client

    def extract_stock_data(self):
        try:
            stock_data = self.client.get_ticker_price(self.ticker,
                                                     frequency='daily',
                                                     startDate=self.start_date,
                                                     endDate=self.end_date)
        except Exception as e:
            raise RuntimeError(f"Data request failed for {self.ticker}") from e

        return stock_data

    def extract_news_data(self):
        try:
            news_data = self.client.get_news(tickers=[self.ticker],
                                             limit=self.articles_per_day * 10,

                                             sources=['Bloomberg.com', 'Reuters.com'],
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

extract = Extract("META", establish_tiingo_connection(), 10)
# pd.DataFrame(extract.extract_news_data()).to_csv('extracted_news_data.csv',index=False)
pd.DataFrame(extract.extract_stock_data()).to_csv("extracted_stock_data.csv", index=False)





