import plotly.express as px
import pandas as pd

gen_data = pd.read_excel('/home/austin/Downloads/annual_generation_state.xlsx')
#print(data.columns)

gen_data = gen_data[(gen_data.YEAR == 2022)]
gen_data = gen_data[gen_data['TYPE OF PRODUCER'] == 'Total Electric Power Industry']
gen_data = gen_data[gen_data['ENERGY SOURCE'] == 'Total']
gen_data = gen_data[gen_data['STATE'] != 'US-Total']
#print(gen_data)

emi_data = pd.read_excel('/home/austin/Downloads/emission_annual.xlsx')
emi_data = emi_data.rename(columns={'Year' : 'YEAR', 'State': 'STATE'})
print(emi_data.columns)
emi_data = emi_data[emi_data.YEAR == 2022]
emi_data = emi_data[emi_data['Producer Type'] == 'Total Electric Power Industry']
emi_data = emi_data[emi_data['Energy Source'] == 'All Sources']
emi_data = emi_data[emi_data['STATE'] != 'US-TOTAL']
print(emi_data)

#fig = px.choropleth(gen_data, locations=data['STATE'], locationmode="USA-states", color='GENERATION (Megawatthours)', scope="usa")
#fig.show()
