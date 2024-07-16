import plotly.express as px
import pandas as pd
import numpy as np

gen_data = pd.read_excel('/home/austin/Downloads/annual_generation_state.xlsx')
#print(data.columns)

gen_data = gen_data[(gen_data.YEAR == 2022)]
gen_data = gen_data[gen_data['TYPE OF PRODUCER'] == 'Total Electric Power Industry']
gen_data['GENERATION(TWh)'] = gen_data['GENERATION(Megawatthours)'] / 1000000.0

gen_data.to_csv('filtered_generation_2022.csv')
