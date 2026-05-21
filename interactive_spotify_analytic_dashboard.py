# spotify_dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data
data = {
    "Artist": ["Drake", "Taylor Swift", "Weeknd", "Travis Scott"],
    "Streams": [120, 150, 90, 110]
}

df = pd.DataFrame(data)

st.title("Spotify Analytics Dashboard")

fig = px.bar(
    df,
    x="Artist",
    y="Streams",
    color="Artist"
)

st.plotly_chart(fig)
