import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import base64
import os
from PIL import Image, ExifTags, ImageOps

theme_css = """
<style>
/* Page background */
html, body, [class*="css"]  {
    background-color: #faf7f8 !important;
}

/* Headers */
h1, h2, h3, h4, h5, h6 {
    color: #b3003b !important;
    font-weight: 700 !important;
}

/* Default text */
p, span, div {
    color: #444 !important;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    background-color: #ffd6e0 !important;
    color: #b3003b !important;
    border-radius: 10px 10px 0 0;
    padding: 10px 16px !important;
    font-weight: 600;
}
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    background-color: #ffccd5 !important;
    color: #80002a !important;
}

/* Itinerary cards */
.itinerary-card {
    padding:16px;
    border-radius:12px;
    background-color:#fff0f4;
    border:1px solid #ffd6e0;
    margin-bottom:12px;
}

/* Day label */
.day-label {
    display:inline-block;
    background:#ffccd5;
    color:#b3003b;
    padding:4px 10px;
    border-radius:8px;
    font-weight:600;
    font-size:14px;
    margin-bottom:6px;
}

/* Divider */
hr {
    border: 0;
    height: 1px;
    background: #ffccd5;
    margin: 2rem 0;
}
</style>
"""

st.markdown(theme_css, unsafe_allow_html=True)

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

def open_image_correct_orientation(path):
    img = Image.open(path)

    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break
        exif = img._getexif()
        if exif is not None:
            orientation_value = exif.get(orientation, None)

            if orientation_value == 3:
                img = img.rotate(180, expand=True)
            elif orientation_value == 6:
                img = img.rotate(270, expand=True)
            elif orientation_value == 8:
                img = img.rotate(90, expand=True)
    except Exception as e:
        pass
    return img
    

# main content
st.markdown("""
# 🗺️ 2025 Japan Trip Blog  
### Tokyo • Osaka • Kyoto • Hakone
""")

tab1, tab2, tab3, tab4 = st.tabs(["Map", "Itinerary", "Highlights", "Gallery"])

with tab1:
    places = {
        "place": ["Shinjuku", "Shibuya", "Asakusa", "Akihabara", "Ryogoku", "Ikebukuro", "Odaiba", "Yokohama", "Chiba", "Edogawa", "Chiyoda", "Ueno"],
        "lat": [35.6938, 35.6580, 35.7148, 35.6984, 35.6938, 35.7348, 35.6206, 35.4437, 35.6329, 35.6399, 35.6940, 35.7087],
        "lon": [139.7034, 139.7016, 139.7967, 139.7730, 139.7927, 139.7077, 139.7805, 139.6380, 139.8804, 139.8622, 139.7538, 139.7742],
        "photo": ["img/shinjuku.jpg", "img/shibuya.jpg", "img/asakusa.jpg", "img/akiba.jpg", "img/ryogoku.jpg", "img/ikebukuro.jpg", "img/odaiba.jpg", "img/yokohama.jpg", "img/chiba.jpg", "img/edogawa.jpg", "img/chiyoda.jpg", "img/ueno.jpg"],
        "caption": ["Godzilla Statue", "Shibuya Scramble Building", "Asahi Beer Headquarters", "Kanda Myoujin Shrine", "Former Yasuda Garden", "Shopping in Animate", "Statue of Liberty", "Yamashita Park", "Disneyland", "Tokyo Sea Life Park", "Imperial Palace Gardens", "Ueno Zoo"]
    }

    df = pd.DataFrame(places)

    col1, col2, col3 = st.columns(3)

    metric_style = """
        font-size:16px;
        background-color:#fff5f7;
        padding:18px 20px;
        border-radius:16px;
        border:1px solid #ffd6e0;
        box-shadow:2px 2px 8px rgba(0,0,0,0.05);
        text-align:center;
    """
    
    col1.markdown(f"""
        <div style="{metric_style}">
            <div style="font-size:28px;">🗼</div>
            <div style="font-weight:600; margin-top:4px;">Areas Visited</div>
            <div style="font-size:22px; color:#b3003b;">{df["place"].nunique()}</div>
        </div>
    """, unsafe_allow_html=True)
    
    col2.markdown(f"""
        <div style="{metric_style}">
            <div style="font-size:28px;">📸</div>
            <div style="font-weight:600; margin-top:4px;">Total Photos</div>
            <div style="font-size:22px; color:#b3003b;">518</div>
        </div>
    """, unsafe_allow_html=True)
    
    col3.markdown(f"""
        <div style="{metric_style}">
            <div style="font-size:28px;">📅</div>
            <div style="font-weight:600; margin-top:4px;">Trip Length</div>
            <div style="font-size:22px; color:#b3003b;">12 days</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('######')
    
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
            <div class="itinerary-card">
                <span class="day-label">{stop['day']}</span>
                <h4 style="margin:6px 0 2px 0;">{stop['place']}</h4>
                <p style="font-size:14px;">{stop['notes']}</p>
            </div>
            """, unsafe_allow_html=True)

