# %%
import pandas as pd
import os
# %%
df = pd.read_excel('story-1-data.xlsx')
df.head()
# %%
df.describe()
# %%
df.dtypes
# %%
df['Political Affiliation'].value_counts()
# %%
