import pandas as pd

class transform:
    def __init__(self, extracted_file_path):
        self.extracted_file_path = extracted_file_path
        self.stock_df = self.transform_stock_df()

    def transform_stock_df(self):

        headers = ['date', 'close', 'high', 'low', 'open', 'volume']
        df = pd.read_csv(self.extracted_file_path,
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




transformed = transform("extracted_stock_data.csv")

print(transformed.stock_df.head())

