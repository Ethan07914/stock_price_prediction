from main import overwrite_files, run_extract_stock, run_extract_news, run_transform, run_load
import datetime as dt
import pandas as pd

overwrite_files()

end_date = dt.date.today()
start_date = dt.date.today() - dt.timedelta(days=1000)

article_limit = 1000
ticker = 'META'

run_extract_news(ticker, start_date, end_date, article_limit)


for i in range(10):
    current_extracted_df = pd.read_csv('data/extracted_news_data.csv')
    current_extracted_df['publishedDate'] = pd.to_datetime(current_extracted_df['publishedDate'], format='mixed').dt.date
    end_date = current_extracted_df['publishedDate'].min()
    start_date = end_date - dt.timedelta(days=1000)
    print(start_date, end_date)

    run_extract_news(ticker, start_date, end_date, article_limit)

extracted_news_df = pd.read_csv('data/extracted_news_data.csv')
extracted_news_df['publishedDate'] = pd.to_datetime(extracted_news_df['publishedDate'], format='mixed').dt.date

end_date = extracted_news_df['publishedDate'].min()
start_date = extracted_news_df['publishedDate'].max()

run_extract_stock(ticker, start_date, end_date, article_limit)
run_transform()
run_load()