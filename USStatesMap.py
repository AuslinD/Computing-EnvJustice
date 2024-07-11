import plotly.express as px
import pandas as pd

data = pd.read_excel('/home/austin/Downloads/annual_generation_state.xlsx')
print(data.columns)

data = data[(data.YEAR == 2022)]
data = data[data['TYPE OF PRODUCER'] == 'Total Electric Power Industry']
data = data[data['ENERGY SOURCE'] == 'Total']
data = data[data['STATE'] != 'US-Total']
print(data)


fig = px.choropleth(data, locations=data['STATE'], locationmode="USA-states", color='GENERATION (Megawatthours)', scope="usa")
fig.show()
