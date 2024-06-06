import streamlit as st
import plotly.express as px
from modules.filter_data import filter_data

def show_comparison_by_state(data):

    st.subheader("Comparison by State")
    
    per_capita = st.checkbox("Show Per Capita", value=False)
    selected_states = st.multiselect("Select States", data['state'].unique(), default=["United States Total"])
    year_range = st.slider("Select a Year Range", data['year'].min(), data['year'].max(), (data['year'].min(), data['year'].max()), key="year_state_comp")
    crime_type = st.selectbox("Select a Crime Type", data['crime_type'].unique())

    filtered_data = filter_data(data, year_range, selected_states, [crime_type])
    fig = px.line(filtered_data, x='year', y='count' if not per_capita else 'count_per_capita', color='state', title=f"Crime Cases by State")
    fig.update_layout(xaxis_title="Year", yaxis_title=f"Cases of {crime_type}" if not per_capita else f"Cases of {crime_type} Per Capita")
    fig.update_layout(legend_title="State")
    st.plotly_chart(fig)

def show_comparison_by_crime_type(data):
    st.subheader("Comparison by Crime Type")

    per_capita = st.checkbox("Show Per Capita", value=False)
    selected_crime_types = st.multiselect("Select Crime Types", data['crime_type'].unique(), default=["Violent Crime"])
    year_range = st.slider("Select a Year Range", data['year'].min(), data['year'].max(), (data['year'].min(), data['year'].max()), key="year_crime_comp")
    state = st.selectbox("Select a State", data['state'].unique())
    
    filtered_data = filter_data(data, year_range, [state], selected_crime_types)
    fig = px.line(filtered_data, x='year', y='count' if not per_capita else 'count_per_capita', color='crime_type', title=f"Crime Cases by Type")
    fig.update_layout(xaxis_title="Year", yaxis_title="Number of Cases" if not per_capita else "Number of Cases Per Capita")
    fig.update_layout(legend_title="Crime Type")
    st.plotly_chart(fig)

def show_temporal_analysis(data, geo_data):
    st.title("Temporal Analysis")
    show_comparison_by_state(data)
    show_comparison_by_crime_type(data)