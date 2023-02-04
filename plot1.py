import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('FootballStats.csv',delimiter=',')
data[0:20].plot(x='squad', y='goals_for')
plt.xticks(range(len(data[0:20])), data['squad'][0:20], rotation=90)
plt.show()
