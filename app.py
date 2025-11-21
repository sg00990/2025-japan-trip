import streamlit as st


st.set_page_config(
    page_title="2025 Japan Trip Blog",
    page_icon="🇯🇵",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:
  col1, col2, col3 = st.columns([.5, 3, .5])
  col2.header("2025 Tokyo Blog")
  col2.write("*Nov. 1-12, 2025*")
