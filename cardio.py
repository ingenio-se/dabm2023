import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import math

cwd = os.getcwd()
archivo = cwd + "/libs/ecg_data.csv"
ecg_data = pd.read_csv(archivo)

time = ecg_data['time']
signal = ecg_data['signal']

descripcion = ecg_data['signal'].describe()
#print(descripcion)

promedio = np.mean(ecg_data.signal)
#print(promedio)

#print(ecg_data['signal'].head(50))
#print(ecg_data['signal'].tail(50))

promedio_dinamico = pd.DataFrame.rolling(ecg_data.signal,window=(100)).mean()
#print(promedio_dinamico)

promedio_dinamico =[promedio*1.2 if math.isnan(x) else (x*1.2)  for x in promedio_dinamico]
#print(promedio_dinamico)
ecg_data['promedio_dinamico'] = promedio_dinamico

#deteccion de picos
cont =0
rango=[]
maximosy = []
maximosx = []
for punto in ecg_data.signal :
    if (punto <= ecg_data.promedio_dinamico[cont]) and (len(rango) <1):
        cont+=1
    elif punto > ecg_data.promedio_dinamico[cont]:
        rango.append(punto)
        cont+=1
    else:
        maximo = max(rango)
        maximosy.append(maximo)
        maximox = cont - len(rango) + rango.index(maximo)
        maximosx.append(maximox)

        rango = []
        cont+=1
cont=0
dist=[]
while cont < len(maximosx) -1:
    distancia = maximosx[cont+1] - maximosx[cont]
    distancia = distancia / 100
    dist.append(distancia)
    cont+=1

bpm = 60 / np.mean(dist)

print("BPM:",round(bpm,1))


plt.plot(time,signal)
plt.plot(ecg_data.promedio_dinamico, color="red")
plt.scatter(maximosx,maximosy,color="orange", label=bpm)
plt.xlabel('Time (s)')
plt.ylabel('ECG signal (mV)')
plt.title('ECG Signal Over Time')
plt.legend(loc=4,framealpha = 0.6)
plt.show()
