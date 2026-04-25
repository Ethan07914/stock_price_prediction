import pandas as pd
from pipeline.extract import establish_tiingo_connection, extract
from pipeline.transform import transform


load = load('../data/article_metrics.csv', '../data/transformed_stock_data.csv')
load.combined_df.to_csv('../data/combined_output.csv', index=False)


def run_etl_pipeline(ticker):
    # EXTRACT:
    # Initialised extract object
    extract_obj = extract(ticker, establish_tiingo_connection())

    extracted_news_df = pd.DataFrame(extract_obj.extract_news_data())
    extracted_news_df.to_csv('../data/extracted_news_data.csv', index=False)

    extracted_stock_df = pd.DataFrame(extract_obj.extract_stock_data())
    extracted_stock_df.to_csv("../data/extracted_stock_data.csv", index=False)

    # TRANSFORM:
    # Initialise transform object
    transform_obj = transform("../data/extracted_stock_data.csv",
                              "../data/extracted_news_data.csv")

    transformed_news_df = transform_obj.news_df
    transformed_news_df.to_csv("../data/transformed_news_data.csv", index=False)

    transformed_stock_df = transform_obj.stock_df
    transformed_stock_df.to_csv('../data/transformed_stock_data.csv', index=False)


if __name__ == '__main__':
    ticker = 'META'
    run_etl_pipeline(ticker)