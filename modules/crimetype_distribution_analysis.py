import streamlit as st
import plotly.express as px
from modules.filter_data import filter_data

def show_crimetype_distribution(data):

    st.subheader("Crime Type Distribution")

    year_range = st.slider("Select a Year Range", data['year'].min(), data['year'].max(), (data['year'].min(), data['year'].max()), key="year_dist")
    state = st.selectbox("Select a State", data['state'].unique())
    selected_crime_types = st.multiselect("Select Crime Types", data['crime_type'].unique(), default=data['crime_type'].unique(), key="crimetype_dist")

    filtered_data = filter_data(data, year_range, [state], selected_crime_types)
    fig = px.bar(filtered_data, x='crime_type', y='count', title=f"Crime Cases by Type in {state}")
    fig.update_layout(xaxis_title="Crime Type", yaxis_title="Number of Cases")
    st.plotly_chart(fig)

    fig = px.pie(filtered_data, values='count', names='crime_type')
    fig.update_layout(legend_title="Crime Type")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig)

def show_crimetype_distribution_by_state(data, per_capita=False):

    

    year_range = st.slider("Select a Year Range", data['year'].min(), data['year'].max(), (data['year'].min(), data['year'].max()), key="year_dist_state" + ("_per_capita" if per_capita else ""))
    selected_states = st.multiselect("Select States", data['state'].unique(), default=["United States Total"], key="state_dist_state" + ("_per_capita" if per_capita else ""))
    selected_crime_types = st.multiselect("Select Crime Types", data['crime_type'].unique(), default=data['crime_type'].unique(), key="crimetype_dist_state" + ("_per_capita" if per_capita else ""))

    filtered_data = filter_data(data, year_range, selected_states, selected_crime_types)
    fig = px.bar(filtered_data, x='state', y='count' + ("_per_capita" if per_capita else ""), color='crime_type', title=f"Crime Cases by State {'Per Capita' if per_capita else ''}")
    fig.update_layout(legend_title="Crime Type")
    fig.update_layout(xaxis_title="State", yaxis_title=f"Number of Cases {'Per Capita' if per_capita else ''}")
    st.plotly_chart(fig)

def show_crimetype_distribution_analysis(data, geo_data):
    st.title("Crime Type Analysis")
    show_crimetype_distribution(data)

    subheader_placeholder = st.empty()
    per_capita = st.checkbox("Show Per Capita", value=False)
    subheader_placeholder.subheader(f"Crime Type Distribution Comparison by State {'Per Capita' if per_capita else ''}")
    show_crimetype_distribution_by_state(data, per_capita)