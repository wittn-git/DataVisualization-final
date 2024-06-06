import streamlit as st
from modules.filter_data import filter_data
import plotly.express as px
import time

def animation(yearly_data, animation_speed, per_capita, selected_crime_type, min_value, max_value):
    fig_placeholder = st.empty()
    for year, data in yearly_data.items():
        if not st.session_state["animation_running"]:
            break
        fig = px.choropleth(data, geojson=data.geometry, locations=data.index, color='count_per_capita' if per_capita else 'count', hover_name='name', title=f"{selected_crime_type} Cases {'Per Capita' if per_capita else ''} in {year}", color_continuous_scale='Viridis', range_color=(min_value, max_value))
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(coloraxis_colorbar=dict(title=f"Number of Cases {'Per Capita' if per_capita else ''}"))
        fig_placeholder.plotly_chart(fig)
        time.sleep(animation_speed)

def show_temporal_spatial_analysis(data, geo_data):
    st.title("Temporal-Spatial Analysis")

    per_capita = st.checkbox("Per Capita", value=False)

    year_range = st.slider("Select a Year Range", data['year'].min(), data['year'].max(), (data['year'].min(), data['year'].max()), key="year_temporal_spatial" + ("_per_capita" if per_capita else ""))
    selected_crime_type = st.selectbox("Select a Crime Type", data['crime_type'].unique(), key="crimetype_temporal_spatial" + ("_per_capita" if per_capita else ""))
    animation_speed = st.slider("Animation Speed (seconds)", 0.5, 5.0, 1.5)
    filtered_data = filter_data(data, year_range, None, [selected_crime_type])

    yearly_data = {}
    for year in range(year_range[0], year_range[1] + 1):
        year_filter_data = filtered_data[filtered_data['year'] == year]
        yearly_data[year] = geo_data.merge(year_filter_data, left_on='name', right_on='state', how='left')
    
    min_value = min([data['count_per_capita'].min() if per_capita else data['count'].min() for data in yearly_data.values()])
    max_value = max([data['count_per_capita'].max() if per_capita else data['count'].max() for data in yearly_data.values()])

    st.session_state["animation_running"] = False

    col1, col2 = st.columns([1, 1])
    with col1:
        button_value_start = st.button("Start Animation")
    with col2:
        button_value_stop = st.button("Stop Animation")

    if button_value_start:
        st.session_state["animation_running"] = True
        animation(yearly_data, animation_speed, per_capita, selected_crime_type, min_value, max_value)
    
    if button_value_stop:
        st.session_state["animation_running"] = False
    
    if button_value_start or button_value_stop:
        st.experimental_rerun()

    st.experimental_set_query_params(**st.experimental_get_query_params())