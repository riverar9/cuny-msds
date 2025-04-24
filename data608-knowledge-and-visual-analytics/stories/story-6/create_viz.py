# %%
import pandas as pd
# %%
df = pd.read_csv(r'data/foodsecurity_state_2023.csv', sep=',', encoding='windows-1252')
df = df.loc[df['Year'] == '2021–2023']
df = df.loc[df['State'] != 'U.S.']

df.head()
# %%
