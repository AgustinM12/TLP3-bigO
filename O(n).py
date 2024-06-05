import time
import matplotlib.pyplot as plt
from measure_time import measure_time as mt

# Ejemplo de función con complejidad O(n)
def linear_algorithm(arr, n):
    for i in arr:
        if i == n:
            return i

# Tamaños de entrada
sizes = [10, 100, 1000, 10000, 100000, 1000000]
times = []

# Medir el tiempo de ejecución para cada tamaño de entrada
for size in sizes:
    times.append(mt(size, linear_algorithm))
# Crear gráfica
plt.plot(sizes, times, label='O(n)')
plt.xlabel('Tamaño de la entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecucion de busqueda lineal')
plt.legend()
plt.show()