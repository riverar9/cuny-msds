# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %%
food_df = pd.read_csv('data/dec23pub.csv')
food_df.head()
# %%
food_df.shape
# %%
food_columns = [
    'GESTFIPS',
    'HRPOOR', # lowest income in Income range above or below 185% poverty - 1=Below 185% poverty 2=Above 185% poverty or income not reported
    'HRFS12MC',# Children's Food Security Status, 12-Month Recall | 1 Children Food Secure, High or Marginal Food Security| 2 Low Food Security | 3 Very Low Food Security 
    'PESEX', # SEX | 1 MALE | 2 FEMALE
    'HRFS12M8', # Adult Food Security Status, 12-Month Recall | 1 High Food Security among Adults |2 Marginal Food Security among Adults |3 Low Food Security among Adults |4 Very Low Food Security among Adults |-9 No Response
]

# %%
filter_df = food_df[food_columns]
filter_df.head()
# %%
# 1. Define the mapping dictionaries based on your descriptions
# Define the GESTFIPS mapping dictionary
gestfips_map = {
    1: 'AL', 2: 'AK', 4: 'AZ', 5: 'AR', 6: 'CA', 8: 'CO', 9: 'CT', 10: 'DE',
    11: 'DC', 12: 'FL', 13: 'GA', 15: 'HI', 16: 'ID', 17: 'IL', 18: 'IN',
    19: 'IA', 20: 'KS', 21: 'KY', 22: 'LA', 23: 'ME', 24: 'MD', 25: 'MA',
    26: 'MI', 27: 'MN', 28: 'MS', 29: 'MO', 30: 'MT', 31: 'NE', 32: 'NV',
    33: 'NH', 34: 'NJ', 35: 'NM', 36: 'NY', 37: 'NC', 38: 'ND', 39: 'OH',
    40: 'OK', 41: 'OR', 42: 'PA', 44: 'RI', 45: 'SC', 46: 'SD', 47: 'TN',
    48: 'TX', 49: 'UT', 50: 'VT', 51: 'VA', 53: 'WA', 54: 'WV', 55: 'WI', 56: 'WY'
}

# 1. Define the master mapping dictionary including all columns to recode
recode_maps = {
    'HRPOOR': {
        1: 'Below 185% poverty',
        2: 'Above 185% poverty or income not reported'
    },
    'HRFS12MC': {
        -1: 'Not in universe',
        1: 'Children Food Secure, High or Marginal Food Security',
        2: 'Low Food Security',
        3: 'Very Low Food Security',
        -9: 'No Response'
    },
    'PESEX': {
        1: 'MALE',
        2: 'FEMALE'
    },
    'HRFS12M8': {
        1: 'High Food Security among Adults',
        2: 'Marginal Food Security among Adults',
        3: 'Low Food Security among Adults',
        4: 'Very Low Food Security among Adults',
       -9: 'No Response'
    },
    'GESTFIPS': gestfips_map  # Add the FIPS map here
}

# Create a copy to store the recoded values (optional, but good practice)
# Make sure filter_df actually contains all columns listed below before copying
recoded_df = filter_df.copy()

# 2. Update the list of columns to include GESTFIPS
columns_to_recode = [
    'HRPOOR',
    'HRFS12MC',
    'PESEX',
    'HRFS12M8',
    'GESTFIPS' # Added GESTFIPS here
]

# Iterate through the specified columns and apply replace using the maps
for col in columns_to_recode:
    if col in recode_maps: # Check if a map exists for this column
        recoded_df[col] = recoded_df[col].replace(recode_maps[col])
    else:
        # This case should ideally not happen if columns_to_recode and recode_maps are aligned
        print(f"Warning: No recoding map found for column '{col}'")

# Display the recoded DataFrame
recoded_df.head()

# %%
# Child food security Metrics
low_food_secure_child_pct = recoded_df[recoded_df['HRFS12MC'].isin(['Low Food Security'])].shape[0] / recoded_df[recoded_df['HRFS12MC'].isin(['Low Food Security','Very Low Food Security','Children Food Secure, High or Marginal Food Security'])].shape[0]
vlow_food_secure_child_pct = recoded_df[recoded_df['HRFS12MC'].isin(['Very Low Food Security'])].shape[0] / recoded_df[recoded_df['HRFS12MC'].isin(['Low Food Security','Very Low Food Security','Children Food Secure, High or Marginal Food Security'])].shape[0]

