import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.log(x)


# Crea un array de 404 elementos entre 1 y 3
x = np.linspace(1, 3, 404)
y1 = f(x)
# Se rotula los ejes
plt.ylabel("f(x) = log(x)")
plt.xlabel("x")

# Título del gráfico
plt.title("Gráfico de la función f(x) = log(x)")

# Se colocan límites a los ejes
plt.xlim(1, 3)
plt.ylim(0, 1)

# Se grafica la función
plt.plot(x, y1, linewidth=2, linestyle='-',
         color='blue', label='f(x) = log(x)')

# Se usa .grid para mostrar una cuadrícula
plt.grid()
# Se usa .legend para mostrar la leyenda
plt.legend()
