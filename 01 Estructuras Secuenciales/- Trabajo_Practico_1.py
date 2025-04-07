# Ejercicio 1: Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola mundo!")   

# -----------------------------------------------------------

# Ejercicio 2 : Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla

# Pedimos al usuario ingresar su nombre.
nombre = input("Ingresa tu nombre: ")

# Mostramos en pantalla el nombre del usuario, concatenando strings colocando f antes de las commilas.
print(f"Hola {nombre}!") 

# -----------------------------------------------------------

# Ejercicio 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

# Pedimos datos al usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

# Mostramos en pantalla los datos del usuario, concatenando strings colocando f antes de las commilas.
print(f"Usted es {nombre} {apellido}, tiene {edad} años, y vive en {residencia}.")

# -----------------------------------------------------------

# Ejercicio 4: Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

# Al principio del programa necesitamos importar la librería math ya que la necesitaremos para utilizar el número pi.
from math import pi

# Pedimos al usuario ingresar un radio.
radio = float(input("Ingrese un radio para que devolvamos su area y perimetro: ")) 

# Calculamos area y perimetro a partir del radio dado por el usuario.
area = pi * (radio)**2
perimetro = 2 * pi * radio 
print(f"El area del circulo es de {area} y el perimetro es de {perimetro}")

# -----------------------------------------------------------

# Ejercicio 5: Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = float(input("Ingrese una cantidad de segundos: "))

# Agregamos la funcion round para redondear y un dos tras la coma para que el resultado muestre solo dos decimales.
equivalenciaHora = round(segundos/3600, 2)
print(f"La cantidad de {segundos} segundos equivale a {equivalenciaHora} horas") 

# -----------------------------------------------------------

# Ejercicio 6: 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

# Pedimos al usuario ingresare un numero.
num = int(input("Ingrese un numero entero: "))

# Realizamos la tabla de multiplicacion hasta el 9 del numero ingresado.
numx1 = num * 1
numx2 = num * 2
numx3 = num * 3
numx4 = num * 4
numx5 = num * 5 
numx6 = num * 6
numx7 = num * 7
numx8 = num * 8
numx9 = num * 9

# Mostramos en pantalla la tabla de multiplicacion hasta el 9 del numero ingresado.
print(f"{num} x 1 = {numx1}")
print(f"{num} x 2 = {numx2}")
print(f"{num} x 3 = {numx3}")
print(f"{num} x 4 = {numx4}")
print(f"{num} x 5 = {numx5}")
print(f"{num} x 6 = {numx6}")
print(f"{num} x 7 = {numx7}")
print(f"{num} x 8 = {numx8}")
print(f"{num} x 9 = {numx9}")

# -----------------------------------------------------------

# Ejercicio 7: Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

# Pedimos al usuario ingresar dos numero.
num1 = int(input("Ingrese un numero entero distinto de 0: "))
num2 = int(input("Ingrese un segundo numero entero distinto de 0: "))

# Mostramos en pantalla las operaciones basicas entre estos dos numeros.
print(f"La suma entre {num1} y {num2} es: ", num1 + num2)
print(f"La resta entre {num1} y {num2} es: ", num1 - num2)
print(f"La multiplicacion entre {num1} y {num2} es: ", num1 * num2)
print(f"La division entre {num1} y {num2} es: ", round(num1 / num2, 2))

# -----------------------------------------------------------

# Ejercicio 8: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

# Pedimos datos al usuario
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso: "))

# Calculamos IMC a traves de su formula.
imc = round(peso / altura**2, 2)
print(f"Tu IMC es {imc}")

# -----------------------------------------------------------

# Ejercicio 9: rear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

# Pedimos al usuario que ingrese una temperatura en Celsius.
celsius = int(input("Ingrese una temperatura en Celsius: "))

# Convertimos los celsius a fahrenheit.
fahrenheit = 9/5*celsius + 32
print(f"{celsius} grados celsius equivalen a {fahrenheit} grados fahrenheit")

# -----------------------------------------------------------

# Ejercicio 10: Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

# Pedimos al usuario 3 numeros.
num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese un numero: "))
num3 = float(input("Ingrese un numero: "))

# Calculamos el promedio sumando los 3 numeros y diviendo el total entre 3.
promedio = (num1 + num2 + num3) / 3
print(f"El promedio entre {num1}, {num2} y {num3} da {promedio}")