with tab3:

    # soba place, odaiba at night
    col1, col2 = st.columns([1, 3])
    col1.image('img/skytree.jpg')
    col2.subheader('*1) Asakusa in general*')
    col2.write("""My friend and I stayed at the Hen na Hotel Tawaramachi in Asakusa, and we ended up rearranging our plans more than once just so we could spend extra time in the neighborhood. Our room had an incredible view of the Tokyo Skytree and waking up to that skyline never got old. Honestly, we could see the Skytree from the plane!""")
    col2.write("""Asakusa isn’t as overwhelming as Shibuya or Shinjuku, but that’s exactly what makes it special. It strikes the perfect balance: quiet side streets, cozy cafés, a Don Quixote and Uniqlo for late-night errands, and of course the iconic Senso-ji temple. The whole neighborhood feels charming and lived-in, the kind of place where you can wander without feeling rushed. I could definitely see myself living here one day… in my dreams, at least.""")
    st.divider()
    
    col3, col4 = st.columns([3, 1])
    col4.image('img/jojo.jpg')
    col3.subheader('*2) JOJO World*')
    col3.write("""JoJo’s Bizarre Adventure is my all-time favorite anime, so stumbling upon a whole JOJO World store in Shibuya was a very pleasant surprise, especially since it wasn’t there during my last trip. The space had everything: a merch shop, a themed café, and a few mini-games.""")
    col3.write("""Because I went on Culture Day (rookie mistake), it was incredibly crowded, and I didn’t get to explore as much as I wanted. Still, I managed to grab a Giorno Giovanna shoulder bag as a souvenir, which instantly became one of my favorite purchases from the trip. Maybe next time I’ll treat myself and go all-in on some artwork!""")
    st.divider()
    
    col5, col6 = st.columns([1, 3])
    img = Image.open('img/febcafe.jpg')
    img = ImageOps.exif_transpose(img)
    col5.image(img)
    col6.subheader('*3) February Café*')
    col6.write("""Just a short walk from our hotel in Asakusa was the cutest little spot called February Café, known for its delicious toast. Since my friend and I always got there early, we had our pick between the butter toast set and the cheese toast set. I went with the butter toast both times and honestly, I still think about it in the mornings.""")
    col6.write("""It’s a thick, warm slice of toast layered with butter and syrup, with just the slightest hint of cinnamon. If you’re ever in Asakusa, I definitely recommend making a stop here!""")
    st.divider()

    col7, col8 = st.columns([3, 1])
    col8.image('img/cablecar.jpg')
    col7.subheader('*4) Cable Cars in Yokohama*')
    col7.write("""While exploring Yokohama, my friend and I made our way through Yamashita Park, Chinatown, and World Porters. By the end of the day, we were exhausted and quickly discovered that the nearest train station was nearly a 30-minute walk away. Total devastation (for our feet).""")
    col7.write("""Our saving grace was YOKOHAMA AIR CABIN! It is a cable car system that glides across the Ooka River straight to Sakuragichō Station. We hopped on immediately, and it ended up being one of the most unexpectedly magical moments of the trip. Since it was already dark, the whole landscape was glowing: the Ferris wheel lit up in colors, the Landmark Tower shining over the waterfront, and the reflections shimmering on the river below.""")
    st.divider()
        
    col9, col10 = st.columns([1, 3])
    col9.image('img/photobooth.jpg')
    col10.subheader('*5) Purikura*')
    col10.write("""My friend and I take Korea-style photo booth pictures all the time, so we were very excited to finally try a Japanese purikura machine. And wow, it was crazy.""")
    col10.write("""The booth actually gives you poses to follow, so we were scrambling to keep up while trying not to laugh. Afterward, you get to decorate the photos with stickers, doodles, and effects, which was honestly the best part. We were a little shocked at how much the machine lightened our skin and reshaped our faces, but it just added to the hilarity. Best 500 yen spent!""")
    st.divider()

    col11, col12 = st.columns([3, 1])
    col12.image('img/kimono.jpg')
    col11.subheader('*6) Tea Ceremony + Kimono Rental*')
    col11.write("""I didn’t do a kimono rental during my last trip to Japan, but someone I exchange postcards with recommended MAIKOYA in Asakusa, so my friend and I booked a kimono rental and tea ceremony experience. They offer lots of different packages, but this one felt good for us.""")
    col11.write("""Honestly, the highlight for me wasn’t even the photos or the ceremony — it was chatting with the ladies who helped me put on my kimono. At first they were pretty quiet, but once they realized I could speak Japanese, they opened up and became so talkative and sweet. It made the whole experience feel so personal!""")
    col11.write("""The tea ceremony itself was interesting to sit through, and afterward my friend and I spent time wandering around Senso-ji in our kimonos, taking photos and enjoying the atmosphere. It ended up being one of the most memorable parts of our trip.""")
    st.divider()

    col13, col14 = st.columns([1, 3])
    img = Image.open('img/soba.jpg')
    img = ImageOps.exif_transpose(img)
    col13.image(img)
    col14.subheader('*7) Soba at Kanda Matsuya*')
    col14.write("""Before this trip, my only experience with soba was from a microwavable cup or a quick meal at Haneda Airport, so when my friend and I found ourselves near Akihabara, we decided to try real soba at a restaurant called Kanda Matsuya. There was a bit of a wait, but it was absolutely worth it.""")
    col14.write("""I ordered kitsune soba, which comes topped with a piece of deep-fried tofu, and a drink listed as “soda pop.” The soba was amazing, but the surprise star was the “soda pop,” which turned out to be Mitsuya Cider. It instantly became my new favorite soda. It tastes like a cross between Sprite and ginger ale, but lighter and a little sweeter. Highly recommend trying it if you see it!""")
    st.divider()

    col15, col16 = st.columns([3, 1])
    col16.image('img/liberty.jpg')
    col15.subheader('*8) Odaiba at Night*')
    col15.write("""On our last full day in Japan, my friend and I decided to spend the evening in Odaiba and it ended up being one of the most beautiful nights of the trip. We explored teamLab Planets, wandered through three different shopping malls, and even stopped by the Odaiba Statue of Liberty. But nothing prepared us for how magical the area looks after dark.""")
    col15.write("""As we stepped out of DiverCity, we were immediately met with the massive Gundam statue glowing against the night sky. Then, as we walked toward DECKS, the view opened up to the Rainbow Bridge and a skyline of skyscrapers shimmering across the water. Even the Statue of Liberty replica looked cooler at night, illuminated with the city behind it. We honestly couldn’t stop saying “whoa” as we walked along the waterfront.""")
    st.divider()

    col17, col18 = st.columns([1, 3])
    img = Image.open('img/misc/IMG_1498.jpg')
    img = ImageOps.exif_transpose(img)
    col17.image(img)
    col18.subheader('*9) Mt. Fuji from the Plane*')
    col18.write("""As we were arriving in Japan, I thought it was a little strange that our plane started looping north of Haneda Airport. But then I realized what was happening. The pilots were giving everyone a perfect view of Mt. Fuji! It felt like the best possible welcome to the country.""")
    col18.write("""Seeing the mountain rising behind a sea of buildings was incredible. It’s such a surreal contrast: this massive, snow-topped peak towering behind Tokyo’s dense skyline. Definitely one of the coolest views I’ve ever had from a plane.""")
    st.divider()

    col19, col20 = st.columns([3, 1])
    img = Image.open('img/misc/IMG_1975.jpg')
    img = ImageOps.exif_transpose(img)
    col20.image(img)
    col19.subheader('*10) Going to the Movie Theater*')
    col19.write("""While we were in Japan, Jujutsu Kaisen: Execution came out in theaters. Since it wouldn’t be released in the U.S. for another month, we figured why not watch it here? And honestly, Japanese movie theaters are amazing!""")
    col19.write("""The food prices were so much lower than back home, and we even got little snack trays that attach to the cup holder (10/10 design innovation). At the end of the movie, they handed out a special postcard as a bonus.""")
    col19.write("""I haven’t been keeping up with my Japanese as much lately, but I was proud to understand about 50–60% of the dialogue. Overall, such a fun experience and definitely something I want to do again next time.""")

with tab4:
    folder = "img/misc"
    photos = sorted([p for p in os.listdir(folder) if p.endswith((".jpg",".png",".jpeg"))])
    
    cols = st.columns(2)
    
    for i, p in enumerate(photos):
        img_path = os.path.join(folder, p)  # full path to the image
        img = Image.open(img_path)
        img = ImageOps.exif_transpose(img)
        cols[i % 2].image(img, use_column_width=True)
