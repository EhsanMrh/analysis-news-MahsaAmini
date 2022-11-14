import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sources", 
                    page_icon="🗄️")

if 'df' not in st.session_state:
    df = pd.read_csv('data/clean_dataset.csv')
    st.session_state['df'] = df
else:
    df = st.session_state['df']


option = st.selectbox(
    'How would you like to be contacted?',
    ('Sources', 'Topics', 'Languages'))

st.header(option)

if option == 'Sources':
    st.write("The bar chart below represents the distribution of number of articles per source which have been written about the Iran protests and Mahsa Amini.")
    st.subheader("Number of articles on each source")
    urls = df['clean_url'].value_counts()
    urls = urls.reset_index(name='Count')
    urls.rename(columns={'index': 'Source'}, inplace=True)
    st.bar_chart(urls, x='Source', y='Count')

elif option == 'Topics':
    st.write("The bar chart below shows the topics of released articles about the Iran protests and Mahsa Amini.")
    st.subheader("Number of articles on each topic")
    topics = df['topic'].value_counts()
    topics = topics.reset_index(name='Count')
    topics.rename(columns={'index': 'Topic'}, inplace=True)
    st.bar_chart(topics, x='Topic', y='Count')


    fig, ax = plt.subplots()
    ax.pie(topics['Count'], labels=topics['Topic'], autopct='%1.1f%%')
    st.pyplot(fig)



elif option == 'Languages':
    st.write("The bar chart below shows the languages of released articles about the Iran protests and Mahsa Amini.")
    st.subheader("Number of articles written in each language")
    topics = df['language'].value_counts()
    topics = topics.reset_index(name='Count')
    topics.rename(columns={'index': 'Language'}, inplace=True)
    st.bar_chart(topics, x='Language', y='Count')
else:
    st.error("Choose correct option please!")

