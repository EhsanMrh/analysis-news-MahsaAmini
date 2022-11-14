import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium  



st.set_page_config(page_title="Countries", 
                    page_icon="🌎")

if 'df' not in st.session_state:
    df = pd.read_csv('data/clean_dataset.csv')
    st.session_state['df'] = df
else:
    df = st.session_state['df']


countries= pd.read_csv('data/geolocations.csv')
countries.dropna(subset=['latitude', 'longitude'], how="any", inplace=True)


st.header("Countries")
st.write("The map below shows countries that released articles about the Iran protests and Mahsa Amini.")

with st.spinner("Loading the Map..."):
    world_map= folium.Map(tiles="cartodbpositron")
    marker_cluster = MarkerCluster().add_to(world_map)
    #for each coordinate, create circlemarker of user percent
    for i in range(len(countries)):
        lat = countries.iloc[i]['latitude']
        long = countries.iloc[i]['longitude']
        radius=5
        popup_text = """Country : {}<br>
                    %of News : {}<br>"""
        popup_text = popup_text.format(countries.iloc[i]['country_name'],
                                countries.iloc[i]['news_num']
                                )
        folium.CircleMarker(location = [lat, long], radius=radius, popup= popup_text, fill =True).add_to(marker_cluster)

#show the map
st_folium(world_map)

