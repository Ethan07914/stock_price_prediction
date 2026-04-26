import os

import pandas as pd
from pipeline.extract import establish_tiingo_connection, extract
from pipeline.transform import transform
from pipeline.load import load
import datetime as dt
from ipynb.fs.defs.models.sentiment_model import run_text_classification, enrich_df, calculate_metrics

def run_extract(ticker, start_date, end_date, article_limit):
    print(
    '''
    STARTING ETL PIPELINE:
    
    EXTRACT
    ''')
    # EXTRACT
    # Initialised extract object
    extract_obj = extract(ticker, establish_tiingo_connection(), article_limit, end_date, start_date)

    extracted_news_df = pd.DataFrame(extract_obj.extract_news_data())
    extracted_news_df.to_csv('data/extracted_news_data.csv', index=False, mode='a')

    extracted_stock_df = pd.DataFrame(extract_obj.extract_stock_data())
    extracted_stock_df.to_csv("data/extracted_stock_data.csv", index=False, mode='a')

    return extracted_news_df, extracted_stock_df

def  run_transform():
    print('''
    TRANSFORM''')
    # TRANSFORM:
    # Initialise transform object
    transform_obj = transform("data/extracted_stock_data.csv",
                              "data/extracted_news_data.csv")

    transformed_news_df = transform_obj.news_df
    transformed_news_df.to_csv("data/transformed_news_data.csv", index=False, mode='a')

    transformed_stock_df = transform_obj.stock_df
    transformed_stock_df.to_csv('data/transformed_stock_data.csv', index=False, mode='a')

    print('''
    TEXT-CLASSIFICATION''')
    # TEXT-CLASSIFICATION:
    # Get Sentiment Classifications
    news_df_with_classifications = run_text_classification(transformed_news_df)

    # Enrich with additional columns
    enriched_news_df = enrich_df(news_df_with_classifications)

    # Calculate metrics & output as CSV
    news_df_with_metrics = calculate_metrics(enriched_news_df)
    news_df_with_metrics.to_csv('data/news_df_with_metrics.csv', index=False, mode='a')

    return news_df_with_metrics, transformed_stock_df

def run_load():
    print('''
    LOAD''')
    # LOAD:
    # Initialise load object
    load_obj = load('data/news_df_with_metrics.csv', 'data/transformed_stock_data.csv')
    load_obj.combined_df.to_csv('data/combined_output.csv', index=False, mode='a')

    print('''
    END''')

    return load_obj.combined_df

def initial_load():
    end_date = dt.date.today()
    start_date = end_date - dt.timedelta(days=1000)
    article_limit = 1000

def overwrite_files():
    files = ['combined_output.csv', 'news_df_with_metrics.csv', 'transformed_news_data.csv',
             'extracted_news_data.csv', 'extracted_stock_data.csv', 'transformed_stock_data.csv']
    prefix = 'data/'
    for file in files:
        if os.path.exists(prefix+file):
            os.remove(prefix+file)


if __name__ == '__main__':
    overwrite_files()
    ticker = 'META'
    run_extract(ticker, dt.date.today() - dt.timedelta(days=2), dt.date.today(), 10)
    run_transform()
    run_load()