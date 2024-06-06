import streamlit as st
import plotly.express as px
from modules.filter_data import filter_data

def show_map(data, geo_data, column_name, key, per_capita=False):
    
    crime_type = st.selectbox("Select a Crime Type", data['crime_type'].unique(), key=key + "_crime")
    year = st.slider("Select a Year", data['year'].min(), data['year'].max(), data['year'].max(), key=key + "_year")

    filtered_data = filter_data(data, (year, year), None, [crime_type])
    merged_data = geo_data.merge(filtered_data, left_on='name', right_on='state', how='left')
    fig = px.choropleth(merged_data, geojson=merged_data.geometry, locations=merged_data.index, color=column_name, hover_name='name', title=f"{crime_type} Cases {'Per Capita' if per_capita else ''} in {year}", color_continuous_scale='Viridis')
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(coloraxis_colorbar=dict(title=f"Number of Cases {'Per Capita' if per_capita else ''}"))
    st.plotly_chart(fig)

def show_map_per_capita(data, geo_data):
    st.subheader("Comparison by Case Per Capita")
    show_map(data, geo_data, 'count_per_capita', 'per_capita', True)

def show_map_total(data, geo_data):
    st.subheader("Comparison by Total Cases")
    show_map(data, geo_data, 'count', 'total')

def show_spatial_analysis(data, geo_data):
    st.title("Spatial Analysis")    
    per_capita = st.checkbox("Show Per Capita", value=False)
    if per_capita:
        show_map_per_capita(data, geo_data)
    else:
        show_map_total(data, geo_data)