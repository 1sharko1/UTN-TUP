# Inicializamos el contador de suma en 0 y pedimos al usuario que ingrese un primer numero.
suma = 0
num = int(input("Ingrese un numero entero: "))

# Definimos un bucle que funcionara mientras el numero ingresado sea distinto a 0. Y vamos sumandole cada numero ingresado a la variable suma.
while num != 0:
    suma += num
    num = int(input("Ingrese un nuevo numero (0 para terminar): "))
print("La suma entre los numeros ingresados es: ", suma)