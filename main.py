import streamlit as st
import pandas as pd
import geopandas as gpd
from modules.spatial_analysis import show_spatial_analysis
from modules.temporal_analysis import show_temporal_analysis
from modules.dataset_information import show_dataset_info
from modules.crimetype_distribution_analysis import show_crimetype_distribution_analysis
from modules.crimetype_correlation_analysis import show_crimetype_correlation_analysis
from modules.temporal_spatial_analysis import show_temporal_spatial_analysis

def build_navbar():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", 
                                [
                                    "Dataset Information", 
                                    "Temporal Analysis", 
                                    "Spatial Analysis", 
                                    "Temporal-Spatial Analysis",
                                    "Crime Type Distribution Analysis",
                                    "Crime Type Correlation Analysis"
                                ]
                            )
    return page

@st.cache_data
def load_data():
    data = pd.read_csv('data/processed_data.csv')
    geo_data = gpd.read_file('data/USA.geo.json')
    return data, geo_data

if __name__ == "__main__":
    
    data, geo_data = load_data()

    page = build_navbar()

    page_mapping = {
        "Dataset Information": show_dataset_info,
        "Temporal Analysis": show_temporal_analysis,
        "Spatial Analysis": show_spatial_analysis,
        "Temporal-Spatial Analysis": show_temporal_spatial_analysis,
        "Crime Type Distribution Analysis": show_crimetype_distribution_analysis,
        "Crime Type Correlation Analysis": show_crimetype_correlation_analysis
    }

    page_mapping[page](data, geo_data)