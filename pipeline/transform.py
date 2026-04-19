import pandas as pd

class transform:
    def __init__(self, stock_data_file_path, news_data_file_path):
        self.stock_data_file_path =stock_data_file_path
        self.stock_df = self.transform_stock_data()
        self.news_data_file_path = news_data_file_path
        self.news_df = self.transform_news_data()

    def transform_stock_data(self):

        headers = ['date', 'close', 'high', 'low', 'open', 'volume']
        df = pd.read_csv(self.stock_data_file_path,
                         skiprows=3,
                         names=headers)

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

        return df

    def transform_news_data(self):
        return pd.read_csv(self.news_data_file_path)





transformed = transform("extracted_stock_data.csv", "news_data.csv")

# transformed.stock_df.to_csv("transformed_stock_data.csv", index=False)

transformed.news_df.to_csv('transformed_news_data.csv')
