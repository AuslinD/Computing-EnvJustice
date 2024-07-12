import plotly.express as px
import pandas as pd
import numpy as np
"""
gen_data = pd.read_excel('/home/austin/Downloads/annual_generation_state.xlsx')
#print(data.columns)

gen_data = gen_data[(gen_data.YEAR == 2022)]
gen_data = gen_data[gen_data['TYPE OF PRODUCER'] == 'Total Electric Power Industry']
gen_data = gen_data[gen_data['ENERGY SOURCE'] == 'Total']
gen_data = gen_data[gen_data['STATE'] != 'US-Total']
#print(gen_data)
gen_data.to_csv('~/filtered_genneration.csv')

emi_data = pd.read_excel('/home/austin/Downloads/emission_annual.xlsx')
emi_data = emi_data[emi_data.Year == 2022]
emi_data = emi_data[emi_data['Producer Type'] == 'Total Electric Power Industry']
emi_data = emi_data[emi_data['Energy Source'] == 'All Sources']
emi_data = emi_data[emi_data['State'] != 'US-TOTAL']

emi_data['Nox CO2 Eq'] = emi_data['Nox(Metric Tons)'].multiply(298)
emi_data['Total CO2 Eq'] = emi_data['Nox CO2 Eq'].add(emi_data['CO2(Metric Tons)'])
emi_data.to_csv('~/filtered_emissions.csv')

emi_data = pd.read_csv('~/filtered_emissions.csv')

comb_data = pd.DataFrame()
comb_data['STATE'] = gen_data['STATE']
comb_data['GENERATION (MwH)'] = gen_data['GENERATION(Megawatthours)']

comb_data['CO2 eq Tons'] = emi_data['Total CO2 Eq']

#comb_data.to_csv('combined.csv')
"""

data = pd.read_csv('combined.csv')
data['CO2 eq / MwH'] = data['Total CO2 Eq'] / data['GENERATION (MwH)'] 

fig = px.choropleth(data, locations=data['STATE'], locationmode="USA-states", color='CO2 eq / MwH', scope="usa")
fig.show()
