import matplotlib.pyplot as plt 
import pandas as pd
import os 

os.makedirs("images", exist_ok=True)

df = pd.read_csv('/Users/rababbpannu/Downloads/Fifa_world_cup_matches.csv')


x = df.index
countr_names = []
statistic = {}


for i in range(len(x)):
  if df.loc[i, "team1"] not in countr_names:
    countr_names.append(df.loc[i, "team1"])
    statistic[df.loc[i, "team1"]] = 0
for i in range(len(x)):
  if df.loc[i, "team2"] not in countr_names:
    countr_names.append(df.loc[i, "team2"])
    statistic[df.loc[i, "team2"]] = 0

for i in range(len(x)):
   statistic[df.loc[i, "team1"]]+=df.loc[i, "conceded team1"]
   statistic[df.loc[i, "team2"]]+=df.loc[i, "conceded team2"]

   
  
cols = ['statName']


statistic = pd.DataFrame.from_dict(statistic, orient='index', columns=cols)
y_statistic = statistic["statName"]
statistic.reset_index(inplace=True)
statistic.rename(columns={"index": "Country"}, inplace=True)
x_statistic = []


for i in range(len(y_statistic)):
  x_statistic.append(i)
print(y_statistic)
print(len(y_statistic))

print(len(x_statistic))

plt.figure(figsize=(16,14))
plt.bar(statistic["Country"],y_statistic)
plt.xticks(rotation=45, ha='right')

plt.title("Goals Conceded")


plot_path = os.path.join("images", "conceded.png")
plt.savefig(plot_path)
plt.show()