import streamlit as st
import pandas as pd
import pydeck as pdk

# page settings
st.set_page_config(
    page_title="2025 Japan Trip Blog",
    page_icon="🇯🇵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# main content
st.header("**2025 Japan Trip Blog**")
st.write("*November 1-12*")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Map", "Itinerary", "Highlights", "Gallery", "Thoughts"])

with tab1:
    places = {
        "place": ["Shinjuku", "Shibuya", "Asakusa", "Akihabara", "Ryogoku", "Ikebukuro", "Odaiba", "Yokohama", "Chiba", "Edogawa", "Chiyoda", "Ueno"],
        "lat": [35.6938, 35.6580, 35.7148, 35.6984, 35.6938, 35.7348, 35.6206, 35.4437, 35.6329, 35.6399, 35.6940, 35.7087],
        "lon": [139.7034, 139.7016, 139.7967, 139.7730, 139.7927, 139.7077, 139.7805, 139.6380, 139.8804, 139.8622, 139.7538, 139.7742]
    }

    df = pd.DataFrame(places)
    layer = pdk.Layer(
        "ScatterplotLayer",
        df,
        get_position=["lon", "lat"],
        get_radius=80,
        get_color=[255, 0, 0],
        pickable=True,
    )
    
    view_state = pdk.ViewState(
        latitude=35.68, longitude=139.76, zoom=10
    )
    
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{place}"}))
