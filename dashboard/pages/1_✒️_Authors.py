import streamlit as st
import pandas as pd


st.set_page_config(page_title="Authors", 
                    page_icon="✒️")

if 'df' not in st.session_state:
    df = pd.read_csv('data/clean_dataset.csv')
    st.session_state['df'] = df
else:
    df = st.session_state['df']


st.header("Authors")
st.write("The bar chart below represents the distribution of number of articles which authors have written about the Iran protests and Mahsa Amini")
st.subheader("Number of articles per each author")



authors = df['author'].value_counts()
min_article = st.slider('Limit of number of articles:', 1, 43, 10)
active_authors = authors[authors>min_article]
active_authors = active_authors.reset_index(name='Count')
active_authors.rename(columns={'index': 'Author'}, inplace=True)



st.bar_chart(active_authors, x='Author', y='Count')
