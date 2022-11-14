import streamlit as st
import pandas as pd


st.set_page_config(page_title="Opinion", 
                    page_icon="✋")

if 'df' not in st.session_state:
    df = pd.read_csv('data/clean_dataset.csv')
    st.session_state['df'] = df
else:
    df = st.session_state['df']


st.header("Is Opinion?")
st.write("The bar chart below shows the distribution of opinion and fact articles about the Iran protests and Mahsa Amini.")
st.subheader("Number of articles written as a opinion or not")


topics = df['is_opinion'].value_counts()

topics = topics.reset_index(name='Count')
topics.rename(columns={'index': 'Is opinion?'}, inplace=True)

st.bar_chart(topics, x='Is opinion?', y='Count')
