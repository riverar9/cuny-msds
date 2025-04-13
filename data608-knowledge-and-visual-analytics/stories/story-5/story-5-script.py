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

for temp_col in temp_df.columns:
    temp_df[temp_col] = pd.to_numeric(temp_df[temp_col])

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
    'Tornado',
    'Hurricane',
    'Hurricane (Typhoon)',
    'Marine Hurricane/Typhoon',
    'TORNADO/WATERSPOUT',
    'TORNADOES, TSTM WIND, HAIL',
]

event_df = storm_df.loc[storm_df['EVENT_TYPE'].isin(events_to_keep)]

event_df.info(verbose=True, show_counts=True)

# %%
def parse_damage(value):
    if pd.isnull(value) or value in ('','K') or isinstance(value, int):
        return 0
    value = value.upper().strip()
    if value.endswith('M'):
        return float(value[:-1]) * 1e6
    elif value.endswith('K'):
        return float(value[:-1]) * 1e3
    elif value.endswith('B'):
        return float(value[:-1]) * 1e9
    else:
        return float(value)
    
event_df['total_damage'] = (event_df['DAMAGE_PROPERTY'].apply(parse_damage) + event_df['DAMAGE_CROPS'].apply(parse_damage)).astype(int)

event_df.head()

# %%
years_to_keep = 100
report_df = event_df.loc[event_df['year'] >= datetime.datetime.today().year-years_to_keep][['year','total_damage']]

report_df = report_df.merge(
    temp_df,
    on = 'year',
    how='left'
)

report_df.head()
# %%
viz1_df = report_df.copy()
viz1_df['temp_bin'] = (viz1_df['temp_index'] // 0.2) * 0.1

viz_x = 'temp_bin'

viz1_df = viz1_df[['year',viz_x]].groupby(viz_x).count().reset_index().rename(columns={'year':'storm_count'}).merge(
    viz1_df[['year',viz_x]].drop_duplicates().groupby(viz_x).count().reset_index().rename(columns={'year':'years_at_temp'}),
    on = viz_x
)

viz1_df['avg_yrly_storms'] = viz1_df['storm_count']/viz1_df['years_at_temp']


sns.lineplot(
    data=viz1_df,
    x='temp_bin',
    y='avg_yrly_storms',
    color='#FF6D00',  # teal-green line like in image
    linewidth=3,
    marker='o'
)

# Style adjustments to match the image
plt.title("Storm Frequency by Temperature Increase", fontsize=24, fontweight='bold', loc='left', color='#7a695a')
plt.xlabel("Temperature Increase (°C)", fontsize=14)
plt.ylabel("Average Yearly Storms", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(False)
plt.gca().spines[['top', 'right']].set_visible(False)
plt.gca().set_facecolor('#f2f2f2')      # plot area
plt.gcf().set_facecolor('#f2f2f2')      # entire figure
plt.tight_layout()
plt.show()
# %%
import matplotlib.ticker as ticker
viz2_df = report_df.copy()
viz2_df['temp_bin'] = (viz2_df['temp_index'] // 0.2) * 0.1

viz_x = 'temp_bin'

viz2_df = viz2_df[['total_damage',viz_x]].groupby(viz_x).mean().reset_index().merge(
    viz2_df[['year',viz_x]].drop_duplicates().groupby(viz_x).count().reset_index().rename(columns={'year':'years_at_temp'}),
    on = viz_x
)

viz2_df['avg_storm_intensity'] = viz2_df['total_damage']/viz2_df['years_at_temp']


sns.lineplot(
    data=viz2_df,
    x=viz_x,
    y='avg_storm_intensity',
    color='#00BFAE',  # teal-green line like in image
    linewidth=3,
    marker='o'
)

# Style adjustments to match the image
plt.title("Storm Severity by Temperature Increase", fontsize=24, fontweight='bold', loc='left', color='#7a695a')
plt.xlabel("Temperature Increase (°C)", fontsize=14)
plt.ylabel("Average Damage per Storm\n(Millions USD)", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'${x/1e6:.1f}B'))
plt.grid(False)
plt.gca().spines[['top', 'right']].set_visible(False)
plt.gca().set_facecolor('#f2f2f2')      # plot area
plt.gcf().set_facecolor('#f2f2f2')      # entire figure
plt.tight_layout()
plt.show()
# %%
