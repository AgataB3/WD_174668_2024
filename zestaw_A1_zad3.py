import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame(pd.read_csv('automobile.csv', header=0, sep=';', decimal='.'))
df = df.sample(100)
grupa = df.groupby(['Car model']).agg({'Price':['mean']})
grupa.plot(kind='pie', subplots=True, title='Wykres kolowy',
           legend=False, fontsize=14, autopct='%.2f%%', pctdistance=0.8, figsize=(7, 7))
plt.show()
