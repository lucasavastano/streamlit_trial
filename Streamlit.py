#!/usr/bin/env python
# coding: utf-8

# pip install streamlit

# In[1]:


import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from scipy.interpolate import griddata
import json

Segrate_Parco_Natura = pd.read_csv('Segrate_Parco_Natura.csv').assign(location='Parco_Natura', lat=45.46288, lon=9.29905)
Segrate_Capolinea_autobus = pd.read_csv('Segrate_Capolinea_autobus.csv').assign(location='Capolinea_autobus', lat=45.49923, lon=9.29323)
Segrate_Ponte_Rovagnasco = pd.read_csv('Segrate_Ponte_Rovagnasco.csv').assign(location='Ponte_Rovagnasco', lat=45.49619, lon=9.28812)
Segrate_Centro = pd.read_csv('Segrate_Centro.csv').assign(location='Centro', lat=45.49176, lon=9.29414)
Segrate_Milano_2 = pd.read_csv('Segrate_Milano_2.csv').assign(location='Milano_2',lat=45.50144, lon=9.26828)
Segrate_Redecesio = pd.read_csv('Segrate_Redecesio.csv').assign(location='Redecesio', lat=45.48266, lon=9.26993) 
Segrate_Stazione = pd.read_csv('Segrate_Stazione.csv').assign(location='Stazione', lat=45.48081, lon=9.29872) 
Segrate_Novegro = pd.read_csv('Segrate_Novegro.csv').assign(location='Novegro', lat=45.47384, lon=9.28438) 
Segrate_Spazio_pubblico_Rovagnasco = pd.read_csv('Segrate_Spazio_pubblico_Rovagnasco.csv').assign(location='Spazio_pubblico_Rovagnasco', lat=45.49955, lon=9.28508)
Segrate_Scuola_Rovagnasco = pd.read_csv('Segrate_Scuola_Rovagnasco.csv').assign(location='Scuola_Rovagnasco', lat=45.49779, lon=9.28667)
Segrate_Piazza_centrale = pd.read_csv('Segrate_Piazza_centrale.csv').assign(location='Piazza_centrale', lat=45.490825, lon=9.293608)
Segrate_Centro_parco_1 = pd.read_csv('Segrate_Centro_parco_1.csv').assign(location='Centro_parco_1', lat=45.4904, lon=9.2885)
Segrate_Centro_parco_2 = pd.read_csv('Segrate_Centro_parco_2.csv').assign(location='Centro_parco_2', lat=45.49013,lon=9.2871)
Segrate_Centro_parco_3 = pd.read_csv('Segrate_Centro_parco_3.csv').assign(location='Centro_parco_3', lat=45.48853,lon=9.2752)
Segrate_Rotatoria = pd.read_csv('Segrate_Rotatoria.csv').assign(location='Rotatoria', lat=45.48915, lon=9.26241)
Segrate_Sud_Milano_2 = pd.read_csv('Segrate_Sud_Milano_2.csv').assign(location='Sud_Milano_2', lat=45.49022, lon=9.2621)
Segrate_Milano_2_CAMPO_CALCIO = pd.read_csv('Segrate_Milano_2_CAMPO_CALCIO.csv').assign(location='Milano_2_CAMPO_CALCIO', lat=45.49739, lon=9.26544)
Segrate_Laghetto_Milano_2 = pd.read_csv('Segrate_Laghetto_Milano_2.csv').assign(location='Laghetto_Milano_2', lat=45.50099, lon=9.26734)
Segrate_Redecesio_scalo_FS = pd.read_csv('Segrate_Redecesio_scalo_FS.csv').assign(location='Redecesio_scalo_FS', lat=45.47873, lon=9.2768)
Segrate_San_Felice= pd.read_csv('Segrate_San_Felice.csv').assign(location='San_Felice', lat=45.47334, lon=9.30668)
Segrate_Idroscalo = pd.read_csv('Segrate_Idroscalo.csv').assign(location='Idroscalo', lat=45.46595, lon=9.2872)
Segrate_Centro_civico_Novegro = pd.read_csv('Segrate_Centro_civico_Novegro.csv').assign(location='Centro_civico_Novegro', lat=45.47304, lon=9.28391)
Segrate_Pizzeria_3_Piramidi = pd.read_csv('Segrate_Pizzeria_3_Piramidi.csv').assign(location='Pizzeria_3_Piramidi', lat=45.4895, lon=9.2659)
Segrate_Pensilina_ingresso_est_Cassanese= pd.read_csv('Segrate_Pensilina_ingresso_est_Cassanese.csv').assign(location='Pensilina_ingresso_est_Cassanese', lat=45.49781, lon=9.30007)
Segrate_Ponte_ciclopedonale_Rivoltana= pd.read_csv('Segrate_Ponte_ciclopedonale_Rivoltana.csv').assign(location='Ponte_ciclopedonale_Rivoltana', lat=45.47718, lon=9.29982)
Segrate_Comune = pd.read_csv('Segrate_Comune.csv').assign(location='Comune', lat=45.48951, lon=9.2925)
Segrate_Rotatoria_commercial_district = pd.read_csv('Segrate_Rotatoria_commercial_district.csv').assign(location='Rotatoria_commercial_district', lat=45.4858, lon=9.26299)
Segrate_Centro_civico_Redecesio= pd.read_csv('Segrate_Centro_civico_Redecesio.csv').assign(location='Centro_civico_Redecesio', lat=45.480782, lon=9.270980)
Segrate_Centro_sede_PD = pd.read_csv('Segrate_Centro_sede_PD.csv').assign(location='Centro_sede_PD', lat=45.49328, lon=9.29557)
Segrate_Ingresso_Nord_Segrate_centro = pd.read_csv('Segrate_Ingresso_Nord_Segrate_centro.csv').assign(location='Ingresso_Nord_Segrate_centro', lat=45.49678, lon=9.29406)

