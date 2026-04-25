import pandas as pd
from pipeline.extract import establish_tiingo_connection, extract
from pipeline.transform import transform
from pipeline.load import load
from ipynb.fs.defs.models.sentiment_model import run_text_classification, enrich_df, calculate_metrics

def run_etl_pipeline(ticker):
    print(
    '''
    STARTING ETL PIPELINE:
    
    EXTRACT
    ''')
    # EXTRACT
    # Initialised extract object
    extract_obj = extract(ticker, establish_tiingo_connection())

    extracted_news_df = pd.DataFrame(extract_obj.extract_news_data())
    extracted_news_df.to_csv('data/extracted_news_data.csv', index=False)

    extracted_stock_df = pd.DataFrame(extract_obj.extract_stock_data())
    extracted_stock_df.to_csv("data/extracted_stock_data.csv", index=False)

    print('''
    TRANSFORM''')
    # TRANSFORM:
    # Initialise transform object
    transform_obj = transform("data/extracted_stock_data.csv",
                              "data/extracted_news_data.csv")

    transformed_news_df = transform_obj.news_df
    transformed_news_df.to_csv("data/transformed_news_data.csv", index=False)

    transformed_stock_df = transform_obj.stock_df
    transformed_stock_df.to_csv('data/transformed_stock_data.csv', index=False)

    print('''
    TEXT-CLASSIFICATION''')
    # TEXT-CLASSIFICATION:
    # Get Sentiment Classifications
    news_df_with_classifications = run_text_classification(transformed_news_df)

    # Enrich with additional columns
    enriched_news_df = enrich_df(news_df_with_classifications)

    # Calculate metrics & output as CSV
    news_df_with_metrics = calculate_metrics(enriched_news_df)
    news_df_with_metrics.to_csv('data/news_df_with_metrics.csv', index=False)

    print('''
    LOAD''')
    # LOAD:
    # Initialise load object
    load_obj = load('data/news_df_with_metrics.csv', 'data/transformed_stock_data.csv')
    load_obj.combined_df.to_csv('data/combined_output.csv', index=False)

    print('''
    END''')


if __name__ == '__main__':
    ticker = 'META'
    run_etl_pipeline(ticker)