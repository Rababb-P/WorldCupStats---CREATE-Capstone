# Defensive Pressure Graph

import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import os 

os.makedirs("images", exist_ok=True)

df = pd.read_csv(r"C:\Users\Jeevan\VSCode\uoft_create\Fifa_world_cup_matches.csv")

df["possession team1"] = df["possession team1"].str.rstrip('%').astype('float')
df["possession team2"] = df["possession team2"].str.rstrip('%').astype('float')

games_played_team1 = df['team1'].value_counts()
games_played_team2 = df['team2'].value_counts()
total_games_played = games_played_team1.add(games_played_team2, fill_value=0)

possession = {}
games_played = {}


for i in range(len(df)):
    team1 = df.loc[i, "team1"]
    team2 = df.loc[i, "team2"]

    if team1 not in possession:
        possession[team1] = 0
        games_played[team1] = 0
    if team2 not in possession:
        possession[team2] = 0
        games_played[team2] = 0

    possession[team1] += df.loc[i, "possession team1"]
    possession[team2] += df.loc[i, "possession team2"]

    games_played[team1] += 1
    games_played[team2] += 1


df_possession = pd.DataFrame.from_dict(possession, orient='index', columns=['Total Possession'])
df_games_played = pd.DataFrame.from_dict(games_played, orient='index', columns=['Games Played'])

dfstatistic = df_possession.join(df_games_played)
dfstatistic['Average Possession'] = dfstatistic['Total Possession'] / dfstatistic['Games Played']

dfstatistic.reset_index(inplace=True)
dfstatistic.rename(columns={"index": "Country"}, inplace=True)

data = dfstatistic[['Country', 'Average Possession']]
print(round(data))

plt.figure(figsize=(16,19))
plt.bar(dfstatistic["Country"], dfstatistic['Average Possession'], color='skyblue')

plt.xticks(rotation=45, ha='right')
plt.title("Average Posession")
plt.xlabel("Teams")
plt.ylabel("Posession (%)")


plot_path = os.path.join("images", "possession.png")
plt.savefig(plot_path)
plt.show()
