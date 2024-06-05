import matplotlib.pyplot as plt
from measure_time import measure_time as mt

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1

# Tamaños de entrada
sizes = [10, 100, 1000, 10000, 100000, 1000000]
times = []

# Medir el tiempo de ejecución para cada tamaño de entrada
for size in sizes:
    times.append(mt(size, binary_search))

# Graficar los resultados
plt.plot(sizes, times, label='O(log n)')
plt.xlabel('Tamaño de la entrada (n)')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de la búsqueda binaria')
plt.legend()
plt.show()
