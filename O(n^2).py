import matplotlib.pyplot as plt
import time
import numpy as np

# ORDENACION POR INSERCION
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def measure_time(size, func):
    # Crear un arreglo aleatorio de tamaño `size`
    arr = np.random.randint(0, size, size)
    
    start_time = time.time()
    func(arr)
    end_time = time.time()
    
    return end_time - start_time

# Tamaños de entrada
sizes = [10, 100, 1000, 3000, 5000, 7000]
times = []

# Medir el tiempo de ejecución para cada tamaño de entrada
for size in sizes:
    times.append(measure_time(size, insertion_sort))

# Graficar los resultados
plt.plot(sizes, times, label='O(n^2)')
plt.xlabel('Tamaño de la entrada (n)')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de Insertion Sort')
plt.legend()
plt.show()
