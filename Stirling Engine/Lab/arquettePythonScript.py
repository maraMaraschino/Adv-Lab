import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os



data = pd.read_csv("run1.csv",header=0, 
                   names=["time", "angle", "volume", "pressure","temp1", "temp2"])

time = data['time']
angle = data['angle']
volume = data['volume']
pressure = data['pressure']
heaterTemp = data['temp1']
heatSinkTemp= data['temp2']

lowSortingPres = np.zeros(len(pressure))

for i, pres in enumerate(pressure):
    if (i+1) <= len(pressure) - 1:
        if pressure[i+1] >= pres:
            lowSortingPres[i] = pres
        elif pressure[i+1] <= pres:
            lowSortingPres[i] = (pres - pressure[i+1]) + pres
    else:
        lowSortingPres[i] = 0
        break

highSortingPres = np.zeros(len(pressure))

for i, pres in enumerate(pressure):
    if (i+1) <= len(pressure) - 1:
        if pressure[i+1] <= pres:
            highSortingPres[i] = pres
        elif pressure[i+1] >= pres:
            highSortingPres[i] = 0
    else:
        highSortingPres[i] = 0
        break

plt.plot(volume,highSortingPres)
plt.plot(volume, lowSortingPres)
plt.show()
