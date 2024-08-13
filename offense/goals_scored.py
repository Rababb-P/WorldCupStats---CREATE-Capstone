import matplotlib.pyplot as plt 
import pandas as pd
import os 

os.makedirs("images", exist_ok=True)

df = pd.read_csv(r"/Users/jeevansanchez/create2024/Fifa_world_cup_matches.csv")
# change inner brackets to "Fifa_world_cup_matches.csv"

x = df.index
countr_names = []
goals_scored = {}
defensive_pressures = []

for i in range(len(x)):
  if df.loc[i, "team1"] not in countr_names:
    countr_names.append(df.loc[i, "team1"])
    goals_scored[df.loc[i, "team1"]] = 0
for i in range(len(x)):
  if df.loc[i, "team2"] not in countr_names:
    countr_names.append(df.loc[i, "team2"])
    goals_scored[df.loc[i, "team2"]] = 0
for i in range(len(x)):
  goals_scored[df.loc[i, "team1"]]+=df.loc[i, "number of goals team1"]
  goals_scored[df.loc[i, "team2"]]+=df.loc[i, "number of goals team2"]
cols = ['Goals scored']


dfgoals_scored = pd.DataFrame.from_dict(goals_scored, orient='index', columns=cols)
ygoals_scored = dfgoals_scored["Goals scored"]
dfgoals_scored.reset_index(inplace=True)
dfgoals_scored.rename(columns={"index": "Country"}, inplace=True)
xgoals_scored = []


for i in range(len(ygoals_scored)):
  xgoals_scored.append(i)
print(ygoals_scored)
print(len(ygoals_scored))

print(len(xgoals_scored))

plt.figure(figsize=(16,14))
plt.bar(dfgoals_scored["Country"],ygoals_scored)
plt.xticks(rotation=45, ha='right')

plt.title("Tournament Goals Scored")
plt.xlabel("Teams")
plt.ylabel("Goals Scored")


plot_path = os.path.join("images", "goals.png")
plt.savefig(plot_path)
plt.show()
