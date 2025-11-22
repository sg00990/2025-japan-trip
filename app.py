import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import base64

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
        "photo": ["img/shinjuku.jpg", "img/shibuya.jpg", "img/asakusa.jpg", "img/akiba.jpg", "img/ryogoku.jpg", "img/ikebukuro.jpg", "img/odaiba.jpg", "img/yokohama.jpg", "img/chiba.jpg", "img/edogawa.jpg", "img/chiyoda.jpg", "img/ueno.jpg"],
        "caption": ["Godzilla Statue", "Shibuya Scramble Building", "Asahi Beer Headquarters", "Kanda Shrine", "Former Yasuda Garden", "Shopping in Animate", "Statue of Liberty", "Yamashita Park", "Disneyland", "Tokyo Sea Life Park", "Imperial Palace Gardens", "Ueno Zoo"]
    }

    df = pd.DataFrame(places)
    # center map on Tokyo
    m = folium.Map(location=[35.68, 139.76], zoom_start=11)

    # add markers
    for _, row in df.iterrows():
    
            html = f"""
            <div style="width:200px">
                {embed_image(row["photo"])}
                <p style="font-size:12px">{row['caption']}</p>
            </div>
            """
    
            popup = folium.Popup(html, max_width=250)
    
            folium.Marker(
                [row["lat"], row["lon"]],
                popup=popup,
                tooltip=row["place"],
                icon=folium.Icon(color="red", icon="camera")
            ).add_to(m)
    st_folium(m, use_container_width=True)

with tab2:
    itinerary = [
        {"day": "Day 1 — Nov 1", "place": "Atlanta", "notes": "Flights (ATL->LAX, LAX->HND)"},
        {"day": "Day 2 — Nov 2", "place": "Asakusa", "notes": "Check-in to hotel, grab dinner at Family Mart"},
        {"day": "Day 3 — Nov 3", "place": "Shibuya", "notes": "Shibuya Scramble Crossing, get glasses at JINS, shopping"},
        {"day": "Day 4 - Nov 4", "place": "Chiba", "notes": "Tokyo Sea Life Park, Tokyo Disneyland"},
        {"day": "Day 5 - Nov 5", "place": "Yokohama", "notes": "Yamashita Park, Chinatown, World Porters, cable cars to the station"},
        {"day": "Day 6 - Nov 6", "place": "Asakusa", "notes": "Tea ceremony, wear kimonos, Senso-ji, eat some melon bread"},
        {"day": "Day 7 - Nov 7", "place": "Ikebukuro", "notes": "Largest Animate in Ikebukuro, revisit Shibuya"},
        {"day": "Day 8 - Nov 8", "place": "Chiyoda", "notes": "Imperial Palace East National Gardens, Kanda Myoujin Shrine, Jimbocho, JJK movie at TOHO Ueno"},
        {"day": "Day 9 - Nov 9", "place": "Shinjuku", "notes": "Koreatown, see the Godzilla statue, Harajuku, eat crepes"},
        {"day": "Day 10 - Nov 10", "place": "Asakusa", "notes": "Nakemise Shopping Street, Former Yasuda Garden, Sumo Museum"},
        {"day": "Day 11 - Nov 11", "place": "Odaiba", "notes": "teamLab Planets, Unicorn Gundam, DECKS, Diver City, Aqua City, Statue of Liberty"},
        {"day": "Day 12 - Nov 12", "place": "Ueno", "notes": "Check out of hotel, Ueno Zoo, Ueno Park, Haneda airport (HND->ATL)"}
    ]
    
    for stop in itinerary:
        with st.container():
            st.markdown(f"""
            <div style="
                padding:16px;
                border-radius:12px;
                background-color:#f8f8f8;
                margin-bottom:12px;
            ">
                <!-- Date pill -->
                <span style="
                    display:inline-block;
                    background:#ffccd5;
                    color:#b3003b;
                    padding:4px 10px;
                    border-radius:8px;
                    font-weight:600;
                    font-size:14px;
                    margin-bottom:6px;
                ">
                    {stop['day']}
                </span>
            
                <!-- Place name -->
                <h4 style="margin:6px 0 2px 0; color:#333333;">{stop['place']}</h4>
            
                <!-- Notes -->
                <p style="font-size:14px; color:#555555;">{stop['notes']}</p>
            </div>
            """, unsafe_allow_html=True)