# Poverty Metrics
poverty_pct = recoded_df[recoded_df['HRPOOR'] == 'Below 185% poverty'].shape[0] / recoded_df[recoded_df['HRPOOR'] != -1].shape[0]
poverty_female_pct = recoded_df[(recoded_df['HRPOOR'] == 'Below 185% poverty') & (recoded_df['PESEX'] == 'FEMALE')].shape[0] / recoded_df[(recoded_df['HRPOOR'] != -1) & (recoded_df['PESEX'] == 'FEMALE')].shape[0]
poverty_male_pct = recoded_df[(recoded_df['HRPOOR'] == 'Below 185% poverty') & (recoded_df['PESEX'] == 'MALE')].shape[0] / recoded_df[(recoded_df['HRPOOR'] != -1) & (recoded_df['PESEX'] == 'MALE')].shape[0]

# Food insecure Adults metrics
adult_low_sec = recoded_df[recoded_df['HRFS12M8'].isin(['Very Low Food Security among Adults','Low Food Security among Adults'])]
low_food_secure_adult_pct = adult_low_sec[adult_low_sec['HRFS12M8'] == 'Low Food Security among Adults'].shape[0] /recoded_df[~recoded_df['HRFS12M8'].isin([-1, 'No Response'])].shape[0]
vlow_food_secure_adult_pct = adult_low_sec[adult_low_sec['HRFS12M8'] == 'Very Low Food Security among Adults'].shape[0] /recoded_df[~recoded_df['HRFS12M8'].isin([-1, 'No Response'])].shape[0]

# Child Food security given poor
poverty_df = recoded_df[recoded_df['HRPOOR'] == 'Below 185% poverty']
npoverty_df = recoded_df[recoded_df['HRPOOR'] == 'Above 185% poverty or income not reported']

poverty_lowfoodsec_child_pct = poverty_df[poverty_df['HRFS12MC'].isin(['Low Food Security'])].shape[0] / poverty_df[poverty_df['HRFS12MC'].isin(['Low Food Security','Very Low Food Security','Children Food Secure, High or Marginal Food Security'])].shape[0]
poverty_vlowfoodsec_child_pct = poverty_df[poverty_df['HRFS12MC'].isin(['Very Low Food Security'])].shape[0] / poverty_df[poverty_df['HRFS12MC'].isin(['Low Food Security','Very Low Food Security','Children Food Secure, High or Marginal Food Security'])].shape[0]

npoverty_lowfoodsec_child_pct = npoverty_df[npoverty_df['HRFS12MC'].isin(['Low Food Security'])].shape[0] / npoverty_df[npoverty_df['HRFS12MC'].isin(['Low Food Security','Very Low Food Security','Children Food Secure, High or Marginal Food Security'])].shape[0]
npoverty_vlowfoodsec_child_pct = npoverty_df[npoverty_df['HRFS12MC'].isin(['Very Low Food Security'])].shape[0] / npoverty_df[npoverty_df['HRFS12MC'].isin(['Low Food Security','Very Low Food Security','Children Food Secure, High or Marginal Food Security'])].shape[0]

# Food insecure Adults metrics given poor
poverty_female_low_food_secure_adult_pct = poverty_df[(poverty_df['HRFS12M8'] == 'Low Food Security among Adults') & (poverty_df['PESEX'] == 'FEMALE')].shape[0] / poverty_df[(~poverty_df['HRFS12M8'].isin([-1, 'No Response'])) & (poverty_df['PESEX'] == 'FEMALE')].shape[0]
poverty_male_low_food_secure_adult_pct = poverty_df[(poverty_df['HRFS12M8'] == 'Low Food Security among Adults') & (poverty_df['PESEX'] == 'MALE')].shape[0] / poverty_df[(~poverty_df['HRFS12M8'].isin([-1, 'No Response'])) & (poverty_df['PESEX'] == 'MALE')].shape[0]

# %%
# Create first bar chart

