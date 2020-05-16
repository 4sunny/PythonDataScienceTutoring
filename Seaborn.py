#http://sankeymatic.com/build/
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('matrix.csv', header=None)
df = df.astype(float)
fig, ax = plt.subplots(1,1)
sns.heatmap(df, annot=True, ax=ax, fmt="g")
plt.show()