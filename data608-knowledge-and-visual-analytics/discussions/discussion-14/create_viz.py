# %%
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import seaborn as sns
import pycountry # For ISO code conversion
import io # For handling image data in memory
import urllib.request # For fetching images from URLs

# --- Helper function to convert ISO Alpha-3 to Alpha-2 ---
def get_iso_a2_code(iso_a3_code):
    """
    Converts a 3-letter ISO country code (alpha_3) to a 2-letter code (alpha_2).
    Args:
        iso_a3_code (str): The 3-letter ISO country code.
    Returns:
        str or None: The 2-letter ISO country code in lowercase, or None if not found.
    """
    try:
        country = pycountry.countries.get(alpha_3=iso_a3_code)
        return country.alpha_2.lower() if country else None
    except LookupError:
        print(f"LookupError: Could not find ISO A2 code for {iso_a3_code}")
        return None

# --- Helper function to fetch flag image ---
def fetch_flag_image(iso_a2_code, size_code="w20"):
    """
    Constructs a URL for flagcdn.com and attempts to fetch the flag image.
    Args:
        iso_a2_code (str): The 2-letter ISO country code (lowercase).
        size_code (str): The size code for the flag image (e.g., "w20" for 20px width).
    Returns:
        numpy.ndarray or None: The image data as a NumPy array, or None if fetching fails.
    """
    if not iso_a2_code:
        return None
    # URL for flag images from flagcdn.com
    flag_url = f"https://flagcdn.com/{size_code}/{iso_a2_code}.png"
    
    try:
        # Open the URL and read the image data with a timeout
        with urllib.request.urlopen(flag_url, timeout=5) as url_response:
            image_data = url_response.read()
        # Convert image data from bytes to a NumPy array using matplotlib
        img = mpimg.imread(io.BytesIO(image_data), format='png')
        return img
    except Exception as e:
        print(f"Could not fetch or read image for {iso_a2_code} from {flag_url}: {e}")
        return None # Return None if any error occurs

# Get the data
df = pd.read_csv(
    'https://raw.githubusercontent.com/TheEconomist/big-mac-data/refs/heads/master/output-data/big-mac-full-index.csv',
    parse_dates=['date']
)

df = df.loc[df['date'] == df['date'].max()]
# --- Prepare data for plotting ---
df_to_plot = df.drop_duplicates(subset=['iso_a3', 'dollar_price']).copy()

# --- Create the plot ---
sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(20, 10)) # Adjusted figure size for more items

# --- Logic for Y-axis positioning ---
# Define y_level_height for vertical separation of stacked items
y_level_height = 0.45  # Adjust this for spacing between circles at the same x

# Group by 'dollar_price' and assign a cumulative count (0, 1, 2...) for items in each group
# This determines the vertical stacking order
df_to_plot['y_offset_group'] = df_to_plot.groupby('dollar_price')['iso_a3'].cumcount()

