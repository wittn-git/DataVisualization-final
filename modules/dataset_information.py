import streamlit as st
import pandas as pd

def get_column_df(data):
    column_description = {
        "year": "Year of the statistic.",
        "state": "The state in which the crimes were reported.",
        "crime_type": "The type of crime reported.",
        "count": "The number of cases reported.",
        "count_per_capita": "The number of cases reported per capita."
    }
    column_df = []
    for col in data.columns:
        column_df.append([col, data[col].dtype, column_description[col]])
    return pd.DataFrame(column_df, columns=["Column", "Data Type", "Description"])

def show_dataset_info(data, geo_data):
    st.title("Dataset Information")
    
    num_datapoints = data.shape[0]
    st.subheader("Number of Data Points")
    st.write(num_datapoints)

    st.subheader("Column Information")
    column_df = get_column_df(data)
    st.table(column_df)
    
    st.subheader("Source")
    source = "Crime Data Explorer (CDE) of the FBI's UCR Program"
    source_url = "https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/crime-trend"
    st.markdown(f"[{source}]({source_url})")

    st.subheader("Description")
    description = '''
        The Crime Data Explorer (CDE) provides access to the FBI's crime data, reflecting the constant changes in the nation's crime circumstances. 
        It offers estimated national and state data from the National Incident-Based Reporting System (NIBRS). 
        The CDE represents the FBI's effort to modernize national crime data reporting.
    '''
    st.write(description)
    st.markdown(f"(https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/about)")