import streamlit as st

st.set_page_config(page_title="World Cities", page_icon="🌍", layout="wide")

st.title("🌍 World Cities")

st.markdown("""
Welcome to the **World Cities Streamlit App**!

This application provides information and insights about cities around the world.
Explore different cities, their characteristics, and discover interesting facts.

---
""")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🚀 Explore Cities", use_container_width=True, key="explore_btn"):
        st.switch_page("pages/app.py")

st.markdown("""
---

### Features
- 🔍 Search and explore world cities
- 📊 View city statistics and information
- 🗺️ Discover unique characteristics of different regions

Navigate to the Cities page using the button above to get started!
""")