# --- Iterate through data points and plot flags ---
for _, row in df_to_plot.iterrows():
    x_coord = row['dollar_price']
    iso_a3 = row['iso_a3']
    country_name = row['name']
    
    # Calculate the y-coordinate for the center of the circle
    # (row['y_offset_group'] + 0.5) ensures the first circle (group 0) is nicely above the baseline
    circle_center_y = (row['y_offset_group'] + 0.5) * y_level_height 
    
    line_bottom_y = 0.0  # All lines start from y=0
    line_top_y = circle_center_y # Line goes up to the center of the circle

    iso_a2 = get_iso_a2_code(iso_a3)
    
    if iso_a2:
        print(f"Plotting: {country_name} ({iso_a3}/{iso_a2}) at x={x_coord:.2f}, circle_y={circle_center_y:.2f}")
        
        # Draw the vertical line (zorder=1 to be behind the circle/flag)
        ax.plot([x_coord, x_coord], [line_bottom_y, line_top_y], 
                color='dimgray', linestyle='-', linewidth=1.2, zorder=1)

        flag_img_arr = fetch_flag_image(iso_a2, size_code="w20") # Fetch 20px width flag

        if flag_img_arr is not None:
            # Create an OffsetImage for the flag. Zoom adjusts apparent size.
            imagebox = OffsetImage(flag_img_arr, zoom=0.65) 
            imagebox.image.axes = ax # Crucial for rendering
            
            # Create AnnotationBbox with a circular frame
            ab = AnnotationBbox(imagebox, 
                                (x_coord, circle_center_y), # Positioned at circle_center_y
                                xybox=(0., 0.), 
                                xycoords='data',
                                boxcoords="offset points",
                                frameon=True, # Enable bboxprops to draw the circle
                                bboxprops=dict(boxstyle="circle,pad=0.35", # 'pad' controls circle size relative to image
                                               fc="white",       # Fill color of the circle
                                               ec="darkgray",    # Edge color of the circle
                                               lw=1.0,           # Linewidth of circle edge
                                               alpha=0.9),      # Transparency of the circle
                                pad=0.0, # Outer pad for AnnotationBbox itself (usually 0 for images)
                                zorder=2) # Ensure flag & circle are on top of the line
            ax.add_artist(ab)
        else:
            # Placeholder if flag image failed: draw line and an empty red circle
            ax.plot([x_coord, x_coord], [line_bottom_y, line_top_y], color='red', linestyle='-', linewidth=1.2, zorder=1)
            ax.scatter([x_coord], [circle_center_y], marker='o', facecolors='white', edgecolors='red', s=120, 
                       label='Flag failed to load' if 'Flag failed to load' not in ax.get_legend_handles_labels()[1] else "",
                       zorder=2)
            print(f"  -> Failed to load flag for {country_name}, plotted placeholder circle.")
    else:
        # Placeholder if ISO A2 code not found: draw dashed line and an empty grey circle
        ax.plot([x_coord, x_coord], [line_bottom_y, line_top_y], color='dimgray', linestyle='--', linewidth=1.2, zorder=1)
        ax.scatter([x_coord], [circle_center_y], marker='o', facecolors='lightgray', edgecolors='dimgray', s=120,
                   label='ISO A2 not found' if 'ISO A2 not found' not in ax.get_legend_handles_labels()[1] else "",
                   zorder=2)
        print(f"  -> Could not find ISO A2 for {country_name}, plotted placeholder circle.")

# --- Customize the plot ---
ax.set_xlabel("Big Mac Index (Dollar Price)", fontsize=14)
ax.set_ylabel("") 
ax.set_title("Big Mac Index: Country Flags vs. Dollar Price", fontsize=16)

# Adjust plot limits
if not df_to_plot.empty:
    ax.set_xlim(df_to_plot['dollar_price'].min() - 0.75, df_to_plot['dollar_price'].max() + 0.75)
    # Y-limits: bottom is below 0, top accommodates the highest circle
    # Max y_offset_group determines highest stack. Add 1 to include its full height.
    max_y_for_plot = (df_to_plot['y_offset_group'].max() + 1.0) * y_level_height + (y_level_height * 0.25) # Extra padding at top
    ax.set_ylim(line_bottom_y - (y_level_height * 0.25), max_y_for_plot) # Padding at bottom
else:
    ax.set_xlim(0, 10) 
    ax.set_ylim(-0.1, 1.5)


# Y-axis ticks are generally not needed as y-axis is for layout/stacking
ax.set_yticks([])

# Add a legend for placeholder markers if any were used
handles, labels = ax.get_legend_handles_labels()
if handles: 
    ax.legend(handles, labels, loc='upper right', fontsize=10, framealpha=0.7)

plt.tight_layout()
plt.show()

print("\n--- Important Notes ---")
print("1. Ensure 'pycountry' library is installed (`pip install pycountry`).")
print("2. Requires internet access to download flag images from flagcdn.com.")
print("3. 'zoom' for OffsetImage and 'pad' in bboxprops for AnnotationBbox control flag/circle appearance.")
print("4. 'y_level_height' adjusts vertical spacing of stacked flags.")
print("5. Check console output for errors if flags/placeholders are not as expected.")

# %%
