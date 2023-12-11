import numpy as np
import matplotlib.pyplot as plt

X, Y = np.meshgrid(np.linspace(-4, 4, 9), np.linspace(-4, 4, 9))
print('Y = ', Y)

U = 1.0
V = 2*Y
print('V = ', V)

N = np.sqrt(U ** 2 + V ** 2)  # Normalizamos los vectores
U = U / N
V = V / N
print('U = ', U)
print('V = ', V)
print('N = ', N)

# graficamos los vectores con origen en (x,y) y término (u,v)
plt.quiver(X, Y, U, V)
plt.xlim([-5, 5])  # limites en eje x
plt.ylim([-5, 5])  # limites en eje y

plt.xlabel('x')  # etiqueta eje x
plt.ylabel('y')  # etiqueta eje y
plt.grid()  # para establecer red en la región
