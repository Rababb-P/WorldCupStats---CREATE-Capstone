# Shots assists/passes target scatter plot

import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import os 

os.makedirs("images", exist_ok=True)

df = pd.read_csv(r"C:\Users\Jeevan\VSCode\uoft_create\Fifa_world_cup_matches.csv")

games_played_team1 = df['team1'].value_counts()
games_played_team2 = df['team2'].value_counts()

games_played = games_played_team1.add(games_played_team2, fill_value=0)

# dict team : 0
statistic = {team:{'passes':0, 'assists': 0} for team in df ['team1'].unique()}

for i in range(len(df)):
    statistic[df.loc[i, "team1"]]['assists']+=df.loc[i,"assists team1"]
    statistic[df.loc[i, "team2"]]['assists']+=df.loc[i,"assists team2"]

for i in range(len(df)):
    statistic[df.loc[i, "team1"]]['passes']+=df.loc[i,"passes completed team1"]
    statistic[df.loc[i, "team2"]]['passes']+=df.loc[i,"passes completed team2"]

joined_stats = pd.DataFrame.from_dict(statistic, orient='index').reset_index()
joined_stats = joined_stats.rename(columns = {'index' : 'team'})


joined_stats['games_played'] = joined_stats['team'].map(games_played)
joined_stats['avg_passes'] = round(joined_stats['passes'] / joined_stats['games_played'])

data = joined_stats[['avg_passes', 'assists']]

print(data)


# Scatter plot


plt.show()