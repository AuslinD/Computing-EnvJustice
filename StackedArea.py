import pandas as pd
import matplotlib.pyplot as plt

file_path = 'ArizonaOverTime.csv'
df = pd.read_csv(file_path)

df = df[df['ENERGY SOURCE'] != 'Other']
df = df[df['ENERGY SOURCE'] != 'Total']
df = df[df['ENERGY SOURCE'] != 'Pumped Storage']
df = df[df['ENERGY SOURCE'] != 'Petroleum']
df = df[df['ENERGY SOURCE'] != 'Other Biomass']
df = df[df['ENERGY SOURCE'] != 'Wood and Wood Derived Fuels']



df = df.groupby(['YEAR', 'ENERGY SOURCE'])['GENERATION(Megawatthours)'].sum().reset_index()

pivot_df = df.pivot(index='YEAR', columns='ENERGY SOURCE', values='GENERATION(Megawatthours)')
pivot_df.to_csv('test.csv')

order = ['Nuclear', 'Hydroelectric Conventional', 'Solar Thermal and Photovoltaic', 'Wind', 'Natural Gas', 'Coal']

ordered_columns = [source for source in order if source in pivot_df.columns]
pivot_df = pivot_df[ordered_columns]

pivot_df.plot(kind='area', stacked=True)




plt.title('Stacked Area Chart of Energy Generation by Source')
plt.xlabel('Year')
plt.ylabel('Generation (Megawatthours)')
plt.legend(title='Energy Source')
plt.grid(True)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.rc('font', size=14)  
plt.rc('axes', titlesize=14)
plt.rc('axes', labelsize=14)
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)

plt.tight_layout()
plt.show()
