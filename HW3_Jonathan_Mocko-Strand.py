###########################################################
##                                                       ##
##    Jonathan Mocko-Strand                              ##
##    Dept. of Geology & Geophysics, TAMU. 2013-10-15    ##
##    Python for Geoscientists                           ##
##    Homework Assignment 3                              ##
##                                                       ##
###########################################################

##This script will import windspeed data from apdrc.soest.
##hawaii and create a map focused on the northern polar region.
##The script will also plot the wind speed of 2001 on a graph.

##########################################################
##    Plot Windspeed on Map of Northern Polar Region    ##
##########################################################

import netCDF4
from datetime import datetime
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

netCDF = netCDF4.Dataset('http://apdrc.soest.hawaii.edu:80/dods/public_data/satellite_product/QSCAT/qscat_clima')

sp      = netCDF.variables['sp'][0,:]
lat     = netCDF.variables['lat'][:]
lon     = netCDF.variables['lon'][:]
time    = netCDF.variables['time']
lon,lat = np.meshgrid(lon,lat)

m = Basemap(llcrnrlon=177,llcrnrlat=45,
            urcrnrlon=91,urcrnrlat=75,
            projection='npstere',
            resolution='l',
            lon_0=0, boundinglat=40)
            
x,y = m(lon,lat)

m.drawmapboundary(color='k')
m.drawcoastlines()        
m.fillcontinents(color='0.8', lake_color='None', ax=None, zorder=None, alpha=None) 
m.drawcoastlines(linewidth = 0.3)
m.drawmeridians(np.arange(-360,360,10),labels=[1,0,0,1],fontsize=7)
m.drawparallels(np.arange(30,100,10),labels=[0,1,1,0],fontsize=7)

plt.contourf(x, y, sp, np.arange(0, 25.0, 1.0), cmap=plt.cm.jet)
#plt.colorbar(orientation='horizontal', drawedges='False')
plt.colorbar(drawedges='False')
plt.title('Windspeed Over the Polar North Water Bodies [$m / s$]\n',fontsize=18)
plt.show()
plt.savefig('HW3_Map_Jonathan_Mocko-Strand.pdf')
plt.close("all")


###################################
##    Plot Windspeed on Graph    ##
###################################


import netCDF4
import matplotlib.pyplot as plt
import pandas as pd

netCDF = netCDF4.Dataset('http://apdrc.soest.hawaii.edu:80/dods/public_data/satellite_product/QSCAT/qscat_clima')

time = netCDF.variables['time']
sp = netCDF.variables['sp'][:500,140,0]


data_range = pd.date_range('01/2000',periods= sp.size, freq='M')
series = pd.Series(sp,index = data_range)

series.plot(figsize=(16.0, 8.0),legend = False)
plt.title('Windspeed Over the Polar North Water Bodies [$m / s$]\n', fontsize =14)
plt.xlabel('Time [Year]',fontsize =14)
plt.ylabel('Windspeed [$m / s$]',fontsize =14)
plt.show()
plt.savefig('HW3_Plot_Jonathan_Mocko-Strand.pdf')
plt.close("all")
