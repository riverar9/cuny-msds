# %%
import pandas as pd
import seaborn as sns
# %%
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df = pd.read_csv(url, header=None)
df.columns = ['sepal_length','sepal_width','petal_length','petal_width','species']
df.head()
# %%
sns.pairplot(df, hue="species", diag_kind = "kde")
# %%
