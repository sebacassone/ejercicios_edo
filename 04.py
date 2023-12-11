import numpy as np
import matplotlib.pyplot as plt

X, Y = np.meshgrid(np.linspace(-5, 5, 12), np.linspace(-5, 5, 12))

U = 1.0
V = X-Y

N = np.sqrt(U ** 2 + V ** 2)  # Normalizamos los vectores
U = U / N
V = V / N

# graficamos los vectores con origen en (x,y) y término (u,v)
plt.quiver(X, Y, U, V)
plt.xlim([-5, 5])  # limites en eje x
plt.ylim([-5, 5])  # limites en eje y

plt.xlabel('x')  # etiqueta eje x
plt.ylabel('y')  # etiqueta eje y
plt.grid()  # para establecer red en la región

x = np.linspace(-5, 5, 200)
def h(x): return np.exp(-x)+x-1


h = h(x)
plt.plot(x, h, label='h(x)')


def s(x): return 2*np.exp(-x)-x+1


s = s(x)
plt.plot(x, s, label='s(x)')
plt.legend()
