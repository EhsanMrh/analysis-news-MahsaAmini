import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

if 'df' not in st.session_state:
    df = pd.read_csv('data/clean_dataset.csv')
    st.session_state['df'] = df
else:
    df = st.session_state['df']


st.header("This is start page! 👋")
st.write("Write a cool description here")
st.markdown("""
            **Professor's name**

            **Created By Sepideh**
            
            """)




# st.markdown(
#     """
#     Streamlit is an open-source app framework built specifically for
#     Machine Learning and Data Science projects.
#     **👈 Select a demo from the sidebar** to see some examples
#     of what Streamlit can do!
#     ### Want to learn more?
#     - Check out [streamlit.io](https://streamlit.io)
#     - Jump into our [documentation](https://docs.streamlit.io)
#     - Ask a question in our [community
#         forums](https://discuss.streamlit.io)
#     ### See more complex demos
#     - Use a neural net to [analyze the Udacity Self-driving Car Image
#         Dataset](https://github.com/streamlit/demo-self-driving)
#     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
# """
# )