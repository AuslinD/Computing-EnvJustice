import plotly.express as px
import pandas as pd
import numpy as np

data = pd.read_csv('combined.csv')
data['CO2 eq (Metric Tons) / MwH'] = data['Total CO2 Eq'] / data['GENERATION (MwH)'] 
#data.to_csv('combined.csv')

fig = px.choropleth(data, locations=data['STATE'], locationmode="USA-states", color='CO2 eq (Metric Tons) / MwH', scope="usa")
fig.show()
