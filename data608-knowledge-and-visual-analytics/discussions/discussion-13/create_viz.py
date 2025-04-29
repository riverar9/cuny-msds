# %%
def weekly_traffic_plot():
    """
    Generates a line plot of simulated weekly website traffic over 10 weeks,
    highlights a week with a significant drop, and saves the plot to a file.
    """
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import matplotlib.dates as mdates # Import module for date formatting
    import os # Import the os module for directory operations

    # --- Data Generation ---
    # Generate fake weekly traffic data for 10 weeks
    np.random.seed(42) # for reproducible results
    # Generate 10 weekly dates starting from a recent Monday
    # Example: Start from Monday, March 3rd, 2025
    start_date = '2025-03-03'
    dates = pd.date_range(start=start_date, periods=10, freq='W-MON') # Weekly frequency, starting on Monday

    # Generate baseline traffic with some noise
    traffic = np.random.randint(80000, 120000, size=10)

    # Introduce a significant drop in a specific week (e.g., week 6)
    drop_week_index = 5 # Index 5 corresponds to the 6th date
    traffic[drop_week_index] = np.random.randint(30000, 40000) # Lower traffic for this week

    # Create a Pandas DataFrame
    df = pd.DataFrame({
        'Date': dates, # Use dates instead of week numbers
        'Traffic': traffic
    })

    # --- Visualization ---
    plt.style.use('seaborn-v0_8-whitegrid') # Use a clean seaborn style
    plt.figure(figsize=(14, 7)) # Adjust figure size slightly for dates

    # Create the line plot using the Date column
    ax = sns.lineplot(
        x='Date', # Use the Date column for the x-axis
        y='Traffic',
        data=df,
        marker='o', # Add markers to data points
        linewidth=2.5,
        markersize=8,
        color='#003f5c' # A blue color similar to the infographic's top section
    )

    # --- Highlight the Drop ---
    # Find the row (date and traffic) with the minimum traffic
    min_traffic_row = df.loc[df['Traffic'].idxmin()]
    min_date = min_traffic_row['Date'] # Get the date of the minimum traffic
    min_traffic_val = min_traffic_row['Traffic']

    # Add a red circle annotation around the drop point using scatter
    ax.scatter(
        min_date, # Use the date for the x-coordinate
        min_traffic_val,
        s=500, # Size of the circle marker (adjust as needed)
        facecolors='none',
        edgecolors='red',
        linewidth=2,
        label='Week of Concern' # Updated label for the legend
    )

    # --- Styling and Labels ---
    ax.set_title('Weekly Website Traffic', fontsize=18, pad=20, weight='bold') # Simplified title
    ax.set_xlabel('Date', fontsize=14, labelpad=15) # Updated x-axis label
    # Updated y-axis label to match the infographic example more closely
    ax.set_ylabel('Total Website Traffic', fontsize=14, labelpad=15)

    # Format y-axis labels for better readability
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))

    # Format x-axis to display dates nicely (e.g., 'Apr 07')
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1)) # Ensure a tick for every week's start date
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d')) # Format as 'Month Day'
    plt.xticks(rotation=45, ha='right') # Rotate labels for better readability

    # Customize ticks
    ax.tick_params(axis='both', which='major', labelsize=12)

    # Add grid lines for better readability
    ax.grid(True, which='major', linestyle='--', linewidth=0.5)

    # Add legend
    ax.legend(fontsize=12)

    # Adjust layout to prevent labels overlapping
    plt.tight_layout()

    # --- Save the Plot ---
    # Define the full output path including the desired filename
    output_filename = "02-weekly-traffic.png"
    output_dir = "data608-knowledge-and-visual-analytics/discussions/discussion-13"
    output_path = os.path.join(output_dir, output_filename)

    # Create the target directory structure if it doesn't exist
    # The `exist_ok=True` argument prevents an error if the directory already exists
    os.makedirs(output_dir, exist_ok=True)
    print(f"Ensuring directory exists: {output_dir}") # Confirmation message

    # Save the figure to the specified path
    # Using bbox_inches='tight' helps ensure labels aren't cut off
    plt.savefig(output_path, bbox_inches='tight')
    print(f"Plot successfully saved to: {output_path}") # Confirmation message

    # Close the plot figure to free up memory
    plt.close()

    # --- Display DataFrame (Optional) ---
    print("\nGenerated Traffic Data with Dates:")
    print(df)

