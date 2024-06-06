def filter_data(data, year_range, states, crime_types):
    if year_range is not None:
        data = data[(data['year'] >= year_range[0]) & (data['year'] <= year_range[1])]
    if states is not None:
        data = data[data['state'].isin(states)]
    if crime_types is not None:
        data = data[data['crime_type'].isin(crime_types)]
    return data