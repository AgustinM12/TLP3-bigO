import time

def measure_time(n, function):
    arr = list(range(n))
    x = -1  # Buscamos un elemento que no está en la lista para asegurar el peor caso
    start_time = time.time()
    function(arr, x)
    end_time = time.time()
    return end_time - start_time