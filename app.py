import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# page settings
st.set_page_config(
    page_title="2025 Japan Trip Blog",
    page_icon="🇯🇵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def embed_image(path, width=200):
    with open(path, "rb") as f:
        img = base64.b64encode(f.read()).decode()
    return f'<img src="data:image/jpeg;base64,{img}" width="{width}"/>'

# main content
st.header("**2025 Japan Trip Blog**")
st.write("*November 1-12*")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Map", "Itinerary", "Highlights", "Gallery", "Thoughts"])

with tab1:
    places = {
        "place": ["Shinjuku", "Shibuya", "Asakusa", "Akihabara", "Ryogoku", "Ikebukuro", "Odaiba", "Yokohama", "Chiba", "Edogawa", "Chiyoda", "Ueno"],
        "lat": [35.6938, 35.6580, 35.7148, 35.6984, 35.6938, 35.7348, 35.6206, 35.4437, 35.6329, 35.6399, 35.6940, 35.7087],
        "lon": [139.7034, 139.7016, 139.7967, 139.7730, 139.7927, 139.7077, 139.7805, 139.6380, 139.8804, 139.8622, 139.7538, 139.7742],
        "photo": ["img/shinjuku.jpg", "img/shibuya.jpg", "img/asakusa.jpg", "img/akiba.jpg", "img/ryogoku.jpg", "img/ikebukuro.jpg", "img/odaiba.jpg", "img/yokohama.jpg", "img/chiba.jpg", "img/edogawa.jpg", "img/chiyoda.jpg", "img/ueno.jpg"]
    }

    df = pd.DataFrame(places)
    # center map on Tokyo
    m = folium.Map(location=[35.68, 139.76], zoom_start=11)

    # add markers
    for _, row in df.iterrows():
    
            html = f"""
            <div style="width:200px">
                {embed_image(row["photo"])}
                <p style="font-size:12px">{row["caption"]}</p>
            </div>
            """
    
            popup = folium.Popup(html, max_width=250)
    
            folium.Marker(
                [row["lat"], row["lon"]],
                popup=popup,
                tooltip=row["place"],
                icon=folium.Icon(color="red", icon="camera")
            ).add_to(m)
