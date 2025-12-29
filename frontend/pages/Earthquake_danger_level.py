import streamlit as st
from datetime import datetime
import requests




st.header("Earthquake Danger Level")
col1, col2 = st.columns(2)

with col1:
    # Latitude: -90 to 90
    lat = st.number_input("Latitude", min_value=-90.0, max_value=90.0, value=27.7, format="%.4f")
    # Year: From historic data to current
    year = st.number_input("Year", min_value=1900, max_value=2100, value=2024)

with col2:
    # Longitude: -180 to 180
    lon = st.number_input("Longitude", min_value=-180.0, max_value=180.0, value=85.3, format="%.4f")
    # Month: 1 to 12
    month = st.slider("Month", min_value=1, max_value=12, value=1)

# Hour: 0 to 23
hour = st.select_slider("Hour of Day", options=list(range(24)), value=12)

# Display the captured data
st.info(f"Target Location: {lat}, {lon} at {hour}:00, Month: {month}, Year: {year}")

if st.button("Submit"):
    param = {
        "lat": lat,
        "lon": lon,
        "hour": hour,
        "month": month,
        "year": year
    }

    response = requests.post("http://localhost:8000/predict_Danger_level", params=param)
    if response.status_code == 200:
        result = response.json()
        st.metric("Predicted Risk level",result['prediction'])
    else:
        st.error("Failed to connect to the Backend.")

import streamlit.components.v1 as components

# Load your HTML file
with open("02_EDA/nepal_earthquakes_map.html", 'r', encoding='utf-8') as f:
    html_data = f.read()

st.title("Nepal_Earthquake map")

# Inject the HTML into the app
components.html(html_data, height=600, scrolling=True)