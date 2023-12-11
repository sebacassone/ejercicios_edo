import numpy as np
import matplotlib.pyplot as plt

# Definir la función de la EDO


def f(y, x):
    return y**2


# Definir las condiciones iniciales
x0 = 0  # Valor inicial de x
y0 = 1  # Valor inicial de y

# Definir el paso de integración
h = 0.01

# Definir las listas para almacenar los valores calculados
x_values = [x0]
y_values = [y0]

# Resolver la EDO utilizando el método de Euler
while x_values[-1] < 1:  # Definir un límite para detener la integración
    x_new = x_values[-1] + h
    y_new = y_values[-1] + h * f(y_values[-1], x_values[-1])
    x_values.append(x_new)
    y_values.append(y_new)

# Convertir las listas a arrays de NumPy
x_values = np.array(x_values)
y_values = np.array(y_values)

# Graficar la solución
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de la EDO')
plt.show()
