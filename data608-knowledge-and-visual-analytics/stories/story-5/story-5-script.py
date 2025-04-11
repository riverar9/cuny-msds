# %%
# imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
from concurrent.futures import ThreadPoolExecutor
# %%
import os
import gzip
import shutil
import requests
def download_file(year):
    download_url = f'https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_details-ftp_v1.0_d{year}_c20250401.csv.gz'
    file_name = f'StormEvents_details-ftp_v1.0_d{year}_c20250401.csv.gz'

    response = requests.get(download_url)

    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)

        with gzip.open(file_name, 'rb') as f_in:
            with open(file_name[:-3], 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    
        return_df =  pd.read_csv(file_name[:-3], low_memory=False)
        return_df['year'] = year
        
        os.remove(file_name)
        os.remove(file_name[:-3])

        print(f"Downloaded Data for {year}.")

        return return_df
    else:
        return None

# %%
# Get temperature data
nasa_url = "https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt"
temp_df = pd.read_table(nasa_url, skiprows=5, header = None)

temp_df = temp_df[0].str.split(5*' ', expand=True)

temp_df.columns = ['year','temp_index','smoothed_temp_index']

temp_df

# %%
storm_dfs = []
download_years = range(1950, datetime.datetime.today().year)

with ThreadPoolExecutor() as executor:
    for df in executor.map(download_file, download_years):
        if df is not None:
            storm_dfs.append(df)

storm_df = pd.concat(storm_dfs)
# %%
events_to_keep = [
    'Tornado'
    ,'Hurricane'
    ,'Hurricane (Typhoon)'
    ,'Marine Hurricane/Typhoon'
    ,'TORNADO/WATERSPOUT'
    ,'TORNADOES, TSTM WIND, HAIL'
]

event_df = storm_df.loc[storm_df['EVENT_TYPE'].isin(events_to_keep)]

# %%
# Apply scale mapping
event_df['f_scale'] = event_df['TOR_F_SCALE'].str[-1].astype(int)

ef_scale_mapping = {
    0: "Light Damage (40 - 72 mph)",
    1: "Moderate Damage (73 - 112 mph)",
    2: "Significant damage (113 - 157 mph)",
    3: "Severe Damage (158 - 206 mph)",
    4: "Devastating Damage (207 - 260 mph)",
    5: "Incredible Damage (261 - 318 mph)"
}



# %%
event_df.info(verbose=True, show_counts=True)
# %%
