import pandas as pd

class load:
    def __init__(self, transformed_news_path, transformed_stock_path):
        self.transformed_news_path = transformed_news_path
        self.transformed_stock_path = transformed_stock_path
        self.news_df = pd.read_csv(self.transformed_news_path)
        self.stock_df = pd.read_csv(self.transformed_stock_path)
        self.combined_df = self.join()

    def join(self):
        return pd.merge(self.stock_df, self.news_df, how='inner', on='date')



