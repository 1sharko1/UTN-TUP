# Inicializamos todos los contadores en 0.
pares = 0
impares = 0 
positivos = 0
negativos = 0
# Comienza un bucle for en el que se va a pedir numeros al usuario hasta que ingrese 100 numeros.
print("Ingrese 100 numeros: ")
for x in range (100):
    # Sumamos valor a las variables segun la categoria de cada numero.
    num = int(input())    
    if num % 2 == 0:
        pares += 1
    else:
        impares +=1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print("La cantidad de numeros pares fue: ", pares)
print("La cantidad de numeros impares fue: ", impares)
print("La cantidad de numeros positivos fue: ", positivos)
print("La cantidad de numeros negativos fue: ", negativos)

