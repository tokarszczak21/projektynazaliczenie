import numpy as np
import matplotlib.pyplot as plt

data = np.array([[1.0, 3.0], [2.0, 1.0], [3.5, 4.0], [5.0, 0.0], [6.0, 0.5], [9.0, -2.0], [9.5, -3.0]]) #[t,y]

def h_i(n):
    h_return = np.zeros(n)
    for i in range(n):
        h_return[i] = data[i+1, 0] - data[i,0]
    
    return h_return

def b_i(n):
    b_return = np.zeros(n)
    h_v = h_i(n)
    for i in range(n):
        b_return[i] = (6/h_v[i])*(data[i+1, 1] - data[i, 1])
    
    return b_return

def u_i(n):
    h_v=h_i(n)
    u_return = np.zeros(n-1)
    u1 = 2*( h_v[0]+h_v[1])
    u_return[0] = u1
    for i in range(1, n-1):
        u_return[i]= 2 * (h_v[i]+h_v[i+1]) - ((h_v[i])**2)/u_return[i-1]
    return u_return

def v_i(n):
    h_v = h_i(n)
    u_v = u_i(n)
    b_v = b_i(n)    
    v1 = b_v[1] - b_v[0]
    v_return = np.zeros(n-1)
    v_return[0] = v1
    for i in range(1, n-1):
        v_return[i] = b_v[i+1] - b_v[i] - (h_v[i] * v_return[i-1])/u_v[i-1]
    return v_return

def z_i(n):
    v_v = v_i(n)
    u_v = u_i(n)
    h_v = h_i(n)
    z_return = np.zeros(n+1)
    z_return[-1] = 0
    z_return[0] = 0
    for i in range(n-1,0,-1):
        z_return[i] = (v_v[i-1] - (h_v[i]*z_return[i+1]))/u_v[i-1]
    return z_return

def sklejpizde(n=data.shape[0]-1):
    a = np.zeros(n)
    b =  np.zeros(n)
    c =  np.zeros(n)
    r = 1000
    s = np.zeros(r)
    x= np.linspace(.5,10,r)
    h_v = h_i(n)
    z_v= z_i(n)
    for i  in range(n):
        a[i] = (z_v[i+1] - z_v[i])/(6*h_v[i])
        b[i]  = z_v[i]/2
        c[i] = (((-1 * h_v[i])*(z_v[i+1]+2*z_v[i]))/6) + ((data[i+1, 1] - data[i, 1])/h_v[i])
    for i in range(n):
        s += (data[i,1] + (x-data[i,0])*(c[i]+(x-data[i,0])*(b[i]+(x-data[i,0])*a[i])))*(x<data[i+1,0])*(x >= data[i,0])
    s += (data[0,1] + (x-data[0,0])*(c[0]+(x-data[0,0])*(b[0]+(x-data[0,0])*a[0])))*(x <= data[0,0])*(x >= 0)
    s += (data[-1,1] + (x-data[-1,0])*(c[-1]+(x-data[-1,0])*(b[-1]+(x-data[-1,0])*a[-1])))*(x>=data[-1,0])*(x<=10 )
    
    
    return s

