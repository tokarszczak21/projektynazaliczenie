import sklejana3st as sk3
import sklejana1st as sk1
import lagrange as lg
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

data = np.array([[1.0, 3.0], [2.0, 1.0], [3.5, 4.0], [5.0, 0.0], [6.0, 0.5], [9.0, -2.0], [9.5, -3.0]])
x = np.linspace(0,10,1000)
r = sk3.sklejpizde()
t = sk1.S_i()
m = lg.wzor_lagrange()
plt.plot(x, r, label = 'sklejana3st')
plt.plot(x, t, label = 'sklejana1st')
plt.plot(x, m, label = 'Lagrange')
plt.legend()
plt.show()

fun = CubicSpline(data[:, 0], data[:, 1])
fun = fun(x)
plt.plot(x,fun, label='Cubuc Spline')
plt.plot(x, r, label = 'sklejana3st')
plt.legend()
plt.show()