def melt_df(df):
    return df.melt(id_vars=['time', 'lat', 'lon', 'location'], var_name='measurement', value_name='value')

melted_dfs = [melt_df(df) for df in [Segrate_Parco_Natura, 
                                     Segrate_Capolinea_autobus, 
                                     Segrate_Ponte_Rovagnasco, 
                                     Segrate_Centro,
                                     Segrate_Milano_2,
                                     Segrate_Redecesio,
                                     Segrate_Stazione,
                                     Segrate_Novegro,
                                     Segrate_Spazio_pubblico_Rovagnasco,
                                     Segrate_Scuola_Rovagnasco,
                                     Segrate_Piazza_centrale,
                                     Segrate_Centro_parco_1,
                                     Segrate_Centro_parco_2,
                                     Segrate_Centro_parco_3,
                                     Segrate_Rotatoria,
                                     Segrate_Sud_Milano_2,
                                     Segrate_Milano_2_CAMPO_CALCIO,
                                     Segrate_Laghetto_Milano_2,
                                     Segrate_Redecesio_scalo_FS,
                                     Segrate_San_Felice,
                                     Segrate_Idroscalo,
                                     Segrate_Centro_civico_Novegro,
                                     Segrate_Pizzeria_3_Piramidi,
                                     Segrate_Pensilina_ingresso_est_Cassanese,
                                     Segrate_Ponte_ciclopedonale_Rivoltana,
                                     Segrate_Comune,
                                     Segrate_Rotatoria_commercial_district,
                                     Segrate_Centro_civico_Redecesio,
                                     Segrate_Centro_sede_PD,
                                     Segrate_Ingresso_Nord_Segrate_centro
                                     ]
             ]

# Concatenate melted dataframes
combined_df = pd.concat(melted_dfs, ignore_index=True)
combined_df['time'] = pd.to_datetime(combined_df['time']).dt.floor('h')

# Separate dataframes for each measurement
df_CO2 = combined_df[combined_df['measurement'] == 'CO2_SCD4x']
df_PM25 = combined_df[combined_df['measurement'] == 'PM_2p5']
df_PM10 = combined_df[combined_df['measurement'] == 'PM_10p0']
df_Temp = combined_df[combined_df['measurement'] == 'TEMP_SHT40']

