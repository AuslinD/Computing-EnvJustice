import plotly.express as px
import pandas as pd
import numpy as np

file_path = '/home/austin/Downloads/annual_generation_state.xlsx'

gen_data = pd.read_excel(file_path)
#print(data.columns)

gen_data = gen_data[(gen_data.YEAR == 2022)]
gen_data = gen_data[gen_data['TYPE OF PRODUCER'] == 'Total Electric Power Industry']
gen_data['GENERATION(TWh)'] = gen_data['GENERATION(Megawatthours)'] / 1000000.0

gen_data.to_csv('filtered_generation_2022.csv')

gen_data = gen_data[gen_data['ENERGY SOURCE'] == 'Total']
gen_data = gen_data[gen_data['STATE'] != 'US-Total']

fig = px.choropleth(gen_data, locations=gen_data['STATE'], locationmode = "USA-states", color='GENERATION(TWh)', scope="usa")
fig.show()
