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
        "caption": ["Godzilla Statue", "Shibuya Scramble Building", "Asahi Beer Headquarters", "Kanda Myoujin Shrine", "Former Yasuda Garden", "Shopping in Animate", "Statue of Liberty", "Yamashita Park", "Disneyland", "Tokyo Sea Life Park", "Imperial Palace Gardens", "Ueno Zoo"]
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
        {"day": "Day 4 - Nov 4", "place": "Edogawa/Chiba", "notes": "Tokyo Sea Life Park, Tokyo Disneyland"},
        {"day": "Day 5 - Nov 5", "place": "Yokohama", "notes": "Yamashita Park, Chinatown, World Porters, cable cars to the station"},
        {"day": "Day 6 - Nov 6", "place": "Asakusa", "notes": "Tea ceremony, wear kimonos, Senso-ji, eat some melon bread"},
        {"day": "Day 7 - Nov 7", "place": "Ikebukuro/Shibuya", "notes": "Largest Animate in Ikebukuro, revisit Shibuya"},
        {"day": "Day 8 - Nov 8", "place": "Chiyoda/Ueno", "notes": "Imperial Palace East National Gardens, Kanda Myoujin Shrine, Jimbocho, JJK movie at TOHO Ueno"},
        {"day": "Day 9 - Nov 9", "place": "Shinjuku/Shibuya", "notes": "Koreatown, see the Godzilla statue, Harajuku, eat crepes"},
        {"day": "Day 10 - Nov 10", "place": "Asakusa/Ryogoku", "notes": "Nakamise Shopping Street, Former Yasuda Garden, Sumo Museum"},
        {"day": "Day 11 - Nov 11", "place": "Odaiba", "notes": "teamLab Planets, Unicorn Gundam, DECKS, Diver City, Aqua City, Statue of Liberty"},
        {"day": "Day 12 - Nov 12", "place": "Asakusa, Ueno", "notes": "Check out of hotel, last shopping in Asakusa, Ueno Zoo, Ueno Park, Haneda airport (HND->ATL)"}
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
                <h4 style="margin:6px 0 2px 0; color:#333333;">{stop['place']}</h4>
                <p style="font-size:14px; color:#555;">{stop['notes']}</p>
            </div>
            """, unsafe_allow_html=True)

with tab3:

    # jojo store, february cafe, yokohama cable car, photobooth, kimono, soba place, odaiba at night, asakusa in general
    col1, col2 = st.columns([1, 3])
    col1.image('img/skytree.jpg')
    col2.subheader('*1) Asakusa in general*')
    col2.write("""My friend and I stayed at the Hen na Hotel Tawaramachi in Asakusa, and we ended up rearranging our plans more than once just so we could spend extra time in the neighborhood. Our room had an incredible view of the Tokyo Skytree and waking up to that skyline never got old. Honestly, we could see the Skytree from the plane!""")
    col2.write("""Asakusa isn’t as overwhelming as Shibuya or Shinjuku, but that’s exactly what makes it special. It strikes the perfect balance: quiet side streets, cozy cafés, a Don Quixote and Uniqlo for late-night errands, and of course the iconic Senso-ji temple. The whole neighborhood feels charming and lived-in, the kind of place where you can wander without feeling rushed. I could definitely see myself living here one day… in my dreams, at least.""")

    col3, col4 = st.columns([3, 1])
    col4.image('img/jojo.jpg')
    col3.write("""JoJo’s Bizarre Adventure is my all-time favorite anime, so stumbling upon a whole JOJO World store in Shibuya was a very pleasant surprise, especially since it wasn’t there during my last trip. The space had everything: a merch shop, a themed café, and a few mini-games.""")
    col3.write("""Because I went on Culture Day (rookie mistake), it was incredibly crowded, and I didn’t get to explore as much as I wanted. Still, I managed to grab a Giorno Giovanna shoulder bag as a souvenir, which instantly became one of my favorite purchases from the trip. Maybe next time I’ll treat myself and go all-in on some artwork!""")
    
