import pandas as pd 
import plotly.figure_factory as ff 
import csv

df = pd.read_csv("ic-cd.csv")

# fig = ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist = False)
fig1 = ff.create_distplot([df["Ice-cream Sales"].tolist()],["Sale of Ice Cream"],show_hist = False)

# fig.show()
fig1.show()