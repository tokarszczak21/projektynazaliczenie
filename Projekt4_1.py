import matplotlib.pyplot as plt
import numpy  as np



beta = 1
sigma = 1
gamma = 0.1
dt = 0.001
t = np.arange(0,50,0.001)
N = len(t)
s = np.zeros(t.shape[0])
e = np.zeros(t.shape[0])
i = np.zeros(t.shape[0])
r = np.zeros(t.shape[0])

s[0] = 0.99
e[0] = 0.01
i[0] = 0
r[0] = 0



for j in range(1,t.shape[0]):
    s_F1 = dt * (-sigma * i[j-1] * s[j-1])
    e_F1 = dt * ((beta * i[j-1] * s[j-1]) - (sigma * e[j-1]))
    i_F1 = dt * ((sigma * e[j-1]) - (gamma * i[j-1]))
    r_F1 = dt * gamma * i[j-1]

    s_F2 = dt * (-sigma *(i[j-1]+i_F1/2) * (s[j-1]+s_F1/2))
    e_F2 = dt * ((beta * ((i[j-1]+i_F1/2)*(s[j-1]+s_F1/2))-(sigma * (e[j-1]+e_F1/2))))
    i_F2 = dt * (sigma * ((e[j-1]+e_F1/2) - (gamma * (i[j-1]+i_F1/2))))
    r_F2 = dt * (gamma * (i[j-1]+i_F1/2))

    s_F3 = dt * (-sigma *(i[j-1]+i_F2/2) * (s[j-1]+s_F2/2))
    e_F3 = dt * (beta * (((i[j-1]+i_F2/2)*(s[j-1]+s_F2/2))-(sigma * (e[j-1]+e_F2/2))))
    i_F3 = dt * (sigma * ((e[j-1]+e_F2/2) - (gamma * (i[j-1]+i_F2/2))))
    r_F3 = dt * (gamma * (i[j-1]+i_F2/2))

    s_F4 = dt * (-sigma *(i[j-1]+i_F3) * (s[j-1]+s_F3))
    e_F4 = dt * (beta * (((i[j-1]+i_F3)*(s[j-1]+s_F3))-(sigma * (e[j-1]+e_F3))))
    i_F4 = dt * (sigma * ((e[j-1]+e_F3) - (gamma * (i[j-1]+i_F3))))
    r_F4 = dt * (gamma * (i[j-1]+i_F3))

    s[j]=s[j-1]+1/6.*(s_F1 + 2 * s_F2 + 2 * s_F3 + s_F4)
    e[j]=e[j-1]+1/6.*(e_F1 + 2 * e_F2 + 2 * e_F3 + e_F4)
    i[j]=i[j-1]+1/6.*(i_F1 + 2 * i_F2 + 2 * i_F3 + i_F4)
    r[j]=r[j-1]+1/6.*(r_F1 + 2 * r_F2 + 2 * r_F3 + r_F4)
    

plt.plot(t,s,label='Susceptible')
plt.plot(t,e,label='Exposed')
plt.plot(t,i,label='Infectious')
plt.plot(t,r,label='Removed')
plt.ylabel('Liczność populacji')
plt.xlabel('Czas')
plt.legend()
plt.show()
