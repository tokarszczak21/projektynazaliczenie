import matplotlib.pyplot as plt
import numpy as np


#R1 = (beta/gamma)*s[0]
#print(R1)
#dane  z zadania 1 współczynnik R wychodzi większy od 1(jest równy 9.9)(wykres sporządzony w zadaniu 1)

beta2 = 0.61
sigma2 = 1
gamma2 = 3
dt2 = 0.001
t2 = np.arange(0,50,0.001)
N2 = len(t2)
s2 = np.zeros(t2.shape[0])
e2 = np.zeros(t2.shape[0])
i2 = np.zeros(t2.shape[0])
r2 = np.zeros(t2.shape[0])

s2[0] = 0.86
e2[0] = 0.01
i2[0] = 0
r2[0] = 0

R2 = (beta2/gamma2) * s2[0]
print(R2)
for j in range(1,t2.shape[0]):
    s2_F1 = dt2 * (-sigma2 * i2[j-1] * s2[j-1])
    e2_F1 = dt2 * ((beta2 * i2[j-1] * s2[j-1]) - (sigma2 * e2[j-1]))
    i2_F1 = dt2 * ((sigma2 * e2[j-1]) - (gamma2 * i2[j-1]))
    r2_F1 = dt2 * gamma2 * i2[j-1]

    s2_F2 = dt2 * (-sigma2 *(i2[j-1]+i2_F1/2) * (s2[j-1]+s2_F1/2))
    e2_F2 = dt2 * ((beta2 * ((i2[j-1]+i2_F1/2)*(s2[j-1]+s2_F1/2))-(sigma2 * (e2[j-1]+e2_F1/2))))
    i2_F2 = dt2 * (sigma2 * ((e2[j-1]+e2_F1/2) - (gamma2 * (i2[j-1]+i2_F1/2))))
    r2_F2 = dt2 * (gamma2 * (i2[j-1]+i2_F1/2))

    s2_F3 = dt2 * (-sigma2 *(i2[j-1]+i2_F2/2) * (s2[j-1]+s2_F2/2))
    e2_F3 = dt2 * (beta2 * (((i2[j-1]+i2_F2/2)*(s2[j-1]+s2_F2/2))-(sigma2 * (e2[j-1]+e2_F2/2))))
    i2_F3 = dt2 * (sigma2 * ((e2[j-1]+e2_F2/2) - (gamma2 * (i2[j-1]+i2_F2/2))))
    r2_F3 = dt2 * (gamma2 * (i2[j-1]+i2_F2/2))

    s2_F4 = dt2 * (-sigma2 *(i2[j-1]+i2_F3) * (s2[j-1]+s2_F3))
    e2_F4 = dt2 * (beta2 * (((i2[j-1]+i2_F3)*(s2[j-1]+s2_F3))-(sigma2 * (e2[j-1]+e2_F3))))
    i2_F4 = dt2 * (sigma2 * ((e2[j-1]+e2_F3) - (gamma2 * (i2[j-1]+i2_F3))))
    r2_F4 = dt2 * (gamma2 * (i2[j-1]+i2_F3))

    s2[j]=s2[j-1]+1/6.*(s2_F1 + 2 * s2_F2 + 2 * s2_F3 + s2_F4)
    e2[j]=e2[j-1]+1/6.*(e2_F1 + 2 * e2_F2 + 2 * e2_F3 + e2_F4)
    i2[j]=i2[j-1]+1/6.*(i2_F1 + 2 * i2_F2 + 2 * i2_F3 + i2_F4)
    r2[j]=r2[j-1]+1/6.*(r2_F1 + 2 * r2_F2 + 2 * r2_F3 + r2_F4)
    

plt.plot(t2,s2,label='Susceptible')
plt.plot(t2,e2,label='Exposed')
plt.plot(t2,i2,label='Infectious')
plt.plot(t2,r2,label='Removed')
plt.ylabel('Liczność populacji')
plt.xlabel('Czas')
plt.legend()
plt.show()

#Wykresy zmian liczebności zmieniły się znacznie gdy R0 było mniejsze od 1(w programie oznaczone jako R2).wykresy podanych funkcji zmieniają się nieznacznie na danym przedziale.
#Poza tym przedziałem są stałe(gdy epidemia wygaśnie wykresy są stałe)
