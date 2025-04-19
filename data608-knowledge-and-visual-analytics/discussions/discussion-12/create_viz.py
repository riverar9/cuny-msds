# %%
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
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

df['Change'] = df['Post-Training'] - df['Pre-Training']

df.head()
# %%
df_melted = df.melt(
    id_vars=['Employee ID', 'Change'],
    var_name='Stage',        
    value_name='Productivity',
    value_vars=['Pre-Training', 'Post-Training'] 
)

df_melted.head()
# %%

plt.figure(figsize=(8, 10))

sns.lineplot(
    data=df_melted,
    x='Stage',          
    y='Productivity',   
    units='Employee ID',
    estimator=None,     
    color='darkgrey',   
    marker=None,        
    linewidth=1.5,      
    alpha=0.6,          
    sort=False          
)

plt.scatter(
    x=['Pre-Training'] * len(df), 
    y=df['Pre-Training'],         
    s=60,                         
    color='skyblue',              
    label='Pre-Training',         
    zorder=3                      
)

colors = ['red' if change < 0 else 'yellow' if change == 0 else 'lightgreen' for change in df['Change']]

plt.scatter(
    x=['Post-Training'] * len(df), 
    y=df['Post-Training'],         
    s=60,                          
    color=colors,                  
    zorder=3                       
)

plt.title("Employee Productivity Change: Pre vs Post Training", fontsize=16, weight='bold', pad=20)
plt.xlabel("Training Stage", fontsize=12)
plt.ylabel("Productivity Score", fontsize=12)

plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

plt.grid(False)

custom_lines = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='skyblue', markersize=8, label='Pre-Training Score'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgreen', markersize=8, label='Post-Training (Improved/Same)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=8, label='Post-Training (Decreased)')
]

plt.legend(handles=custom_lines, title="Score Type") # Place legend automatically

plt.tight_layout()


plt.show()

# %%
