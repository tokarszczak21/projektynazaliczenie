import numpy as np

def f(x, y):
  return (3*x**7 + 2*y**5 - x**3 + y**3 - 3)
  
def p_f(x, y):
  h = 10e-10
  return (f(x, y) - f(x, y-h))/h
  
def newton(x, y0=1, delta = 10e-10, krok = 4):
  y = y0 - f(x, y0) / p_f(x, y0)
  
  for n in range(krok):
    y = y - f(x, y) / p_f(x, y) 
  return y
def zadanie():
  x = np.linspace(0, 10, 101).round(2)
  y = [1.0]

  for x_value in x:
    if x_value !=0:
      y.append(newton(x_value, y0=y[-1]))

  for i in range(len(x)):
    print(f'{i}\t{x[i]}\t{y[i]}\t{f(x[i], y[i])}')
  return#jak mnie to kurwa zmęczyło ja pierdole kurwa mać

if __name__ == "__main__":
  zadanie()
