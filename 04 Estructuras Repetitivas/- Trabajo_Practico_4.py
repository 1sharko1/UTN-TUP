# Ejercicio 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# Creamos un bucle que recorre desde x (0 por defecto) hasta el parametro final teniendo en cuenta que la fucion range excluye el ultimo numero. Cada iteracion mostrara en pantalla el aumento del valor de la variable x, lo que dara como resultado una lista de los numeros entre 0 y 100.
for x in range (101):
    print(x)
    
# -----------------------------------------------------------

# Ejercicio 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

# Pedimos al usuario ingresar un numero.
print("Ingrese un numero y devolveremos la cantidad de digitos: ")
num = int(input())

# Creamos una variable para almacenar el valor ingresasdo para luego mostrarlo en pantalla.
num_inicial = num

# Inicializamos el contador en 0.
digitos = 0

# Definimos un bucle con la condicion de que se ejecute solo mientras el numero sea distino a 0. 
while num != 0:

    # Contamos la cantidad de digitos basandonos en que tras cada iteracion el numero ira perdiendo un digito hasta llegar a 0 debido a la division baja que aplicamos al numero en cada iteracion.
    digitos += 1
    num = num // 10

# Se muestra en pantalla la cantidad de digitos del numero ingresado.
print("La cantidad de digitos de ", num_inicial, " es de: ", digitos)

# -----------------------------------------------------------

# Ejercicio 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

# Pedimos al usuario ingresar dos numeros enteros.
print("Ingrese dos numero entero: ")
num1 = int(input())
num2 = int(input())

# Inicializamos las variables mayor y menor para poder actualizar su valor segun los numeros ingresados.
mayor = -1000
menor = 1000

# Inicializamos el contador suma en 0
suma = 0

# Comparamos los numeros y se asigna el numero mas grande a la variable mayor, el mas pequeno a la variable menor y en caso de que sean iguales no se inicia el bucle.
if num1 == num2:
    print("No hay suma de valores entre los numeros ingresados ya que son iguales")
else: 
    if num1 > num2:
        mayor = num1
        menor = num2
    else: 
        mayor = num2
        menor = num1
        
# Definimos un bucle que va recorrer desde el numero menor + 1 (ya que se pide no incluir el numero mas pequeno) hasta el mayor (por defecto la funcion range no incluye el numero final). El valor de suma va a actualizarse sumandose el valor de x a la par que se actualiza nuestra variable x, dandonos como resultado la suma entre los dos valores comprendidos de los numeros ingresados.
    for x in range (menor + 1, mayor):
        suma += x
    print("La suma total entre los valores comprendidos de los dos numeros ingresados es: ",suma)

# -----------------------------------------------------------

# Ejercicio 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

# Inicializamos el contador de suma en 0 y pedimos al usuario que ingrese un primer numero.
suma = 0
num = int(input("Ingrese un numero entero: "))

# Definimos un bucle que funcionara mientras el numero ingresado sea distinto a 0. Y vamos sumandole cada numero ingresado a la variable suma.
while num != 0:
    suma += num
    num = int(input("Ingrese un nuevo numero (0 para terminar): "))
print("La suma entre los numeros ingresados es: ", suma)

# -----------------------------------------------------------

# Ejercicio 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

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

# -----------------------------------------------------------

# Ejercicio 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

# Creamos un bucle que recorre desde 100 a 0 con un indicador de que se cuente de dos en dos. Esto lo hacemos colocando una coma y el numero que indica como debe recorrer los valores (luego de definir los dos valores de inicio y fin del for), en este caso -2 ya que nos piden que sea en orden decreciente. Cada iteracion mostrara en pantalla el decremento del valor de la variable x, lo que dara como resultado una lista de los numeros pares comprendidos entre 0 y 100 en orden decreciente.
for x in range (100, -1, -2):
    print(x)

# -----------------------------------------------------------

# Ejercicio 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

print("Ingrese un numero entero positivo:")
num = int(input())
suma = 0
# Definimos un bucle while que se ejecuta mientras el numero sea menor a 0.
while num < 0:
    print("Porfavor el numero a ingresar debe ser positivo: ")
    num = int(input())
# Definimos un bucle for que comienza luego de que el numero ingresado sea mayor a 0 y termina cuando se ingresa el 0.
for x in range (0, num + 1):
    suma += x
print("La suma de los numeros comprendidos entre 0 y ", num, " es: ", suma)

# -----------------------------------------------------------

# Ejercicio 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

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

# -----------------------------------------------------------

# Ejercicio 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

# Inicializamos el contador en 0.
total = 0

# Pedimos 100 numeros al usuario y al finalizar se realizara un promedio dividiendo la suma total de estos por 100.
print("Ingrese 100 numeros: ")
for x in range (100):
    num = int(input())
    total += num
promedio = total / 100
print("La media de los 100 numeros ingresados es: ", promedio)

# -----------------------------------------------------------

# Ejercicio 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Opcion 1 (Trabajando el numero como un string.)
num = (input("Ingrese un numero: "))

# Revertimos el numero 
reverso = num[::-1] # Esto es una tecnica llamada slicing que nos permite sustraer pare te de un texto. Su sintaxis es: cadena[incio:fin:paso]. En este caso al colocar [::-1] es decir valores vacios, estamos diciendo que comience desde el final y termine en el principio contando hacia atras debido a que indicamos el paso en -1.
print(reverso)

# Opcion 2 (Trabajando el numero como un entero)
num = int(input("Ingrese un numero: "))
invertido = 0
while num != 0:
    digito = num % 10 # Esto nos almacena el ultimo digito.
    invertido = invertido * 10 + digito # Esto agrega el digito almacenado al numero invertido.
    num = num // 10 # Esto quita el ultimo digito del numero original.
print("El numero invertido es: ", invertido)
