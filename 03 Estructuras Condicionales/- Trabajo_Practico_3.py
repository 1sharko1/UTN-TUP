# Ejercicio 1: Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# Le pedimos al usuario que ingrese su edad.
edad = int(input("Ingresa tu edad: "))

# Comparamos la edad con 18.
if edad >= 18: 
    print("Eres mayor de edad")

# Si tiene 18 o mas se imprime en pantalla que es mayor, de lo contrario se imprime que es menor.
else:
    print("Eres menor de edad")

# -----------------------------------------------------------

# Ejercicio 2: Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberámostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

# Pedimos al usuario que ingrese su nota
nota = int(input("Ingresa tu nota: "))

# Evaluamos el valor de la nota y determinamos si esta aprobado o desaprobado.
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# -----------------------------------------------------------

# Ejercicio 3: Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

# Pedimos al usuario que ingrese un numero
numero = int(input("Ingrese un numero par: "))

# Utilizamos el operador % llamado modulo, que nos devuelve el resto de una operacion. En caso de ser 0 estamos hablando de un numero par.
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Porfavor ingrese un numero par")

# -----------------------------------------------------------

# Ejercicio 4: Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.

# Le pedimos al usuario que ingrese su edad.
edad = int(input("Ingresa tu edad: "))
categoria = ""

# Evaluamos los rangos de edades y le asignamos una categoria.
if edad >= 0 and edad < 12: 
    categoria = "Niño/a"
elif edad >= 12 and edad < 18:
    categoria = "Adolescente"
elif edad >= 18 and edad < 30:
    categoria = "Adulto/a joven"
elif edad >= 30:
    categoria = "Adulto"
else:
    print("Ingrese una edad valida")
print(categoria)


# -----------------------------------------------------------

# Ejercicio 5: Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

# Le pedimos al usuario que ingrese su contrasena
contrasena = input("Ingrese su contrasena de entre 8 y 14 caracteres: ")

# Utilizamos la funcion len() para verificar la cantidad de caracteres del string ingresado.
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contrasena correcta")
else:
    print("Por favor, ingrese una contrasena de entre 8 y 14 caracteres")
    
# -----------------------------------------------------------

# Ejercicio 6: Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# Importamos las funciones mode, median y mean de la libreria statistics
from statistics import mode, median, mean

# Importamos la libreria random
import random

# Generamos 50 numeros aleatorios entre 1 y 100 utilizando una de las funciones de la libreria random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]

# Creamos una variable moda y le asignamos el valor resultante de mode. La moda de un conjunto de números es el valor que aparece con mayor frecuencia.
moda = mode(numeros_aleatorios)

# Creamos una variable mediana y le asignamos el valor resultante de median. La mediana de un conjunto de números es el número que se encuentra en el medio de la lista, una vez que los números están ordenados de menor a mayor
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

# -----------------------------------------------------------

# Ejercicio 7: Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# Pedimos al usuario que ingrese una frase
string = input("Ingrese una frase o palabra: ")\

# Preguntamos si la ultima letra contiene una vocal
if string[-1] in "aeiouAEIOU":
    print(f"{string}!")
else:  
    print(string)

# -----------------------------------------------------------

# Ejercicio 8: Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 

# Pedimos al usuario que ingrese su nombre
nombre = input("Ingresa tu nombre: ")
num = int(input("Elegi 1 en caso de querer tu nombre en mayusculas, 2 en caso de quererlo en minusculas y 3 en caso de querer solo la primer letra mayuscula: "))

# Con la funcion upper todo el string se convierte en mayuscula.
if num == 1:
    print(nombre.upper())

# Con la funcion lower todo el string se convierte en minuscula.
elif num == 2: 
    print(nombre.lower())

# Con la funcion tittle la primer letra del string se convierte en mayuscula.
elif num == 3: 
    print(nombre.title())
else:
    print("Porfavor, el numero a ingresar debe ser 1 o 2 o 3")

# -----------------------------------------------------------

# Ejercicio 9: Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: ● Menor que 3: "Muy leve" (imperceptible). ● Mayor o igual que 3 y menor que 4: "Leve"(ligeramente perceptible). ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos). ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# Pedimos al usuario que ingrese la magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Comparamos el valor para asignarle una categoria
if magnitud < 3:
    print("Muy leve")
elif 3<= magnitud < 4:
    print("Leve")
elif 4<= magnitud < 5:
    print("Moderado")
elif 5<= magnitud < 6:
    print("Fuerte")
elif 6<= magnitud < 7:
    print("Muy Fuerte")
elif magnitud >=7:
    print("Extremo")

# -----------------------------------------------------------

# Ejercicio 10: Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# Le pedimos al usuario si esta en el hemisferio norte o sur y el dia y mes en el que se encuentra.
hemisferio = input("Ingrese el hemisferio en el que se encuentra (N = norte, S = sur): ").upper()
estacion = ""
dia = int(input("Ingrese en formato numero el dia en el que se encuentra: "))
mes = int(input("Ingrese en formato numero el mes en el que se encuentra: "))

# Validamos si el valor ingresado es correcto
if hemisferio not in ["N", "S"]:
    print("Hemisferio no válido. Debe ser 'N' o 'S'.")
elif mes < 1 or mes > 12:
    print("Mes no válido. Debe ser un número entre 1 y 12.")
elif dia < 1 or dia > 31:
    print("Día no válido. Debe ser un número entre 1 y 31 según el mes.")
    
# Asignamos la estacion a partir del dia y fecha en el que se encuentra, partiendo de que nos ubicamos en el hemisferio norte  .  
if hemisferio == "N":
    if mes in [1, 2]:
        estacion = "Invierno"
    elif mes in [4, 5]:
        estacion = "Primavera"
    elif mes in [7, 8]:
        estacion = "Verano"
    elif mes in[10, 11]:
        estacion = "Otoño"
    if mes == 12: 
        if dia < 21:
            estacion = "Otoño"
        else:
            estacion = "Invierno"
    if mes == 3:
        if dia < 21:
            estacion = "Invierno"
        else:
            estacion = "Primavera"
    if mes == 6:
        if dia < 21:
            estacion = "Primavera"
        else:
            estacion = "Verano"
    if mes == 9:
        if dia < 21:
            estacion = "Verano"
        else:
            estacion = "Otoño"
            
# Asignamos la estacion a partir del dia y fecha en el que se encuentra, partiendo de que nos ubicamos en el hemisferio sur.               
if hemisferio == "S":
    if mes in [1, 2]:
        estacion = "Verano"
    elif mes in [4, 5]:
        estacion = "Otoño"
    elif mes in [7, 8]:
        estacion = "Invierno"
    elif mes in[10, 11]:
        estacion = "Primavera"
    if mes == 12: 
        if dia < 21:
            estacion = "Primavera"
        else:
            estacion = "Verano"
    if mes == 3:
        if dia < 21:
            estacion = "Verano"
        else:
            estacion = "Otoño"
    if mes == 6:
        if dia < 21:
            estacion = "Otoño"
        else:
            estacion = "Invierno"
    if mes == 9:
        if dia < 21:
            estacion = "Invierno"
        else:
            estacion = "Primavera"
print(f"Usted se encuentra en {estacion}")
    

