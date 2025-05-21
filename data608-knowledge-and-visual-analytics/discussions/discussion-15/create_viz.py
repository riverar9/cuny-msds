# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
import calendar

# Apply a seaborn theme for better aesthetics - starting with a clean base
sns.set_theme(style="white") # Changed from darkgrid to white

# Define years and months
years = range(2018, 2024) # Changed to start from 2018
months = range(1, 13)
month_abbr = [calendar.month_abbr[i] for i in months] # Get abbreviated month names

# Create a DataFrame to store the data
data = []

# Base seasonal pattern (higher in summer, lower in winter)
# Values represent proportions, will be scaled later
seasonal_pattern = np.array([0.3, 0.25, 0.4, 0.6, 0.8, 0.9, 1.0, 0.95, 0.85, 0.7, 0.5, 0.35])

# Base ride counts for each year (in millions, to be multiplied by seasonal pattern)
# These are rough estimates to mimic the graph's trends
# Filtered to start from 2018
base_rides_millions = {
    2018: 1.8,
    2019: 1.9,
    2020: 1.4,  # Simulating a dip (e.g., pandemic) - this value makes the dip noticeable
    2021: 2.0,
    2022: 3.0,
    2023: 3.5
}

# Generate data
for year_val in years: # Renamed 'year' to 'year_val' to avoid conflict with legend title
    year_base = base_rides_millions[year_val]
    for month_idx, month_num in enumerate(months):
        # Introduce some randomness/noise to make it look more realistic
        noise = np.random.normal(1, 0.08) # Multiplicative noise
        ride_count = year_base * seasonal_pattern[month_idx] * noise * 1_000_000 # Convert to actual numbers
        # Ensure non-negative ride counts
        ride_count = max(0, ride_count)
        data.append([year_val, month_num, ride_count])

df = pd.DataFrame(data, columns=['year', 'month', 'ride_count'])

# Create the plot
plt.figure(figsize=(13, 8)) # Adjusted figure size for better readability

# Use seaborn's lineplot
# Seaborn automatically creates a legend and stores it in plot.legend_ if one is generated
plot = sns.lineplot(
    data=df,
    x='month',
    y='ride_count',
    hue='year',
    palette='tab10', # Using a palette with good distinction
    linewidth=1.8, # Default linewidth for most lines
    legend='full' # Request a full legend
)

# --- Highlighting the year 2020 ---
# Access the legend object created by seaborn
# Ensure a legend object exists; seaborn might not create one if 'hue' isn't used or if legend=False
if plot.legend_ is not None:
    # Corrected attribute name from legendHandles to legend_handles
    legend_handles = plot.legend_.legend_handles 
    legend_labels = [label.get_text() for label in plot.legend_.get_texts()]

    year_to_highlight = '2020'
    highlight_color = 'red'
    highlight_linewidth = 2.5
    highlight_linestyle = '--' # Dashed line for 2020

    # Iterate through the lines on the plot itself
    # The order of plot.lines should correspond to the order of hue categories
    # which should also match the legend order if created by seaborn.
    
    # Find the index of the year to highlight from the legend labels
    try:
        highlight_idx = legend_labels.index(year_to_highlight)
        if 0 <= highlight_idx < len(plot.lines):
            line_2020 = plot.lines[highlight_idx]
            line_2020.set_color(highlight_color)
            line_2020.set_linewidth(highlight_linewidth)
            line_2020.set_linestyle(highlight_linestyle)
            
            # Add annotation for the 2020 dip
            data_2020 = df[df['year'] == int(year_to_highlight)]
            annotation_month_index = 6 # July (month 7, index 6 for 0-indexed seasonal_pattern)
            
            # Check if data for the annotation point exists
            annotation_point_data = data_2020[data_2020['month'] == (annotation_month_index + 1)] # month is 1-indexed
            if not annotation_point_data.empty:
                annotation_x = annotation_point_data['month'].iloc[0]
                annotation_y = annotation_point_data['ride_count'].iloc[0]
                
                plt.annotate(
                    f'{year_to_highlight} Dip',
                    xy=(annotation_x, annotation_y),
                    xytext=(annotation_x + 0.25, annotation_y - 300000), # Offset text slightly
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
                    fontsize=10,
                    color='black',
                    bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="black", lw=0.5, alpha=0.8)
                )
    except ValueError:
        print(f"Warning: Year {year_to_highlight} not found in legend labels for highlighting.")
    except IndexError:
        print(f"Warning: Index issue while trying to highlight year {year_to_highlight}.")

else:
    print("Warning: No legend found on the plot to modify for highlighting.")
# --- End of highlighting ---


# Customize title and labels
plt.title('Monthly CitiBike Rides by Year', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Ride Count', fontsize=14)

# Set x-axis ticks to show abbreviated month names
plt.xticks(ticks=months, labels=month_abbr, fontsize=12)

# Format y-axis to show numbers in millions with "M"
def millions_formatter_with_m(x, pos):
    """Formats the number in millions and appends 'M'."""
    return f'{x / 1_000_000:.1f}M'

plot.yaxis.set_major_formatter(FuncFormatter(millions_formatter_with_m))
plot.tick_params(axis='y', labelsize=12)

# Adjust legend
# The legend is typically created/updated by seaborn's lineplot call.
# If we modified the line properties directly, the legend created by seaborn should reflect this.
# If not, we might need to regenerate it or update its handles manually.
# The plt.legend() call below will create a NEW legend or update the existing one.
current_legend = plt.legend(title='Year', bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0., fontsize=11, title_fontsize=13)

# Ensure the highlighted line in the RECREATED legend also reflects the changes
if current_legend and year_to_highlight in legend_labels:
    try:
        highlight_idx_legend = legend_labels.index(year_to_highlight)
        if 0 <= highlight_idx_legend < len(current_legend.get_lines()):
            legend_line_2020 = current_legend.get_lines()[highlight_idx_legend]
            legend_line_2020.set_color(highlight_color)
            legend_line_2020.set_linewidth(highlight_linewidth)
            legend_line_2020.set_linestyle(highlight_linestyle)
    except (ValueError, IndexError) as e:
        print(f"Warning: Could not update highlighted year in the legend. {e}")


# Remove grid lines explicitly if any remain from the base style (though "white" should handle it)
plot.grid(False)

# Improve layout to prevent labels from being cut off
plt.tight_layout(rect=[0, 0, 0.88, 1]) # Adjust rect to make space for the legend

# Show plot
plt.show()

# Display some of the generated data
print("Sample of generated data (2018 onwards):")
print(df.head())
print("\nRide counts for a specific year (e.g., 2020):")
print(df[df['year'] == 2020].head())

# %%
