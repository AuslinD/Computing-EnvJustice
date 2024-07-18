import geopandas as gpd
import matplotlib.pyplot as plt

fp = "WBDHU8.shp"

map_df = gpd.read_file(fp)
map_df.plot()
plt.show()
