import numpy as np
import pandas as pd

m = [[41.6, 25.4, 17.4, 12.6, 9.49, 7.33, 5.76, 4.59, 3.7, 3.0],
[57.9, 38.9, 25.3, 17.7, 12.9, 9.78, 7.6, 6.01, 4.81, 3.88],
[66.0, 54.0, 36.9, 25.0, 17.8, 13.2, 10.0, 7.83, 6.22, 5.0],
[70.7, 62.5, 50.9, 35.2, 24.7, 17.8, 13.3, 10.3, 8.03, 6.38],
[73.9, 67.8, 59.6, 48.2, 33.8, 24.2, 17.8, 13.5, 10.4, 8.19],
[76.1, 71.4, 65.3, 57.0, 46.0, 32.6, 23.9, 17.7, 13.5, 10.5],
[77.6, 73.9, 69.2, 62.9, 54.8, 44.0, 31.5, 23.5, 17.7, 13.6],
[78.7, 75.8, 72.0, 67.1, 60.9, 52.8, 42.3, 30.6, 23.1, 17.6],
[79.6, 77.2, 74.1, 70.2, 65.3, 59.0, 50.9, 40.7, 29.7, 22.7],
[80.4, 78.3, 75.7, 72.6, 68.6, 63.6, 57.3, 49.2, 39.3, 29.0]]
np.array(m)
np.arange(10)

df = pd.DataFrame(m)

# Reading the csv with panda, since data is separated by semicolon we specify delimiter ';'
data = pd.read_csv("./student-mat.csv", sep=';')

# Specifying the attributes we want to see
data = data[['G1', 'G2', 'G3', 'studytime', 'absences', 'failures']]

for i, row in data.iterrows():
    if pd.isna(row.values[1]):
        print(row)
        data.drop(i, axis=0)


'''
# Gotta specify a label, which is what we will attempt to predict with our linear regression ML
predict = "G3"

# creating data frame x and y
x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
#needs xl lib
xlDF = pd.read_excel(open('Sample_xl.xlsx','rb'))
print(xlDF)
'''