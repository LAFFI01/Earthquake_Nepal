import streamlit as st 

Home_page = st.Page('pages/overview.py',title="EQ-Nepal")
EQ_danger_level = st.Page('pages/Earthquake_danger_level.py',title="EQ_Danger_level")
pg = st.navigation([Home_page,EQ_danger_level])
pg.run()