import pandas as pd
import ast


class load:
    def __init__(self, transformed_news_path, transformed_stock_path):
        self.transformed_news_path = transformed_news_path
        self.transformed_stock_path = transformed_stock_path
        self.news_df = pd.read_csv(self.transformed_news_path)
        self.stock_df = pd.read_csv(self.transformed_stock_path)
        self.combined_df = self.join()

    def join(self):
        # Nest news data
        self.nest()

        # Rename for joining purposes
        self.news_df = self.news_df.rename(columns={'published_date': 'date'})

        # Inner join stock and news data
        combined_df = pd.merge(self.stock_df, self.news_df, how='inner', on='date')

        return combined_df

    def nest(self):
        # Nest columns as a dictionary
        self.news_df['articles'] = self.news_df.apply(lambda x: x.to_dict(), axis=1)

        # Array/list aggregation
        self.news_df = self.news_df.groupby('published_date').agg(list).reset_index()

        # Only select required columns
        self.news_df = self.news_df[['published_date', 'articles']]

        return self.news_df


load = load('../data/sentiment_model_output.csv', '../data/transformed_stock_data.csv')
load.combined_df.to_csv('../data/combined_output.csv', index=False)

