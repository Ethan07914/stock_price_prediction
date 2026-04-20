import pandas as pd
import datetime as dt

class transform:
    def __init__(self, stock_data_file_path, news_data_file_path):
        self.stock_data_file_path =stock_data_file_path
        self.stock_df = self.transform_stock_data()
        self.news_data_file_path = news_data_file_path
        self.news_df = self.transform_news_data()

    def transform_stock_data(self):

        df = pd.read_csv(self.stock_data_file_path)

        lag_days = (1,5,10,30)
        # Lag Features
        for day in lag_days:
            df[f'{day}d_prior_close'] = df['close'].shift(day)
            df[f'{day}d_prior_high'] = df['high'].shift(day)
            df[f'{day}d_prior_low'] = df['low'].shift(day)
            df[f'{day}d_prior_open'] = df['open'].shift(day)
            df[f'{day}d_prior_volume'] = df['volume'].shift(day)

        # Drops rows with NULL values in lagged columns to prevent performance reductions
        df = df.dropna()

        # Transform timestamp string to date
        df['date'] = pd.to_datetime(df['date']).dt.date

        # Enrich with day name
        df['day_name'] = df.apply(lambda x: x['date'].strftime("%A"), axis=1)

        return df

    def transform_news_data(self):
        df = pd.read_csv(self.news_data_file_path)

        # Convert timestamp columns to date
        df['publishedDate'] = pd.to_datetime(df['publishedDate'], format='mixed').dt.date
        df['crawlDate'] = pd.to_datetime(df['crawlDate'], format='mixed').dt.date

        # Drop unnecessary columns
        df = df.drop(['url', 'description'], axis=1)

        # Enrich with day name
        df['day_name'] = df.apply(lambda x: x['publishedDate'].strftime("%A"), axis=1)

        # Standardise naming conventions
        df = df.rename(columns={'publishedDate':'published_date', 'crawlDate':'crawl_date'})

        return df


transformed = transform("../data/extracted_stock_data.csv", "../data/extracted_news_data.csv")

transformed.news_df.to_csv("../data/transformed_news_data.csv", index=False)
transformed.stock_df.to_csv('../data/transformed_stock_data.csv', index=False)
