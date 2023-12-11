import numpy as np
import matplotlib.pyplot as plt

# X e Y son el vector posición
X, Y = [[2, 2, 3], [2, 3, 6]]
U, V = [[1, 2, 4], [1, 1, 4]]

# Le colocamos limites
plt.xlim(0, 10)
plt.ylim(0, 10)

# Quiver es para vectores, grafica un vector en el punto X,Y y con dirección U,V
plt.quiver(X, Y, U, V)
plt.grid()
plt.plot()

# Se arma una matiz
V = np.meshgrid(np.linspace(-4, 4, 9), np.linspace(-4, 4, 9))
print(V)
