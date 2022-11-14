import streamlit as st
import pandas as pd


st.set_page_config(page_title="Date", 
                    page_icon="📅")

if 'df' not in st.session_state:
    df = pd.read_csv('data/clean_dataset.csv')
    st.session_state['df'] = df
else:
    df = st.session_state['df']


st.header("Date")
st.write("The bar chart below represents the distribution of number of articles per date which have been written about the Iran protests and Mahsa Amini.")
st.subheader("Number of articles in each day")


dates = df['date'].value_counts()

dates = dates.reset_index(name='Count')
dates.rename(columns={'index': 'Date'}, inplace=True)

st.line_chart(dates, x='Date', y='Count')
