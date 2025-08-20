# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
import calendar
import matplotlib.cm as cm # For colormaps

# Apply a seaborn theme for better aesthetics - starting with a clean base
sns.set_theme(style="white") 

# Define years and months
all_years_list = list(range(2018, 2024)) 
months = range(1, 13)
month_abbr = [calendar.month_abbr[i] for i in months] 

# Create a DataFrame to store the data
data = []

# Base seasonal pattern 
seasonal_pattern = np.array([0.3, 0.25, 0.4, 0.6, 0.8, 0.9, 1.0, 0.95, 0.85, 0.7, 0.5, 0.35])

# Base ride counts for each year (in millions)
base_rides_millions = {
    2018: 1.8,
    2019: 1.9,
    2020: 1.4, 
    2021: 2.0,
    2022: 3.0,
    2023: 3.5
}

# Generate data
for year_val in all_years_list: 
    year_base = base_rides_millions[year_val]
    for month_idx, month_num in enumerate(months):
        noise = np.random.normal(1, 0.08) 
        ride_count = year_base * seasonal_pattern[month_idx] * noise * 1_000_000 
        ride_count = max(0, ride_count)
        data.append([year_val, month_num, ride_count])

df = pd.DataFrame(data, columns=['year', 'month', 'ride_count'])

# --- Create Custom Palette ---
year_to_highlight_numeric = 2020
highlight_color = 'red'

# Years for gradient (excluding the highlighted year)
gradient_years = sorted([y for y in all_years_list if y != year_to_highlight_numeric])
num_gradient_years = len(gradient_years)

# Get a colormap (e.g., 'Blues' which goes Dark to Light by default)
# We will apply it in reverse to make 2018 (earliest) -> Lightest, 2023 (latest) -> Darkest
colormap = cm.get_cmap('Blues', num_gradient_years + 5000) # Using 'Blues' instead of 'Blues_r'
custom_palette = {}
for i, year_val in enumerate(gradient_years):
    # Normalize i to be from 0 to 1
    # This ensures that for the first year, normalized_i is 0, and for the last, it's 1.
    normalized_i = i / (num_gradient_years - 1 if num_gradient_years > 1 else 1)

    # Apply colormap in the original direction:
    # normalized_i maps 0 to color(0) (lightest blue) and 1 to color(1) (darkest blue)
    custom_palette[year_val] = colormap(normalized_i)

# Apply the highlight color to the specified year
custom_palette[year_to_highlight_numeric] = highlight_color
# --- End Custom Palette ---


# Create the plot
plt.figure(figsize=(13, 8)) 

df = df[df['year'] != 2018]

plot = sns.lineplot(
    data=df,
    x='month',
    y='ride_count',
    hue='year',
    palette=custom_palette, # Use the custom palette
    linewidth=1.8, 
    legend='full' 
)

# --- Highlighting the year 2020 ---
legend_labels = [] # Initialize to avoid NameError if legend is not found
if plot.legend_ is not None:
    legend_handles = plot.legend_.legend_handles 
    legend_labels = [label.get_text() for label in plot.legend_.get_texts()]

    year_to_highlight_str = str(year_to_highlight_numeric)
    # highlight_color is already defined above
    highlight_linewidth = 2.5
    highlight_linestyle = '--' 
    
    try:
        highlight_idx = legend_labels.index(year_to_highlight_str)
        if 0 <= highlight_idx < len(plot.lines):
            line_2020 = plot.lines[highlight_idx]
            # Color is set by palette, but ensure other properties are applied
            line_2020.set_color(highlight_color) # Reinforce color
            line_2020.set_linewidth(highlight_linewidth)
            line_2020.set_linestyle(highlight_linestyle)
            
            data_2020 = df[df['year'] == year_to_highlight_numeric]
            annotation_month_index = 6 
            
            annotation_point_data = data_2020[data_2020['month'] == (annotation_month_index + 1)] 
            if not annotation_point_data.empty:
                annotation_x = annotation_point_data['month'].iloc[0]
                annotation_y = annotation_point_data['ride_count'].iloc[0]
                
                plt.annotate(
                    f'{year_to_highlight_str} Dip',
                    xy=(annotation_x, annotation_y),
                    xytext=(annotation_x + 0.25, annotation_y - 300000), # User's updated offset
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
                    fontsize=10,
                    color='black',
                    bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="black", lw=0.5, alpha=0.8)
                )
    except ValueError:
        print(f"Warning: Year {year_to_highlight_str} not found in legend labels for highlighting.")
    except IndexError:
        print(f"Warning: Index issue while trying to highlight year {year_to_highlight_str}.")
else:
    print("Warning: No legend found on the plot to modify for highlighting.")
# --- End of highlighting ---


# Customize title and labels
plt.title('Monthly CitiBike Rides by Year', fontsize=18) # User's updated title
plt.xlabel('Month', fontsize=14)
plt.ylabel('Ride Count', fontsize=14)

# Set x-axis ticks 
plt.xticks(ticks=months, labels=month_abbr, fontsize=12)

# Format y-axis
def millions_formatter_with_m(x, pos):
    return f'{x / 1_000_000:.1f}M'
plot.yaxis.set_major_formatter(FuncFormatter(millions_formatter_with_m))
plot.tick_params(axis='y', labelsize=12)

# Adjust legend
current_legend = plt.legend(title='Year', bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0., fontsize=11, title_fontsize=13)

# Ensure the highlighted line in the RECREATED legend also reflects the changes
if current_legend and str(year_to_highlight_numeric) in legend_labels:
    try:
        highlight_idx_legend = legend_labels.index(str(year_to_highlight_numeric))
        if 0 <= highlight_idx_legend < len(current_legend.get_lines()):
            legend_line_2020 = current_legend.get_lines()[highlight_idx_legend]
            legend_line_2020.set_color(highlight_color) 
            legend_line_2020.set_linewidth(highlight_linewidth)
            legend_line_2020.set_linestyle(highlight_linestyle)
    except (ValueError, IndexError) as e:
        print(f"Warning: Could not update highlighted year in the legend. {e}")

plot.grid(False)
plt.tight_layout(rect=[0, 0, 0.88, 1]) 
plt.show()

print("Sample of generated data (2018 onwards):")
print(df.head())
print("\nRide counts for 2020:")
print(df[df['year'] == 2020].head())

# %%
