
import pandas as pd
import statistics
import plotly.express as px


from google.colab import files
dataLoad = files.upload()

df = pd.read_csv('savings_data_final.csv')
fig = px.scatter(df, y = 'quant_saved', color = 'rem_any')
fig.show()

import csv
import plotly.graph_objects as pg

with open('savings_data_final.csv', newline = '') as f:
    reader  = csv.reader(f)
    data = list(reader)

data.pop(0)

totalEntries = len(data)

reminder = 0

for i in data:
    if int(i[3]) == 1:
        reminder += 1

fig = pg.Figure(pg.Bar(x = ['reminded', 'not reminded'], y = [reminder, totalEntries - reminder]))

fig.show()


allSavings = []

for a in data:
    allSavings.append(float(a[0]))

mean = statistics.mean(allSavings)
print(mean)

median = statistics.median(allSavings)
print(median)

mode = statistics.mode(allSavings)
print(mode)


notReminded = []
reminded = []

for b in data:
    if int(b[3]) == 1:
        reminded.append(float(b[0]))
    else:
        notReminded.append(float(b[0]))

print("Reminded Peoples Data")
print("Mean", statistics.mean(reminded))
print("Median", statistics.median(reminded))
print("Mode", statistics.mode(reminded))

print("Not Reminded Peoples Data")
print("Mean", statistics.mean(notReminded))
print("Median", statistics.median(notReminded))
print("Mode", statistics.mode(notReminded))



stdAll = statistics.stdev(allSavings)
print("Std Of All", stdAll)

stdRem = statistics.stdev(reminded)
print("Std Of Rem", stdRem)

stdNot = statistics.stdev(notReminded)
print("Std Of Not Rem", stdNot)


import numpy as np

age = []
savings = []

for c in data:
    if float(c[5]) != 0:
        age.append(float(c[5]))
        savings.append(float(c[0]))
cor = np.corrcoef(age, savings)
print("Correlation between age and saving is ", {cor[0,1]})


import plotly.figure_factory as pf

fig = pf.create_distplot([df['quant_saved'].tolist()], ['savings'], show_hist = False)
fig.show()
