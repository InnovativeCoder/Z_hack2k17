#import importlib
#mpl_toolkits = importlib.import_module('mpl_toolkits')
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap()
m.drawcoastlines(linewidth=0.2,color='black')
m.drawcountries(linewidth=0.2, color='black', zorder=20)
#m.bluemarble()
m.drawlsmask(land_color='coral',ocean_color='aqua',lakes=True)

lons = [2.1734, -9.1393, 28.9784,12.4964,33.4299]
lats = [41.3851, 38.7223, 41.0082,41.9028,35.1264]
x,y = m(lons, lats)
m.plot(x, y, 'go', markersize=10)
labels = ['Spain', 'Portugal', 'Istanbul','Italy','Cyprus']
for label, xpt, ypt in zip(labels, x, y):
    plt.text(xpt, ypt, label,fontsize=7)

lons1 = [-95.7129, 113.552971, -7.0926,-51.9253,133.7751]
lats1 = [37.0902, 22.210928, 31.7917,-14.2350,-25.2744]
x1,y1 = m(lons1, lats1)
m.plot(x1, y1, 'wo', markersize=18)
labels1 = ['USA', 'China', 'Morocco','Brazil','Australia']
for label, xpt, ypt in zip(labels1, x1, y1):
    plt.text(xpt, ypt, label,fontsize=14)

plt.show()
plt.savefig('test.png')
