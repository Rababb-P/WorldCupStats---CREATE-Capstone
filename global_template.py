# GLOBAL CHART TEMPLATE CODE 
# REPLACE POSESSION STUFF IN DOUBLE QUOTATIONS WITH WHATEVER STAT YOU ARE WORKING WITH
# CHANGE TITLES, LABELS ETC
# REPLACE CSV FILE PATH

import matplotlib.pyplot as plt 
import pandas as pd
import os 

os.makedirs("images", exist_ok=True)

df = pd.read_csv(r"/Users/jeevansanchez/create2024/control/Fifa_world_cup_matches.csv")


x = df.index
countr_names = []
statistic = {}


# For percentages 
df["possession team1"] = df["possession team1"].str.rstrip('%').astype('float')
df["possession team2"] = df["possession team2"].str.rstrip('%').astype('float')

for i in range(len(x)):
  if df.loc[i, "team1"] not in countr_names:
    countr_names.append(df.loc[i, "team1"])
    statistic[df.loc[i, "team1"]] = 0
for i in range(len(x)):
  if df.loc[i, "team2"] not in countr_names:
    countr_names.append(df.loc[i, "team2"])
    statistic[df.loc[i, "team2"]] = 0

for i in range(len(x)):
   statistic[df.loc[i, "team1"]]+=df.loc[i, "possession team1"]
   statistic[df.loc[i, "team2"]]+=df.loc[i, "possession team2"]

cols = ['statName']

dfstatistic = pd.DataFrame.from_dict(statistic, orient='index', columns= cols)



dfstatistic.reset_index(inplace=True)
dfstatistic.rename(columns={"index": "Country"}, inplace=True)
y_statistic = dfstatistic['statName']


plt.figure(figsize=(16,14))
plt.plot(dfstatistic["Country"], y_statistic)

plt.xticks(rotation=45, ha='right')
plt.title("Ball Possession")
plt.xlabel("Teams")
plt.ylabel("Ball Posession (%)")


plot_path = os.path.join("images", "possession.png")
plt.savefig(plot_path)
plt.show()
