import pandas as pd
import matplotlib.pyplot as plt
import os
'''
cwd = os.getcwd()
archivo = cwd + "/libs/ecg_data.csv"
ecg_data = pd.read_csv(archivo)

time = ecg_data['time']
signal = ecg_data['signal']

plt.plot(time,signal)
plt.xlabel('Time (s)')
plt.ylabel('ECG signal (mV)')
plt.title('ECG Signal Over Time')
plt.show()


x = [20,25,30,35,40,45,50,55,60]
y = [80,100,125,140,160,180,200,220,240]

plt.scatter(x,y)
plt.title("IMC vs Azucar en sangre")
plt.xlabel('IMC (kg/m2)')
plt.ylabel('Azucar en sangre (md/dL)')
plt.show()


labels = ["Cancer de seno","Cancer de prostata","Cancer de pulmon","Cancer de colon","Otros"]
values = [30,20,15,10,25]

plt.bar(labels,values,color=['red','green','yellow','orange'])
plt.title("Frecuencia de tipo de cáncer")
plt.xlabel("Tipo de cáncer")
plt.ylabel('Porcentaje de paciente(%)')

plt.show()



import numpy as np
data = np.random.rand(5,5)
print(data)

plt.imshow(data,cmap='coolwarm')

plt.title("Correlación de genes")
plt.xlabel('Genes')
plt.ylabel('Genes')

plt.colorbar()
plt.show()


data = [20,22,25,26,26,28,30,31,33,35,40,42,45]

plt.boxplot(data)
plt.title('Distribución de IMC')
plt.ylabel('IMC (kg/m2)')
plt.show()
'''

labels = ["Cirugia","Radiación","Quimioterapia","Otros"]
values=[50,30,15,5]

plt.pie(values,labels=labels)
plt.title("Tipos de procedimientos Médicos")

plt.show()