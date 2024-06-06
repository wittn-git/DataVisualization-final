import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from modules.filter_data import filter_data

def show_crimetype_correlation_analysis(data, geodata):

    st.title("Crime Type Correlation Analysis")

    year_range = st.slider("Select a Year Range", data['year'].min(), data['year'].max(), (data['year'].min(), data['year'].max()), key="year_corr")
    selected_crime_types = st.multiselect("Select Crime Types", data['crime_type'].unique(), default=data['crime_type'].unique(), key="crimetype_corr")
    selected_state = st.selectbox("Select a State", data['state'].unique(), key="state_corr")

    filtered_data = filter_data(data, year_range, [selected_state], selected_crime_types)
    pivot_table = filtered_data.pivot_table(index='year', columns='crime_type', values='count_per_capita')
    correlation_matrix = pivot_table.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, linewidths=.5)
    plt.title(f"Correlation Matrix of Crime Types in {selected_state}")
    plt.xlabel("Crime Type")
    plt.ylabel("Crime Type")
    st.pyplot(plt.gcf())