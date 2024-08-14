# Shots on/off target scatter plot

import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import os 

os.makedirs("images", exist_ok=True)

df = pd.read_csv(r"C:\Users\Jeevan\VSCode\uoft_create\Fifa_world_cup_matches.csv")

# dict team : 0
statistic = {team:{'on_target':0, 'off_target': 0} for team in df ['team1'].unique()}

for i in range(len(df)):
    statistic[df.loc[i, "team1"]]['on_target']+=df.loc[i,"on target attempts team1"]
    statistic[df.loc[i, "team2"]]['on_target']+=df.loc[i,"on target attempts team2"]

# off target
for i in range(len(df)):
    statistic[df.loc[i, "team1"]]['off_target']+=df.loc[i,"off target attempts team1"]
    statistic[df.loc[i, "team2"]]['off_target']+=df.loc[i,"off target attempts team2"]


joined_stats = pd.DataFrame.from_dict(statistic, orient='index').reset_index()
joined_stats = joined_stats.rename(columns = {'index' : 'team'})
print(joined_stats)


# Scatter plot


plt.show()