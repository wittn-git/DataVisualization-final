import pandas as pd

crime_mapping = {
    "violent_crime": "Violent Crime",
    "homicide": "Homicide",
    "rape": "Rape",
    "robbery": "Robbery",
    "aggravated_assault": "Aggravated Assault",
    "property_crime": "Property Crime",
    "burglary": "Burglary",
    "larceny": "Larceny",
    "motor_vehicle_theft": "Motor Vehicle Theft"
}

if __name__ == "__main__":
    
    data = pd.read_csv("data/estimated_crimes_1979_2022.csv")
    data['state_name'].fillna('United States Total', inplace=True)
    data.drop(columns=['caveats', 'state_abbr'], inplace=True)
    
    crime_types = data.columns[3:]
    new_rows = []
    for _, row in data.iterrows():
        for crime in crime_types:
            crime_new = crime
            if crime == "rape_legacy" or crime == "rape_revised":
                crime_new = "rape"
            if pd.notna(row[crime]):
                new_rows.append([row['year'], row['state_name'], crime_new, row[crime], row[crime]/row['population']])

    data = pd.DataFrame(new_rows, columns=['year', 'state', 'crime_type', 'count', "count_per_capita"])
    
    data_types = [int, str, str, int, float]
    data = data.astype(dict(zip(data.columns, data_types)))
    
    data['crime_type'] = data['crime_type'].apply(lambda x: crime_mapping[x] if x in crime_mapping else x)
    data.to_csv("data/processed_data.csv", index=False)