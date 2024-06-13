import matplotlib.pyplot as plt
import time
import numpy as np

## El algoritmo de ordenación por mezcla (merge sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def measure_time(size, func):
    # Crear un arreglo aleatorio de tamaño `size`
    arr = np.random.randint(0, size, size)
    
    start_time = time.time()
    func(arr)
    end_time = time.time()
    
    return end_time - start_time

# Tamaños de entrada
sizes = [10, 100, 1000, 10000, 100000, 1000000]
times = []

# Medir el tiempo de ejecución para cada tamaño de entrada
for size in sizes:
    times.append(measure_time(size, merge_sort))

# Graficar los resultados
plt.plot(sizes, times, label='O(n log n)')
plt.xlabel('Tamaño de la entrada (n)')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de Merge Sort')
plt.legend()
plt.show()
