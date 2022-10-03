import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('random1000pairs.csv')
print(df.head())
plt.scatter(df['corr'], df['di'],c='red')
plt.xlabel('correlation')
plt.ylabel('di')
plt.plot([0,80],[85,5])
