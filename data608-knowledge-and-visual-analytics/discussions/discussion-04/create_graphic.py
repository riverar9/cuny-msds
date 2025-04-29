# %%
"""
In this context, we are looking to verify data actualizations for an ongoing production model.
The audience here are marketing analytics leaders who are data literate and data scientists who are concerned about how any changes in historical data impacts the accepted model.
They are to understand what kind of changes they can expect from the model and if there are any new preprocessing steps necessary.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# %%
df = pd.read_csv('Media Spend Data.csv', parse_dates=['Calendar_Week'])

df.columns = map(str.lower, df.columns)

df = df[['insert_date','calendar_week','overall_views','sales']]

# Calculate metric in thousands
df['views_in_thousands'] = df['overall_views'] / 1000
df['sales_in_thousands'] = round(df['sales'] / 1000,2)

# Modify metric date to be in the YYYY-MM-DD format
df['insert_date'] = pd.to_datetime(df['insert_date']).dt.strftime('%Y-%m-%d')

df = df.loc[df['calendar_week'] >= '2019-01-01']

df.head()
# %%

# Notes:
#   - Have each ramp up and peak documented
#   - If there isn't a christmas peak, then simply create a new one and relabel it
#   - sales and overall_views change between insert_dates

plt.figure(figsize=(8, 5))
sns.lineplot(
    data=df.loc[df['calendar_week'] >= '2019-01-01']
    , x='calendar_week'
    , y='sales_in_thousands'
    , hue='insert_date'
    , palette = {
        '2019-10-26'    : '#D55E00',
        '2020-01-18'    : 'blue',
    }
)

# Add line and annotation for 2019 Black Friday
plt.axvline(
    pd.Timestamp('2019-11-30')
    , color='gray'
    , linestyle='dashed'
    , alpha=0.7
)

plt.text(
    pd.Timestamp('2019-12-01')
    , .15 * max(df['sales_in_thousands'])
    ,"Black Friday"
    , rotation=0
    , verticalalignment='center'
    , fontsize=10
    , color='black'
)

# Add line and annotation the first divergence
plt.axvline(
    pd.Timestamp('2019-08-03')
    , color='gray'
    , linestyle='dashed'
    , alpha=0.7
)

plt.text(
    pd.Timestamp('2019-08-05')
    , 0.6 * max(df['sales_in_thousands'])
    ,"Actualization\nBegins"
    , rotation=0
    , verticalalignment='center'
    , fontsize=10
    , color='black'
)

# Compute the 95% confidence interval
mean_sales = df.loc[df['calendar_week'] <= '2019-10-26']['sales_in_thousands'].mean()
std_sales = df.loc[df['calendar_week'] <= '2019-10-26']['sales_in_thousands'].std()
lower_bound = mean_sales - 1.5 * std_sales  # Lower bound
upper_bound = mean_sales + 1.5 * std_sales  # Upper bound

# Add horizontal shaded confidence interval
plt.fill_between(
    df['calendar_week'],  # X values
    lower_bound,          # Lower 95% bound
    upper_bound,          # Upper 95% bound
    color='lightgrey',    # Fill color
    alpha=0.3,            # Transparency
    label='95% CI'
)

# Create the model redo time period
plt.axvspan(
    pd.Timestamp('2019-10-01')
    , pd.Timestamp('2019-10-26')
    , color='#E69F00'
    , alpha=0.3
    , label='Model Update Required'
)


# Format y-axis in thousands
plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter("{x:,.0f}K"))

plt.xlabel('')
plt.ylabel('Orders (K)')
plt.legend(title='Version', bbox_to_anchor=(1.05, 1), loc='upper left', labelspacing=1.2)
plt.xticks(rotation=45)
plt.title('Impact of Sales Data Actualizations (2019-2020)')

plt.show()
# %%
