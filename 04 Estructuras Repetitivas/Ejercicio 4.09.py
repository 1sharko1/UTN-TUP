# Inicializamos el contador en 0.
total = 0

# Pedimos 100 numeros al usuario y al finalizar se realizara un promedio dividiendo la suma total de estos por 100.
print("Ingrese 100 numeros: ")
for x in range (100):
    num = int(input())
    total += num
promedio = total / 100
print("La media de los 100 numeros ingresados es: ", promedio)