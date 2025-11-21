import streamlit as st

with st.sidebar:
  col1, col2, col3 = st.columns(3)
  col2.header("My Japan Trip")
  col2.write("*November 1-12, 2025*")