# Funzione per normalizzare i valori della scala di colori
def normalize_color_scale(color_scale):
    min_val = color_scale[0][0]
    max_val = color_scale[-1][0]
    normalized_scale = [(float(value - min_val) / (max_val - min_val), color) for value, color in color_scale]
    return normalized_scale

# Mappa delle scale di colori per ogni tipo di misurazione 
color_scales = {
    'CO2': [
        [200, "#ffba08"], [400, "#faa307"], [600, "#e85d04"], [800, "#dc2f02"], [1000, "#d00000"], [1200, "#9d0208"],
        [1500, "#6a040f"], [1800, "#03071e"]  
           
    ],
    'PM2.5': [
        [5, "#ffba08"], [20, "#faa307"], [30, "#e85d04"], [40, "#dc2f02"], [50, "#d00000"], [60, "#9d0208"],
        [70, "#6a040f"], [100, "#03071e"]  
    ],
    'PM10': [
        [5, "#ffba08"], [20, "#faa307"], [30, "#e85d04"], [40, "#dc2f02"], [50, "#d00000"], [60, "#9d0208"],
        [70, "#6a040f"], [100, "#03071e"]
    ],
    'Temperature': [
        [-5, "#ffba08"], [0, "#faa307"], [5, "#e85d04"], [10, "#dc2f02"], [15, "#d00000"], [20, "#9d0208"],
        [30, "#6a040f"], [40, "#03071e"]  
    ],
}

normalized_color_scales = {key: normalize_color_scale(value) for key, value in color_scales.items()}


z_limits = {
    'CO2': {'zmin': 0, 'zmax': 1800},
    'PM2.5': {'zmin': 0, 'zmax': 100},
    'PM10': {'zmin': 0, 'zmax': 100},
    'Temperature': {'zmin': 0, 'zmax': 40},
}

# Load geojson
with open('sensor_locations.geojson') as f:
    geojson_data = json.load(f)
    
unique_times = df_CO2['time'].unique()
timestamps = sorted(pd.to_datetime(unique_times))
slider_marks = {0: {'label': timestamps[0].strftime('%Y-%m-%d %H:%M')}}

# Streamlit UI
st.title('Sensor Data Visualization')

# Measurement type selector
measurement = st.selectbox(
    "Select Measurement Type:",
    ["CO2", "PM2.5", "PM10", "Temperature"],
    index=0
)

# Assuming you have a timestamps list
timestamps = pd.date_range(start='2023-11-27', periods=100, freq='h')
selected_time = st.select_slider(
    "Select Time:",
    options=timestamps,
    format_func=lambda x: x.strftime('%Y-%m-%d %H:%M')
)

# Function to filter your data based on the selected time and measurement type
def filter_data(measurement, selected_time):
    # Your filtering logic here
    # Example return statement, replace with actual filtering
    return pd.DataFrame({
        'lat': np.random.uniform(45.4, 45.5, size=100),
        'lon': np.random.uniform(9.2, 9.3, size=100),
        'value': np.random.uniform(0, 100, size=100),
    })

filtered_data = filter_data(measurement, selected_time)

# Function to create and display the map
def display_map(df, measurement):
    fig = go.Figure(go.Scattermapbox(
        lat=df['lat'],
        lon=df['lon'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9,
            color=df['value'],  # Example coloring by value
            colorscale=normalized_color_scales.get(measurement, "Viridis"),  # Fallback to Viridis
            showscale=True,
        ),
        text=df['value'],
    ))

    # Note: No Mapbox access token is set here, so it uses Plotly's default public token
    fig.update_layout(
        mapbox_style="light",
        mapbox_zoom=10,
        mapbox_center={"lat": df['lat'].mean(), "lon": df['lon'].mean()}
    )

    st.plotly_chart(fig, use_container_width=True)

# Display the map
display_map(filtered_data, measurement)

