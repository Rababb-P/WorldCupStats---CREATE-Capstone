
# Defensive Pressure Graph

import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import os 
import matplotlib.font_manager as fm

os.makedirs("images", exist_ok=True)

df = pd.read_csv(r"/Users/jeevansanchez/create2024/Fifa_world_cup_matches.csv")

font_path = '/Users/jeevansanchez/Downloads/Poppins/Poppins-SemiBold copy.ttf'
prop = fm.FontProperties(fname=font_path)

games_played_team1 = df['team1'].value_counts()
games_played_team2 = df['team2'].value_counts()
total_games_played = games_played_team1.add(games_played_team2, fill_value=0)

countr_names = []
defensive_pressures = {}
games_played = {}


for i in range(len(df)):
    team1 = df.loc[i, "team1"]
    team2 = df.loc[i, "team2"]

    if team1 not in defensive_pressures:
        defensive_pressures[team1] = 0
        games_played[team1] = 0
    if team2 not in defensive_pressures:
        defensive_pressures[team2] = 0
        games_played[team2] = 0

    defensive_pressures[team1] += df.loc[i, "defensive pressures applied team1"]
    defensive_pressures[team2] += df.loc[i, "defensive pressures applied team2"]

    games_played[team1] += 1
    games_played[team2] += 1


df_defensive_pressures = pd.DataFrame.from_dict(defensive_pressures, orient='index', columns=['Total Defensive Pressure'])
df_games_played = pd.DataFrame.from_dict(games_played, orient='index', columns=['Games Played'])

dfstatistic = df_defensive_pressures.join(df_games_played)
dfstatistic['Average Defensive Pressure'] = dfstatistic['Total Defensive Pressure'] / dfstatistic['Games Played']

dfstatistic.reset_index(inplace=True)
dfstatistic.rename(columns={"index": "Country"}, inplace=True)

data = dfstatistic[['Country', 'Average Defensive Pressure']]
print(round(data))


plt.figure(figsize=(16,19), facecolor= 'black')
plt.bar(dfstatistic["Country"], dfstatistic['Average Defensive Pressure'], color='#f8f6ee')
plt.gca().set_facecolor('black')
plt.gca().spines['bottom'].set_color('white')
plt.gca().spines['left'].set_color('white')

plt.xticks(rotation=45, ha='right', color = 'white')
plt.title("Average Defensive Pressures Applied", fontproperties = prop, fontsize = 22, color = 'white' )
plt.xlabel("Teams", fontproperties = prop, fontsize = 22, color = 'white' )
plt.ylabel("Defensive Pressure", fontproperties = prop, fontsize = 22, color = 'white' )


plot_path = os.path.join("images", "defensive_pressures.png")
plt.savefig(plot_path)
plt.show()
