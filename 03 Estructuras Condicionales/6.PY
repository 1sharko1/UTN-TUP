from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
if media > mediana > moda:
    print("La distribución tiene sesgo positivo (a la derecha).")
elif media < mediana < moda:
    print("La distribución tiene sesgo negativo (a la izquierda).")
else:
    print("La distribución no tiene sesgo.")