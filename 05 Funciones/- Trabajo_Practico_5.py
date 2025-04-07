# Ejercicio 1: Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola mundo!")
imprimir_hola_mundo()

# -----------------------------------------------------------

# Ejercicio 2: Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

# Funcion saludar usuario
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# Programa principal
nombre = input("Ingresa tu nombre: ")
saludar_usuario(nombre)

# -----------------------------------------------------------

# Ejercicio 3: Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Funcion informacion personal.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa principal
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
informacion_personal(nombre,apellido,edad,residencia)

# -----------------------------------------------------------

# Ejercicio 4: Crear dos funciones: calcular_area_circulo(radio) que reciba el ra- dio como parámetro y devuelva el área del círculo. calcular_peri- metro_circulo(radio) que reciba el radio como parámetro y devuel- va el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# Funcion 1
from math import pi
def calcular_area_circulo(radio):
    area = pi * radio**2
    print(f"El area del circulo a partir de que el radio sea {radio} es: {area}")

# Funcion 2
def calcular_perimetro_circulo(radio):
    perimetro = 2 * radio * pi
    print(f"El perimetro del circulo a partir de que el radio sea {radio} es: {perimetro}")

radio = float(input("Ingresa el radio: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

# -----------------------------------------------------------

# Ejercicio 5: Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# Funcion segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
segundos = int(input("Ingrese una cantidad de segundos: "))
equivalencia_segundos_a_horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {equivalencia_segundos_a_horas} horas.")

# -----------------------------------------------------------

# Ejercicio 6: Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Funcion tabla de multiplicar.
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)

# -----------------------------------------------------------

# Ejercicio 7: Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# Funcion operaciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

# Programa principal
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
resultados = operaciones_basicas(a,b)
print(f"El resultado de sumar {a} y {b} es {resultados[0]}")
print(f"El resultado de restar {a} y {b} es {resultados[1]}")
print(f"El resultado de multiplicar {a} y {b} es {resultados[2]}")
print(f"El resultado de dividir {a} y {b} es {resultados[3]}")

# -----------------------------------------------------------

# Ejercicio 8: Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# Funcion
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

# -----------------------------------------------------------

# Ejercicio 9: Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return 9/5*celsius + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La equivalencia de {celsius} grados Celsius a fahrenheit seria: {fahrenheit:.2f}")


# -----------------------------------------------------------

# Ejercicio 10: Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3
a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un numero: "))
c = int(input("Ingresa un numero: "))
promedio = calcular_promedio(a,b,c)
print(f"El promedio entre {a}, {b} y {c} es: {promedio:.2f}")