import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv("run1.csv",header=0, 
                   names=["time", "angle", "volume", "pressure","temp1", "temp2"])

time = data['time']
angle = data['angle']
volume = data['volume']
pressure = data['pressure']
heaterTemp = data['temp1']
heatSinkTemp= data['temp2']


sortingPres = np.zeros(len(pressure))

for i, pres in enumerate(pressure):
    if pres[i+1] < pres[i]:
        sortingPres[i] = pres[i]
    elif pres[i+1] > pres[i]:
        sortingPres[i] = 0


plt.plot(volume,sortingPres)
plt.show()
