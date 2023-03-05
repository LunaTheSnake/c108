import pandas as pd
#import plotly.express as px
import plotly.figure_factory as ff

df =pd.read_csv("height.csv")
print(df.head())
fig = ff.create_distplot([df["Height(Inches)"].tolist()], ["Height"])
fig.show()