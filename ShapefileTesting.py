import geopandas as gpd
import matplotlib.pyplot as plt

fp = "~/Downloads/SI_Shapefile/SI_Shapefile.shp"

map_df = gpd.read_file(fp)
map_df.plot()
plt.show()
