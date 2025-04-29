# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %%
data_url = 'https://data.cityofnewyork.us/resource/6y5g-5hkj.csv?$limit=50000'

df = pd.read_csv(data_url)

df.head()
# %%
top_10_cities = df['city'].value_counts().nlargest(10).index

top_10_df = df[df['city'].isin(top_10_cities)]

plt.figure(figsize=(10, 6))
sns.countplot(
    data = top_10_df
    , x = 'city'
    , order = top_10_df['city'].value_counts().index
)

plt.xlabel('City', fontsize=14, fontweight='bold')
plt.ylabel('Count of Entries', fontsize=14, fontweight='bold')
plt.title('Bus Delays By City', fontsize=16, fontweight='bold', pad=20)
plt.xticks(rotation=45, fontsize=12, ha='right')

plt.show()
# %%
