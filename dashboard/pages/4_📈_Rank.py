import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



st.set_page_config(page_title="Ranks", 
                    page_icon="📈")

if 'df' not in st.session_state:
    df = pd.read_csv('data/clean_dataset.csv')
    st.session_state['df'] = df
else:
    df = st.session_state['df']

option = st.selectbox(
    'How would you like to be contacted?',
    ('Ranks', 'Scores'))

st.header(option)

if option == 'Ranks':
    st.write("The bar chart below represents the distribution of ranks of articles which have been written about the Iran protests and Mahsa Amini.")
    st.subheader("Rank distribution")
    fig, ax = plt.subplots(1, 1)
    ax.hist(df['rank'])
    ax.set_xlabel("Rank")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

elif option == 'Scores':
    st.write("The bar chart below represents the distribution of scores of articles which have been written about the Iran protests and Mahsa Amini.")
    st.subheader("Score distribution")
    fig, ax = plt.subplots(1, 1)
    ax.hist(df['_score'])
    ax.set_xlabel("Score")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

else:
    st.error("Choose correct option please!")




