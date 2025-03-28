# %%
import pandas as pd
# %%
# Read in the file from Kaggle
# https://www.kaggle.com/code/dhirajaiexpert/data-science-jobs-salaries-2024-by-dhiraj/input
df = pd.read_csv('glassdoor_jobs.csv')
df.head()
# %%
# Clean up the salary column
df['Salary'] = df['Salary Estimate'].str.replace(
    ' (Glassdoor est.)','').str.replace(
    'Employer Provided Salary:', '').str.replace(
    '(Employer est.)', '').str.replace(
    '(Glassdoor est.)', '')

list(df['Salary'].unique())
# %%
# Remove the entries of -1
df = df.loc[df['Salary'] != '-1']

df.head()
# %%
# Create a low to high range for salaries
df['str_sal_low'] = df['Salary'].str.split('-').str[0].str.replace('$','').str.replace('K', '')
df['str_sal_high'] = df['Salary'].str.split('-').str[1].str.replace('$','').str.replace('K', '')

df['sal_high'] = df['str_sal_high'].apply(lambda x: 2800*int(x.replace(' Per Hour','')) if 'Hour' in x else 1000*int(x))
df['sal_low'] = df['str_sal_low'].apply(lambda x: 2800*int(x.replace(' Per Hour','')) if 'Hour' in x else 1000*int(x))

df['sal_avg'] = (df['sal_high'] + df['sal_low'])/2

df[['Salary','sal_low','sal_high']]
# %%
# Parse the state information
df['state'] = df['Location'].str[-2:]
df.head()
# %%
# Keep only necessary columns
viz_df = df[['Job Title','sal_low','sal_avg','sal_high','state']]
viz_df.columns = ['title','sal_low','sal_avg','sal_high','state']
viz_df.head()
# %%
# Clean up titles so they're standardized
ds = 'Data Scientist'
de = 'Data Engineer'
contains_logic = {
    'Consult':'Data Consulting',
    'Direct':'Management',
    'Manage' : 'Management',
    'Machine Learning': ds,
    'Data Scientist': ds,
    'Data Engineer': de,
    'Analyst' : 'Data Analyst',
    'Spark Engineer' : de,
    'Modeler' : ds,
    'Analytical Development' : ds,
    'Quantitative':ds,
    'Data Science':ds,
    'Data Management Engineering':de,
    'Research Scientist':ds,
    'Scientist':ds,
    'Enterprise Architect, Data':de,
    'Visualization':ds,
    'Operations':de,
    'Tech':ds
}

clean_df = viz_df.copy()
for key, value in contains_logic.items():
    clean_df['title'] = clean_df['title'].apply(lambda x: value if key.lower() in x.lower() else x)

# Remove states with less than 10 salaries
#clean_df = clean_df[clean_df.groupby('state')['state'].transform('count') >= 10]

clean_df.head()
# %%
# Try a bar chartvisualization for size
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

# Get unique titles
sorted_states = clean_df.groupby('state')['sal_avg'].median().sort_values().index

# Create a figure
fig, ax = plt.subplots(figsize=(6, 10))

# Create box plots for each title
data = [clean_df.loc[clean_df['state'] == state, 'sal_avg'] for state in sorted_states]

ax.boxplot(
    data,
    vert=False,
    patch_artist=True, 
    boxprops=dict(facecolor="white"), 
    flierprops=dict(marker='.', color='black', markersize=1)
)

# Set y-axis labels
ax.set_yticks(range(1, len(sorted_states) + 1))
ax.set_yticklabels(sorted_states)

# Labels and title
ax.set_xlabel("Salary", fontsize=14, fontweight="bold")
ax.set_ylabel("State", fontsize=14, fontweight="bold")
ax.set_title("Data Science Practioner Salary by State", fontsize=14, fontweight="bold")

# remove border
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)

# Add vertical lines at each 50K interval behind other elements
for x in np.arange(50000, ax.get_xlim()[1], 50000):
    ax.axvline(x, color='grey', linestyle='dotted', alpha=0.5, zorder=0)

# Set x-axis
ax.xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'${x/1000:.0f}K'))

plt.tight_layout()
plt.show()
# %%
# Attempt 2, heatmap
heatmap_df = clean_df.groupby(['title','state']).median().reset_index()
heatmap_df = heatmap_df.loc[heatmap_df['title'] != 'Management']

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap

# Pivot the DataFrame for heatmap
heatmap_data = heatmap_df.pivot(index="state", columns="title", values="sal_avg") / 1000

# Sort by the average salary across all job titles per state
heatmap_data = heatmap_data.loc[heatmap_data['Data Scientist'].sort_values(ascending=False).index]
custom_title_order = ['Data Scientist', 'Data Engineer','Data Analyst','Data Consulting']
heatmap_data = heatmap_data[custom_title_order]

# Custom colormap from magenta (low) to green (high)
custom_cmap = LinearSegmentedColormap.from_list("magenta_green", ["lightgreen", "darkgreen"])

# Format values as dollar amounts in thousands
annot_labels = heatmap_data.applymap(lambda x: f"${x:,.0f}K" if pd.notnull(x) else "")

# Plot the heatmap
plt.figure(figsize=(12, 12))  # Increase height to 12
ax = sns.heatmap(heatmap_data, cmap=custom_cmap, annot=annot_labels, fmt="", linewidths=0.5)

# Set the colorbar with dollar amounts in thousands
colorbar = ax.collections[0].colorbar
colorbar.set_ticks(np.linspace(heatmap_data.min().min(), heatmap_data.max().max(), 5))
colorbar.set_ticklabels([f"${x:,.0f}K" for x in np.linspace(heatmap_data.min().min(), heatmap_data.max().max(), 5)])

ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)

plt.xlabel("Job Title")
plt.ylabel("State")

plt.xticks(rotation=0)
plt.yticks(rotation=0)

plt.show()

# %%
