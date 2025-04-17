# %%
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
# %%
data = {
    "Employee ID": list(range(1, 21)),
    "Pre-Training": [
        65, 70, 55, 68, 77, 62, 55, 80, 78, 69,
        60, 67, 71, 55, 73, 64, 68, 75, 66, 70
    ],
    "Post-Training": [
        72, 85, 60, 75, 80, 65, 50, 90, 82, 74,
        62, 70, 75, 58, 78, 70, 72, 77, 68, 76
    ]
}

df = pd.DataFrame(data)

df.head()
# %%
df_melted = df.melt(
    id_vars='Employee ID', 
    var_name='Stage',
    value_name='Productivity'
)
df_melted.head()
# %%
plt.figure(figsize=(8, 6))
sns.set_style("whitegrid")
sns.boxplot(data=df_melted, x="Stage", y="Productivity", palette=['white','white'], width=0.5)
sns.despine()

plt.title("Productivity Before vs After Training", fontsize=14, weight='bold')
plt.xlabel("")
plt.ylabel("Productivity Score", fontsize=12)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.grid(False)
plt.tight_layout()
plt.show()
# %%
bar_width = 0.35
index = df["Employee ID"]

plt.bar(index - bar_width / 2, df["Pre-Training"], bar_width, label='Pre-Training', color='orange')
plt.bar(index + bar_width / 2, df["Post-Training"], bar_width, label='Post-Training', color='green')

# Average line plot to show the trend
average_pre = df["Pre-Training"].mean()
average_post = df["Post-Training"].mean()

plt.axhline(y=average_pre, color='orange', linestyle='--', label=f"Avg Pre-Training ({average_pre:.2f})")
plt.axhline(y=average_post, color='green', linestyle='--', label=f"Avg Post-Training ({average_post:.2f})")

# Customizing the plot
plt.title("Productivity Changes Pre- and Post-Training", fontsize=14)
plt.xlabel("Employee ID")
plt.ylabel("Productivity Score")
plt.xticks(index, index)
plt.legend()
plt.tight_layout()

# Show plot
plt.show()
# %%
