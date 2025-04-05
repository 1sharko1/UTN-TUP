# Importamos la libreria random para poder generar un numero aleatorio.
import random

# Utilizamos la funcion randint del modulo random, que nos permite generar un numero entero aleatorio entre los parametros que les demos. En este casa 0 y 9.
num_a_adviniar = random.randint(0, 9)   

# Pedimos al usuario que ingrese un numero.
print("Adivina el numero entre 0 y 9!: ")
num = int(input())

# Inicializamos el contador en uno ya que al entrar al bucle ya se tuvo que ingresar un numero.
intentos = 1

# Definimos la condicion de que mientras el numero ingresado sea diferente al numero a adivinar, el contador intentos va a aumentar su valor en uno.
while num != num_a_adviniar:
    intentos += 1
    num = int(input())

# Mostramos en pantalla la cantidad de intentos para adivinar.
print("Exacto el numero es: ", num_a_adviniar, ". La cantidad de intentos fue de: ", intentos)