# Example of how to call the function (optional, comment out if not needed immediately)
# weekly_traffic_plot()

# %%
def total_sales_contribution():
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    import os # Import the os module for directory operations

    # --- Data Generation ---
    # Define sales channels
    channels = ['Online', 'Retail Store', 'Partner Sales', 'Direct Mail', 'Events']

    # Manually assign sales figures to meet the criteria:
    # - Total around 20,000
    # - Online is one of the largest
    # - Events, Partner Sales, Retail Store are smallest
    # - Retail Store > Partner Sales and Events among the smallest

    # Example assignment:
    sales_dict = {
        'Online': 8500,        # Largest
        'Direct Mail': 6000,   # Second largest
        'Retail Store': 2500,  # Largest of the smallest three
        'Partner Sales': 1800, # Smaller
        'Events': 1200         # Smallest
    }
    # Total = 8500 + 6000 + 2500 + 1800 + 1200 = 20000

    # Create lists in the original order for the DataFrame
    sales = [sales_dict[channel] for channel in channels]

    # Create a Pandas DataFrame
    df_sales = pd.DataFrame({
        'Channel': channels,
        'Total Sales': sales
    })

    # Sort data for potentially better visualization (optional, but often nice for bars)
    # Sorting ensures the visual hierarchy matches the data hierarchy
    df_sales = df_sales.sort_values('Total Sales', ascending=False)

    # --- Visualization ---
    plt.style.use('seaborn-v0_8-whitegrid') # Use a clean seaborn style
    plt.figure(figsize=(10, 6)) # Set the figure size

    # Create the horizontal bar plot
    # Using seaborn directly makes it easy to map columns to axes
    ax = sns.barplot(
        x='Total Sales',
        y='Channel',
        data=df_sales,
        palette='viridis', # Choose a color palette
        orient='h' # Specify horizontal orientation
    )

    # --- Styling and Labels ---
    ax.set_title('YTD Total Sales by Channel', fontsize=16, pad=20, weight='bold')
    ax.set_xlabel('Total Number of Sales', fontsize=12, labelpad=15)
    ax.set_ylabel('Sales Channel', fontsize=12, labelpad=15)

    # Format x-axis labels for better readability (e.g., 10,000 instead of 10000)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))

    # Add data labels to the bars for clarity
    # Iterate through the patches (bars) and add text annotation
    for container in ax.containers:
        # Use the sorted dataframe's order for labels
        ax.bar_label(container, fmt='{:,.0f}', padding=3, fontsize=10) # Format as integer with comma

    # Customize ticks
    ax.tick_params(axis='both', which='major', labelsize=11)

    # Remove grid lines on the y-axis if desired, keep x-axis grid
    ax.grid(True, axis='x', linestyle='--', linewidth=0.5)
    ax.grid(False, axis='y') # Turn off y-axis grid lines for a cleaner look

    # Adjust layout to prevent labels overlapping
    plt.tight_layout()

    # --- Save the Plot ---
    # Define the full output path provided by the user
    output_path = "03-sales-distributions.png"

    # Extract the directory part from the full path
    output_dir = os.path.dirname(output_path)

    # Create the target directory structure if it doesn't exist
    # The `exist_ok=True` argument prevents an error if the directory already exists
    # Check if output_dir is not an empty string (which happens if the path is just a filename)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        print(f"Ensuring directory exists: {output_dir}") # Confirmation message

    # Save the figure to the specified path
    # Using bbox_inches='tight' helps ensure labels aren't cut off in the saved image
    plt.savefig(output_path, bbox_inches='tight')
    print(f"Plot successfully saved to: {output_path}") # Confirmation message

    # Close the plot figure to free up memory (good practice when saving files)
    plt.close()

    # --- Display DataFrame (Optional) ---
    # Display the dataframe *after* sorting to show the order used in the plot
    print("\nGenerated and Sorted Sales Data:")
    print(df_sales)
# %%
def main():
    weekly_traffic_plot()
    total_sales_contribution()
# %%
