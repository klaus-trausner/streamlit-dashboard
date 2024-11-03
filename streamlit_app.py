import streamlit as st

# create pages

current_page = st.Page("1_current_data.py", title="Current Data", icon=":material/add_circle:")
charts_page = st.Page("2_charts.py", title="Charts", icon=":material/delete:")
dashboard_page = st.Page("3_dashboard.py", title="Dashboard", icon=":material/delete:")

pg = st.navigation([current_page, charts_page, dashboard_page])
st.set_page_config(page_title="Home Dashboard", page_icon=":material/edit:")
pg.run()


st.title("🎈 My Home Dashboard")
st.image("http://localhost:8501/app/static/haus.jpg")



