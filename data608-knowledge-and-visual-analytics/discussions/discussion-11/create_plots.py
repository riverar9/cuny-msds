# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %%
df = pd.read_csv('Weekly_U.S._Product_Supplied_of_Finished_Motor_Gasoline.csv', skiprows=5, parse_dates=['week'], names=['week','fmg'])

df = df.loc[df['week'] >= '2000-01-01']

df = df.loc[df['week'] < '2020-01-01']

df.head()
# %%
sns.lineplot(df, x='week',y='fmg')
plt.title('Weekly Total of Finished Motor Gasoline (FMG) Supplied')
plt.xlabel('Week')
plt.ylabel('FMG (1k Barrels/Day)')
# %%
rolling_window = 4
df['7d_avg_fmg'] = df['fmg'].rolling(window=rolling_window).mean()

sns.lineplot(df, x='week',y='7d_avg_fmg')
plt.title(f'{rolling_window} Week Rolling Average of Finished Motor Gasoline (FMG) Supplied')
plt.xlabel('Week')
plt.ylabel('FMG (1k Barrels/Day)')
# %%
df['1y_avg_fmg'] = df['fmg'].rolling(window=52).mean()

sns.lineplot(df, x='week',y='1y_avg_fmg')
plt.title('Yearly Rolling Average of Finished Motor Gasoline (FMG) Supplied')
plt.xlabel('Week')
plt.ylabel('FMG (1k Barrels/Day)')
# %%