poverty_status = ['Not in Poverty', 'In Poverty']
food_insec_pct = [round(100*(npoverty_lowfoodsec_child_pct + npoverty_vlowfoodsec_child_pct)),
                    round(100*(poverty_lowfoodsec_child_pct + poverty_vlowfoodsec_child_pct))]

# Define the colors based on the visual
bar_colors = ['#333333', '#5F9EA0']
background_color = '#A1C8D1'  # Approximate background color (light blue)

# Create the bar chart using seaborn
plt.figure(figsize=(4, 6), facecolor=background_color)  # Set figure background color
ax = sns.barplot(x=poverty_status, y=food_insec_pct, palette=bar_colors)
ax.set_facecolor(background_color)  # Set axes background color

# Add labels on the bars with whole number percentage signs
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{int(round(height))}%',  # Round to the nearest whole number and format
                (p.get_x() + p.get_width() / 2., height),
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')

# Remove y-axis ticks and labels
ax.set(yticks=[])
ax.set_ylabel('')

# Set x-axis label
ax.set_xlabel('')

# Add a title that clearly explains the chart
plt.title('Percentage of Children Facing Food Insecurity by Poverty Status')

# Remove the legend
# plt.legend(['Food Insecurity Percentage'])

# Remove spines
sns.despine(left=True, bottom=False)

# Show the plot
plt.tight_layout()
plt.show()
# %%
###
# FROM HERE:
#   1. Get child insecurty % by state
#   2. Create a heatmap of states with the highest food insecurity
#   3. Find a way to incorporate it into the infographic
###

#child_food_insecurity_by_sate = 
all_valid_response_children = recoded_df[recoded_df['HRFS12MC'].isin(['Low Food Security','Very Low Food Security','Children Food Secure, High or Marginal Food Security'])]
food_insecurity_children = recoded_df[recoded_df['HRFS12MC'].isin(['Low Food Security', 'Very Low Food Security'])]

state_child_food_insecurity = all_valid_response_children[['GESTFIPS','HRFS12MC']].groupby('GESTFIPS').count().reset_index().rename(columns = {'HRFS12MC' : 'c_tot'}).merge(
    food_insecurity_children[['GESTFIPS','HRFS12MC']].groupby('GESTFIPS').count().reset_index().rename(columns = {'HRFS12MC' : 'c_f_insec'}),
    on = 'GESTFIPS',
    how='left'
)

state_child_food_insecurity['c_food_insec_pct'] = state_child_food_insecurity['c_f_insec']/state_child_food_insecurity['c_tot']

state_child_food_insecurity.head()

# %%
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio # Import for renderer setting if needed

# --- Optional: Set Renderer (if needed for your environment) ---
# pio.renderers.default = 'plotly_mimetype+notebook' # Example, adjust as needed

# Assume 'state_child_food_insecurity' is your existing DataFrame
# state_child_food_insecurity = pd.read_csv(...) # Or however you load it

# Make a copy to avoid modifying the original DataFrame if needed
# Ensure the DataFrame is loaded before this line
try:
    df = state_child_food_insecurity.copy()
except NameError:
    print("Error: DataFrame 'state_child_food_insecurity' not found.")
    print("Please ensure the DataFrame is loaded before this script runs.")
    # Example loading (replace with your actual loading):
    data_example = {
        'GESTFIPS': ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'],
        'c_tot': [445, 623, 563, 486, 3187, 500, 300, 50, 80, 2000, 1000, 150, 300, 150, 1200, 600, 300, 400, 500, 600, 550, 130, 900, 550, 600, 350, 100, 950, 70, 200, 130, 850, 200, 280, 1800, 1100, 400, 380, 1200, 100, 450, 80, 650, 2500, 300, 800, 60, 700, 570, 180, 55],
        'c_f_insec': [57, 41, 71, 20, 285, 30, 20, 5, 5, 150, 80, 10, 18, 12, 96, 48, 21, 36, 55, 36, 44, 10, 72, 33, 48, 35, 8, 85, 4, 14, 7, 51, 20, 22, 126, 99, 36, 27, 84, 7, 40, 5, 52, 250, 18, 56, 3, 49, 34, 16, 4],
        'c_food_insec_pct': [0.128090, 0.065811, 0.126110, 0.041152, 0.089426, 0.06, 0.0666, 0.1, 0.0625, 0.075, 0.08, 0.0667, 0.06, 0.08, 0.08, 0.08, 0.07, 0.09, 0.11, 0.06, 0.08, 0.0769, 0.08, 0.06, 0.08, 0.1, 0.08, 0.0895, 0.0571, 0.07, 0.0538, 0.06, 0.1, 0.0786, 0.07, 0.09, 0.09, 0.0711, 0.07, 0.07, 0.0889, 0.0625, 0.08, 0.1, 0.06, 0.07, 0.05, 0.07, 0.0596, 0.0889, 0.0727]
    }
    state_child_food_insecurity = pd.DataFrame(data_example)
    df = state_child_food_insecurity.copy()
    print("Info: Using example data because 'state_child_food_insecurity' was not found.")


