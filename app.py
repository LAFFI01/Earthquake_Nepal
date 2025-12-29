import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# ------------------------------
# Load data
# ------------------------------
df = pd.read_csv("02_EDA/earthquake_Nepal_EDA_AFTER.csv")
df['date_ad'] = pd.to_datetime(df['date_ad'], errors='coerce')
df['year'] = df['date_ad'].dt.year

# Categorize magnitude
df['category'] = pd.cut(df['magnitude'], bins=[-float('inf'),5,6,float('inf')],
                        labels=['green','orange','red'])

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.title("Filters")
selected_year = st.sidebar.selectbox("Select Year", options=sorted(df['year'].dropna().unique()))
selected_mag = st.sidebar.slider("Select Magnitude Range", 0.0, df['magnitude'].max(), (0.0, df['magnitude'].max()))

# Filter data
filtered_df = df[(df['year'] == selected_year) &
                 (df['magnitude'] >= selected_mag[0]) &
                 (df['magnitude'] <= selected_mag[1])]

# ------------------------------
# Main page
# ------------------------------
st.title("🌏 Nepal Earthquakes Dashboard")
st.write(f"Showing {len(filtered_df)} earthquakes for year {selected_year}")

# ------------------------------
# EDA: Histogram
# ------------------------------
st.subheader("Magnitude Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_df['magnitude'], bins=10, kde=True, ax=ax)
st.pyplot(fig)

# ------------------------------
# EDA: Bar chart by category
# ------------------------------
st.subheader("Earthquake Count by Magnitude Category")
cat_counts = filtered_df['category'].value_counts()
fig2, ax2 = plt.subplots()
sns.barplot(x=cat_counts.index, y=cat_counts.values, palette=['green','orange','red'], ax=ax2)
for i, v in enumerate(cat_counts.values):
    ax2.text(i, v+0.2, str(v), ha='center', fontweight='bold')
st.pyplot(fig2)

# ------------------------------
# Map
# ------------------------------
st.subheader("Earthquake Map")
m = folium.Map(location=[28.2,84.0], zoom_start=7)
cluster = MarkerCluster().add_to(m)
for _, row in filtered_df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=max(4, row['magnitude']*2),
        color='green' if row['category']=='green' else 'orange' if row['category']=='orange' else 'red',
        fill=True,
        fill_opacity=0.7,
        popup=f"Epicenter: {row['epicenter']}<br>Magnitude: {row['magnitude']}<br>Date: {row['ad_date'].date()}"
    ).add_to(cluster)
st_data = st_folium(m, width=700)


