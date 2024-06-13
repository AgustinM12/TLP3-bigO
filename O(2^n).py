import matplotlib.pyplot as plt
import time

# cálculo del n-ésimo número de Fibonacci de manera recursiva sin memorización.
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def measure_time(size, func):
    start_time = time.time()
    func(size)
    end_time = time.time()
    
    return end_time - start_time

# Tamaños de entrada
sizes = [5, 10, 15, 20, 25, 30]
times = []

# Medir el tiempo de ejecución para cada tamaño de entrada
for size in sizes:
    times.append(measure_time(size, fibonacci_recursive))

# Graficar los resultados
plt.plot(sizes, times, label='O(2^n)')
plt.xlabel('Tamaño de la entrada (n)')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de Fibonacci Recursivo')
plt.legend()
plt.show()