# --- Step 1: Identify State Identifier ---
state_abbr_col = 'GESTFIPS' # Adjust if your abbreviation column has a different name
if state_abbr_col not in df.columns:
    raise ValueError(f"DataFrame must contain the state identifier column named '{state_abbr_col}'.")

# --- Step 2: Map State Abbreviations to FIPS codes ---
fips_map = { # Same map as before... }
    'AL': '01', 'AK': '02', 'AZ': '04', 'AR': '05', 'CA': '06', 'CO': '08', 'CT': '09', 'DE': '10', 'DC': '11',
    'FL': '12', 'GA': '13', 'HI': '15', 'ID': '16', 'IL': '17', 'IN': '18', 'IA': '19', 'KS': '20', 'KY': '21',
    'LA': '22', 'ME': '23', 'MD': '24', 'MA': '25', 'MI': '26', 'MN': '27', 'MS': '28', 'MO': '29', 'MT': '30',
    'NE': '31', 'NV': '32', 'NH': '33', 'NJ': '34', 'NM': '35', 'NY': '36', 'NC': '37', 'ND': '38', 'OH': '39',
    'OK': '40', 'OR': '41', 'PA': '42', 'RI': '44', 'SC': '45', 'SD': '46', 'TN': '47', 'TX': '48', 'UT': '49',
    'VT': '50', 'VA': '51', 'WA': '53', 'WV': '54', 'WI': '55', 'WY': '56',
    'PR': '72'
}
df['FIPS'] = df[state_abbr_col].map(fips_map)

# --- Step 3: Data Validation ---
food_insec_col = 'c_food_insec_pct' # Adjust if your percentage column name is different
if food_insec_col not in df.columns:
    raise ValueError(f"DataFrame must contain the column '{food_insec_col}'.")
df[food_insec_col] = pd.to_numeric(df[food_insec_col], errors='coerce')
original_rows = len(df)
df = df.dropna(subset=['FIPS', food_insec_col])
if len(df) < original_rows:
    print(f"Warning: Dropped {original_rows - len(df)} rows due to missing/invalid FIPS or '{food_insec_col}' data.")
if len(df) == 0:
     raise ValueError("No valid data remaining after cleaning. Cannot create map.")

# --- Step 4: Create the heatmap (choropleth map) with Percentage Formatting ---
fig = go.Figure(data=go.Choropleth(
    locations=df['GESTFIPS'],             # Use the 'FIPS' column for locations
    z=df[food_insec_col],             # Use original decimal data for coloring
    locationmode='USA-states',
    colorscale='Reds',
    autocolorscale=False,
    marker_line_color='white',        # Color of borders between states
    colorbar_title="Food Insecurity %",
    colorbar_tickformat='1%'         # Format color bar ticks as percentages
))

# --- Step 5: Update Layout (including background colors) ---
fig.update_layout(
    title_text='Child Food Insecurity Percentage by State',
    paper_bgcolor='#A1C8D1',  # Background for the whole figure area
    geo=dict(                 # Geographic layout settings
        scope='usa',          # Limit map scope to USA
        bgcolor='#A1C8D1',    # ADDED: Set background color for the map geography itself
        lakecolor='#A1C8D1'   # Set lake color to match background (or use '#FFFFFF' for white lakes)
        # You can also control ocean color, land color (for areas not in your data), etc. here
        # landcolor='rgba(0,0,0,0)', # Example: Make land transparent
        # oceancolor='rgba(0,0,0,0)', # Example: Make ocean transparent
    )
)

# Display the figure
fig.show()
# %%
