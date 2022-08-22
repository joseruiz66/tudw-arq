
'''
    Ejemplo 01.py: 

    Tiempo de respuesta (Wall time: reloj de pared): Es la diferencia entre el momento en que un programa terminó  su ejecución
    y el momento en que se inició el programa. Es como medir el tiempo con un cronómetro.
    IMPORTANTE: También incluye el tiempo de espera de los recursos .

    https://www.onlinegdb.com/online_python_compiler

    Ejemplo tomado de:
    https://pynative.com/python-get-execution-time-of-program/#wall-time-vs-cpu-time
'''


import time

# Obtiene tiempo de inicio
st = time.time()

# main program
# Calcular la suma de los números de 0 hasta 1 million
sum_x = 0
for i in range(1000000):
    sum_x += i

# Espera por 3 segundos
time.sleep(3)

print('La suma de los números de 0 hasta 1 million es:', sum_x)

# Obtiene tiempo de finalizacion
et = time.time()

# Calcular diferencia Finalizacion - Inicio 
elapsed_time = et - st
print('Tiempo de respuesta:', elapsed_time, 'segundos')
