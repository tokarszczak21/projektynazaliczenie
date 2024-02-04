import numpy as np
import matplotlib.pyplot as plt
from math import log, exp


#zadanie 2
#Podpuynkt A
epsi1 = 1.25
epsi2 = 0.5
gamma1 = 0.5
gamma2 = 0.2
h1 = 0.1
h2 = 0.2
t0 = 0
tk = 10
h =0.001
t = np.arange(t0,tk,h)

N1 = np.zeros(t.shape[0])
N2 = np.zeros(t.shape[0])
N1[0] = 3
N2[0] = 4

for i in range(1,N1.shape[0]):
    N1[i] = N1[i-1] + (h * (epsi1 - (gamma1 * ((h1*N1[i-1]) + (h2*N2[i-1])))) * N1[i-1])
    N2[i] = N2[i-1] + (h * (epsi2 - (gamma2 * ((h1*N1[i-1]) + (h2*N2[i-1])))) * N2[i-1])

fig = plt.figure(figsize=(8,8))
axes = fig.add_subplot(1,1,1)
axes.plot(t,N1, label ='Populacja 1')
axes.plot(t,N2, label ='Populacja 2')
axes.set_xlabel('Czas')
axes.set_ylabel('Liczność populacji')
plt.legend()
plt.show()
#Populacja pierwsza początkowo ma mniejszą liczność niż populacja 2, ale wielkość tej populacji rośnie znacznie szybciej niż populacji drugiej.
#Obie populacje ostatecznie mają punkty graniczne ale mają one różne wartości
#Podpunkt b
epsi3 = 5
epsi4 = 5
gamma3 = 4
gamma4= 8
h3 = 1
h4 = 4
t0 = 0
tk = 10
h = 0.001
t = np.arange(t0,tk,h)

N3 = np.zeros(t.shape[0])
N4 = np.zeros(t.shape[0])
N3[0] = 3
N4[0] = 4

for i in range(1,N3.shape[0]):
    N3[i] = N3[i-1] + (h * (epsi3 - (gamma3 * ((h3*N3[i-1]) + (h4*N4[i-1])))) * N3[i-1])
    N4[i] = N4[i-1] + (h * (epsi4 - (gamma4 * ((h3*N3[i-1]) + (h4*N4[i-1])))) * N4[i-1])

fig = plt.figure(figsize=(8,8))
axes = fig.add_subplot(1,1,1)
axes.plot(t,N3, label ='Populacja 1')
axes.plot(t,N4, label ='Populacja 2')
axes.set_xlabel('Czas')
axes.set_ylabel('Drapieżnicy')
plt.legend()
plt.show()
#Liczności populacji maleją w czasiebardzo intensywnie, populacja druga osiąga liczność populacji ostateczną równą 0, zaś końcowa liczność populacji 1 wynosi ok.1.25
#Zadanie 3 
epsi1 = 0.8
epsi2 = 0.4
gamma1 = 1
gamma2 = 0.5
h1 = 0.3
h2 = 0.4
t0 = 0
tk = 15
h = 0.001

t = np.arange(t0,tk,h)
N1_1 = np.zeros(t.shape[0])
N1_2 = np.zeros(t.shape[0])
N2_1 = np.zeros(t.shape[0])
N2_2 = np.zeros(t.shape[0])
N3_1 = np.zeros(t.shape[0])
N3_2 = np.zeros(t.shape[0])

N1_1[0] = 4
N1_2[0] = 8
N2_1[0] = 8
N2_2[0] = 8
N3_1[0] = 12
N3_2[0] = 8


for i in range(1, N1_1.shape[0]):
    N1_1[i] = N1_1[i-1] + (h * (epsi1 - (gamma1 * ((h1*N1_1[i-1]) + (h2*N1_2[i-1])))) * N1_1[i-1])
    N1_2[i] = N1_2[i-1] + (h * (epsi2 - (gamma2 * ((h1*N1_1[i-1]) + (h2*N1_2[i-1])))) * N1_2[i-1])
    N2_1[i] = N2_1[i-1] + (h * (epsi1 - (gamma1 * ((h1*N2_1[i-1]) + (h2*N2_2[i-1])))) * N2_1[i-1])
    N2_2[i] = N2_2[i-1] + (h * (epsi2 - (gamma2 * ((h1*N2_1[i-1]) + (h2*N2_2[i-1])))) * N2_2[i-1])
    N3_1[i] = N3_1[i-1] + (h * (epsi1 - (gamma1 * ((h1*N3_1[i-1]) + (h2*N3_2[i-1])))) * N3_1[i-1])
    N3_2[i] = N3_2[i-1] + (h * (epsi2 - (gamma2 * ((h1*N3_1[i-1]) + (h2*N3_2[i-1])))) * N3_2[i-1])
    
x=np.linspace(0,12,20)
y=np.linspace(0,10,20)
X,Y=np.meshgrid(x,y)
dX=np.zeros(X.shape)
dY=np.zeros(Y.shape)
for i in range(X.shape[0]):
    for j in range(Y.shape[0]):
        dX[i,j] = (epsi1 - (gamma1 * ((h1*X[i,j]) + (h2*Y[i,j])))) * X[i,j]
        dY[i,j] = (epsi2 - (gamma2 * ((h1*X[i,j]) + (h2*Y[i,j])))) * Y[i,j]

fig = plt.figure(figsize=(8,8))
axes = fig.add_subplot(1,1,1)
axes.plot(N1_1,N1_2, label ='1')
axes.plot(N2_1,N2_2, label ='2')
axes.plot(N3_1,N3_2, label ='3')
plt.quiver(X,Y,dX,dY,color='b')
plt.plot(N1_1,N1_2, color='k')
axes.set_xlabel('Wielkość populacji 1')
axes.set_ylabel('Wielkość populacji 2')
plt.legend()
plt.show()
#Im większa liczność populacji 1 na początku tym szybciej maleje liczność populacji 2.  Mówią o tym długośći wektorów na wykresie(są dłuższe i  większe są populacje. 
