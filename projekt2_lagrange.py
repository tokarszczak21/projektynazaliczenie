import numpy as np


data = np.array([[1.0, 3.0], [2.0, 1.0], [3.5, 4.0], [5.0, 0.0], [6.0, 0.5], [9.0, -2.0], [9.5, -3.0]])
start = .5
end   = 10
step = 1000
data = data
lin_x = np.linspace(start, end ,step)

def lagrange_poly():
    l_return = np.ones((data.shape[0], lin_x.shape[0]))
    for i in range(data.shape[0]):
        for j in range(data.shape[0]):
            if j!=i:
                l_return[i,:] *= (lin_x - data[j,0]) / (data[i,0] - data[j,0])
    
    return l_return
l_poly = lagrange_poly()
def wzor_lagrange():
    p_return = np.zeros(lin_x.shape[0])
    for n in range(data.shape[0]):
        p_return += l_poly[n, :] * data[n, 1]
    
    return p_return
