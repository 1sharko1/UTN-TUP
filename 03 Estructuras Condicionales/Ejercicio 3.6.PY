# Importamos las funciones mode, median y mean de la libreria statistics
from statistics import mode, median, mean
# Importamos la libreria random
import random

# Generamos 50 numeros aleatorios entre 1 y 100 utilizando una de las funciones de la libreria random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]

# Creamos una variable moda y le asignamos el valor resultante de mode
# La moda de un conjunto de números es el valor que aparece con mayor frecuencia.
moda = mode(numeros_aleatorios)

# Creamos una variable mediana y le asignamos el valor resultante de median
# La mediana de un conjunto de números es el número que se encuentra en el medio de la lista, una vez que los números están ordenados de menor a mayor
mediana = median(numeros_aleatorios)

# Creamos una variable media y le asignamos el valor resultante de mean
# La media de un conjunto de números es el promedio de todos los números que lo componen
media = mean(numeros_aleatorios)

# Mostramos en pantalla el valor de moda, mediana y media 
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

# Comparamos los valores de cada variable para determinar si hay sesgo positivo, negativo o no hay sesgo
# Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
# Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,la mediana es menor que la moda.
# Sin sesgo: cuando la media, la mediana y la moda son iguales.
if media > mediana > moda:
    print("La distribución tiene sesgo positivo (a la derecha).")
elif media < mediana < moda:
    print("La distribución tiene sesgo negativo (a la izquierda).")
else:
    print("La distribución no tiene sesgo.")