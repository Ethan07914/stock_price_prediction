import streamlit as st
import pandas as pd
# from stock_price_prediction.initial_load import ticker

# DATAFRAMES
stock_df = pd.read_csv('data/transformed_stock_data.csv')[['date',
                                                           'close',
                                                           'high',
                                                           'low',
                                                           'open',
                                                           'previous_day_close',
                                                           'volume']]\
    .rename(columns={'close':'Close Price',
                     'high':'Max Price',
                     'low':'Min Price',
                     'open':'Open Price',
                     'volume':'Trading Volume',
                     'previous_day_close':'Previous Day Close Price',
                     'date':'Date'})\
    .sort_index(ascending=False)\

# VARIABLES
ticker = 'META'

# TITLE & HEADERS
st.title("Stock Price Prediction")
st.badge(ticker, color="blue", icon="♾️")

st.sidebar.header("Navigation")

st.subheader("Meta ($META) Daily Performance")
st.dataframe(stock_df.style.background_gradient(cmap="RdBu"), hide_index=True)

# BUTTONS
if st.button("Retrain"):
    st.balloons()
    pass

left, centre, right =st.columns(3)

with centre:
    st.subheader("Close Price by Date")

st.line_chart(x='Date', y='Close Price',data=stock_df, color="#0668E1")

import streamlit as st
import time

st.header("META Data Pipeline")

# GEMINI 3 FAST assisted in generation
# 1. Create a styled container for the 'terminal'
terminal_placeholder = st.empty()
terminal_text = "user@meta-pipeline:~$ starting process...\n"


def log_to_terminal(message):
    global terminal_text
    terminal_text += f"> {message}\n"
    # Wrap in st.code to get the terminal font and background
    terminal_placeholder.code(terminal_text, language="bash")


# --- Example Pipeline ---
if st.button("Run Pipeline"):
    log_to_terminal("Initializing extraction...")
    time.sleep(1)

    log_to_terminal("Extracting META stock data from API...")
    time.sleep(2)
    log_to_terminal("Extract Complete. [OK]")

    log_to_terminal("Running Transformations...")
    time.sleep(1)
    log_to_terminal("Transformation Complete. [OK]")

    log_to_terminal("Pipeline Finished Successfully.")

# End of co-generated code