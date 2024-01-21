import numpy as np
import matplotlib.pyplot as plt
from math import log, exp


K = 100000
r = 0.4 #lamda=r
h = 0.001
t0 = 75
tk=120
t = np.arange(t0,tk,h)
x=np.zeros(t.shape[0])
y = np.zeros(t.shape[0])
x[0] = 10
y[0]= 10

for i in range(1,x.shape[0]):
    x[i] =x[i-1]+h* (r*(x[i-1])*(log(K/(x[i-1]))))

for j in range(1,y.shape[0]):
    y[j] = y[j-1]+h*(r*(1-(y[j-1]/K))*y[j-1]+((h**2)/2)*(r**2)*y[j-1]*(1-(y[j-1]/K))*(1-((2*y[j-1])/K)))




fig = plt.figure()
axes = fig.add_subplot(1,1,1)
axes.plot(t,x, label ='Metoda Gompertza')
axes.plot(t,y, label='Metoda Verhulsta')
axes.set_xlabel('Czas')
axes.set_ylabel('Objętość guza')
plt.legend()
plt.show()
